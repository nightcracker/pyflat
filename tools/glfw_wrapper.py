from ctypes import *

glfwdll = cdll.LoadLibrary("pyflat/bin/glfw3.dll")

# Key and button state/action definitions 
RELEASE = 0
PRESS = 1

"""
Keyboard raw key codes.
 These key codes are inspired by the USB HID Usage Tables v1.12 (p. 53-60), but re-arranged to map to 7-bit ASCII for printable keys (function keys are
 put in the 256+ range).
 The naming of the key codes follow these rules:
 - The US keyboard layout is used.
 - Names of printable alpha-numeric characters are used (e.g. "A", "R", "3", etc).
 - For non-alphanumeric characters, Unicode:ish names are used (e.g.
 "COMMA", "LEFT_SQUARE_BRACKET", etc). Note that some names do not
 correspond to the Unicode standard (usually for brevity).
 - Keys that lack a clear US mapping are named "WORLD_x".
 - For non-printable keys, custom names are used (e.g. "F4", "BACKSPACE", etc).
"""

# Printable keys 
KEY_SPACE = 32
KEY_APOSTROPHE = 39 # ' 
KEY_COMMA = 44 #, KEY_MINUS = 45 # - 
KEY_PERIOD = 46 # . 
KEY_SLASH = 47 # / 
KEY_0 = 48
KEY_1 = 49
KEY_2 = 50
KEY_3 = 51
KEY_4 = 52
KEY_5 = 53
KEY_6 = 54
KEY_7 = 55
KEY_8 = 56
KEY_9 = 57
KEY_SEMICOLON = 59 # 
KEY_EQUAL = 61 # = 
KEY_A = 65
KEY_B = 66
KEY_C = 67
KEY_D = 68
KEY_E = 69
KEY_F = 70
KEY_G = 71
KEY_H = 72
KEY_I = 73
KEY_J = 74
KEY_K = 75
KEY_L = 76
KEY_M = 77
KEY_N = 78
KEY_O = 79
KEY_P = 80
KEY_Q = 81
KEY_R = 82
KEY_S = 83
KEY_T = 84
KEY_U = 85
KEY_V = 86
KEY_W = 87
KEY_X = 88
KEY_Y = 89
KEY_Z = 90
KEY_LEFT_BRACKET = 91 # [ 
KEY_BACKSLASH = 92 # \ 
KEY_RIGHT_BRACKET = 93 # ] 
KEY_GRAVE_ACCENT = 96 # ` 
KEY_WORLD_1 = 161 # non-US #1 
KEY_WORLD_2 = 162 # non-US #2 

# Function keys 
KEY_ESCAPE = 256
KEY_ENTER = 257
KEY_TAB = 258
KEY_BACKSPACE = 259
KEY_INSERT = 260
KEY_DELETE = 261
KEY_RIGHT = 262
KEY_LEFT = 263
KEY_DOWN = 264
KEY_UP = 265
KEY_PAGE_UP = 266
KEY_PAGE_DOWN = 267
KEY_HOME = 268
KEY_END = 269
KEY_CAPS_LOCK = 280
KEY_SCROLL_LOCK = 281
KEY_NUM_LOCK = 282
KEY_PRINT_SCREEN = 283
KEY_PAUSE = 284
KEY_F1 = 290
KEY_F2 = 291
KEY_F3 = 292
KEY_F4 = 293
KEY_F5 = 294
KEY_F6 = 295
KEY_F7 = 296
KEY_F8 = 297
KEY_F9 = 298
KEY_F10 = 299
KEY_F11 = 300
KEY_F12 = 301
KEY_F13 = 302
KEY_F14 = 303
KEY_F15 = 304
KEY_F16 = 305
KEY_F17 = 306
KEY_F18 = 307
KEY_F19 = 308
KEY_F20 = 309
KEY_F21 = 310
KEY_F22 = 311
KEY_F23 = 312
KEY_F24 = 313
KEY_F25 = 314
KEY_KP_0 = 320
KEY_KP_1 = 321
KEY_KP_2 = 322
KEY_KP_3 = 323
KEY_KP_4 = 324
KEY_KP_5 = 325
KEY_KP_6 = 326
KEY_KP_7 = 327
KEY_KP_8 = 328
KEY_KP_9 = 329
KEY_KP_DECIMAL = 330
KEY_KP_DIVIDE = 331
KEY_KP_MULTIPLY = 332
KEY_KP_SUBTRACT = 333
KEY_KP_ADD = 334
KEY_KP_ENTER = 335
KEY_KP_EQUAL = 336
KEY_LEFT_SHIFT = 340
KEY_LEFT_CONTROL = 341
KEY_LEFT_ALT = 342
KEY_LEFT_SUPER = 343
KEY_RIGHT_SHIFT = 344
KEY_RIGHT_CONTROL = 345
KEY_RIGHT_ALT = 346
KEY_RIGHT_SUPER = 347
KEY_MENU = 348
KEY_LAST = KEY_MENU

