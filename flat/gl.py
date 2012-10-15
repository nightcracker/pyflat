import os

from ctypes import *
from . import _glfw

if os.name == "nt":
    _functype = WINFUNCTYPE
else:
    _functype = CFUNCTYPE

class OpenGLWrapper(object):
    """Wraps OpenGL functions using _ctypes and glfw.GetProcAddress.
    
    When created with OpenGLWrapper(funcname, restype, argtypes), the object
    will behave like a ctypes function with `restype` as result type and
    `argtypes` as argument types. The ctypes function is initialized using an
    OpenGL function pointer retrieved by passing `funcname` into glfw.GetProcAddress.
    
    This creates a lazy wrapper - the function address is not looked up until
    the first call. This is useful because the function address can not be
    retrieved until there is a opened window.
    
    For example, to wrap `void glClear(unsigned int mask);`:
    
        >>> GL_COLOR_BUFFER_BIT = 0x00004000 # constant from gl.h
        >>> glClear = glfw.ext.OpenGLWrapper("glClear", None, _ctypes.c_uint)
        
    And then the usage is simple:
    
        >>> glClear(GL_COLOR_BUFFER_BIT)
    
    """
    
    def __init__(self, funcname, restype, *argtypes):
        self.funcname = funcname
        self.restype = restype
        self.argtypes = argtypes
        self.funcprototype = WINFUNCTYPE(restype, *argtypes)
        self.glfunc = None
    
    def __call__(self, *args, **kwargs):
        if self.glfunc is None:
            proc_addr = _glfw.GetProcAddress(self.funcname)
            
            if proc_addr is None:
                raise RuntimeError("Couldn't load OpenGL function " + self.funcname)
            
            self.glfunc = self.funcprototype(proc_addr)
            
        return self.glfunc(*args, **kwargs)
    
    def __repr__(self):
        return "flat.gl.OpenGLWrapper(%s, %s, %s)" % (repr(self.funcname), repr(self.restype), repr(self.argtypes))
        
GL_COLOR_BUFFER_BIT = 0x00004000

glClear = OpenGLWrapper("glClear", None, c_uint)
glClearColor = OpenGLWrapper("glClearColor", None, c_float, c_float, c_float, c_float)