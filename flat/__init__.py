from __future__ import print_function

import ctypes
import sys

from . import _glfw

if sys.version_info[0] == 3:
    unichr = chr

# bool saying whether we are polling events right now or not
_polling_events = False

# list containing all opened windows
_open_windows = []

# list containing a list of windows that must be closed when all events are polled
_close_queue = []


# initialise GLFW
_glfw.Init()


def _error_callback(error_num, error_str):
    raise RuntimeError(error_str)


def _size_callback(window, width, height):
    Window._from_handle(window).event.dispatch("on_resize", width, height)
    
    
def _close_callback(window):
    Window._from_handle(window).event.dispatch("on_close")
    
    return False
    
    
def _refresh_callback(window):
    Window._from_handle(window).event.dispatch("on_draw")
    
    
def _focus_callback(window, has_focus):
    try:
        window = Window._from_handle(window)
    except ValueError:
        return
    
    if has_focus:
        window.event.dispatch("on_focus")
    else:
        window.event.dispatch("on_blur")
    
def _key_callback(window, key, downup):
    if key < 256:
        key = unichr(key)
        
    if downup:
        Window._from_handle(window).event.dispatch("on_key_press", key)
    else:
        Window._from_handle(window).event.dispatch("on_key_release", key)
    

def _char_callback(window, char):
    Window._from_handle(window).event.dispatch("on_text", unichr(char))
    

_error_callback.c_callback = _glfw.errorfun(_error_callback)
_glfw.SetErrorCallback(_error_callback.c_callback)

_close_callback.c_callback = _glfw.windowclosefun(_close_callback)
_glfw.SetWindowCloseCallback(_close_callback.c_callback)

_refresh_callback.c_callback = _glfw.windowrefreshfun(_refresh_callback)
_glfw.SetWindowRefreshCallback(_refresh_callback.c_callback)

_focus_callback.c_callback = _glfw.windowfocusfun(_focus_callback)
_glfw.SetWindowFocusCallback(_focus_callback.c_callback)

_key_callback.c_callback = _glfw.keyfun(_key_callback)
_glfw.SetKeyCallback(_key_callback.c_callback)

_char_callback.c_callback = _glfw.charfun(_char_callback)
_glfw.SetCharCallback(_char_callback.c_callback)


class _WindowEvent(object):
    _event_types = ("on_draw", "on_focus", "on_blur", "on_close", "on_iconify", "on_restore", "on_key_press", "on_key_release", "on_motion", "on_enter", "on_leave", "on_mouse_press", "on_mouse_release", "on_scroll", "on_resize", "on_text")

    def __init__(self, window):
        self._window = window
        self._default_handlers = {"on_close": window._on_close}
        self._event_stack = [{}]
        
    def dispatch(self, event_name, *args, **kwargs):
        if event_name not in self._event_types:
            raise RuntimeError("unknown event: " + str(event_name))
            
        default_func = lambda *args, **kwargs: False
        
        for handlers in reversed(self._event_stack):
            if handlers.get(event_name, default_func)(self._window, *args, **kwargs):
                break
        else:
            self._default_handlers.get(event_name, default_func)(*args, **kwargs)
            
            
    def push_handlers(self, handlers = {}, **kwargs):
        handlers.update(kwargs)
        
        for event_name in handlers:
            if event_name not in self._event_types:
                raise RuntimeError("unknown event: " + str(event_name))
        
        self._event_stack.append(handlers)
        
        
    def pop_handlers(self):
        return self._event_stack.pop()
        
    # syntactic sugar
    def __setattr__(self, name, value):
        if name in self._event_types:
            self._event_stack[-1][name] = value
        else:
            # detect accidents, like assigning on_key_down while the correct event is on_key_press
            if name.startswith("on"):
                raise AttributeError("no event named " + name)
                
            object.__setattr__(self, name, value)
        
        
    def __getattr__(self, name):
        if name in self._event_types:
            return self._event_stack[-1][name]
        else:
            raise AttributeError
        
    # decorator
    def __call__(self, event_name):
        if event_name not in self._event_types:
            raise RuntimeError("unknown event: " + str(event_name))
        
        def add_handler(func):
            self.event_stack[-1][event_name] = func
        
        return add_handler
            
class Window(object):
    def __init__(self, width, height, title, pos_x = 50, pos_y = 50, fullscreen=False, resizable=False):
        # set up window parameters
        mode = _glfw.FULLSCREEN if fullscreen else _glfw.WINDOWED
        _glfw.WindowHint(_glfw.RESIZABLE, bool(resizable))
        _glfw.WindowHint(_glfw.VISIBLE, True)
        
        # create window
        self._wnd = _glfw.CreateWindow(width, height, mode, title.encode("utf-8"), None)
        
        # do window management
        _glfw.SetWindowUserPointer(self._wnd, ctypes.c_void_p(id(self)))
        _open_windows.append(self)
        
        self._open = True
        self._title = title
        
        self.event = _WindowEvent(self)
        
        self.position = (pos_x, pos_y)
        self.show()
        
    def _has_focus(self):
        return bool(_glfw.glfwGetWindowParam(_glfw.ACTIVE))
    
    has_focus = property(None, _has_focus)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
        _glfw.SetWindowTitle(self._wnd, title.encode("utf-8"))
        
    @property
    def size(self):
        width = ctypes.c_int()
        height = ctypes.c_int()
        
        _glfw.GetWindowSize(self._wnd, ctypes.byref(width), ctypes.byref(height))
        
        return (width.value, height.value)
        
    @size.setter
    def size(self, size):
        _glfw.SetWindowSize(self._wnd, size[0], size[1])
        
    @property
    def position(self):
        x = ctypes.c_int()
        y = ctypes.c_int()
        
        _glfw.GetWindowSize(self._wnd, ctypes.byref(x), ctypes.byref(y))
        
        return (x, y)
        
    @position.setter
    def position(self, position):
        _glfw.SetWindowPos(self._wnd, position[0], position[1])
        
        
    def show(self):
        _glfw.ShowWindow(self._wnd)
        
    def hide(self):
        _glfw.HideWindow(self._wnd)
        
    def iconify(self):
        _gflw.IconifyWindow(self._wnd)
    
    def restore(self):
        _glfw.RestoreWindow(self._wnd)
        
    def close(self):
        if self._open:
            self._open = False
            
            _open_windows.remove(self)
            
            if _polling_events:
                _close_queue.append(self)
            else:
                _glfw.DestroyWindow(self._wnd)
            
        
    @classmethod
    def _from_handle(cls, handle):
        return ctypes.cast(_glfw.GetWindowUserPointer(handle), ctypes.py_object).value

    # default event handlers
    def _on_close(self):
        self.close()

def run():
    global _close_queue, _polling_events
    
    while _open_windows:
        _polling_events = True
        _glfw.PollEvents()
        _polling_events = False
        
        for window in _close_queue:
            _glfw.DestroyWindow(window._wnd)
        
        _close_queue = []

from . import key