# Mouse button definitions 
MOUSE_BUTTON_1 = 0
MOUSE_BUTTON_2 = 1
MOUSE_BUTTON_3 = 2
MOUSE_BUTTON_4 = 3
MOUSE_BUTTON_5 = 4
MOUSE_BUTTON_6 = 5
MOUSE_BUTTON_7 = 6
MOUSE_BUTTON_8 = 7
MOUSE_BUTTON_LAST = MOUSE_BUTTON_8

# Mouse button aliases 
MOUSE_BUTTON_LEFT = MOUSE_BUTTON_1
MOUSE_BUTTON_RIGHT = MOUSE_BUTTON_2
MOUSE_BUTTON_MIDDLE = MOUSE_BUTTON_3

# Joystick identifiers 
JOYSTICK_1 = 0
JOYSTICK_2 = 1
JOYSTICK_3 = 2
JOYSTICK_4 = 3
JOYSTICK_5 = 4
JOYSTICK_6 = 5
JOYSTICK_7 = 6
JOYSTICK_8 = 7
JOYSTICK_9 = 8
JOYSTICK_10 = 9
JOYSTICK_11 = 10
JOYSTICK_12 = 11
JOYSTICK_13 = 12
JOYSTICK_14 = 13
JOYSTICK_15 = 14
JOYSTICK_16 = 15
JOYSTICK_LAST = JOYSTICK_16

"""
Other definitions
"""

# glfwCreateWindow modes 
WINDOWED = 0x00010001
FULLSCREEN = 0x00010002

# glfwGetWindowParam tokens 
ACTIVE = 0x00020001
ICONIFIED = 0x00020002
CLOSE_REQUESTED = 0x00020003
OPENGL_REVISION = 0x00020004

# glfwWindowHint tokens 
RED_BITS = 0x00021000
GREEN_BITS = 0x00021001
BLUE_BITS = 0x00021002
ALPHA_BITS = 0x00021003
DEPTH_BITS = 0x00021004
STENCIL_BITS = 0x00021005
REFRESH_RATE = 0x00021006
ACCUM_RED_BITS = 0x00021007
ACCUM_GREEN_BITS = 0x00021008
ACCUM_BLUE_BITS = 0x00021009
ACCUM_ALPHA_BITS = 0x0002100A
AUX_BUFFERS = 0x0002100B
STEREO = 0x0002100C
FSAA_SAMPLES = 0x0002100E

"""
The following constants are used with both glfwGetWindowParam
 and glfwWindowHint
"""

OPENGL_VERSION_MAJOR = 0x00022000
OPENGL_VERSION_MINOR = 0x00022001
OPENGL_FORWARD_COMPAT = 0x00022002
OPENGL_DEBUG_CONTEXT = 0x00022003
OPENGL_PROFILE = 0x00022004
OPENGL_ROBUSTNESS = 0x00022005
RESIZABLE = 0x00022006
VISIBLE = 0x00022007

# OPENGL_ROBUSTNESS mode tokens 
OPENGL_NO_ROBUSTNESS = 0x00000000
OPENGL_NO_RESET_NOTIFICATION = 0x00000001
OPENGL_LOSE_CONTEXT_ON_RESET = 0x00000002

# OPENGL_PROFILE bit tokens 
OPENGL_NO_PROFILE = 0x00000000
OPENGL_CORE_PROFILE = 0x00000001
OPENGL_COMPAT_PROFILE = 0x00000002
OPENGL_ES2_PROFILE = 0x00000004

# glfwGetInputMode/glfwSetInputMode tokens 
CURSOR_MODE = 0x00030001
STICKY_KEYS = 0x00030002
STICKY_MOUSE_BUTTONS = 0x00030003
SYSTEM_KEYS = 0x00030004
KEY_REPEAT = 0x00030005

# CURSOR_MODE values 
CURSOR_NORMAL = 0x00040001
CURSOR_HIDDEN = 0x00040002
CURSOR_CAPTURED = 0x00040003

# glfwGetJoystickParam tokens 
PRESENT = 0x00050001
AXES = 0x00050002
BUTTONS = 0x00050003

# glfwGetError/glfwErrorString tokens 
NO_ERROR = 0
NOT_INITIALIZED = 0x00070001
NO_CURRENT_CONTEXT = 0x00070002
INVALID_ENUM = 0x00070003
INVALID_VALUE = 0x00070004
OUT_OF_MEMORY = 0x00070005
OPENGL_UNAVAILABLE = 0x00070006
VERSION_UNAVAILABLE = 0x00070007
PLATFORM_ERROR = 0x00070008
WINDOW_NOT_ACTIVE = 0x00070009
FORMAT_UNAVAILABLE = 0x0007000A

# Gamma ramps 
GAMMA_RAMP_SIZE = 256

"""
Typedefs
"""

# OpenGL function pointer type 
glproc = CFUNCTYPE(None, None)

# Window handle type 
window = c_void_p

# Function pointer types 
errorfun = CFUNCTYPE(None, c_int, c_char_p)
windowsizefun = CFUNCTYPE(None, window, c_int, c_int)
windowclosefun = CFUNCTYPE(c_int, window)
windowrefreshfun = CFUNCTYPE(None, window)
windowfocusfun = CFUNCTYPE(None, window, c_int)
windowiconifyfun = CFUNCTYPE(None, window, c_int)
mousebuttonfun = CFUNCTYPE(None, window, c_int, c_int)
cursorposfun = CFUNCTYPE(None, window, c_int, c_int)
cursorenterfun = CFUNCTYPE(None, window, c_int)
scrollfun = CFUNCTYPE(None, window, c_float, c_float)
keyfun = CFUNCTYPE(None, window, c_int, c_int)
charfun = CFUNCTYPE(None, window, c_int)

# The video mode structure used by glfwGetVideoModes
class vidmode(Structure):
    _fields_ = [
        ("width", c_int),
        ("height", c_int),
        ("redBits", c_int),
        ("blueBits", c_int),
        ("greenBits", c_int),
    ]

# Gamma ramp 
class gammaramp(Structure):
    _fields_ = [
        ("red", c_ushort * GAMMA_RAMP_SIZE),
        ("green", c_ushort * GAMMA_RAMP_SIZE),
        ("blue", c_ushort * GAMMA_RAMP_SIZE),
    ]

"""
Prototypes
"""

# Initialization, termination and version querying 
Init = glfwdll.glfwInit
Init.restype = c_int
Init.argtypes = []
Terminate = glfwdll.glfwTerminate
Terminate.restype = None
Terminate.argtypes = []
GetVersion = glfwdll.glfwGetVersion
GetVersion.restype = None
GetVersion.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
GetVersionString = glfwdll.glfwGetVersionString
GetVersionString.restype = c_char_p
GetVersionString.argtypes = []

# Error handling 
GetError = glfwdll.glfwGetError
GetError.restype = c_int
GetError.argtypes = []
ErrorString = glfwdll.glfwErrorString
ErrorString.restype = c_char_p
ErrorString.argtypes = [c_int]
SetErrorCallback = glfwdll.glfwSetErrorCallback
SetErrorCallback.restype = None
SetErrorCallback.argtypes = [errorfun]

# Video mode functions 
GetVideoModes = glfwdll.glfwGetVideoModes
GetVideoModes.restype = POINTER(vidmode)
GetVideoModes.argtypes = [POINTER(c_int)]
GetDesktopMode = glfwdll.glfwGetDesktopMode
GetDesktopMode.restype = None
GetDesktopMode.argtypes = [POINTER(vidmode)]

# Gamma ramp functions 
SetGamma = glfwdll.glfwSetGamma
SetGamma.restype = None
SetGamma.argtypes = [c_float]
GetGammaRamp = glfwdll.glfwGetGammaRamp
GetGammaRamp.restype = None
GetGammaRamp.argtypes = [POINTER(gammaramp)]
SetGammaRamp = glfwdll.glfwSetGammaRamp
SetGammaRamp.restype = None
SetGammaRamp.argtypes = [POINTER(gammaramp)]

# Window handling 
WindowHint = glfwdll.glfwWindowHint
WindowHint.restype = None
WindowHint.argtypes = [c_int, c_int]
CreateWindow = glfwdll.glfwCreateWindow
CreateWindow.restype = window
CreateWindow.argtypes = [c_int, c_int, c_int, c_char_p, window]
DestroyWindow = glfwdll.glfwDestroyWindow
DestroyWindow.restype = None
DestroyWindow.argtypes = [window]
SetWindowTitle = glfwdll.glfwSetWindowTitle
SetWindowTitle.restype = None
SetWindowTitle.argtypes = [window, c_char_p]
GetWindowSize = glfwdll.glfwGetWindowSize
GetWindowSize.restype = None
GetWindowSize.argtypes = [window, POINTER(c_int), POINTER(c_int)]
SetWindowSize = glfwdll.glfwSetWindowSize
SetWindowSize.restype = None
SetWindowSize.argtypes = [window, c_int, c_int]
GetWindowPos = glfwdll.glfwGetWindowPos
GetWindowPos.restype = None
GetWindowPos.argtypes = [window, POINTER(c_int), POINTER(c_int)]
SetWindowPos = glfwdll.glfwSetWindowPos
SetWindowPos.restype = None
SetWindowPos.argtypes = [window, c_int, c_int]
IconifyWindow = glfwdll.glfwIconifyWindow
IconifyWindow.restype = None
IconifyWindow.argtypes = [window]
RestoreWindow = glfwdll.glfwRestoreWindow
RestoreWindow.restype = None
RestoreWindow.argtypes = [window]
ShowWindow = glfwdll.glfwShowWindow
ShowWindow.restype = None
ShowWindow.argtypes = [window]
HideWindow = glfwdll.glfwHideWindow
HideWindow.restype = None
HideWindow.argtypes = [window]
GetWindowParam = glfwdll.glfwGetWindowParam
GetWindowParam.restype = c_int
GetWindowParam.argtypes = [window, c_int]
SetWindowUserPointer = glfwdll.glfwSetWindowUserPointer
SetWindowUserPointer.restype = None
SetWindowUserPointer.argtypes = [window, POINTER(None)]
GetWindowUserPointer = glfwdll.glfwGetWindowUserPointer
GetWindowUserPointer.restype = POINTER(None)
GetWindowUserPointer.argtypes = [window]
SetWindowSizeCallback = glfwdll.glfwSetWindowSizeCallback
SetWindowSizeCallback.restype = None
SetWindowSizeCallback.argtypes = [windowsizefun]
SetWindowCloseCallback = glfwdll.glfwSetWindowCloseCallback
SetWindowCloseCallback.restype = None
SetWindowCloseCallback.argtypes = [windowclosefun]
SetWindowRefreshCallback = glfwdll.glfwSetWindowRefreshCallback
SetWindowRefreshCallback.restype = None
SetWindowRefreshCallback.argtypes = [windowrefreshfun]
SetWindowFocusCallback = glfwdll.glfwSetWindowFocusCallback
SetWindowFocusCallback.restype = None
SetWindowFocusCallback.argtypes = [windowfocusfun]
SetWindowIconifyCallback = glfwdll.glfwSetWindowIconifyCallback
SetWindowIconifyCallback.restype = None
SetWindowIconifyCallback.argtypes = [windowiconifyfun]

# Event handling 
PollEvents = glfwdll.glfwPollEvents
PollEvents.restype = None
PollEvents.argtypes = []
WaitEvents = glfwdll.glfwWaitEvents
WaitEvents.restype = None
WaitEvents.argtypes = []

# Input handling 
GetInputMode = glfwdll.glfwGetInputMode
GetInputMode.restype = c_int
GetInputMode.argtypes = [window, c_int]
SetInputMode = glfwdll.glfwSetInputMode
SetInputMode.restype = None
SetInputMode.argtypes = [window, c_int, c_int]
GetKey = glfwdll.glfwGetKey
GetKey.restype = c_int
GetKey.argtypes = [window, c_int]
GetMouseButton = glfwdll.glfwGetMouseButton
GetMouseButton.restype = c_int
GetMouseButton.argtypes = [window, c_int]
GetCursorPos = glfwdll.glfwGetCursorPos
GetCursorPos.restype = None
GetCursorPos.argtypes = [window, POINTER(c_int), POINTER(c_int)]
SetCursorPos = glfwdll.glfwSetCursorPos
SetCursorPos.restype = None
SetCursorPos.argtypes = [window, c_int, c_int]
GetScrollOffset = glfwdll.glfwGetScrollOffset
GetScrollOffset.restype = None
GetScrollOffset.argtypes = [window, POINTER(c_float), POINTER(c_float)]
SetKeyCallback = glfwdll.glfwSetKeyCallback
SetKeyCallback.restype = None
SetKeyCallback.argtypes = [keyfun]
SetCharCallback = glfwdll.glfwSetCharCallback
SetCharCallback.restype = None
SetCharCallback.argtypes = [charfun]
SetMouseButtonCallback = glfwdll.glfwSetMouseButtonCallback
SetMouseButtonCallback.restype = None
SetMouseButtonCallback.argtypes = [mousebuttonfun]
SetCursorPosCallback = glfwdll.glfwSetCursorPosCallback
SetCursorPosCallback.restype = None
SetCursorPosCallback.argtypes = [cursorposfun]
SetCursorEnterCallback = glfwdll.glfwSetCursorEnterCallback
SetCursorEnterCallback.restype = None
SetCursorEnterCallback.argtypes = [cursorenterfun]
SetScrollCallback = glfwdll.glfwSetScrollCallback
SetScrollCallback.restype = None
SetScrollCallback.argtypes = [scrollfun]

# Joystick input 
GetJoystickParam = glfwdll.glfwGetJoystickParam
GetJoystickParam.restype = c_int
GetJoystickParam.argtypes = [c_int, c_int]
GetJoystickAxes = glfwdll.glfwGetJoystickAxes
GetJoystickAxes.restype = c_int
GetJoystickAxes.argtypes = [c_int, POINTER(c_float), c_int]
GetJoystickButtons = glfwdll.glfwGetJoystickButtons
GetJoystickButtons.restype = c_int
GetJoystickButtons.argtypes = [c_int, unsigned c_char_p, c_int]

# Clipboard 
SetClipboardString = glfwdll.glfwSetClipboardString
SetClipboardString.restype = None
SetClipboardString.argtypes = [window, c_char_p]
GetClipboardString = glfwdll.glfwGetClipboardString
GetClipboardString.restype = c_char_p
GetClipboardString.argtypes = [window]

# Time 
GetTime = glfwdll.glfwGetTime
GetTime.restype = c_float
GetTime.argtypes = []
SetTime = glfwdll.glfwSetTime
SetTime.restype = None
SetTime.argtypes = [c_float]

# OpenGL support 
MakeContextCurrent = glfwdll.glfwMakeContextCurrent
MakeContextCurrent.restype = None
MakeContextCurrent.argtypes = [window]
GetCurrentContext = glfwdll.glfwGetCurrentContext
GetCurrentContext.restype = window
GetCurrentContext.argtypes = []
SwapBuffers = glfwdll.glfwSwapBuffers
SwapBuffers.restype = None
SwapBuffers.argtypes = [window]
SwapInterval = glfwdll.glfwSwapInterval
SwapInterval.restype = None
SwapInterval.argtypes = [c_int]
ExtensionSupported = glfwdll.glfwExtensionSupported
ExtensionSupported.restype = c_int
ExtensionSupported.argtypes = [c_char_p]
GetProcAddress = glfwdll.glfwGetProcAddress
GetProcAddress.restype = glproc
GetProcAddress.argtypes = [c_char_p]
CopyContext = glfwdll.glfwCopyContext
CopyContext.restype = None
CopyContext.argtypes = [window, window, c_ulong]
