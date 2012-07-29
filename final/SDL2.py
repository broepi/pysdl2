import os

from ctypes import *

STRING = c_char_p
_libraries = {}
lib = CDLL(os.path.dirname(os.path.realpath(__file__))+"/libSDL2.so")
WSTRING = c_wchar_p


SDLK_8 = 56
SDLK_7 = 55
SDLK_6 = 54
SDLK_5 = 53
SDLK_4 = 52
SDLK_3 = 51
SDLK_2 = 50
SDLK_1 = 49
SDLK_0 = 48
SDLK_SLASH = 47
SDLK_PERIOD = 46
SDLK_MINUS = 45
SDLK_m = 109
SDLK_COMMA = 44
SDLK_PLUS = 43
# def SDL_AtomicAdd(a,v): return __sync_fetch_and_add(&(a)->value, v) # macro
SDLK_RIGHTPAREN = 41
SDLK_LEFTPAREN = 40
SDLK_AMPERSAND = 38
SDLK_DOLLAR = 36
SDLK_PERCENT = 37
SDLK_HASH = 35
SDLK_QUOTEDBL = 34
SDLK_EXCLAIM = 33
SDLK_SPACE = 32
SDLK_BACKSPACE = 8
SDLK_ESCAPE = 27
SDL_TEXTUREACCESS_TARGET = 2
SDLK_RETURN = 13
SDLK_UNKNOWN = 0
SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG = 4
SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG = 2
SDL_GL_CONTEXT_DEBUG_FLAG = 1
SDLK_KP_MEMRECALL = 1073742033
SDL_TEXTUREACCESS_STREAMING = 1
SDLK_k = 107
SDL_TEXTUREACCESS_STATIC = 0
SDLK_ASTERISK = 42
SDL_TRUE = 1
SDLK_QUOTE = 39
SDL_RENDERER_ACCELERATED = 2
SDLK_AT = 64
SDL_SCANCODE_V = 25
SDLK_h = 104
SDLK_F15 = 1073741930
SDL_PIXELTYPE_INDEX8 = 3
SDL_SCANCODE_CLEAR = 156
SDL_ASSERTION_ALWAYS_IGNORE = 4
SDL_ASSERTION_IGNORE = 3
SDL_ASSERTION_ABORT = 2
SDL_ASSERTION_BREAK = 1
SDL_ASSERTION_RETRY = 0
SDLK_F14 = 1073741929
SDL_SCANCODE_CANCEL = 155
SDLK_KP_BINARY = 1073742042
SDL_PIXELTYPE_INDEX1 = 1
SDL_GETEVENT = 2
SDL_PEEKEVENT = 1
SDLK_KP_EQUALS = 1073741927
SDL_BITMAPORDER_1234 = 2
SDL_BITMAPORDER_4321 = 1
SDL_BITMAPORDER_NONE = 0
SDLK_d = 100
SDLK_POWER = 1073741926
SDL_SCANCODE_LANG9 = 152
SDL_WINDOW_FOREIGN = 2048
SDL_WINDOW_MOUSE_FOCUS = 1024
SDL_WINDOW_INPUT_FOCUS = 512
SDL_WINDOW_INPUT_GRABBED = 256
SDL_WINDOW_MAXIMIZED = 128
SDL_WINDOW_MINIMIZED = 64
SDL_WINDOW_RESIZABLE = 32
SDL_WINDOW_BORDERLESS = 16
SDL_WINDOW_HIDDEN = 8
SDL_WINDOW_SHOWN = 4
SDL_WINDOW_OPENGL = 2
SDL_WINDOW_FULLSCREEN = 1
SDLK_c = 99
SDL_SCANCODE_LANG8 = 151
SDL_LOG_CATEGORY_RESERVED10 = 16
SDL_LOG_CATEGORY_RESERVED9 = 15
SDL_SCANCODE_LANG6 = 149
SDL_LOG_CATEGORY_RESERVED3 = 9
SDL_LOG_CATEGORY_RENDER = 5
SDL_INPUTPROXIMITYOUT = 1285
SDL_INPUTBUTTONUP = 1282
SDL_INPUTBUTTONDOWN = 1281
SDL_INPUTMOTION = 1280
SDL_RENDERER_TARGETTEXTURE = 8
SDL_RENDERER_PRESENTVSYNC = 4
SDL_MOUSEMOTION = 1024
SDL_TEXTINPUT = 771
SDL_KEYUP = 769
SDL_KEYDOWN = 768
SDL_SYSWMEVENT = 513
SDL_QUIT = 256
SDLK_s = 115
SDLK_SLEEP = 1073742106
SDLK_EJECT = 1073742105
SDLK_KBDILLUMDOWN = 1073742103
SDLK_DISPLAYSWITCH = 1073742101
SDLK_BRIGHTNESSUP = 1073742100
SDLK_BRIGHTNESSDOWN = 1073742099
SDL_PIXELFORMAT_RGB24 = -2028988413
SDLK_AC_REFRESH = 1073742097
SDLK_AC_STOP = 1073742096
SDLK_AC_FORWARD = 1073742095
SDLK_AC_BACK = 1073742094
SDLK_AC_SEARCH = 1073742092
SDLK_COMPUTER = 1073742091
SDLK_CALCULATOR = 1073742090
SDLK_WWW = 1073742088
SDLK_MEDIASELECT = 1073742087
SDLK_AUDIOMUTE = 1073742086
SDLK_AUDIOSTOP = 1073742084
SDLK_AUDIOPREV = 1073742083
SDLK_AUDIONEXT = 1073742082
SDL_SCANCODE_LSHIFT = 225
strstr = lib.strstr
strstr.restype = STRING
strstr.argtypes = [STRING, STRING]
SDL_strstr = strstr # alias
SDLK_KP_F = 1073742017
SDL_SCANCODE_LCTRL = 224
SDL_LOG_PRIORITY_INFO = 3
SDL_SCANCODE_KP_MEMCLEAR = 210
SDLK_KP_4 = 1073741916
SDL_WINDOWEVENT_RESTORED = 9
SDL_FALSE = 0
SDLK_KP_E = 1073742016
SDL_NUM_LOG_PRIORITIES = 7
SDL_LOG_PRIORITY_CRITICAL = 6
SDL_LOG_PRIORITY_ERROR = 5
SDL_UNSUPPORTED = 4
SDL_EFSEEK = 3
SDL_EFWRITE = 2
SDL_EFREAD = 1
SDL_ENOMEM = 0
SDLK_KP_3 = 1073741915
SDL_AUDIO_PAUSED = 2
SDL_AUDIO_PLAYING = 1
SDL_AUDIO_STOPPED = 0
size_t = c_ulong
snprintf = lib.snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
SDL_snprintf = snprintf # alias
SDL_SCANCODE_KP_DECIMAL = 220
setenv = lib.setenv
setenv.restype = c_int
setenv.argtypes = [STRING, STRING, c_int]
SDL_setenv = setenv # alias
SDLK_KP_C = 1073742014
SDL_JOYAXISMOTION = 1536
SDL_INPUTPROXIMITYIN = 1284
SDL_INPUTWHEEL = 1283
SDLK_EQUALS = 61
SDLK_KP_PLUSMINUS = 1073742039
log = lib.log
log.restype = c_double
log.argtypes = [c_double]
SDL_log = log # alias
SDLK_KP_ENTER = 1073741912
SDL_SCANCODE_F12 = 69
SDL_MOUSEWHEEL = 1027
SDLK_KP_A = 1073742012
SDL_SCANCODE_INTERNATIONAL5 = 139
SDL_MOUSEBUTTONUP = 1026
SDL_MOUSEBUTTONDOWN = 1025
SDL_RENDERER_SOFTWARE = 1
SDL_SCANCODE_Y = 28
SDL_SCANCODE_X = 27
SDL_SCANCODE_W = 26
SDL_SCANCODE_U = 24
SDL_TEXTEDITING = 770
SDL_WINDOWEVENT_MOVED = 4
SDL_WINDOWEVENT = 512
SDL_FIRSTEVENT = 0
class __va_list_tag(Structure):
    pass
vsnprintf = lib.vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
SDL_vsnprintf = vsnprintf # alias
strtoull = lib.strtoull
strtoull.restype = c_ulonglong
strtoull.argtypes = [STRING, POINTER(STRING), c_int]
SDL_strtoull = strtoull # alias
strtoul = lib.strtoul
strtoul.restype = c_ulong
strtoul.argtypes = [STRING, POINTER(STRING), c_int]
SDL_strtoul = strtoul # alias
strtoll = lib.strtoll
strtoll.restype = c_longlong
strtoll.argtypes = [STRING, POINTER(STRING), c_int]
SDL_strtoll = strtoll # alias
SDLK_KP_MULTIPLY = 1073741909
strtol = lib.strtol
strtol.restype = c_long
strtol.argtypes = [STRING, POINTER(STRING), c_int]
SDL_strtol = strtol # alias
SDLK_KBDILLUMUP = 1073742104
strtod = lib.strtod
strtod.restype = c_double
strtod.argtypes = [STRING, POINTER(STRING)]
SDL_strtod = strtod # alias
SDL_WINDOWEVENT_HIDDEN = 2
strrchr = lib.strrchr
strrchr.restype = STRING
strrchr.argtypes = [STRING, c_int]
SDL_strrchr = strrchr # alias
strncmp = lib.strncmp
strncmp.restype = c_int
strncmp.argtypes = [STRING, STRING, size_t]
SDL_strncmp = strncmp # alias
strncasecmp = lib.strncasecmp
strncasecmp.restype = c_int
strncasecmp.argtypes = [STRING, STRING, size_t]
SDL_strncasecmp = strncasecmp # alias
strlen = lib.strlen
strlen.restype = size_t
strlen.argtypes = [STRING]
SDL_strlen = strlen # alias
strdup = lib.strdup
strdup.restype = STRING
strdup.argtypes = [STRING]
SDL_strdup = strdup # alias
strcmp = lib.strcmp
strcmp.restype = c_int
strcmp.argtypes = [STRING, STRING]
SDL_strcmp = strcmp # alias
strchr = lib.strchr
strchr.restype = STRING
strchr.argtypes = [STRING, c_int]
SDL_strchr = strchr # alias
strcasecmp = lib.strcasecmp
strcasecmp.restype = c_int
strcasecmp.argtypes = [STRING, STRING]
SDL_strcasecmp = strcasecmp # alias
sscanf = lib.sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
SDL_sscanf = sscanf # alias
sqrt = lib.sqrt
sqrt.restype = c_double
sqrt.argtypes = [c_double]
SDL_sqrt = sqrt # alias
SDLK_KBDILLUMTOGGLE = 1073742102
sinf = lib.sinf
sinf.restype = c_float
sinf.argtypes = [c_float]
SDL_sinf = sinf # alias
sin = lib.sin
sin.restype = c_double
sin.argtypes = [c_double]
SDL_sin = sin # alias
scalbn = lib.scalbn
scalbn.restype = c_double
scalbn.argtypes = [c_double, c_int]
SDL_scalbn = scalbn # alias
realloc = lib.realloc
realloc.restype = c_void_p
realloc.argtypes = [c_void_p, size_t]
SDL_realloc = realloc # alias
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
qsort = lib.qsort
qsort.restype = None
qsort.argtypes = [c_void_p, size_t, size_t, __compar_fn_t]
SDL_qsort = qsort # alias
pow = lib.pow
pow.restype = c_double
pow.argtypes = [c_double, c_double]
SDL_pow = pow # alias
memset = lib.memset
memset.restype = c_void_p
memset.argtypes = [c_void_p, c_int, size_t]
SDL_memset = memset # alias
memmove = lib.memmove
memmove.restype = c_void_p
memmove.argtypes = [c_void_p, c_void_p, size_t]
SDL_memmove = memmove # alias
memcpy = lib.memcpy
memcpy.restype = c_void_p
memcpy.argtypes = [c_void_p, c_void_p, size_t]
SDL_memcpy = memcpy # alias
memcmp = lib.memcmp
memcmp.restype = c_int
memcmp.argtypes = [c_void_p, c_void_p, size_t]
SDL_memcmp = memcmp # alias
malloc = lib.malloc
malloc.restype = c_void_p
malloc.argtypes = [size_t]
SDL_malloc = malloc # alias
iconv_t = c_void_p
SDL_iconv_t = iconv_t # alias
iconv_open = lib.iconv_open
iconv_open.restype = iconv_t
iconv_open.argtypes = [STRING, STRING]
SDL_iconv_open = iconv_open # alias
# SDL_FILE = __FILE__ # alias
iconv_close = lib.iconv_close
iconv_close.restype = c_int
iconv_close.argtypes = [iconv_t]
SDL_iconv_close = iconv_close # alias
getenv = lib.getenv
getenv.restype = STRING
getenv.argtypes = [STRING]
SDL_getenv = getenv # alias
free = lib.free
free.restype = None
free.argtypes = [c_void_p]
SDL_free = free # alias
floor = lib.floor
floor.restype = c_double
floor.argtypes = [c_double]
SDL_floor = floor # alias
fabs = lib.fabs
fabs.restype = c_double
fabs.argtypes = [c_double]
SDL_fabs = fabs # alias
cosf = lib.cosf
cosf.restype = c_float
cosf.argtypes = [c_float]
SDL_cosf = cosf # alias
cos = lib.cos
cos.restype = c_double
cos.argtypes = [c_double]
SDL_cos = cos # alias
copysign = lib.copysign
copysign.restype = c_double
copysign.argtypes = [c_double, c_double]
SDL_copysign = copysign # alias
SDLK_AC_BOOKMARKS = 1073742098
ceil = lib.ceil
ceil.restype = c_double
ceil.argtypes = [c_double]
SDL_ceil = ceil # alias
calloc = lib.calloc
calloc.restype = c_void_p
calloc.argtypes = [size_t, size_t]
SDL_calloc = calloc # alias
atoi = lib.atoi
atoi.restype = c_int
atoi.argtypes = [STRING]
SDL_atoi = atoi # alias
atof = lib.atof
atof.restype = c_double
atof.argtypes = [STRING]
SDL_atof = atof # alias
atan2 = lib.atan2
atan2.restype = c_double
atan2.argtypes = [c_double, c_double]
SDL_atan2 = atan2 # alias
atan = lib.atan
atan.restype = c_double
atan.argtypes = [c_double]
SDL_atan = atan # alias
abs = lib.abs
abs.restype = c_int
abs.argtypes = [c_int]
SDL_abs = abs # alias
# SDL_LINE = __LINE__ # alias
# SDL_FUNCTION = __FUNCTION__ # alias
class SDL_Surface(Structure):
    pass
class SDL_Rect(Structure):
    pass
SDL_UpperBlitScaled = lib.SDL_UpperBlitScaled
SDL_UpperBlitScaled.restype = c_int
SDL_UpperBlitScaled.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
SDL_BlitScaled = SDL_UpperBlitScaled # alias
class SDL_Color(Structure):
    pass
SDL_Colour = SDL_Color # alias
SDL_UpperBlit = lib.SDL_UpperBlit
SDL_UpperBlit.restype = c_int
SDL_UpperBlit.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
SDL_BlitSurface = SDL_UpperBlit # alias
__LITTLE_ENDIAN = 1234 # Variable c_int '1234'
__BYTE_ORDER = __LITTLE_ENDIAN # alias
SDL_BYTEORDER = __BYTE_ORDER # alias
SDL_GL_CONTEXT_PROFILE_MASK = 21
SDL_GL_CONTEXT_EGL = 19
SDLK_AC_HOME = 1073742093
SDL_GL_CONTEXT_MINOR_VERSION = 18
SDL_GL_CONTEXT_MAJOR_VERSION = 17
SDL_GL_RETAINED_BACKING = 16
SDL_GL_MULTISAMPLESAMPLES = 14
SDL_PIXELFORMAT_YVYU = 1431918169
SDL_GL_STEREO = 12
SDL_GL_ACCUM_ALPHA_SIZE = 11
SDL_PIXELFORMAT_IYUV = 1448433993
SDL_PIXELFORMAT_YV12 = 842094169
SDL_PIXELFORMAT_ARGB2101010 = -2043207676
SDL_PIXELFORMAT_BGRA8888 = -2038030332
SDL_GL_DEPTH_SIZE = 6
SDL_GL_DOUBLEBUFFER = 5
SDL_GL_BUFFER_SIZE = 4
SDL_GL_ALPHA_SIZE = 3
SDL_GL_BLUE_SIZE = 2
SDL_GL_RED_SIZE = 0
SDLK_MAIL = 1073742089
SDL_PIXELFORMAT_BGRX8888 = -2040129532
SDL_PIXELFORMAT_BGR888 = -2041178108
SDL_PIXELFORMAT_RGB888 = -2045372412
SDL_PIXELFORMAT_BGR24 = -2025842685
SDL_PIXELFORMAT_BGR565 = -2058022910
SDL_PIXELFORMAT_RGB565 = -2062217214
SDL_PIXELFORMAT_BGRA5551 = -2054942718
SDL_PIXELFORMAT_ABGR1555 = -2056056830
SDL_PIXELFORMAT_RGBA5551 = -2059137022
SDL_PIXELFORMAT_ARGB1555 = -2060251134
SDL_PIXELFORMAT_BGRA4444 = -2055073790
SDL_PIXELFORMAT_ABGR4444 = -2056122366
SDL_PIXELFORMAT_RGBA4444 = -2059268094
SDL_PIXELFORMAT_ARGB4444 = -2060316670
SDL_PIXELFORMAT_BGR555 = -2058154238
SDL_PIXELFORMAT_RGB555 = -2062348542
SDL_PIXELFORMAT_RGB444 = -2062414846
SDL_PIXELFORMAT_RGB332 = -2079258623
SDL_PIXELFORMAT_INDEX8 = -2097149951
SDL_PIXELFORMAT_INDEX4MSB = -2111831040
SDL_PIXELFORMAT_INDEX4LSB = -2112879616
SDL_PIXELFORMAT_INDEX1MSB = -2128609024
SDL_PIXELFORMAT_INDEX1LSB = -2129657600
SDL_PIXELFORMAT_UNKNOWN = 0
SDL_PACKEDLAYOUT_1010102 = 8
SDL_PACKEDLAYOUT_2101010 = 7
SDL_PACKEDLAYOUT_8888 = 6
SDL_PACKEDLAYOUT_565 = 5
SDL_PACKEDLAYOUT_5551 = 4
SDL_PACKEDLAYOUT_1555 = 3
SDL_PACKEDLAYOUT_4444 = 2
SDL_PACKEDLAYOUT_332 = 1
SDL_PACKEDLAYOUT_NONE = 0
SDL_ARRAYORDER_ABGR = 6
SDL_ARRAYORDER_BGR = 4
SDL_ARRAYORDER_ARGB = 3
SDL_ARRAYORDER_RGBA = 2
SDL_ARRAYORDER_RGB = 1
SDL_GL_CONTEXT_FLAGS = 20
SDL_ARRAYORDER_NONE = 0
SDL_PACKEDORDER_BGRA = 8
SDL_PACKEDORDER_BGRX = 6
SDL_PACKEDORDER_XBGR = 5
SDL_PACKEDORDER_ARGB = 3
SDL_PACKEDORDER_RGBX = 2
SDL_PACKEDORDER_XRGB = 1
SDL_PACKEDORDER_NONE = 0
SDL_PIXELTYPE_ARRAYF32 = 11
SDL_PIXELTYPE_ARRAYF16 = 10
SDL_PIXELTYPE_ARRAYU32 = 9
SDL_PIXELTYPE_ARRAYU16 = 8
SDL_PIXELTYPE_PACKED32 = 6
SDL_PIXELTYPE_PACKED16 = 5
SDL_PIXELTYPE_PACKED8 = 4
SDL_SCANCODE_S = 22
SDL_SCANCODE_R = 21
SDL_SCANCODE_P = 19
SDL_SCANCODE_L = 15
SDL_SCANCODE_K = 14
SDL_WINDOWEVENT_FOCUS_LOST = 13
SDL_SCANCODE_LALT = 226
SDL_WINDOWEVENT_FOCUS_GAINED = 12
SDL_WINDOWEVENT_LEAVE = 11
SDL_WINDOWEVENT_ENTER = 10
SDL_TEXTUREMODULATE_ALPHA = 2
SDL_WINDOWEVENT_MAXIMIZED = 8
SDL_WINDOWEVENT_MINIMIZED = 7
SDL_WINDOWEVENT_SIZE_CHANGED = 6
SDL_SCANCODE_B = 5
SDL_SCANCODE_A = 4
SDL_WINDOWEVENT_EXPOSED = 3
SDL_GL_MULTISAMPLEBUFFERS = 13
SDL_WINDOWEVENT_NONE = 0
SDL_SCANCODE_KP_HEXADECIMAL = 221
SDL_PIXELFORMAT_YUY2 = 844715353
SDL_ADDEVENT = 0
SDLK_RCTRL = 1073742052
SDLK_LGUI = 1073742051
SDL_SCANCODE_KP_CLEARENTRY = 217
SDL_GL_CONTEXT_PROFILE_ES2 = 4
SDL_GL_CONTEXT_PROFILE_COMPATIBILITY = 2
SDL_GL_CONTEXT_PROFILE_CORE = 1
SDL_SCANCODE_KP_CLEAR = 216
SDL_BLENDMODE_MOD = 4
SDL_BLENDMODE_BLEND = 1
SDL_BLENDMODE_NONE = 0
SDL_PIXELFORMAT_RGBA8888 = -2042224636
def SDL_PIXELLAYOUT(X): return (((X) >> 16) & 0x0F) # macro
SDL_PIXELFORMAT_ARGB8888 = -2043273212
SDL_SCANCODE_F1 = 58
SDL_SCANCODE_KP_MEMSUBTRACT = 212
SDL_GL_GREEN_SIZE = 1
SDLK_KP_CLEAR = 1073742040
SDL_SCANCODE_KP_MEMSTORE = 208
SDLK_KP_MEMDIVIDE = 1073742038
SDL_THREAD_PRIORITY_HIGH = 2
SDL_THREAD_PRIORITY_NORMAL = 1
SDL_THREAD_PRIORITY_LOW = 0
SDL_SCANCODE_KP_AT = 206
SDLK_KP_MEMSUBTRACT = 1073742036
SDL_SCANCODE_KP_HASH = 204
SDLK_KP_MEMCLEAR = 1073742034
SDL_SCANCODE_KP_DBLVERTICALBAR = 202
SDL_SCANCODE_CUT = 123
SDL_SCANCODE_KP_VERTICALBAR = 201
SDL_SCANCODE_KP_DBLAMPERSAND = 200
SDL_SCANCODE_KP_AMPERSAND = 199
SDLK_KP_SPACE = 1073742029
SDL_SCANCODE_KP_LESS = 197
SDL_SCANCODE_KP_PERCENT = 196
SDLK_KP_DBLVERTICALBAR = 1073742026
SDL_SCANCODE_KP_XOR = 194
SDL_SCANCODE_KP_F = 193
SDLK_HOME = 1073741898
SDLK_KP_AMPERSAND = 1073742023
SDLK_KP_GREATER = 1073742022
SDLK_KP_PERCENT = 1073742020
SDL_SCANCODE_KP_MEMDIVIDE = 214
SDLK_KP_POWER = 1073742019
SDLK_INSERT = 1073741897
SDL_SCANCODE_KP_BACKSPACE = 187
SDL_SCANCODE_STOP = 120
SDLK_AUDIOPLAY = 1073742085
SDLK_KP_D = 1073742015
SDL_PIXELFORMAT_RGBX8888 = -2044323836
SDLK_KP_B = 1073742013
SDL_SCANCODE_SELECT = 119
SDL_SCANCODE_CURRENCYUNIT = 180
SDL_SCANCODE_DECIMALSEPARATOR = 179
SDLK_KP_RIGHTBRACE = 1073742009
SDL_SCANCODE_KP_000 = 177
SDL_SCANCODE_T = 23
SDL_SCANCODE_KP_00 = 176
SDL_SCANCODE_F14 = 105
SDLK_KP_LEFTPAREN = 1073742006
SDLK_CURRENCYSUBUNIT = 1073742005
SDL_SCANCODE_G = 10
SDL_SCANCODE_CLEARAGAIN = 162
SDL_SCANCODE_OPER = 161
SDL_SCANCODE_OUT = 160
SDL_FLIP_VERTICAL = 2
SDL_FLIP_HORIZONTAL = 1
SDL_FLIP_NONE = 0
SDL_SCANCODE_SEPARATOR = 159
SDLK_KP_00 = 1073742000
SDL_SCANCODE_BACKSLASH = 49
SDL_SCANCODE_PRIOR = 157
SDLK_RETURN2 = 1073741982
SDLK_CRSEL = 1073741987
SDLK_MODE = 1073742081
SDLK_CLEARAGAIN = 1073741986
# def SDL_iconv_utf8_ucs2(S): return (Uint16 *)SDL_iconv_string("UCS-2", "UTF-8", S, SDL_strlen(S)+1) # macro
SDLK_OPER = 1073741985
SDL_SCANCODE_KP_MEMMULTIPLY = 213
SDL_SCANCODE_ALTERASE = 153
SDL_SCANCODE_RIGHTBRACKET = 48
SDL_SCANCODE_F24 = 115
SDLK_PRIOR = 1073741981
SDL_SCANCODE_LANG5 = 148
SDL_SCANCODE_LEFTBRACKET = 47
SDLK_SYSREQ = 1073741978
SDL_SCANCODE_LANG3 = 146
SDL_HINT_OVERRIDE = 2
SDL_HINT_NORMAL = 1
SDL_HINT_DEFAULT = 0
SDL_SCANCODE_LANG2 = 145
SDLK_KP_COMMA = 1073741957
def SDL_AtomicCASPtr(a,oldval,newval): return __sync_bool_compare_and_swap(a, oldval, newval) # macro
# def SDL_AtomicCAS(a,oldval,newval): return __sync_bool_compare_and_swap(&(a)->value, oldval, newval) # macro
SDLK_VOLUMEDOWN = 1073741953
# def SDL_AUDIO_ISUNSIGNED(x): return (!SDL_AUDIO_ISSIGNED(x)) # macro
def SDL_AUDIO_ISSIGNED(x): return (x & SDL_AUDIO_MASK_SIGNED) # macro
SDL_SCANCODE_INTERNATIONAL8 = 142
# def SDL_AUDIO_ISLITTLEENDIAN(x): return (!SDL_AUDIO_ISBIGENDIAN(x)) # macro
# def SDL_AUDIO_ISINT(x): return (!SDL_AUDIO_ISFLOAT(x)) # macro
def SDL_AUDIO_ISFLOAT(x): return (x & SDL_AUDIO_MASK_DATATYPE) # macro
SDLK_MUTE = 1073741951
def SDL_AUDIO_ISBIGENDIAN(x): return (x & SDL_AUDIO_MASK_ENDIAN) # macro
def SDL_AUDIO_BITSIZE(x): return (x & SDL_AUDIO_MASK_BITSIZE) # macro
SDL_SCANCODE_INTERNATIONAL6 = 140
SDL_PACKEDORDER_ABGR = 7
SDL_SCANCODE_INTERNATIONAL3 = 137
SDL_SCANCODE_F21 = 112
SDL_SCANCODE_N = 17
SDL_GL_ACCELERATED_VISUAL = 15
SDL_SCANCODE_INTERNATIONAL2 = 136
SDL_SCANCODE_INTERNATIONAL1 = 135
SDL_LOG_CATEGORY_CUSTOM = 17
SDL_SCANCODE_KP_EQUALSAS400 = 134
SDL_LASTERROR = 5
SDL_LOG_CATEGORY_RESERVED8 = 14
SDL_LOG_CATEGORY_RESERVED7 = 13
SDL_LOG_CATEGORY_RESERVED6 = 12
SDL_LOG_CATEGORY_RESERVED5 = 11
SDLK_SELECT = 1073741943
SDL_LOG_CATEGORY_RESERVED4 = 10
SDL_LOG_PRIORITY_WARN = 4
SDL_LOG_CATEGORY_RESERVED2 = 8
SDL_LOG_CATEGORY_RESERVED1 = 7
SDL_LOG_CATEGORY_INPUT = 6
SDL_LOG_CATEGORY_VIDEO = 4
SDL_LOG_CATEGORY_AUDIO = 3
SDL_LOG_CATEGORY_SYSTEM = 2
SDL_LOG_CATEGORY_ERROR = 1
SDL_SCANCODE_M = 16
SDL_LOG_CATEGORY_APPLICATION = 0
SDL_LOG_PRIORITY_DEBUG = 2
SDL_LOG_PRIORITY_VERBOSE = 1
SDL_LASTEVENT = 65535
SDL_USEREVENT = 32768
SDL_DROPFILE = 4096
SDL_CLIPBOARDUPDATE = 2304
SDLK_F23 = 1073741938
SDL_MULTIGESTURE = 2050
SDL_DOLLARRECORD = 2049
SDL_DOLLARGESTURE = 2048
SDL_TOUCHBUTTONUP = 1796
SDL_TOUCHBUTTONDOWN = 1795
SDL_FINGERMOTION = 1794
SDL_SCANCODE_COPY = 124
SDL_FINGERUP = 1793
SDL_FINGERDOWN = 1792
SDL_SCANCODE_F19 = 110
SDL_JOYBUTTONUP = 1540
SDL_ARRAYORDER_BGRA = 5
SDL_JOYBUTTONDOWN = 1539
SDL_JOYHATMOTION = 1538
SDL_JOYBALLMOTION = 1537
SDLK_F21 = 1073741936
SDL_SCANCODE_UNDO = 122
SDL_SCANCODE_AGAIN = 121
SDLK_F18 = 1073741933
SDLK_F5 = 1073741886
SDLK_F17 = 1073741932
SDL_SCANCODE_F18 = 109
SDLK_F16 = 1073741931
SDL_SCANCODE_7 = 36
SDL_SCANCODE_KP_C = 190
SDL_PIXELTYPE_INDEX4 = 2
SDL_SCANCODE_Q = 20
SDL_PIXELTYPE_UNKNOWN = 0
SDL_SCANCODE_O = 18
SDL_SCANCODE_J = 13
SDLK_RALT = 1073742054
# def SDL_RectEquals(A,B): return (((A)) && ((B)) && ((A)->x == (B)->x) && ((A)->y == (B)->y) && ((A)->w == (B)->w) && ((A)->h == (B)->h)) # macro
SDL_SCANCODE_F20 = 111
SDL_WINDOWEVENT_CLOSE = 14
SDLK_F3 = 1073741884
SDL_SCANCODE_F16 = 107
SDL_PIXELTYPE_ARRAYU8 = 7
SDL_SCANCODE_I = 12
SDL_GL_ACCUM_BLUE_SIZE = 10
SDLK_KP_8 = 1073741920
def SDL_zerop(x): return SDL_memset((x), 0, sizeof(*(x))) # macro
# def SDL_zero(x): return SDL_memset(&(x), 0, sizeof((x))) # macro
# def SDL_uitoa(value,string,radix): return SDL_ultoa((long)value, string, radix) # macro
SDL_PIXELFORMAT_UYVY = 1498831189
def SDL_toupper(X): return toupper(X) # macro
def SDL_tolower(X): return tolower(X) # macro
def SDL_static_cast(type,expression): return static_cast<type>(expression) # macro
# def SDL_stack_alloc(type,count): return (type*)alloca(sizeof(type)*(count)) # macro
# def SDL_RWclose(ctx): return (ctx)->close(ctx) # macro
def SDL_reinterpret_cast(type,expression): return reinterpret_cast<type>(expression) # macro
# def SDL_min(x,y): return (((x) < (y)) ? (x) : (y)) # macro
SDL_SCANCODE_F15 = 106
# def SDL_memset4(dst,val,len): return do { unsigned _count = (len); unsigned _n = (_count + 3) / 4; Uint32 *_p = SDL_static_cast(Uint32 *, dst); Uint32 _val = (val); if (len == 0) break; switch (_count % 4) { case 0: do { *_p++ = _val; case 3: *_p++ = _val; case 2: *_p++ = _val; case 1: *_p++ = _val; } while ( --_n ); } } while(0) # macro
def SDL_memcpy4(dst,src,len): return SDL_memcpy((dst), (src), (len) << 2) # macro
# def SDL_max(x,y): return (((x) > (y)) ? (x) : (y)) # macro
# def SDL_itoa(value,string,radix): return SDL_ltoa((long)value, string, radix) # macro
SDL_SCANCODE_F = 9
def SDL_isspace(X): return isspace(X) # macro
def SDL_isdigit(X): return isdigit(X) # macro
SDL_BLENDMODE_ADD = 2
# def SDL_iconv_utf8_ucs4(S): return (Uint32 *)SDL_iconv_string("UCS-4", "UTF-8", S, SDL_strlen(S)+1) # macro
def SDL_iconv_utf8_locale(S): return SDL_iconv_string("", "UTF-8", S, SDL_strlen(S)+1) # macro
SDL_TEXTUREMODULATE_COLOR = 1
# def SDL_enabled_assert(condition): return do { while ( !(condition) ) { static struct SDL_assert_data assert_data = { 0, 0, #condition, 0, 0, 0, 0 }; const SDL_assert_state state = SDL_ReportAssertion(&assert_data, SDL_FUNCTION, SDL_FILE, SDL_LINE); if (state == SDL_ASSERTION_RETRY) { continue; } else if (state == SDL_ASSERTION_BREAK) { SDL_TriggerBreakpoint(); } break; } } while (0) # macro
# def SDL_disabled_assert(condition): return do { (void) sizeof ((condition)); } while (0) # macro
def SDL_assert_release(condition): return SDL_enabled_assert(condition) # macro
def SDL_assert_paranoid(condition): return SDL_disabled_assert(condition) # macro
SDL_SCANCODE_H = 11
def SDL_assert(condition): return SDL_disabled_assert(condition) # macro
SDL_GL_ACCUM_GREEN_SIZE = 9
def SDL_arraysize(array): return (sizeof(array)/sizeof(array[0])) # macro
SDL_TEXTUREMODULATE_NONE = 0
def SDL_WINDOWPOS_UNDEFINED_DISPLAY(X): return (SDL_WINDOWPOS_UNDEFINED_MASK|(X)) # macro
def SDL_WINDOWPOS_ISUNDEFINED(X): return (((X)&0xFFFF0000) == SDL_WINDOWPOS_UNDEFINED_MASK) # macro
def SDL_WINDOWPOS_ISCENTERED(X): return (((X)&0xFFFF0000) == SDL_WINDOWPOS_CENTERED_MASK) # macro
def SDL_WINDOWPOS_CENTERED_DISPLAY(X): return (SDL_WINDOWPOS_CENTERED_MASK|(X)) # macro
def SDL_VERSION_ATLEAST(X,Y,Z): return (SDL_COMPILEDVERSION >= SDL_VERSIONNUM(X, Y, Z)) # macro
def SDL_VERSIONNUM(X,Y,Z): return ((X)*1000 + (Y)*100 + (Z)) # macro
# def SDL_VERSION(x): return { (x)->major = SDL_MAJOR_VERSION; (x)->minor = SDL_MINOR_VERSION; (x)->patch = SDL_PATCHLEVEL; } # macro
def SDL_Unsupported(): return SDL_Error(SDL_UNSUPPORTED) # macro
SDL_WINDOWEVENT_RESIZED = 5
def SDL_UnlockMutex(m): return SDL_mutexV(m) # macro
SDLK_TAB = 9
# def SDL_TriggerBreakpoint(): return __asm__ __volatile__ ( "int $3\n\t" ) # macro
def SDL_TABLESIZE(table): return SDL_arraysize(table) # macro
def SDL_SwapLE64(X): return (X) # macro
def SDL_SwapLE32(X): return (X) # macro
def SDL_SwapLE16(X): return (X) # macro
def SDL_SwapFloatLE(X): return (X) # macro
def SDL_SwapFloatBE(X): return SDL_SwapFloat(X) # macro
def SDL_SwapBE64(X): return SDL_Swap64(X) # macro
SDL_SCANCODE_UNKNOWN = 0
def SDL_SwapBE32(X): return SDL_Swap32(X) # macro
def SDL_SwapBE16(X): return SDL_Swap16(X) # macro
def SDL_SaveBMP(surface,file): return SDL_SaveBMP_RW(surface, SDL_RWFromFile(file, "wb"), 1) # macro
SDL_GL_ACCUM_RED_SIZE = 8
def SDL_SCANCODE_TO_KEYCODE(X): return (X | SDLK_SCANCODE_MASK) # macro
SDL_SCANCODE_KP_0 = 98
# def SDL_RectEmpty(X): return ((!(X)) || ((X)->w <= 0) || ((X)->h <= 0)) # macro
# def SDL_RWwrite(ctx,ptr,size,n): return (ctx)->write(ctx, ptr, size, n) # macro
# def SDL_RWtell(ctx): return (ctx)->seek(ctx, 0, RW_SEEK_CUR) # macro
# def SDL_RWseek(ctx,offset,whence): return (ctx)->seek(ctx, offset, whence) # macro
# def SDL_RWread(ctx,ptr,size,n): return (ctx)->read(ctx, ptr, size, n) # macro
SDL_WINDOWEVENT_SHOWN = 1
def SDL_QuitRequested(): return (SDL_PumpEvents(), (SDL_PeepEvents(NULL,0,SDL_PEEKEVENT,SDL_QUIT,SDL_QUIT) > 0)) # macro
def SDL_PIXELTYPE(X): return (((X) >> 24) & 0x0F) # macro
def SDL_PIXELORDER(X): return (((X) >> 20) & 0x0F) # macro
SDL_SCANCODE_KP_8 = 96
def SDL_OutOfMemory(): return SDL_Error(SDL_ENOMEM) # macro
# def SDL_MUSTLOCK(S): return (((S)->flags & SDL_RLEACCEL) != 0) # macro
def SDL_LockMutex(m): return SDL_mutexP(m) # macro
SDLK_NUMLOCKCLEAR = 1073741907
def SDL_LoadWAV(file,spec,audio_buf,audio_len): return SDL_LoadWAV_RW(SDL_RWFromFile(file, "rb"),1, spec,audio_buf,audio_len) # macro
def SDL_LoadBMP(file): return SDL_LoadBMP_RW(SDL_RWFromFile(file, "rb"), 1) # macro
# def SDL_ISPIXELFORMAT_INDEXED(format): return (!SDL_ISPIXELFORMAT_FOURCC(format) && ((SDL_PIXELTYPE(format) == SDL_PIXELTYPE_INDEX1) || (SDL_PIXELTYPE(format) == SDL_PIXELTYPE_INDEX4) || (SDL_PIXELTYPE(format) == SDL_PIXELTYPE_INDEX8))) # macro
# def SDL_ISPIXELFORMAT_FOURCC(format): return ((format) && !((format) & 0x80000000)) # macro
SDL_SCANCODE_KP_6 = 94
# def SDL_ISPIXELFORMAT_ALPHA(format): return (!SDL_ISPIXELFORMAT_FOURCC(format) && ((SDL_PIXELORDER(format) == SDL_PACKEDORDER_ARGB) || (SDL_PIXELORDER(format) == SDL_PACKEDORDER_RGBA) || (SDL_PIXELORDER(format) == SDL_PACKEDORDER_ABGR) || (SDL_PIXELORDER(format) == SDL_PACKEDORDER_BGRA))) # macro
def SDL_GetEventState(type): return SDL_EventState(type, SDL_QUERY) # macro
def SDL_FOURCC(A,B,C,D): return ((SDL_static_cast(Uint32, SDL_static_cast(Uint8, (A))) << 0) | (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (B))) << 8) | (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (C))) << 16) | (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (D))) << 24)) # macro
def SDL_DEFINE_PIXELFOURCC(A,B,C,D): return SDL_FOURCC(A, B, C, D) # macro
SDL_GL_STENCIL_SIZE = 7
SDLK_DOWN = 1073741905
def SDL_DEFINE_PIXELFORMAT(type,order,layout,bits,bytes): return ((1 << 31) | ((type) << 24) | ((order) << 20) | ((layout) << 16) | ((bits) << 8) | ((bytes) << 0)) # macro
# def SDL_CompilerBarrier(): return __asm__ __volatile__ ("" : : : "memory") # macro
SDLK_LEFT = 1073741904
def SDL_BUTTON(X): return (1 << ((X)-1)) # macro
def SDL_AtomicSetPtr(a,v): return __sync_lock_test_and_set(a, v) # macro
# def SDL_AtomicSet(a,v): return __sync_lock_test_and_set(&(a)->value, v) # macro
def SDL_AtomicIncRef(a): return SDL_AtomicAdd(a, 1) # macro
def SDL_AtomicDecRef(a): return (SDL_AtomicAdd(a, -1) == 1) # macro
SDL_SCANCODE_KP_3 = 91
SDLK_z = 122
SDL_SCANCODE_KP_2 = 90
SDLK_COPY = 1073741948
SDL_SCANCODE_E = 8
SDLK_END = 1073741901
SDLK_DELETE = 127
SDLK_PAGEUP = 1073741899
SDL_SCANCODE_D = 7
SDL_SCANCODE_KP_MULTIPLY = 85
SDL_SCANCODE_POWER = 102
SDLK_PAUSE = 1073741896
SDLK_LCTRL = 1073742048
SDL_SCANCODE_NUMLOCKCLEAR = 83
SDLK_PRINTSCREEN = 1073741894
SDLK_F12 = 1073741893
SDLK_F11 = 1073741892
# def SDL_COMPILE_TIME_ASSERT(name,x): return typedef int SDL_dummy_ ## name[(x) * 2 - 1] # macro
SDL_SCANCODE_APPLICATION = 101
SDL_SCANCODE_C = 6
SDLK_F10 = 1073741891
SDL_PIXELFORMAT_ABGR8888 = -2039078908
SDL_SCANCODE_PAGEDOWN = 78
# def SDL_BYTESPERPIXEL(X): return (SDL_ISPIXELFORMAT_FOURCC(X) ? ((((X) == SDL_PIXELFORMAT_YUY2) || ((X) == SDL_PIXELFORMAT_UYVY) || ((X) == SDL_PIXELFORMAT_YVYU)) ? 2 : 1) : (((X) >> 0) & 0xFF)) # macro
SDLK_F8 = 1073741889
SDL_SCANCODE_DELETE = 76
def SDL_BITSPERPIXEL(X): return (((X) >> 8) & 0xFF) # macro
SDL_SCANCODE_PAGEUP = 75
SDL_SCANCODE_HOME = 74
SDL_SCANCODE_INSERT = 73
SDL_SCANCODE_SCROLLLOCK = 71
SDL_SCANCODE_PRINTSCREEN = 70
SDL_SCANCODE_KP_PERIOD = 99
SDL_PACKEDORDER_RGBA = 4
SDL_SCANCODE_F11 = 68
SDL_SCANCODE_F10 = 67
SDL_SCANCODE_F9 = 66
SDL_SCANCODE_F8 = 65
SDL_SCANCODE_F7 = 64
SDL_NUM_SCANCODES = 512
SDL_SCANCODE_SLEEP = 282
SDL_SCANCODE_EJECT = 281
SDL_SCANCODE_KBDILLUMUP = 280
SDL_SCANCODE_KBDILLUMDOWN = 279
SDL_SCANCODE_KBDILLUMTOGGLE = 278
SDL_SCANCODE_F6 = 63
SDL_SCANCODE_DISPLAYSWITCH = 277
SDL_SCANCODE_BRIGHTNESSUP = 276
SDL_SCANCODE_BRIGHTNESSDOWN = 275
SDL_SCANCODE_AC_BOOKMARKS = 274
SDL_SCANCODE_AC_REFRESH = 273
SDL_SCANCODE_AC_STOP = 272
SDLK_t = 116
SDL_SCANCODE_AC_FORWARD = 271
SDL_SCANCODE_AC_BACK = 270
SDL_SCANCODE_AC_HOME = 269
SDL_SCANCODE_AC_SEARCH = 268
SDL_SCANCODE_COMPUTER = 267
SDL_SCANCODE_CALCULATOR = 266
SDL_SCANCODE_MAIL = 265
SDL_SCANCODE_WWW = 264
SDL_SCANCODE_MEDIASELECT = 263
SDL_SCANCODE_AUDIOMUTE = 262
SDL_SCANCODE_AUDIOPLAY = 261
SDL_SCANCODE_AUDIOSTOP = 260
SDL_SCANCODE_F3 = 60
SDL_SCANCODE_AUDIOPREV = 259
SDLK_MENU = 1073741942
SDL_SCANCODE_AUDIONEXT = 258
SDL_SCANCODE_MODE = 257
SDL_SCANCODE_RGUI = 231
SDL_SCANCODE_RALT = 230
SDLK_q = 113
SDL_SCANCODE_RSHIFT = 229
SDL_SCANCODE_RCTRL = 228
SDL_SCANCODE_LGUI = 227
SDLK_RGUI = 1073742055
SDLK_p = 112
SDLK_RSHIFT = 1073742053
SDL_SCANCODE_KP_OCTAL = 219
SDL_SCANCODE_KP_BINARY = 218
SDLK_LALT = 1073742050
SDLK_LSHIFT = 1073742049
SDLK_o = 111
SDL_SCANCODE_KP_PLUSMINUS = 215
SDLK_KP_HEXADECIMAL = 1073742045
SDLK_KP_DECIMAL = 1073742044
SDLK_KP_OCTAL = 1073742043
SDL_SCANCODE_KP_MEMADD = 211
SDLK_KP_CLEARENTRY = 1073742041
SDL_SCANCODE_SLASH = 56
SDL_SCANCODE_KP_MEMRECALL = 209
SDL_SCANCODE_KP_EXCLAM = 207
SDLK_KP_MEMMULTIPLY = 1073742037
SDL_SCANCODE_KP_SPACE = 205
SDLK_KP_MEMADD = 1073742035
SDL_SCANCODE_KP_COLON = 203
SDLK_HELP = 1073741941
SDLK_KP_MEMSTORE = 1073742032
SDLK_KP_EXCLAM = 1073742031
SDLK_KP_AT = 1073742030
SDL_SCANCODE_KP_GREATER = 198
SDLK_l = 108
SDLK_KP_HASH = 1073742028
SDLK_KP_COLON = 1073742027
SDL_SCANCODE_KP_POWER = 195
SDLK_KP_VERTICALBAR = 1073742025
SDLK_KP_DBLAMPERSAND = 1073742024
SDL_SCANCODE_KP_E = 192
SDL_SCANCODE_GRAVE = 53
SDL_SCANCODE_KP_D = 191
SDLK_KP_LESS = 1073742021
SDL_SCANCODE_KP_B = 189
SDL_SCANCODE_KP_A = 188
SDLK_KP_XOR = 1073742018
SDL_SCANCODE_KP_TAB = 186
SDL_SCANCODE_APOSTROPHE = 52
SDL_SCANCODE_KP_RIGHTBRACE = 185
SDL_SCANCODE_KP_LEFTBRACE = 184
SDL_SCANCODE_KP_RIGHTPAREN = 183
SDL_SCANCODE_KP_LEFTPAREN = 182
SDL_SCANCODE_CURRENCYSUBUNIT = 181
SDLK_KP_BACKSPACE = 1073742011
SDLK_i = 105
SDLK_KP_TAB = 1073742010
SDL_SCANCODE_THOUSANDSSEPARATOR = 178
SDLK_KP_LEFTBRACE = 1073742008
SDLK_KP_RIGHTPAREN = 1073742007
SDL_SCANCODE_EXSEL = 164
SDL_SCANCODE_CRSEL = 163
SDL_POWERSTATE_CHARGED = 4
SDLK_CURRENCYUNIT = 1073742004
SDLK_DECIMALSEPARATOR = 1073742003
SDLK_EXECUTE = 1073741940
SDLK_THOUSANDSSEPARATOR = 1073742002
SDLK_KP_000 = 1073742001
SDL_SCANCODE_RETURN2 = 158
SDLK_g = 103
SDLK_EXSEL = 1073741988
SDL_SCANCODE_SYSREQ = 154
SDLK_OUT = 1073741984
SDLK_SEPARATOR = 1073741983
SDLK_f = 102
SDL_SCANCODE_LANG7 = 150
SDLK_CLEAR = 1073741980
SDLK_CANCEL = 1073741979
SDL_SCANCODE_LANG4 = 147
SDLK_ALTERASE = 1073741977
SDLK_e = 101
SDLK_KP_EQUALSAS400 = 1073741958
SDL_SCANCODE_LANG1 = 144
SDL_SCANCODE_INTERNATIONAL9 = 143
SDLK_VOLUMEUP = 1073741952
SDL_SCANCODE_INTERNATIONAL7 = 141
SDLK_FIND = 1073741950
SDL_SCANCODE_EQUALS = 46
SDLK_PASTE = 1073741949
SDL_SCANCODE_INTERNATIONAL4 = 138
SDLK_CUT = 1073741947
SDLK_UNDO = 1073741946
SDLK_AGAIN = 1073741945
SDLK_STOP = 1073741944
SDL_SCANCODE_KP_COMMA = 133
SDL_SCANCODE_VOLUMEDOWN = 129
SDLK_F24 = 1073741939
SDL_SCANCODE_VOLUMEUP = 128
SDL_SCANCODE_MUTE = 127
SDL_SCANCODE_FIND = 126
SDL_SCANCODE_PASTE = 125
SDLK_b = 98
SDLK_F22 = 1073741937
SDLK_F20 = 1073741935
SDLK_F19 = 1073741934
SDL_SCANCODE_TAB = 43
SDL_SCANCODE_MENU = 118
SDL_SCANCODE_HELP = 117
SDL_SCANCODE_EXECUTE = 116
SDLK_F13 = 1073741928
SDL_SCANCODE_F23 = 114
SDL_SCANCODE_F22 = 113
SDLK_BACKQUOTE = 96
SDLK_APPLICATION = 1073741925
SDLK_KP_PERIOD = 1073741923
SDLK_KP_0 = 1073741922
SDLK_KP_9 = 1073741921
SDL_SCANCODE_F17 = 108
SDLK_KP_7 = 1073741919
SDLK_UNDERSCORE = 95
SDLK_KP_6 = 1073741918
SDLK_KP_5 = 1073741917
SDL_SCANCODE_F13 = 104
SDL_SCANCODE_KP_EQUALS = 103
SDLK_KP_2 = 1073741914
SDLK_KP_1 = 1073741913
SDL_SCANCODE_RETURN = 40
SDL_SCANCODE_NONUSBACKSLASH = 100
SDLK_KP_PLUS = 1073741911
SDLK_KP_MINUS = 1073741910
SDL_SCANCODE_KP_9 = 97
SDLK_KP_DIVIDE = 1073741908
SDL_SCANCODE_KP_7 = 95
SDLK_RIGHTBRACKET = 93
SDLK_UP = 1073741906
SDL_SCANCODE_KP_5 = 93
SDL_SCANCODE_KP_4 = 92
SDLK_RIGHT = 1073741903
SDLK_PAGEDOWN = 1073741902
SDL_SCANCODE_9 = 38
SDL_SCANCODE_KP_1 = 89
SDL_SCANCODE_KP_ENTER = 88
SDL_SCANCODE_KP_PLUS = 87
SDL_SCANCODE_KP_MINUS = 86
SDL_SCANCODE_KP_DIVIDE = 84
SDLK_LEFTBRACKET = 91
SDLK_SCROLLLOCK = 1073741895
SDL_SCANCODE_UP = 82
SDL_SCANCODE_DOWN = 81
SDL_SCANCODE_LEFT = 80
SDL_SCANCODE_RIGHT = 79
SDLK_F9 = 1073741890
SDL_SCANCODE_END = 77
SDLK_F7 = 1073741888
SDLK_F6 = 1073741887
SDLK_F4 = 1073741885
SDL_SCANCODE_PAUSE = 72
SDLK_QUESTION = 63
SDLK_F2 = 1073741883
SDLK_F1 = 1073741882
SDLK_CAPSLOCK = 1073741881
SDLK_y = 121
SDLK_x = 120
SDLK_GREATER = 62
SDLK_w = 119
SDLK_v = 118
SDLK_u = 117
SDL_SCANCODE_F5 = 62
SDL_SCANCODE_F4 = 61
SDLK_r = 114
SDL_SCANCODE_F2 = 59
SDL_SCANCODE_CAPSLOCK = 57
SDLK_n = 110
SDL_SCANCODE_PERIOD = 55
SDL_SCANCODE_COMMA = 54
SDLK_LESS = 60
SDLK_j = 106
SDL_SCANCODE_SEMICOLON = 51
SDL_SCANCODE_NONUSHASH = 50
SDL_POWERSTATE_CHARGING = 3
SDL_POWERSTATE_NO_BATTERY = 2
SDLK_SEMICOLON = 59
SDL_POWERSTATE_ON_BATTERY = 1
SDL_POWERSTATE_UNKNOWN = 0
SDL_SCANCODE_MINUS = 45
SDL_SCANCODE_SPACE = 44
SDLK_a = 97
SDL_SCANCODE_BACKSPACE = 42
SDLK_COLON = 58
SDL_SCANCODE_ESCAPE = 41
SDLK_CARET = 94
SDL_SCANCODE_0 = 39
SDLK_BACKSLASH = 92
SDL_SCANCODE_8 = 37
SDLK_9 = 57
SDL_SCANCODE_6 = 35
SDL_SCANCODE_5 = 34
SDL_SCANCODE_4 = 33
SDL_SCANCODE_3 = 32
SDL_SCANCODE_2 = 31
SDL_SCANCODE_1 = 30
SDL_SCANCODE_Z = 29
uint32_t = c_uint32
Uint32 = uint32_t
SDL_Init = lib.SDL_Init
SDL_Init.restype = c_int
SDL_Init.argtypes = [Uint32]
SDL_InitSubSystem = lib.SDL_InitSubSystem
SDL_InitSubSystem.restype = c_int
SDL_InitSubSystem.argtypes = [Uint32]
SDL_QuitSubSystem = lib.SDL_QuitSubSystem
SDL_QuitSubSystem.restype = None
SDL_QuitSubSystem.argtypes = [Uint32]
SDL_WasInit = lib.SDL_WasInit
SDL_WasInit.restype = Uint32
SDL_WasInit.argtypes = [Uint32]
SDL_Quit = lib.SDL_Quit
SDL_Quit.restype = None
SDL_Quit.argtypes = []

# values for enumeration 'SDL_assert_state'
SDL_assert_state = c_int # enum
class SDL_assert_data(Structure):
    pass
SDL_assert_data._fields_ = [
    ('always_ignore', c_int),
    ('trigger_count', c_uint),
    ('condition', STRING),
    ('filename', STRING),
    ('linenum', c_int),
    ('function', STRING),
    ('next', POINTER(SDL_assert_data)),
]
SDL_ReportAssertion = lib.SDL_ReportAssertion
SDL_ReportAssertion.restype = SDL_assert_state
SDL_ReportAssertion.argtypes = [POINTER(SDL_assert_data), STRING, STRING, c_int]
SDL_AssertionHandler = CFUNCTYPE(SDL_assert_state, POINTER(SDL_assert_data), c_void_p)
SDL_SetAssertionHandler = lib.SDL_SetAssertionHandler
SDL_SetAssertionHandler.restype = None
SDL_SetAssertionHandler.argtypes = [SDL_AssertionHandler, c_void_p]
SDL_GetAssertionReport = lib.SDL_GetAssertionReport
SDL_GetAssertionReport.restype = POINTER(SDL_assert_data)
SDL_GetAssertionReport.argtypes = []
SDL_ResetAssertionReport = lib.SDL_ResetAssertionReport
SDL_ResetAssertionReport.restype = None
SDL_ResetAssertionReport.argtypes = []
SDL_SpinLock = c_int

# values for enumeration 'SDL_bool'
SDL_bool = c_int # enum
SDL_AtomicTryLock = lib.SDL_AtomicTryLock
SDL_AtomicTryLock.restype = SDL_bool
SDL_AtomicTryLock.argtypes = [POINTER(SDL_SpinLock)]
SDL_AtomicLock = lib.SDL_AtomicLock
SDL_AtomicLock.restype = None
SDL_AtomicLock.argtypes = [POINTER(SDL_SpinLock)]
SDL_AtomicUnlock = lib.SDL_AtomicUnlock
SDL_AtomicUnlock.restype = None
SDL_AtomicUnlock.argtypes = [POINTER(SDL_SpinLock)]
class SDL_atomic_t(Structure):
    pass
SDL_atomic_t._fields_ = [
    ('value', c_int),
]
SDL_AtomicCAS_ = lib.SDL_AtomicCAS_
SDL_AtomicCAS_.restype = SDL_bool
SDL_AtomicCAS_.argtypes = [POINTER(SDL_atomic_t), c_int, c_int]
SDL_AtomicCASPtr_ = lib.SDL_AtomicCASPtr_
SDL_AtomicCASPtr_.restype = SDL_bool
SDL_AtomicCASPtr_.argtypes = [POINTER(c_void_p), c_void_p, c_void_p]
uint16_t = c_uint16
Uint16 = uint16_t
SDL_AudioFormat = Uint16
uint8_t = c_uint8
Uint8 = uint8_t
SDL_AudioCallback = CFUNCTYPE(None, c_void_p, POINTER(Uint8), c_int)
class SDL_AudioSpec(Structure):
    pass
SDL_AudioSpec._fields_ = [
    ('freq', c_int),
    ('format', SDL_AudioFormat),
    ('channels', Uint8),
    ('silence', Uint8),
    ('samples', Uint16),
    ('padding', Uint16),
    ('size', Uint32),
    ('callback', SDL_AudioCallback),
    ('userdata', c_void_p),
]
class SDL_AudioCVT(Structure):
    pass
SDL_AudioFilter = CFUNCTYPE(None, POINTER(SDL_AudioCVT), SDL_AudioFormat)
SDL_AudioCVT._fields_ = [
    ('needed', c_int),
    ('src_format', SDL_AudioFormat),
    ('dst_format', SDL_AudioFormat),
    ('rate_incr', c_double),
    ('buf', POINTER(Uint8)),
    ('len', c_int),
    ('len_cvt', c_int),
    ('len_mult', c_int),
    ('len_ratio', c_double),
    ('filters', SDL_AudioFilter * 10),
    ('filter_index', c_int),
]
SDL_GetNumAudioDrivers = lib.SDL_GetNumAudioDrivers
SDL_GetNumAudioDrivers.restype = c_int
SDL_GetNumAudioDrivers.argtypes = []
SDL_GetAudioDriver = lib.SDL_GetAudioDriver
SDL_GetAudioDriver.restype = STRING
SDL_GetAudioDriver.argtypes = [c_int]
SDL_AudioInit = lib.SDL_AudioInit
SDL_AudioInit.restype = c_int
SDL_AudioInit.argtypes = [STRING]
SDL_AudioQuit = lib.SDL_AudioQuit
SDL_AudioQuit.restype = None
SDL_AudioQuit.argtypes = []
SDL_GetCurrentAudioDriver = lib.SDL_GetCurrentAudioDriver
SDL_GetCurrentAudioDriver.restype = STRING
SDL_GetCurrentAudioDriver.argtypes = []
SDL_OpenAudio = lib.SDL_OpenAudio
SDL_OpenAudio.restype = c_int
SDL_OpenAudio.argtypes = [POINTER(SDL_AudioSpec), POINTER(SDL_AudioSpec)]
SDL_AudioDeviceID = Uint32
SDL_GetNumAudioDevices = lib.SDL_GetNumAudioDevices
SDL_GetNumAudioDevices.restype = c_int
SDL_GetNumAudioDevices.argtypes = [c_int]
SDL_GetAudioDeviceName = lib.SDL_GetAudioDeviceName
SDL_GetAudioDeviceName.restype = STRING
SDL_GetAudioDeviceName.argtypes = [c_int, c_int]
SDL_OpenAudioDevice = lib.SDL_OpenAudioDevice
SDL_OpenAudioDevice.restype = SDL_AudioDeviceID
SDL_OpenAudioDevice.argtypes = [STRING, c_int, POINTER(SDL_AudioSpec), POINTER(SDL_AudioSpec), c_int]

# values for enumeration 'SDL_AudioStatus'
SDL_AudioStatus = c_int # enum
SDL_GetAudioStatus = lib.SDL_GetAudioStatus
SDL_GetAudioStatus.restype = SDL_AudioStatus
SDL_GetAudioStatus.argtypes = []
SDL_GetAudioDeviceStatus = lib.SDL_GetAudioDeviceStatus
SDL_GetAudioDeviceStatus.restype = SDL_AudioStatus
SDL_GetAudioDeviceStatus.argtypes = [SDL_AudioDeviceID]
SDL_PauseAudio = lib.SDL_PauseAudio
SDL_PauseAudio.restype = None
SDL_PauseAudio.argtypes = [c_int]
SDL_PauseAudioDevice = lib.SDL_PauseAudioDevice
SDL_PauseAudioDevice.restype = None
SDL_PauseAudioDevice.argtypes = [SDL_AudioDeviceID, c_int]
class SDL_RWops(Structure):
    pass
SDL_LoadWAV_RW = lib.SDL_LoadWAV_RW
SDL_LoadWAV_RW.restype = POINTER(SDL_AudioSpec)
SDL_LoadWAV_RW.argtypes = [POINTER(SDL_RWops), c_int, POINTER(SDL_AudioSpec), POINTER(POINTER(Uint8)), POINTER(Uint32)]
SDL_FreeWAV = lib.SDL_FreeWAV
SDL_FreeWAV.restype = None
SDL_FreeWAV.argtypes = [POINTER(Uint8)]
SDL_BuildAudioCVT = lib.SDL_BuildAudioCVT
SDL_BuildAudioCVT.restype = c_int
SDL_BuildAudioCVT.argtypes = [POINTER(SDL_AudioCVT), SDL_AudioFormat, Uint8, c_int, SDL_AudioFormat, Uint8, c_int]
SDL_ConvertAudio = lib.SDL_ConvertAudio
SDL_ConvertAudio.restype = c_int
SDL_ConvertAudio.argtypes = [POINTER(SDL_AudioCVT)]
SDL_MixAudio = lib.SDL_MixAudio
SDL_MixAudio.restype = None
SDL_MixAudio.argtypes = [POINTER(Uint8), POINTER(Uint8), Uint32, c_int]
SDL_MixAudioFormat = lib.SDL_MixAudioFormat
SDL_MixAudioFormat.restype = None
SDL_MixAudioFormat.argtypes = [POINTER(Uint8), POINTER(Uint8), SDL_AudioFormat, Uint32, c_int]
SDL_LockAudio = lib.SDL_LockAudio
SDL_LockAudio.restype = None
SDL_LockAudio.argtypes = []
SDL_LockAudioDevice = lib.SDL_LockAudioDevice
SDL_LockAudioDevice.restype = None
SDL_LockAudioDevice.argtypes = [SDL_AudioDeviceID]
SDL_UnlockAudio = lib.SDL_UnlockAudio
SDL_UnlockAudio.restype = None
SDL_UnlockAudio.argtypes = []
SDL_UnlockAudioDevice = lib.SDL_UnlockAudioDevice
SDL_UnlockAudioDevice.restype = None
SDL_UnlockAudioDevice.argtypes = [SDL_AudioDeviceID]
SDL_CloseAudio = lib.SDL_CloseAudio
SDL_CloseAudio.restype = None
SDL_CloseAudio.argtypes = []
SDL_CloseAudioDevice = lib.SDL_CloseAudioDevice
SDL_CloseAudioDevice.restype = None
SDL_CloseAudioDevice.argtypes = [SDL_AudioDeviceID]

# values for enumeration 'SDL_BlendMode'
SDL_BlendMode = c_int # enum
SDL_SetClipboardText = lib.SDL_SetClipboardText
SDL_SetClipboardText.restype = c_int
SDL_SetClipboardText.argtypes = [STRING]
SDL_GetClipboardText = lib.SDL_GetClipboardText
SDL_GetClipboardText.restype = STRING
SDL_GetClipboardText.argtypes = []
SDL_HasClipboardText = lib.SDL_HasClipboardText
SDL_HasClipboardText.restype = SDL_bool
SDL_HasClipboardText.argtypes = []
SDL_GetCPUCount = lib.SDL_GetCPUCount
SDL_GetCPUCount.restype = c_int
SDL_GetCPUCount.argtypes = []
SDL_GetCPUCacheLineSize = lib.SDL_GetCPUCacheLineSize
SDL_GetCPUCacheLineSize.restype = c_int
SDL_GetCPUCacheLineSize.argtypes = []
SDL_HasRDTSC = lib.SDL_HasRDTSC
SDL_HasRDTSC.restype = SDL_bool
SDL_HasRDTSC.argtypes = []
SDL_HasAltiVec = lib.SDL_HasAltiVec
SDL_HasAltiVec.restype = SDL_bool
SDL_HasAltiVec.argtypes = []
SDL_HasMMX = lib.SDL_HasMMX
SDL_HasMMX.restype = SDL_bool
SDL_HasMMX.argtypes = []
SDL_Has3DNow = lib.SDL_Has3DNow
SDL_Has3DNow.restype = SDL_bool
SDL_Has3DNow.argtypes = []
SDL_HasSSE = lib.SDL_HasSSE
SDL_HasSSE.restype = SDL_bool
SDL_HasSSE.argtypes = []
SDL_HasSSE2 = lib.SDL_HasSSE2
SDL_HasSSE2.restype = SDL_bool
SDL_HasSSE2.argtypes = []
SDL_HasSSE3 = lib.SDL_HasSSE3
SDL_HasSSE3.restype = SDL_bool
SDL_HasSSE3.argtypes = []
SDL_HasSSE41 = lib.SDL_HasSSE41
SDL_HasSSE41.restype = SDL_bool
SDL_HasSSE41.argtypes = []
SDL_HasSSE42 = lib.SDL_HasSSE42
SDL_HasSSE42.restype = SDL_bool
SDL_HasSSE42.argtypes = []
SDL_SetError = lib.SDL_SetError
SDL_SetError.restype = None
SDL_SetError.argtypes = [STRING]
SDL_GetError = lib.SDL_GetError
SDL_GetError.restype = STRING
SDL_GetError.argtypes = []
SDL_ClearError = lib.SDL_ClearError
SDL_ClearError.restype = None
SDL_ClearError.argtypes = []

# values for enumeration 'SDL_errorcode'
SDL_errorcode = c_int # enum
SDL_Error = lib.SDL_Error
SDL_Error.restype = None
SDL_Error.argtypes = [SDL_errorcode]

# values for enumeration 'SDL_EventType'
SDL_EventType = c_int # enum
class SDL_WindowEvent(Structure):
    pass
SDL_WindowEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('event', Uint8),
    ('padding1', Uint8),
    ('padding2', Uint8),
    ('padding3', Uint8),
    ('data1', c_int),
    ('data2', c_int),
]
class SDL_KeyboardEvent(Structure):
    pass
class SDL_Keysym(Structure):
    pass

# values for enumeration 'SDL_Scancode'
SDL_Scancode = c_int # enum
int32_t = c_int32
Sint32 = int32_t
SDL_Keycode = Sint32
SDL_Keysym._fields_ = [
    ('scancode', SDL_Scancode),
    ('sym', SDL_Keycode),
    ('mod', Uint16),
    ('unicode', Uint32),
]
SDL_KeyboardEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('state', Uint8),
    ('repeat', Uint8),
    ('padding2', Uint8),
    ('padding3', Uint8),
    ('keysym', SDL_Keysym),
]
class SDL_TextEditingEvent(Structure):
    pass
SDL_TextEditingEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('text', c_char * 32),
    ('start', c_int),
    ('length', c_int),
]
class SDL_TextInputEvent(Structure):
    pass
SDL_TextInputEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('text', c_char * 32),
]
class SDL_MouseMotionEvent(Structure):
    pass
SDL_MouseMotionEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('state', Uint8),
    ('padding1', Uint8),
    ('padding2', Uint8),
    ('padding3', Uint8),
    ('x', c_int),
    ('y', c_int),
    ('xrel', c_int),
    ('yrel', c_int),
]
class SDL_MouseButtonEvent(Structure):
    pass
SDL_MouseButtonEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('button', Uint8),
    ('state', Uint8),
    ('padding1', Uint8),
    ('padding2', Uint8),
    ('x', c_int),
    ('y', c_int),
]
class SDL_MouseWheelEvent(Structure):
    pass
SDL_MouseWheelEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('x', c_int),
    ('y', c_int),
]
class SDL_JoyAxisEvent(Structure):
    pass
SDL_JoyAxisEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('which', Uint8),
    ('axis', Uint8),
    ('padding1', Uint8),
    ('padding2', Uint8),
    ('value', c_int),
]
class SDL_JoyBallEvent(Structure):
    pass
SDL_JoyBallEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('which', Uint8),
    ('ball', Uint8),
    ('padding1', Uint8),
    ('padding2', Uint8),
    ('xrel', c_int),
    ('yrel', c_int),
]
class SDL_JoyHatEvent(Structure):
    pass
SDL_JoyHatEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('which', Uint8),
    ('hat', Uint8),
    ('value', Uint8),
    ('padding1', Uint8),
]
class SDL_JoyButtonEvent(Structure):
    pass
SDL_JoyButtonEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('which', Uint8),
    ('button', Uint8),
    ('state', Uint8),
    ('padding1', Uint8),
]
class SDL_TouchFingerEvent(Structure):
    pass
int64_t = c_int64
Sint64 = int64_t
SDL_TouchID = Sint64
SDL_FingerID = Sint64
int16_t = c_int16
Sint16 = int16_t
SDL_TouchFingerEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('touchId', SDL_TouchID),
    ('fingerId', SDL_FingerID),
    ('state', Uint8),
    ('padding1', Uint8),
    ('padding2', Uint8),
    ('padding3', Uint8),
    ('x', Uint16),
    ('y', Uint16),
    ('dx', Sint16),
    ('dy', Sint16),
    ('pressure', Uint16),
]
class SDL_TouchButtonEvent(Structure):
    pass
SDL_TouchButtonEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('touchId', SDL_TouchID),
    ('state', Uint8),
    ('button', Uint8),
    ('padding1', Uint8),
    ('padding2', Uint8),
]
class SDL_MultiGestureEvent(Structure):
    pass
SDL_MultiGestureEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('touchId', SDL_TouchID),
    ('dTheta', c_float),
    ('dDist', c_float),
    ('x', c_float),
    ('y', c_float),
    ('numFingers', Uint16),
    ('padding', Uint16),
]
class SDL_DollarGestureEvent(Structure):
    pass
SDL_GestureID = Sint64
SDL_DollarGestureEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('touchId', SDL_TouchID),
    ('gestureId', SDL_GestureID),
    ('numFingers', Uint32),
    ('error', c_float),
]
class SDL_DropEvent(Structure):
    pass
SDL_DropEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('file', STRING),
]
class SDL_QuitEvent(Structure):
    pass
SDL_QuitEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
]
class SDL_UserEvent(Structure):
    pass
SDL_UserEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('windowID', Uint32),
    ('code', c_int),
    ('data1', c_void_p),
    ('data2', c_void_p),
]
class SDL_SysWMmsg(Structure):
    pass
SDL_SysWMmsg._fields_ = [
]
class SDL_SysWMEvent(Structure):
    pass
SDL_SysWMEvent._fields_ = [
    ('type', Uint32),
    ('timestamp', Uint32),
    ('msg', POINTER(SDL_SysWMmsg)),
]
class SDL_Event(Union):
    pass
SDL_Event._fields_ = [
    ('type', Uint32),
    ('window', SDL_WindowEvent),
    ('key', SDL_KeyboardEvent),
    ('edit', SDL_TextEditingEvent),
    ('text', SDL_TextInputEvent),
    ('motion', SDL_MouseMotionEvent),
    ('button', SDL_MouseButtonEvent),
    ('wheel', SDL_MouseWheelEvent),
    ('jaxis', SDL_JoyAxisEvent),
    ('jball', SDL_JoyBallEvent),
    ('jhat', SDL_JoyHatEvent),
    ('jbutton', SDL_JoyButtonEvent),
    ('quit', SDL_QuitEvent),
    ('user', SDL_UserEvent),
    ('syswm', SDL_SysWMEvent),
    ('tfinger', SDL_TouchFingerEvent),
    ('tbutton', SDL_TouchButtonEvent),
    ('mgesture', SDL_MultiGestureEvent),
    ('dgesture', SDL_DollarGestureEvent),
    ('drop', SDL_DropEvent),
]
SDL_PumpEvents = lib.SDL_PumpEvents
SDL_PumpEvents.restype = None
SDL_PumpEvents.argtypes = []

# values for enumeration 'SDL_eventaction'
SDL_eventaction = c_int # enum
SDL_PeepEvents = lib.SDL_PeepEvents
SDL_PeepEvents.restype = c_int
SDL_PeepEvents.argtypes = [POINTER(SDL_Event), c_int, SDL_eventaction, Uint32, Uint32]
SDL_HasEvent = lib.SDL_HasEvent
SDL_HasEvent.restype = SDL_bool
SDL_HasEvent.argtypes = [Uint32]
SDL_HasEvents = lib.SDL_HasEvents
SDL_HasEvents.restype = SDL_bool
SDL_HasEvents.argtypes = [Uint32, Uint32]
SDL_FlushEvent = lib.SDL_FlushEvent
SDL_FlushEvent.restype = None
SDL_FlushEvent.argtypes = [Uint32]
SDL_FlushEvents = lib.SDL_FlushEvents
SDL_FlushEvents.restype = None
SDL_FlushEvents.argtypes = [Uint32, Uint32]
SDL_PollEvent = lib.SDL_PollEvent
SDL_PollEvent.restype = c_int
SDL_PollEvent.argtypes = [POINTER(SDL_Event)]
SDL_WaitEvent = lib.SDL_WaitEvent
SDL_WaitEvent.restype = c_int
SDL_WaitEvent.argtypes = [POINTER(SDL_Event)]
SDL_WaitEventTimeout = lib.SDL_WaitEventTimeout
SDL_WaitEventTimeout.restype = c_int
SDL_WaitEventTimeout.argtypes = [POINTER(SDL_Event), c_int]
SDL_PushEvent = lib.SDL_PushEvent
SDL_PushEvent.restype = c_int
SDL_PushEvent.argtypes = [POINTER(SDL_Event)]
SDL_EventFilter = CFUNCTYPE(c_int, c_void_p, POINTER(SDL_Event))
SDL_SetEventFilter = lib.SDL_SetEventFilter
SDL_SetEventFilter.restype = None
SDL_SetEventFilter.argtypes = [SDL_EventFilter, c_void_p]
SDL_GetEventFilter = lib.SDL_GetEventFilter
SDL_GetEventFilter.restype = SDL_bool
SDL_GetEventFilter.argtypes = [POINTER(SDL_EventFilter), POINTER(c_void_p)]
SDL_AddEventWatch = lib.SDL_AddEventWatch
SDL_AddEventWatch.restype = None
SDL_AddEventWatch.argtypes = [SDL_EventFilter, c_void_p]
SDL_DelEventWatch = lib.SDL_DelEventWatch
SDL_DelEventWatch.restype = None
SDL_DelEventWatch.argtypes = [SDL_EventFilter, c_void_p]
SDL_FilterEvents = lib.SDL_FilterEvents
SDL_FilterEvents.restype = None
SDL_FilterEvents.argtypes = [SDL_EventFilter, c_void_p]
SDL_EventState = lib.SDL_EventState
SDL_EventState.restype = Uint8
SDL_EventState.argtypes = [Uint32, c_int]
SDL_RegisterEvents = lib.SDL_RegisterEvents
SDL_RegisterEvents.restype = Uint32
SDL_RegisterEvents.argtypes = [c_int]
SDL_RecordGesture = lib.SDL_RecordGesture
SDL_RecordGesture.restype = c_int
SDL_RecordGesture.argtypes = [SDL_TouchID]
SDL_SaveAllDollarTemplates = lib.SDL_SaveAllDollarTemplates
SDL_SaveAllDollarTemplates.restype = c_int
SDL_SaveAllDollarTemplates.argtypes = [POINTER(SDL_RWops)]
SDL_SaveDollarTemplate = lib.SDL_SaveDollarTemplate
SDL_SaveDollarTemplate.restype = c_int
SDL_SaveDollarTemplate.argtypes = [SDL_GestureID, POINTER(SDL_RWops)]
SDL_LoadDollarTemplates = lib.SDL_LoadDollarTemplates
SDL_LoadDollarTemplates.restype = c_int
SDL_LoadDollarTemplates.argtypes = [SDL_TouchID, POINTER(SDL_RWops)]

# values for enumeration 'SDL_HintPriority'
SDL_HintPriority = c_int # enum
SDL_SetHintWithPriority = lib.SDL_SetHintWithPriority
SDL_SetHintWithPriority.restype = SDL_bool
SDL_SetHintWithPriority.argtypes = [STRING, STRING, SDL_HintPriority]
SDL_SetHint = lib.SDL_SetHint
SDL_SetHint.restype = SDL_bool
SDL_SetHint.argtypes = [STRING, STRING]
SDL_GetHint = lib.SDL_GetHint
SDL_GetHint.restype = STRING
SDL_GetHint.argtypes = [STRING]
SDL_ClearHints = lib.SDL_ClearHints
SDL_ClearHints.restype = None
SDL_ClearHints.argtypes = []
class _SDL_Joystick(Structure):
    pass
SDL_Joystick = _SDL_Joystick
SDL_NumJoysticks = lib.SDL_NumJoysticks
SDL_NumJoysticks.restype = c_int
SDL_NumJoysticks.argtypes = []
SDL_JoystickName = lib.SDL_JoystickName
SDL_JoystickName.restype = STRING
SDL_JoystickName.argtypes = [c_int]
SDL_JoystickOpen = lib.SDL_JoystickOpen
SDL_JoystickOpen.restype = POINTER(SDL_Joystick)
SDL_JoystickOpen.argtypes = [c_int]
SDL_JoystickOpened = lib.SDL_JoystickOpened
SDL_JoystickOpened.restype = c_int
SDL_JoystickOpened.argtypes = [c_int]
SDL_JoystickIndex = lib.SDL_JoystickIndex
SDL_JoystickIndex.restype = c_int
SDL_JoystickIndex.argtypes = [POINTER(SDL_Joystick)]
SDL_JoystickNumAxes = lib.SDL_JoystickNumAxes
SDL_JoystickNumAxes.restype = c_int
SDL_JoystickNumAxes.argtypes = [POINTER(SDL_Joystick)]
SDL_JoystickNumBalls = lib.SDL_JoystickNumBalls
SDL_JoystickNumBalls.restype = c_int
SDL_JoystickNumBalls.argtypes = [POINTER(SDL_Joystick)]
SDL_JoystickNumHats = lib.SDL_JoystickNumHats
SDL_JoystickNumHats.restype = c_int
SDL_JoystickNumHats.argtypes = [POINTER(SDL_Joystick)]
SDL_JoystickNumButtons = lib.SDL_JoystickNumButtons
SDL_JoystickNumButtons.restype = c_int
SDL_JoystickNumButtons.argtypes = [POINTER(SDL_Joystick)]
SDL_JoystickUpdate = lib.SDL_JoystickUpdate
SDL_JoystickUpdate.restype = None
SDL_JoystickUpdate.argtypes = []
SDL_JoystickEventState = lib.SDL_JoystickEventState
SDL_JoystickEventState.restype = c_int
SDL_JoystickEventState.argtypes = [c_int]
SDL_JoystickGetAxis = lib.SDL_JoystickGetAxis
SDL_JoystickGetAxis.restype = Sint16
SDL_JoystickGetAxis.argtypes = [POINTER(SDL_Joystick), c_int]
SDL_JoystickGetHat = lib.SDL_JoystickGetHat
SDL_JoystickGetHat.restype = Uint8
SDL_JoystickGetHat.argtypes = [POINTER(SDL_Joystick), c_int]
SDL_JoystickGetBall = lib.SDL_JoystickGetBall
SDL_JoystickGetBall.restype = c_int
SDL_JoystickGetBall.argtypes = [POINTER(SDL_Joystick), c_int, POINTER(c_int), POINTER(c_int)]
SDL_JoystickGetButton = lib.SDL_JoystickGetButton
SDL_JoystickGetButton.restype = Uint8
SDL_JoystickGetButton.argtypes = [POINTER(SDL_Joystick), c_int]
SDL_JoystickClose = lib.SDL_JoystickClose
SDL_JoystickClose.restype = None
SDL_JoystickClose.argtypes = [POINTER(SDL_Joystick)]
class SDL_Window(Structure):
    pass
SDL_GetKeyboardFocus = lib.SDL_GetKeyboardFocus
SDL_GetKeyboardFocus.restype = POINTER(SDL_Window)
SDL_GetKeyboardFocus.argtypes = []
SDL_GetKeyboardState = lib.SDL_GetKeyboardState
SDL_GetKeyboardState.restype = POINTER(Uint8)
SDL_GetKeyboardState.argtypes = [POINTER(c_int)]

# values for enumeration 'SDL_Keymod'
KMOD_NONE = 0
KMOD_LSHIFT = 1
KMOD_RSHIFT = 2
KMOD_LCTRL = 64
KMOD_RCTRL = 128
KMOD_LALT = 256
KMOD_RALT = 512
KMOD_LGUI = 1024
KMOD_RGUI = 2048
KMOD_NUM = 4096
KMOD_CAPS = 8192
KMOD_MODE = 16384
KMOD_RESERVED = 32768
SDL_Keymod = c_int # enum
SDL_GetModState = lib.SDL_GetModState
SDL_GetModState.restype = SDL_Keymod
SDL_GetModState.argtypes = []
SDL_SetModState = lib.SDL_SetModState
SDL_SetModState.restype = None
SDL_SetModState.argtypes = [SDL_Keymod]
SDL_GetKeyFromScancode = lib.SDL_GetKeyFromScancode
SDL_GetKeyFromScancode.restype = SDL_Keycode
SDL_GetKeyFromScancode.argtypes = [SDL_Scancode]
SDL_GetScancodeFromKey = lib.SDL_GetScancodeFromKey
SDL_GetScancodeFromKey.restype = SDL_Scancode
SDL_GetScancodeFromKey.argtypes = [SDL_Keycode]
SDL_GetScancodeName = lib.SDL_GetScancodeName
SDL_GetScancodeName.restype = STRING
SDL_GetScancodeName.argtypes = [SDL_Scancode]
SDL_GetScancodeFromName = lib.SDL_GetScancodeFromName
SDL_GetScancodeFromName.restype = SDL_Scancode
SDL_GetScancodeFromName.argtypes = [STRING]
SDL_GetKeyName = lib.SDL_GetKeyName
SDL_GetKeyName.restype = STRING
SDL_GetKeyName.argtypes = [SDL_Keycode]
SDL_GetKeyFromName = lib.SDL_GetKeyFromName
SDL_GetKeyFromName.restype = SDL_Keycode
SDL_GetKeyFromName.argtypes = [STRING]
SDL_StartTextInput = lib.SDL_StartTextInput
SDL_StartTextInput.restype = None
SDL_StartTextInput.argtypes = []
SDL_StopTextInput = lib.SDL_StopTextInput
SDL_StopTextInput.restype = None
SDL_StopTextInput.argtypes = []
SDL_SetTextInputRect = lib.SDL_SetTextInputRect
SDL_SetTextInputRect.restype = None
SDL_SetTextInputRect.argtypes = [POINTER(SDL_Rect)]
SDL_LoadObject = lib.SDL_LoadObject
SDL_LoadObject.restype = c_void_p
SDL_LoadObject.argtypes = [STRING]
SDL_LoadFunction = lib.SDL_LoadFunction
SDL_LoadFunction.restype = c_void_p
SDL_LoadFunction.argtypes = [c_void_p, STRING]
SDL_UnloadObject = lib.SDL_UnloadObject
SDL_UnloadObject.restype = None
SDL_UnloadObject.argtypes = [c_void_p]

# values for enumeration 'SDL_LogPriority'
SDL_LogPriority = c_int # enum
SDL_LogSetAllPriority = lib.SDL_LogSetAllPriority
SDL_LogSetAllPriority.restype = None
SDL_LogSetAllPriority.argtypes = [SDL_LogPriority]
SDL_LogSetPriority = lib.SDL_LogSetPriority
SDL_LogSetPriority.restype = None
SDL_LogSetPriority.argtypes = [c_int, SDL_LogPriority]
SDL_LogGetPriority = lib.SDL_LogGetPriority
SDL_LogGetPriority.restype = SDL_LogPriority
SDL_LogGetPriority.argtypes = [c_int]
SDL_LogResetPriorities = lib.SDL_LogResetPriorities
SDL_LogResetPriorities.restype = None
SDL_LogResetPriorities.argtypes = []
SDL_Log = lib.SDL_Log
SDL_Log.restype = None
SDL_Log.argtypes = [STRING]
SDL_LogVerbose = lib.SDL_LogVerbose
SDL_LogVerbose.restype = None
SDL_LogVerbose.argtypes = [c_int, STRING]
SDL_LogDebug = lib.SDL_LogDebug
SDL_LogDebug.restype = None
SDL_LogDebug.argtypes = [c_int, STRING]
SDL_LogInfo = lib.SDL_LogInfo
SDL_LogInfo.restype = None
SDL_LogInfo.argtypes = [c_int, STRING]
SDL_LogWarn = lib.SDL_LogWarn
SDL_LogWarn.restype = None
SDL_LogWarn.argtypes = [c_int, STRING]
SDL_LogError = lib.SDL_LogError
SDL_LogError.restype = None
SDL_LogError.argtypes = [c_int, STRING]
SDL_LogCritical = lib.SDL_LogCritical
SDL_LogCritical.restype = None
SDL_LogCritical.argtypes = [c_int, STRING]
SDL_LogMessage = lib.SDL_LogMessage
SDL_LogMessage.restype = None
SDL_LogMessage.argtypes = [c_int, SDL_LogPriority, STRING]
SDL_LogMessageV = lib.SDL_LogMessageV
SDL_LogMessageV.restype = None
SDL_LogMessageV.argtypes = [c_int, SDL_LogPriority, STRING, POINTER(__va_list_tag)]
SDL_LogOutputFunction = CFUNCTYPE(None, c_void_p, c_int, SDL_LogPriority, STRING)
SDL_LogGetOutputFunction = lib.SDL_LogGetOutputFunction
SDL_LogGetOutputFunction.restype = None
SDL_LogGetOutputFunction.argtypes = [POINTER(SDL_LogOutputFunction), POINTER(c_void_p)]
SDL_LogSetOutputFunction = lib.SDL_LogSetOutputFunction
SDL_LogSetOutputFunction.restype = None
SDL_LogSetOutputFunction.argtypes = [SDL_LogOutputFunction, c_void_p]
class SDL_Cursor(Structure):
    pass
SDL_Cursor._fields_ = [
]
SDL_GetMouseFocus = lib.SDL_GetMouseFocus
SDL_GetMouseFocus.restype = POINTER(SDL_Window)
SDL_GetMouseFocus.argtypes = []
SDL_GetMouseState = lib.SDL_GetMouseState
SDL_GetMouseState.restype = Uint8
SDL_GetMouseState.argtypes = [POINTER(c_int), POINTER(c_int)]
SDL_GetRelativeMouseState = lib.SDL_GetRelativeMouseState
SDL_GetRelativeMouseState.restype = Uint8
SDL_GetRelativeMouseState.argtypes = [POINTER(c_int), POINTER(c_int)]
SDL_WarpMouseInWindow = lib.SDL_WarpMouseInWindow
SDL_WarpMouseInWindow.restype = None
SDL_WarpMouseInWindow.argtypes = [POINTER(SDL_Window), c_int, c_int]
SDL_SetRelativeMouseMode = lib.SDL_SetRelativeMouseMode
SDL_SetRelativeMouseMode.restype = c_int
SDL_SetRelativeMouseMode.argtypes = [SDL_bool]
SDL_GetRelativeMouseMode = lib.SDL_GetRelativeMouseMode
SDL_GetRelativeMouseMode.restype = SDL_bool
SDL_GetRelativeMouseMode.argtypes = []
SDL_CreateCursor = lib.SDL_CreateCursor
SDL_CreateCursor.restype = POINTER(SDL_Cursor)
SDL_CreateCursor.argtypes = [POINTER(Uint8), POINTER(Uint8), c_int, c_int, c_int, c_int]
SDL_CreateColorCursor = lib.SDL_CreateColorCursor
SDL_CreateColorCursor.restype = POINTER(SDL_Cursor)
SDL_CreateColorCursor.argtypes = [POINTER(SDL_Surface), c_int, c_int]
SDL_SetCursor = lib.SDL_SetCursor
SDL_SetCursor.restype = None
SDL_SetCursor.argtypes = [POINTER(SDL_Cursor)]
SDL_GetCursor = lib.SDL_GetCursor
SDL_GetCursor.restype = POINTER(SDL_Cursor)
SDL_GetCursor.argtypes = []
SDL_FreeCursor = lib.SDL_FreeCursor
SDL_FreeCursor.restype = None
SDL_FreeCursor.argtypes = [POINTER(SDL_Cursor)]
SDL_ShowCursor = lib.SDL_ShowCursor
SDL_ShowCursor.restype = c_int
SDL_ShowCursor.argtypes = [c_int]
class SDL_mutex(Structure):
    pass
SDL_mutex._fields_ = [
]
SDL_CreateMutex = lib.SDL_CreateMutex
SDL_CreateMutex.restype = POINTER(SDL_mutex)
SDL_CreateMutex.argtypes = []
SDL_mutexP = lib.SDL_mutexP
SDL_mutexP.restype = c_int
SDL_mutexP.argtypes = [POINTER(SDL_mutex)]
SDL_mutexV = lib.SDL_mutexV
SDL_mutexV.restype = c_int
SDL_mutexV.argtypes = [POINTER(SDL_mutex)]
SDL_DestroyMutex = lib.SDL_DestroyMutex
SDL_DestroyMutex.restype = None
SDL_DestroyMutex.argtypes = [POINTER(SDL_mutex)]
class SDL_semaphore(Structure):
    pass
SDL_semaphore._fields_ = [
]
SDL_sem = SDL_semaphore
SDL_CreateSemaphore = lib.SDL_CreateSemaphore
SDL_CreateSemaphore.restype = POINTER(SDL_sem)
SDL_CreateSemaphore.argtypes = [Uint32]
SDL_DestroySemaphore = lib.SDL_DestroySemaphore
SDL_DestroySemaphore.restype = None
SDL_DestroySemaphore.argtypes = [POINTER(SDL_sem)]
SDL_SemWait = lib.SDL_SemWait
SDL_SemWait.restype = c_int
SDL_SemWait.argtypes = [POINTER(SDL_sem)]
SDL_SemTryWait = lib.SDL_SemTryWait
SDL_SemTryWait.restype = c_int
SDL_SemTryWait.argtypes = [POINTER(SDL_sem)]
SDL_SemWaitTimeout = lib.SDL_SemWaitTimeout
SDL_SemWaitTimeout.restype = c_int
SDL_SemWaitTimeout.argtypes = [POINTER(SDL_sem), Uint32]
SDL_SemPost = lib.SDL_SemPost
SDL_SemPost.restype = c_int
SDL_SemPost.argtypes = [POINTER(SDL_sem)]
SDL_SemValue = lib.SDL_SemValue
SDL_SemValue.restype = Uint32
SDL_SemValue.argtypes = [POINTER(SDL_sem)]
class SDL_cond(Structure):
    pass
SDL_cond._fields_ = [
]
SDL_CreateCond = lib.SDL_CreateCond
SDL_CreateCond.restype = POINTER(SDL_cond)
SDL_CreateCond.argtypes = []
SDL_DestroyCond = lib.SDL_DestroyCond
SDL_DestroyCond.restype = None
SDL_DestroyCond.argtypes = [POINTER(SDL_cond)]
SDL_CondSignal = lib.SDL_CondSignal
SDL_CondSignal.restype = c_int
SDL_CondSignal.argtypes = [POINTER(SDL_cond)]
SDL_CondBroadcast = lib.SDL_CondBroadcast
SDL_CondBroadcast.restype = c_int
SDL_CondBroadcast.argtypes = [POINTER(SDL_cond)]
SDL_CondWait = lib.SDL_CondWait
SDL_CondWait.restype = c_int
SDL_CondWait.argtypes = [POINTER(SDL_cond), POINTER(SDL_mutex)]
SDL_CondWaitTimeout = lib.SDL_CondWaitTimeout
SDL_CondWaitTimeout.restype = c_int
SDL_CondWaitTimeout.argtypes = [POINTER(SDL_cond), POINTER(SDL_mutex), Uint32]
SDL_Color._fields_ = [
    ('r', Uint8),
    ('g', Uint8),
    ('b', Uint8),
    ('unused', Uint8),
]
class SDL_Palette(Structure):
    pass
SDL_Palette._fields_ = [
    ('ncolors', c_int),
    ('colors', POINTER(SDL_Color)),
    ('version', Uint32),
    ('refcount', c_int),
]
class SDL_PixelFormat(Structure):
    pass
SDL_PixelFormat._fields_ = [
    ('format', Uint32),
    ('palette', POINTER(SDL_Palette)),
    ('BitsPerPixel', Uint8),
    ('BytesPerPixel', Uint8),
    ('padding', Uint8 * 2),
    ('Rmask', Uint32),
    ('Gmask', Uint32),
    ('Bmask', Uint32),
    ('Amask', Uint32),
    ('Rloss', Uint8),
    ('Gloss', Uint8),
    ('Bloss', Uint8),
    ('Aloss', Uint8),
    ('Rshift', Uint8),
    ('Gshift', Uint8),
    ('Bshift', Uint8),
    ('Ashift', Uint8),
    ('refcount', c_int),
    ('next', POINTER(SDL_PixelFormat)),
]
SDL_GetPixelFormatName = lib.SDL_GetPixelFormatName
SDL_GetPixelFormatName.restype = STRING
SDL_GetPixelFormatName.argtypes = [Uint32]
SDL_PixelFormatEnumToMasks = lib.SDL_PixelFormatEnumToMasks
SDL_PixelFormatEnumToMasks.restype = SDL_bool
SDL_PixelFormatEnumToMasks.argtypes = [Uint32, POINTER(c_int), POINTER(Uint32), POINTER(Uint32), POINTER(Uint32), POINTER(Uint32)]
SDL_MasksToPixelFormatEnum = lib.SDL_MasksToPixelFormatEnum
SDL_MasksToPixelFormatEnum.restype = Uint32
SDL_MasksToPixelFormatEnum.argtypes = [c_int, Uint32, Uint32, Uint32, Uint32]
SDL_AllocFormat = lib.SDL_AllocFormat
SDL_AllocFormat.restype = POINTER(SDL_PixelFormat)
SDL_AllocFormat.argtypes = [Uint32]
SDL_FreeFormat = lib.SDL_FreeFormat
SDL_FreeFormat.restype = None
SDL_FreeFormat.argtypes = [POINTER(SDL_PixelFormat)]
SDL_AllocPalette = lib.SDL_AllocPalette
SDL_AllocPalette.restype = POINTER(SDL_Palette)
SDL_AllocPalette.argtypes = [c_int]
SDL_SetPixelFormatPalette = lib.SDL_SetPixelFormatPalette
SDL_SetPixelFormatPalette.restype = c_int
SDL_SetPixelFormatPalette.argtypes = [POINTER(SDL_PixelFormat), POINTER(SDL_Palette)]
SDL_SetPaletteColors = lib.SDL_SetPaletteColors
SDL_SetPaletteColors.restype = c_int
SDL_SetPaletteColors.argtypes = [POINTER(SDL_Palette), POINTER(SDL_Color), c_int, c_int]
SDL_FreePalette = lib.SDL_FreePalette
SDL_FreePalette.restype = None
SDL_FreePalette.argtypes = [POINTER(SDL_Palette)]
SDL_MapRGB = lib.SDL_MapRGB
SDL_MapRGB.restype = Uint32
SDL_MapRGB.argtypes = [POINTER(SDL_PixelFormat), Uint8, Uint8, Uint8]
SDL_MapRGBA = lib.SDL_MapRGBA
SDL_MapRGBA.restype = Uint32
SDL_MapRGBA.argtypes = [POINTER(SDL_PixelFormat), Uint8, Uint8, Uint8, Uint8]
SDL_GetRGB = lib.SDL_GetRGB
SDL_GetRGB.restype = None
SDL_GetRGB.argtypes = [Uint32, POINTER(SDL_PixelFormat), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
SDL_GetRGBA = lib.SDL_GetRGBA
SDL_GetRGBA.restype = None
SDL_GetRGBA.argtypes = [Uint32, POINTER(SDL_PixelFormat), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
SDL_CalculateGammaRamp = lib.SDL_CalculateGammaRamp
SDL_CalculateGammaRamp.restype = None
SDL_CalculateGammaRamp.argtypes = [c_float, POINTER(Uint16)]
SDL_GetPlatform = lib.SDL_GetPlatform
SDL_GetPlatform.restype = STRING
SDL_GetPlatform.argtypes = []

# values for enumeration 'SDL_PowerState'
SDL_PowerState = c_int # enum
SDL_GetPowerInfo = lib.SDL_GetPowerInfo
SDL_GetPowerInfo.restype = SDL_PowerState
SDL_GetPowerInfo.argtypes = [POINTER(c_int), POINTER(c_int)]
class SDL_Point(Structure):
    pass
SDL_Point._fields_ = [
    ('x', c_int),
    ('y', c_int),
]
SDL_Rect._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('w', c_int),
    ('h', c_int),
]
SDL_HasIntersection = lib.SDL_HasIntersection
SDL_HasIntersection.restype = SDL_bool
SDL_HasIntersection.argtypes = [POINTER(SDL_Rect), POINTER(SDL_Rect)]
SDL_IntersectRect = lib.SDL_IntersectRect
SDL_IntersectRect.restype = SDL_bool
SDL_IntersectRect.argtypes = [POINTER(SDL_Rect), POINTER(SDL_Rect), POINTER(SDL_Rect)]
SDL_UnionRect = lib.SDL_UnionRect
SDL_UnionRect.restype = None
SDL_UnionRect.argtypes = [POINTER(SDL_Rect), POINTER(SDL_Rect), POINTER(SDL_Rect)]
SDL_EnclosePoints = lib.SDL_EnclosePoints
SDL_EnclosePoints.restype = SDL_bool
SDL_EnclosePoints.argtypes = [POINTER(SDL_Point), c_int, POINTER(SDL_Rect), POINTER(SDL_Rect)]
SDL_IntersectRectAndLine = lib.SDL_IntersectRectAndLine
SDL_IntersectRectAndLine.restype = SDL_bool
SDL_IntersectRectAndLine.argtypes = [POINTER(SDL_Rect), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# values for enumeration 'SDL_RendererFlags'
SDL_RendererFlags = c_int # enum
class SDL_RendererInfo(Structure):
    pass
SDL_RendererInfo._fields_ = [
    ('name', STRING),
    ('flags', Uint32),
    ('num_texture_formats', Uint32),
    ('texture_formats', Uint32 * 16),
    ('max_texture_width', c_int),
    ('max_texture_height', c_int),
]

# values for enumeration 'SDL_TextureAccess'
SDL_TextureAccess = c_int # enum

# values for enumeration 'SDL_TextureModulate'
SDL_TextureModulate = c_int # enum

# values for enumeration 'SDL_RendererFlip'
SDL_RendererFlip = c_int # enum
class SDL_Renderer(Structure):
    pass
SDL_Renderer._fields_ = [
]
class SDL_Texture(Structure):
    pass
SDL_Texture._fields_ = [
]
SDL_GetNumRenderDrivers = lib.SDL_GetNumRenderDrivers
SDL_GetNumRenderDrivers.restype = c_int
SDL_GetNumRenderDrivers.argtypes = []
SDL_GetRenderDriverInfo = lib.SDL_GetRenderDriverInfo
SDL_GetRenderDriverInfo.restype = c_int
SDL_GetRenderDriverInfo.argtypes = [c_int, POINTER(SDL_RendererInfo)]
SDL_CreateWindowAndRenderer = lib.SDL_CreateWindowAndRenderer
SDL_CreateWindowAndRenderer.restype = c_int
SDL_CreateWindowAndRenderer.argtypes = [c_int, c_int, Uint32, POINTER(POINTER(SDL_Window)), POINTER(POINTER(SDL_Renderer))]
SDL_CreateRenderer = lib.SDL_CreateRenderer
SDL_CreateRenderer.restype = POINTER(SDL_Renderer)
SDL_CreateRenderer.argtypes = [POINTER(SDL_Window), c_int, Uint32]
SDL_CreateSoftwareRenderer = lib.SDL_CreateSoftwareRenderer
SDL_CreateSoftwareRenderer.restype = POINTER(SDL_Renderer)
SDL_CreateSoftwareRenderer.argtypes = [POINTER(SDL_Surface)]
SDL_GetRenderer = lib.SDL_GetRenderer
SDL_GetRenderer.restype = POINTER(SDL_Renderer)
SDL_GetRenderer.argtypes = [POINTER(SDL_Window)]
SDL_GetRendererInfo = lib.SDL_GetRendererInfo
SDL_GetRendererInfo.restype = c_int
SDL_GetRendererInfo.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_RendererInfo)]
SDL_CreateTexture = lib.SDL_CreateTexture
SDL_CreateTexture.restype = POINTER(SDL_Texture)
SDL_CreateTexture.argtypes = [POINTER(SDL_Renderer), Uint32, c_int, c_int, c_int]
SDL_CreateTextureFromSurface = lib.SDL_CreateTextureFromSurface
SDL_CreateTextureFromSurface.restype = POINTER(SDL_Texture)
SDL_CreateTextureFromSurface.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Surface)]
SDL_QueryTexture = lib.SDL_QueryTexture
SDL_QueryTexture.restype = c_int
SDL_QueryTexture.argtypes = [POINTER(SDL_Texture), POINTER(Uint32), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
SDL_SetTextureColorMod = lib.SDL_SetTextureColorMod
SDL_SetTextureColorMod.restype = c_int
SDL_SetTextureColorMod.argtypes = [POINTER(SDL_Texture), Uint8, Uint8, Uint8]
SDL_GetTextureColorMod = lib.SDL_GetTextureColorMod
SDL_GetTextureColorMod.restype = c_int
SDL_GetTextureColorMod.argtypes = [POINTER(SDL_Texture), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
SDL_SetTextureAlphaMod = lib.SDL_SetTextureAlphaMod
SDL_SetTextureAlphaMod.restype = c_int
SDL_SetTextureAlphaMod.argtypes = [POINTER(SDL_Texture), Uint8]
SDL_GetTextureAlphaMod = lib.SDL_GetTextureAlphaMod
SDL_GetTextureAlphaMod.restype = c_int
SDL_GetTextureAlphaMod.argtypes = [POINTER(SDL_Texture), POINTER(Uint8)]
SDL_SetTextureBlendMode = lib.SDL_SetTextureBlendMode
SDL_SetTextureBlendMode.restype = c_int
SDL_SetTextureBlendMode.argtypes = [POINTER(SDL_Texture), SDL_BlendMode]
SDL_GetTextureBlendMode = lib.SDL_GetTextureBlendMode
SDL_GetTextureBlendMode.restype = c_int
SDL_GetTextureBlendMode.argtypes = [POINTER(SDL_Texture), POINTER(SDL_BlendMode)]
SDL_UpdateTexture = lib.SDL_UpdateTexture
SDL_UpdateTexture.restype = c_int
SDL_UpdateTexture.argtypes = [POINTER(SDL_Texture), POINTER(SDL_Rect), c_void_p, c_int]
SDL_LockTexture = lib.SDL_LockTexture
SDL_LockTexture.restype = c_int
SDL_LockTexture.argtypes = [POINTER(SDL_Texture), POINTER(SDL_Rect), POINTER(c_void_p), POINTER(c_int)]
SDL_UnlockTexture = lib.SDL_UnlockTexture
SDL_UnlockTexture.restype = None
SDL_UnlockTexture.argtypes = [POINTER(SDL_Texture)]
SDL_RenderTargetSupported = lib.SDL_RenderTargetSupported
SDL_RenderTargetSupported.restype = SDL_bool
SDL_RenderTargetSupported.argtypes = [POINTER(SDL_Renderer)]
SDL_SetRenderTarget = lib.SDL_SetRenderTarget
SDL_SetRenderTarget.restype = c_int
SDL_SetRenderTarget.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Texture)]
SDL_RenderSetViewport = lib.SDL_RenderSetViewport
SDL_RenderSetViewport.restype = c_int
SDL_RenderSetViewport.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Rect)]
SDL_RenderGetViewport = lib.SDL_RenderGetViewport
SDL_RenderGetViewport.restype = None
SDL_RenderGetViewport.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Rect)]
SDL_SetRenderDrawColor = lib.SDL_SetRenderDrawColor
SDL_SetRenderDrawColor.restype = c_int
SDL_SetRenderDrawColor.argtypes = [POINTER(SDL_Renderer), Uint8, Uint8, Uint8, Uint8]
SDL_GetRenderDrawColor = lib.SDL_GetRenderDrawColor
SDL_GetRenderDrawColor.restype = c_int
SDL_GetRenderDrawColor.argtypes = [POINTER(SDL_Renderer), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
SDL_SetRenderDrawBlendMode = lib.SDL_SetRenderDrawBlendMode
SDL_SetRenderDrawBlendMode.restype = c_int
SDL_SetRenderDrawBlendMode.argtypes = [POINTER(SDL_Renderer), SDL_BlendMode]
SDL_GetRenderDrawBlendMode = lib.SDL_GetRenderDrawBlendMode
SDL_GetRenderDrawBlendMode.restype = c_int
SDL_GetRenderDrawBlendMode.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_BlendMode)]
SDL_RenderClear = lib.SDL_RenderClear
SDL_RenderClear.restype = c_int
SDL_RenderClear.argtypes = [POINTER(SDL_Renderer)]
SDL_RenderDrawPoint = lib.SDL_RenderDrawPoint
SDL_RenderDrawPoint.restype = c_int
SDL_RenderDrawPoint.argtypes = [POINTER(SDL_Renderer), c_int, c_int]
SDL_RenderDrawPoints = lib.SDL_RenderDrawPoints
SDL_RenderDrawPoints.restype = c_int
SDL_RenderDrawPoints.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Point), c_int]
SDL_RenderDrawLine = lib.SDL_RenderDrawLine
SDL_RenderDrawLine.restype = c_int
SDL_RenderDrawLine.argtypes = [POINTER(SDL_Renderer), c_int, c_int, c_int, c_int]
SDL_RenderDrawLines = lib.SDL_RenderDrawLines
SDL_RenderDrawLines.restype = c_int
SDL_RenderDrawLines.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Point), c_int]
SDL_RenderDrawRect = lib.SDL_RenderDrawRect
SDL_RenderDrawRect.restype = c_int
SDL_RenderDrawRect.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Rect)]
SDL_RenderDrawRects = lib.SDL_RenderDrawRects
SDL_RenderDrawRects.restype = c_int
SDL_RenderDrawRects.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Rect), c_int]
SDL_RenderFillRect = lib.SDL_RenderFillRect
SDL_RenderFillRect.restype = c_int
SDL_RenderFillRect.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Rect)]
SDL_RenderFillRects = lib.SDL_RenderFillRects
SDL_RenderFillRects.restype = c_int
SDL_RenderFillRects.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Rect), c_int]
SDL_RenderCopy = lib.SDL_RenderCopy
SDL_RenderCopy.restype = c_int
SDL_RenderCopy.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Texture), POINTER(SDL_Rect), POINTER(SDL_Rect)]
SDL_RenderCopyEx = lib.SDL_RenderCopyEx
SDL_RenderCopyEx.restype = c_int
SDL_RenderCopyEx.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Texture), POINTER(SDL_Rect), POINTER(SDL_Rect), c_double, POINTER(SDL_Point), SDL_RendererFlip]
SDL_RenderReadPixels = lib.SDL_RenderReadPixels
SDL_RenderReadPixels.restype = c_int
SDL_RenderReadPixels.argtypes = [POINTER(SDL_Renderer), POINTER(SDL_Rect), Uint32, c_void_p, c_int]
SDL_RenderPresent = lib.SDL_RenderPresent
SDL_RenderPresent.restype = None
SDL_RenderPresent.argtypes = [POINTER(SDL_Renderer)]
SDL_DestroyTexture = lib.SDL_DestroyTexture
SDL_DestroyTexture.restype = None
SDL_DestroyTexture.argtypes = [POINTER(SDL_Texture)]
SDL_DestroyRenderer = lib.SDL_DestroyRenderer
SDL_DestroyRenderer.restype = None
SDL_DestroyRenderer.argtypes = [POINTER(SDL_Renderer)]
class N9SDL_RWops4DOT_36E(Union):
    pass
class N9SDL_RWops4DOT_364DOT_37E(Structure):
    pass
class _IO_FILE(Structure):
    pass
FILE = _IO_FILE
N9SDL_RWops4DOT_364DOT_37E._fields_ = [
    ('autoclose', SDL_bool),
    ('fp', POINTER(FILE)),
]
class N9SDL_RWops4DOT_364DOT_38E(Structure):
    pass
N9SDL_RWops4DOT_364DOT_38E._fields_ = [
    ('base', POINTER(Uint8)),
    ('here', POINTER(Uint8)),
    ('stop', POINTER(Uint8)),
]
class N9SDL_RWops4DOT_364DOT_39E(Structure):
    pass
N9SDL_RWops4DOT_364DOT_39E._fields_ = [
    ('data1', c_void_p),
]
N9SDL_RWops4DOT_36E._fields_ = [
    ('stdio', N9SDL_RWops4DOT_364DOT_37E),
    ('mem', N9SDL_RWops4DOT_364DOT_38E),
    ('unknown', N9SDL_RWops4DOT_364DOT_39E),
]
SDL_RWops._fields_ = [
    ('seek', CFUNCTYPE(c_long, POINTER(SDL_RWops), c_long, c_int)),
    ('read', CFUNCTYPE(size_t, POINTER(SDL_RWops), c_void_p, size_t, size_t)),
    ('write', CFUNCTYPE(size_t, POINTER(SDL_RWops), c_void_p, size_t, size_t)),
    ('close', CFUNCTYPE(c_int, POINTER(SDL_RWops))),
    ('type', Uint32),
    ('hidden', N9SDL_RWops4DOT_36E),
]
SDL_RWFromFile = lib.SDL_RWFromFile
SDL_RWFromFile.restype = POINTER(SDL_RWops)
SDL_RWFromFile.argtypes = [STRING, STRING]
SDL_RWFromFP = lib.SDL_RWFromFP
SDL_RWFromFP.restype = POINTER(SDL_RWops)
SDL_RWFromFP.argtypes = [POINTER(FILE), SDL_bool]
SDL_RWFromMem = lib.SDL_RWFromMem
SDL_RWFromMem.restype = POINTER(SDL_RWops)
SDL_RWFromMem.argtypes = [c_void_p, c_int]
SDL_RWFromConstMem = lib.SDL_RWFromConstMem
SDL_RWFromConstMem.restype = POINTER(SDL_RWops)
SDL_RWFromConstMem.argtypes = [c_void_p, c_int]
SDL_AllocRW = lib.SDL_AllocRW
SDL_AllocRW.restype = POINTER(SDL_RWops)
SDL_AllocRW.argtypes = []
SDL_FreeRW = lib.SDL_FreeRW
SDL_FreeRW.restype = None
SDL_FreeRW.argtypes = [POINTER(SDL_RWops)]
SDL_ReadLE16 = lib.SDL_ReadLE16
SDL_ReadLE16.restype = Uint16
SDL_ReadLE16.argtypes = [POINTER(SDL_RWops)]
SDL_ReadBE16 = lib.SDL_ReadBE16
SDL_ReadBE16.restype = Uint16
SDL_ReadBE16.argtypes = [POINTER(SDL_RWops)]
SDL_ReadLE32 = lib.SDL_ReadLE32
SDL_ReadLE32.restype = Uint32
SDL_ReadLE32.argtypes = [POINTER(SDL_RWops)]
SDL_ReadBE32 = lib.SDL_ReadBE32
SDL_ReadBE32.restype = Uint32
SDL_ReadBE32.argtypes = [POINTER(SDL_RWops)]
uint64_t = c_uint64
Uint64 = uint64_t
SDL_ReadLE64 = lib.SDL_ReadLE64
SDL_ReadLE64.restype = Uint64
SDL_ReadLE64.argtypes = [POINTER(SDL_RWops)]
SDL_ReadBE64 = lib.SDL_ReadBE64
SDL_ReadBE64.restype = Uint64
SDL_ReadBE64.argtypes = [POINTER(SDL_RWops)]
SDL_WriteLE16 = lib.SDL_WriteLE16
SDL_WriteLE16.restype = size_t
SDL_WriteLE16.argtypes = [POINTER(SDL_RWops), Uint16]
SDL_WriteBE16 = lib.SDL_WriteBE16
SDL_WriteBE16.restype = size_t
SDL_WriteBE16.argtypes = [POINTER(SDL_RWops), Uint16]
SDL_WriteLE32 = lib.SDL_WriteLE32
SDL_WriteLE32.restype = size_t
SDL_WriteLE32.argtypes = [POINTER(SDL_RWops), Uint32]
SDL_WriteBE32 = lib.SDL_WriteBE32
SDL_WriteBE32.restype = size_t
SDL_WriteBE32.argtypes = [POINTER(SDL_RWops), Uint32]
SDL_WriteLE64 = lib.SDL_WriteLE64
SDL_WriteLE64.restype = size_t
SDL_WriteLE64.argtypes = [POINTER(SDL_RWops), Uint64]
SDL_WriteBE64 = lib.SDL_WriteBE64
SDL_WriteBE64.restype = size_t
SDL_WriteBE64.argtypes = [POINTER(SDL_RWops), Uint64]
SDL_dummy_uint8 = c_int * 1
SDL_dummy_sint8 = c_int * 1
SDL_dummy_uint16 = c_int * 1
SDL_dummy_sint16 = c_int * 1
SDL_dummy_uint32 = c_int * 1
SDL_dummy_sint32 = c_int * 1
SDL_dummy_uint64 = c_int * 1
SDL_dummy_sint64 = c_int * 1

# values for enumeration 'SDL_DUMMY_ENUM'
DUMMY_ENUM_VALUE = 0
SDL_DUMMY_ENUM = c_int # enum
SDL_dummy_enum = c_int * 1
SDL_wcslen = lib.SDL_wcslen
SDL_wcslen.restype = size_t
SDL_wcslen.argtypes = [WSTRING]
SDL_wcslcpy = lib.SDL_wcslcpy
SDL_wcslcpy.restype = size_t
SDL_wcslcpy.argtypes = [WSTRING, WSTRING, size_t]
SDL_wcslcat = lib.SDL_wcslcat
SDL_wcslcat.restype = size_t
SDL_wcslcat.argtypes = [WSTRING, WSTRING, size_t]
SDL_strlcpy = lib.SDL_strlcpy
SDL_strlcpy.restype = size_t
SDL_strlcpy.argtypes = [STRING, STRING, size_t]
SDL_utf8strlcpy = lib.SDL_utf8strlcpy
SDL_utf8strlcpy.restype = size_t
SDL_utf8strlcpy.argtypes = [STRING, STRING, size_t]
SDL_strlcat = lib.SDL_strlcat
SDL_strlcat.restype = size_t
SDL_strlcat.argtypes = [STRING, STRING, size_t]
SDL_strrev = lib.SDL_strrev
SDL_strrev.restype = STRING
SDL_strrev.argtypes = [STRING]
SDL_strupr = lib.SDL_strupr
SDL_strupr.restype = STRING
SDL_strupr.argtypes = [STRING]
SDL_strlwr = lib.SDL_strlwr
SDL_strlwr.restype = STRING
SDL_strlwr.argtypes = [STRING]
SDL_ltoa = lib.SDL_ltoa
SDL_ltoa.restype = STRING
SDL_ltoa.argtypes = [c_long, STRING, c_int]
SDL_ultoa = lib.SDL_ultoa
SDL_ultoa.restype = STRING
SDL_ultoa.argtypes = [c_ulong, STRING, c_int]
SDL_lltoa = lib.SDL_lltoa
SDL_lltoa.restype = STRING
SDL_lltoa.argtypes = [Sint64, STRING, c_int]
SDL_ulltoa = lib.SDL_ulltoa
SDL_ulltoa.restype = STRING
SDL_ulltoa.argtypes = [Uint64, STRING, c_int]
SDL_iconv = lib.SDL_iconv
SDL_iconv.restype = size_t
SDL_iconv.argtypes = [iconv_t, POINTER(STRING), POINTER(size_t), POINTER(STRING), POINTER(size_t)]
SDL_iconv_string = lib.SDL_iconv_string
SDL_iconv_string.restype = STRING
SDL_iconv_string.argtypes = [STRING, STRING, STRING, size_t]
class SDL_BlitMap(Structure):
    pass
SDL_Surface._fields_ = [
    ('flags', Uint32),
    ('format', POINTER(SDL_PixelFormat)),
    ('w', c_int),
    ('h', c_int),
    ('pitch', c_int),
    ('pixels', c_void_p),
    ('userdata', c_void_p),
    ('locked', c_int),
    ('lock_data', c_void_p),
    ('clip_rect', SDL_Rect),
    ('map', POINTER(SDL_BlitMap)),
    ('refcount', c_int),
]
SDL_BlitMap._fields_ = [
]
SDL_blit = CFUNCTYPE(c_int, POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect))
SDL_CreateRGBSurface = lib.SDL_CreateRGBSurface
SDL_CreateRGBSurface.restype = POINTER(SDL_Surface)
SDL_CreateRGBSurface.argtypes = [Uint32, c_int, c_int, c_int, Uint32, Uint32, Uint32, Uint32]
SDL_CreateRGBSurfaceFrom = lib.SDL_CreateRGBSurfaceFrom
SDL_CreateRGBSurfaceFrom.restype = POINTER(SDL_Surface)
SDL_CreateRGBSurfaceFrom.argtypes = [c_void_p, c_int, c_int, c_int, c_int, Uint32, Uint32, Uint32, Uint32]
SDL_FreeSurface = lib.SDL_FreeSurface
SDL_FreeSurface.restype = None
SDL_FreeSurface.argtypes = [POINTER(SDL_Surface)]
SDL_SetSurfacePalette = lib.SDL_SetSurfacePalette
SDL_SetSurfacePalette.restype = c_int
SDL_SetSurfacePalette.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Palette)]
SDL_LockSurface = lib.SDL_LockSurface
SDL_LockSurface.restype = c_int
SDL_LockSurface.argtypes = [POINTER(SDL_Surface)]
SDL_UnlockSurface = lib.SDL_UnlockSurface
SDL_UnlockSurface.restype = None
SDL_UnlockSurface.argtypes = [POINTER(SDL_Surface)]
SDL_LoadBMP_RW = lib.SDL_LoadBMP_RW
SDL_LoadBMP_RW.restype = POINTER(SDL_Surface)
SDL_LoadBMP_RW.argtypes = [POINTER(SDL_RWops), c_int]
SDL_SaveBMP_RW = lib.SDL_SaveBMP_RW
SDL_SaveBMP_RW.restype = c_int
SDL_SaveBMP_RW.argtypes = [POINTER(SDL_Surface), POINTER(SDL_RWops), c_int]
SDL_SetSurfaceRLE = lib.SDL_SetSurfaceRLE
SDL_SetSurfaceRLE.restype = c_int
SDL_SetSurfaceRLE.argtypes = [POINTER(SDL_Surface), c_int]
SDL_SetColorKey = lib.SDL_SetColorKey
SDL_SetColorKey.restype = c_int
SDL_SetColorKey.argtypes = [POINTER(SDL_Surface), c_int, Uint32]
SDL_GetColorKey = lib.SDL_GetColorKey
SDL_GetColorKey.restype = c_int
SDL_GetColorKey.argtypes = [POINTER(SDL_Surface), POINTER(Uint32)]
SDL_SetSurfaceColorMod = lib.SDL_SetSurfaceColorMod
SDL_SetSurfaceColorMod.restype = c_int
SDL_SetSurfaceColorMod.argtypes = [POINTER(SDL_Surface), Uint8, Uint8, Uint8]
SDL_GetSurfaceColorMod = lib.SDL_GetSurfaceColorMod
SDL_GetSurfaceColorMod.restype = c_int
SDL_GetSurfaceColorMod.argtypes = [POINTER(SDL_Surface), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
SDL_SetSurfaceAlphaMod = lib.SDL_SetSurfaceAlphaMod
SDL_SetSurfaceAlphaMod.restype = c_int
SDL_SetSurfaceAlphaMod.argtypes = [POINTER(SDL_Surface), Uint8]
SDL_GetSurfaceAlphaMod = lib.SDL_GetSurfaceAlphaMod
SDL_GetSurfaceAlphaMod.restype = c_int
SDL_GetSurfaceAlphaMod.argtypes = [POINTER(SDL_Surface), POINTER(Uint8)]
SDL_SetSurfaceBlendMode = lib.SDL_SetSurfaceBlendMode
SDL_SetSurfaceBlendMode.restype = c_int
SDL_SetSurfaceBlendMode.argtypes = [POINTER(SDL_Surface), SDL_BlendMode]
SDL_GetSurfaceBlendMode = lib.SDL_GetSurfaceBlendMode
SDL_GetSurfaceBlendMode.restype = c_int
SDL_GetSurfaceBlendMode.argtypes = [POINTER(SDL_Surface), POINTER(SDL_BlendMode)]
SDL_SetClipRect = lib.SDL_SetClipRect
SDL_SetClipRect.restype = SDL_bool
SDL_SetClipRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect)]
SDL_GetClipRect = lib.SDL_GetClipRect
SDL_GetClipRect.restype = None
SDL_GetClipRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect)]
SDL_ConvertSurface = lib.SDL_ConvertSurface
SDL_ConvertSurface.restype = POINTER(SDL_Surface)
SDL_ConvertSurface.argtypes = [POINTER(SDL_Surface), POINTER(SDL_PixelFormat), Uint32]
SDL_ConvertSurfaceFormat = lib.SDL_ConvertSurfaceFormat
SDL_ConvertSurfaceFormat.restype = POINTER(SDL_Surface)
SDL_ConvertSurfaceFormat.argtypes = [POINTER(SDL_Surface), Uint32, Uint32]
SDL_ConvertPixels = lib.SDL_ConvertPixels
SDL_ConvertPixels.restype = c_int
SDL_ConvertPixels.argtypes = [c_int, c_int, Uint32, c_void_p, c_int, Uint32, c_void_p, c_int]
SDL_FillRect = lib.SDL_FillRect
SDL_FillRect.restype = c_int
SDL_FillRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), Uint32]
SDL_FillRects = lib.SDL_FillRects
SDL_FillRects.restype = c_int
SDL_FillRects.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), c_int, Uint32]
SDL_LowerBlit = lib.SDL_LowerBlit
SDL_LowerBlit.restype = c_int
SDL_LowerBlit.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
SDL_SoftStretch = lib.SDL_SoftStretch
SDL_SoftStretch.restype = c_int
SDL_SoftStretch.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
SDL_LowerBlitScaled = lib.SDL_LowerBlitScaled
SDL_LowerBlitScaled.restype = c_int
SDL_LowerBlitScaled.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
class SDL_Thread(Structure):
    pass
SDL_Thread._fields_ = [
]
SDL_threadID = c_ulong

# values for enumeration 'SDL_ThreadPriority'
SDL_ThreadPriority = c_int # enum
SDL_ThreadFunction = CFUNCTYPE(c_int, c_void_p)
SDL_CreateThread = lib.SDL_CreateThread
SDL_CreateThread.restype = POINTER(SDL_Thread)
SDL_CreateThread.argtypes = [SDL_ThreadFunction, STRING, c_void_p]
SDL_GetThreadName = lib.SDL_GetThreadName
SDL_GetThreadName.restype = STRING
SDL_GetThreadName.argtypes = [POINTER(SDL_Thread)]
SDL_ThreadID = lib.SDL_ThreadID
SDL_ThreadID.restype = SDL_threadID
SDL_ThreadID.argtypes = []
SDL_GetThreadID = lib.SDL_GetThreadID
SDL_GetThreadID.restype = SDL_threadID
SDL_GetThreadID.argtypes = [POINTER(SDL_Thread)]
SDL_SetThreadPriority = lib.SDL_SetThreadPriority
SDL_SetThreadPriority.restype = c_int
SDL_SetThreadPriority.argtypes = [SDL_ThreadPriority]
SDL_WaitThread = lib.SDL_WaitThread
SDL_WaitThread.restype = None
SDL_WaitThread.argtypes = [POINTER(SDL_Thread), POINTER(c_int)]
SDL_GetTicks = lib.SDL_GetTicks
SDL_GetTicks.restype = Uint32
SDL_GetTicks.argtypes = []
SDL_GetPerformanceCounter = lib.SDL_GetPerformanceCounter
SDL_GetPerformanceCounter.restype = Uint64
SDL_GetPerformanceCounter.argtypes = []
SDL_GetPerformanceFrequency = lib.SDL_GetPerformanceFrequency
SDL_GetPerformanceFrequency.restype = Uint64
SDL_GetPerformanceFrequency.argtypes = []
SDL_Delay = lib.SDL_Delay
SDL_Delay.restype = None
SDL_Delay.argtypes = [Uint32]
SDL_TimerCallback = CFUNCTYPE(Uint32, Uint32, c_void_p)
SDL_TimerID = c_int
SDL_AddTimer = lib.SDL_AddTimer
SDL_AddTimer.restype = SDL_TimerID
SDL_AddTimer.argtypes = [Uint32, SDL_TimerCallback, c_void_p]
SDL_RemoveTimer = lib.SDL_RemoveTimer
SDL_RemoveTimer.restype = SDL_bool
SDL_RemoveTimer.argtypes = [SDL_TimerID]
class SDL_Finger(Structure):
    pass
SDL_Finger._fields_ = [
    ('id', SDL_FingerID),
    ('x', Uint16),
    ('y', Uint16),
    ('pressure', Uint16),
    ('xdelta', Uint16),
    ('ydelta', Uint16),
    ('last_x', Uint16),
    ('last_y', Uint16),
    ('last_pressure', Uint16),
    ('down', SDL_bool),
]
class SDL_Touch(Structure):
    pass
SDL_Touch._fields_ = [
    ('FreeTouch', CFUNCTYPE(None, POINTER(SDL_Touch))),
    ('pressure_max', c_float),
    ('pressure_min', c_float),
    ('x_max', c_float),
    ('x_min', c_float),
    ('y_max', c_float),
    ('y_min', c_float),
    ('xres', Uint16),
    ('yres', Uint16),
    ('pressureres', Uint16),
    ('native_xres', c_float),
    ('native_yres', c_float),
    ('native_pressureres', c_float),
    ('tilt_x', c_float),
    ('tilt_y', c_float),
    ('rotation', c_float),
    ('id', SDL_TouchID),
    ('focus', POINTER(SDL_Window)),
    ('name', STRING),
    ('buttonstate', Uint8),
    ('relative_mode', SDL_bool),
    ('flush_motion', SDL_bool),
    ('num_fingers', c_int),
    ('max_fingers', c_int),
    ('fingers', POINTER(POINTER(SDL_Finger))),
    ('driverdata', c_void_p),
]
SDL_GetTouch = lib.SDL_GetTouch
SDL_GetTouch.restype = POINTER(SDL_Touch)
SDL_GetTouch.argtypes = [SDL_TouchID]
SDL_GetFinger = lib.SDL_GetFinger
SDL_GetFinger.restype = POINTER(SDL_Finger)
SDL_GetFinger.argtypes = [POINTER(SDL_Touch), SDL_FingerID]
class SDL_version(Structure):
    pass
SDL_version._fields_ = [
    ('major', Uint8),
    ('minor', Uint8),
    ('patch', Uint8),
]
SDL_GetVersion = lib.SDL_GetVersion
SDL_GetVersion.restype = None
SDL_GetVersion.argtypes = [POINTER(SDL_version)]
SDL_GetRevision = lib.SDL_GetRevision
SDL_GetRevision.restype = STRING
SDL_GetRevision.argtypes = []
SDL_GetRevisionNumber = lib.SDL_GetRevisionNumber
SDL_GetRevisionNumber.restype = c_int
SDL_GetRevisionNumber.argtypes = []
class SDL_DisplayMode(Structure):
    pass
SDL_DisplayMode._fields_ = [
    ('format', Uint32),
    ('w', c_int),
    ('h', c_int),
    ('refresh_rate', c_int),
    ('driverdata', c_void_p),
]
SDL_Window._fields_ = [
]

# values for enumeration 'SDL_WindowFlags'
SDL_WindowFlags = c_int # enum

# values for enumeration 'SDL_WindowEventID'
SDL_WindowEventID = c_int # enum
SDL_GLContext = c_void_p

# values for enumeration 'SDL_GLattr'
SDL_GLattr = c_int # enum

# values for enumeration 'SDL_GLprofile'
SDL_GLprofile = c_int # enum

# values for enumeration 'SDL_GLcontextFlag'
SDL_GLcontextFlag = c_int # enum
SDL_GetNumVideoDrivers = lib.SDL_GetNumVideoDrivers
SDL_GetNumVideoDrivers.restype = c_int
SDL_GetNumVideoDrivers.argtypes = []
SDL_GetVideoDriver = lib.SDL_GetVideoDriver
SDL_GetVideoDriver.restype = STRING
SDL_GetVideoDriver.argtypes = [c_int]
SDL_VideoInit = lib.SDL_VideoInit
SDL_VideoInit.restype = c_int
SDL_VideoInit.argtypes = [STRING]
SDL_VideoQuit = lib.SDL_VideoQuit
SDL_VideoQuit.restype = None
SDL_VideoQuit.argtypes = []
SDL_GetCurrentVideoDriver = lib.SDL_GetCurrentVideoDriver
SDL_GetCurrentVideoDriver.restype = STRING
SDL_GetCurrentVideoDriver.argtypes = []
SDL_GetNumVideoDisplays = lib.SDL_GetNumVideoDisplays
SDL_GetNumVideoDisplays.restype = c_int
SDL_GetNumVideoDisplays.argtypes = []
SDL_GetDisplayBounds = lib.SDL_GetDisplayBounds
SDL_GetDisplayBounds.restype = c_int
SDL_GetDisplayBounds.argtypes = [c_int, POINTER(SDL_Rect)]
SDL_GetNumDisplayModes = lib.SDL_GetNumDisplayModes
SDL_GetNumDisplayModes.restype = c_int
SDL_GetNumDisplayModes.argtypes = [c_int]
SDL_GetDisplayMode = lib.SDL_GetDisplayMode
SDL_GetDisplayMode.restype = c_int
SDL_GetDisplayMode.argtypes = [c_int, c_int, POINTER(SDL_DisplayMode)]
SDL_GetDesktopDisplayMode = lib.SDL_GetDesktopDisplayMode
SDL_GetDesktopDisplayMode.restype = c_int
SDL_GetDesktopDisplayMode.argtypes = [c_int, POINTER(SDL_DisplayMode)]
SDL_GetCurrentDisplayMode = lib.SDL_GetCurrentDisplayMode
SDL_GetCurrentDisplayMode.restype = c_int
SDL_GetCurrentDisplayMode.argtypes = [c_int, POINTER(SDL_DisplayMode)]
SDL_GetClosestDisplayMode = lib.SDL_GetClosestDisplayMode
SDL_GetClosestDisplayMode.restype = POINTER(SDL_DisplayMode)
SDL_GetClosestDisplayMode.argtypes = [c_int, POINTER(SDL_DisplayMode), POINTER(SDL_DisplayMode)]
SDL_GetWindowDisplay = lib.SDL_GetWindowDisplay
SDL_GetWindowDisplay.restype = c_int
SDL_GetWindowDisplay.argtypes = [POINTER(SDL_Window)]
SDL_SetWindowDisplayMode = lib.SDL_SetWindowDisplayMode
SDL_SetWindowDisplayMode.restype = c_int
SDL_SetWindowDisplayMode.argtypes = [POINTER(SDL_Window), POINTER(SDL_DisplayMode)]
SDL_GetWindowDisplayMode = lib.SDL_GetWindowDisplayMode
SDL_GetWindowDisplayMode.restype = c_int
SDL_GetWindowDisplayMode.argtypes = [POINTER(SDL_Window), POINTER(SDL_DisplayMode)]
SDL_GetWindowPixelFormat = lib.SDL_GetWindowPixelFormat
SDL_GetWindowPixelFormat.restype = Uint32
SDL_GetWindowPixelFormat.argtypes = [POINTER(SDL_Window)]
SDL_CreateWindow = lib.SDL_CreateWindow
SDL_CreateWindow.restype = POINTER(SDL_Window)
SDL_CreateWindow.argtypes = [STRING, c_int, c_int, c_int, c_int, Uint32]
SDL_CreateWindowFrom = lib.SDL_CreateWindowFrom
SDL_CreateWindowFrom.restype = POINTER(SDL_Window)
SDL_CreateWindowFrom.argtypes = [c_void_p]
SDL_GetWindowID = lib.SDL_GetWindowID
SDL_GetWindowID.restype = Uint32
SDL_GetWindowID.argtypes = [POINTER(SDL_Window)]
SDL_GetWindowFromID = lib.SDL_GetWindowFromID
SDL_GetWindowFromID.restype = POINTER(SDL_Window)
SDL_GetWindowFromID.argtypes = [Uint32]
SDL_GetWindowFlags = lib.SDL_GetWindowFlags
SDL_GetWindowFlags.restype = Uint32
SDL_GetWindowFlags.argtypes = [POINTER(SDL_Window)]
SDL_SetWindowTitle = lib.SDL_SetWindowTitle
SDL_SetWindowTitle.restype = None
SDL_SetWindowTitle.argtypes = [POINTER(SDL_Window), STRING]
SDL_GetWindowTitle = lib.SDL_GetWindowTitle
SDL_GetWindowTitle.restype = STRING
SDL_GetWindowTitle.argtypes = [POINTER(SDL_Window)]
SDL_SetWindowIcon = lib.SDL_SetWindowIcon
SDL_SetWindowIcon.restype = None
SDL_SetWindowIcon.argtypes = [POINTER(SDL_Window), POINTER(SDL_Surface)]
SDL_SetWindowData = lib.SDL_SetWindowData
SDL_SetWindowData.restype = c_void_p
SDL_SetWindowData.argtypes = [POINTER(SDL_Window), STRING, c_void_p]
SDL_GetWindowData = lib.SDL_GetWindowData
SDL_GetWindowData.restype = c_void_p
SDL_GetWindowData.argtypes = [POINTER(SDL_Window), STRING]
SDL_SetWindowPosition = lib.SDL_SetWindowPosition
SDL_SetWindowPosition.restype = None
SDL_SetWindowPosition.argtypes = [POINTER(SDL_Window), c_int, c_int]
SDL_GetWindowPosition = lib.SDL_GetWindowPosition
SDL_GetWindowPosition.restype = None
SDL_GetWindowPosition.argtypes = [POINTER(SDL_Window), POINTER(c_int), POINTER(c_int)]
SDL_SetWindowSize = lib.SDL_SetWindowSize
SDL_SetWindowSize.restype = None
SDL_SetWindowSize.argtypes = [POINTER(SDL_Window), c_int, c_int]
SDL_GetWindowSize = lib.SDL_GetWindowSize
SDL_GetWindowSize.restype = None
SDL_GetWindowSize.argtypes = [POINTER(SDL_Window), POINTER(c_int), POINTER(c_int)]
SDL_ShowWindow = lib.SDL_ShowWindow
SDL_ShowWindow.restype = None
SDL_ShowWindow.argtypes = [POINTER(SDL_Window)]
SDL_HideWindow = lib.SDL_HideWindow
SDL_HideWindow.restype = None
SDL_HideWindow.argtypes = [POINTER(SDL_Window)]
SDL_RaiseWindow = lib.SDL_RaiseWindow
SDL_RaiseWindow.restype = None
SDL_RaiseWindow.argtypes = [POINTER(SDL_Window)]
SDL_MaximizeWindow = lib.SDL_MaximizeWindow
SDL_MaximizeWindow.restype = None
SDL_MaximizeWindow.argtypes = [POINTER(SDL_Window)]
SDL_MinimizeWindow = lib.SDL_MinimizeWindow
SDL_MinimizeWindow.restype = None
SDL_MinimizeWindow.argtypes = [POINTER(SDL_Window)]
SDL_RestoreWindow = lib.SDL_RestoreWindow
SDL_RestoreWindow.restype = None
SDL_RestoreWindow.argtypes = [POINTER(SDL_Window)]
SDL_SetWindowFullscreen = lib.SDL_SetWindowFullscreen
SDL_SetWindowFullscreen.restype = c_int
SDL_SetWindowFullscreen.argtypes = [POINTER(SDL_Window), SDL_bool]
SDL_GetWindowSurface = lib.SDL_GetWindowSurface
SDL_GetWindowSurface.restype = POINTER(SDL_Surface)
SDL_GetWindowSurface.argtypes = [POINTER(SDL_Window)]
SDL_UpdateWindowSurface = lib.SDL_UpdateWindowSurface
SDL_UpdateWindowSurface.restype = c_int
SDL_UpdateWindowSurface.argtypes = [POINTER(SDL_Window)]
SDL_UpdateWindowSurfaceRects = lib.SDL_UpdateWindowSurfaceRects
SDL_UpdateWindowSurfaceRects.restype = c_int
SDL_UpdateWindowSurfaceRects.argtypes = [POINTER(SDL_Window), POINTER(SDL_Rect), c_int]
SDL_SetWindowGrab = lib.SDL_SetWindowGrab
SDL_SetWindowGrab.restype = None
SDL_SetWindowGrab.argtypes = [POINTER(SDL_Window), SDL_bool]
SDL_GetWindowGrab = lib.SDL_GetWindowGrab
SDL_GetWindowGrab.restype = SDL_bool
SDL_GetWindowGrab.argtypes = [POINTER(SDL_Window)]
SDL_SetWindowBrightness = lib.SDL_SetWindowBrightness
SDL_SetWindowBrightness.restype = c_int
SDL_SetWindowBrightness.argtypes = [POINTER(SDL_Window), c_float]
SDL_GetWindowBrightness = lib.SDL_GetWindowBrightness
SDL_GetWindowBrightness.restype = c_float
SDL_GetWindowBrightness.argtypes = [POINTER(SDL_Window)]
SDL_SetWindowGammaRamp = lib.SDL_SetWindowGammaRamp
SDL_SetWindowGammaRamp.restype = c_int
SDL_SetWindowGammaRamp.argtypes = [POINTER(SDL_Window), POINTER(Uint16), POINTER(Uint16), POINTER(Uint16)]
SDL_GetWindowGammaRamp = lib.SDL_GetWindowGammaRamp
SDL_GetWindowGammaRamp.restype = c_int
SDL_GetWindowGammaRamp.argtypes = [POINTER(SDL_Window), POINTER(Uint16), POINTER(Uint16), POINTER(Uint16)]
SDL_DestroyWindow = lib.SDL_DestroyWindow
SDL_DestroyWindow.restype = None
SDL_DestroyWindow.argtypes = [POINTER(SDL_Window)]
SDL_IsScreenSaverEnabled = lib.SDL_IsScreenSaverEnabled
SDL_IsScreenSaverEnabled.restype = SDL_bool
SDL_IsScreenSaverEnabled.argtypes = []
SDL_EnableScreenSaver = lib.SDL_EnableScreenSaver
SDL_EnableScreenSaver.restype = None
SDL_EnableScreenSaver.argtypes = []
SDL_DisableScreenSaver = lib.SDL_DisableScreenSaver
SDL_DisableScreenSaver.restype = None
SDL_DisableScreenSaver.argtypes = []
SDL_GL_LoadLibrary = lib.SDL_GL_LoadLibrary
SDL_GL_LoadLibrary.restype = c_int
SDL_GL_LoadLibrary.argtypes = [STRING]
SDL_GL_GetProcAddress = lib.SDL_GL_GetProcAddress
SDL_GL_GetProcAddress.restype = c_void_p
SDL_GL_GetProcAddress.argtypes = [STRING]
SDL_GL_UnloadLibrary = lib.SDL_GL_UnloadLibrary
SDL_GL_UnloadLibrary.restype = None
SDL_GL_UnloadLibrary.argtypes = []
SDL_GL_ExtensionSupported = lib.SDL_GL_ExtensionSupported
SDL_GL_ExtensionSupported.restype = SDL_bool
SDL_GL_ExtensionSupported.argtypes = [STRING]
SDL_GL_SetAttribute = lib.SDL_GL_SetAttribute
SDL_GL_SetAttribute.restype = c_int
SDL_GL_SetAttribute.argtypes = [SDL_GLattr, c_int]
SDL_GL_GetAttribute = lib.SDL_GL_GetAttribute
SDL_GL_GetAttribute.restype = c_int
SDL_GL_GetAttribute.argtypes = [SDL_GLattr, POINTER(c_int)]
SDL_GL_CreateContext = lib.SDL_GL_CreateContext
SDL_GL_CreateContext.restype = SDL_GLContext
SDL_GL_CreateContext.argtypes = [POINTER(SDL_Window)]
SDL_GL_MakeCurrent = lib.SDL_GL_MakeCurrent
SDL_GL_MakeCurrent.restype = c_int
SDL_GL_MakeCurrent.argtypes = [POINTER(SDL_Window), SDL_GLContext]
SDL_GL_SetSwapInterval = lib.SDL_GL_SetSwapInterval
SDL_GL_SetSwapInterval.restype = c_int
SDL_GL_SetSwapInterval.argtypes = [c_int]
SDL_GL_GetSwapInterval = lib.SDL_GL_GetSwapInterval
SDL_GL_GetSwapInterval.restype = c_int
SDL_GL_GetSwapInterval.argtypes = []
SDL_GL_SwapWindow = lib.SDL_GL_SwapWindow
SDL_GL_SwapWindow.restype = None
SDL_GL_SwapWindow.argtypes = [POINTER(SDL_Window)]
SDL_GL_DeleteContext = lib.SDL_GL_DeleteContext
SDL_GL_DeleteContext.restype = None
SDL_GL_DeleteContext.argtypes = [SDL_GLContext]
SDL_HAT_CENTERED = 0 # Variable c_int '0'
SDL_LOADSO_DLOPEN = 1 # Variable c_int '1'
SDL_AUDIO_ALLOW_FREQUENCY_CHANGE = 1 # Variable c_int '1'
SDL_VIDEO_DRIVER_X11_XCURSOR = 1 # Variable c_int '1'
SDL_BUTTON_X1 = 4 # Variable c_int '4'
SDL_BUTTON_X2 = 5 # Variable c_int '5'
SDL_QUERY = -1 # Variable c_int '-0x00000000000000001'
SDL_DISABLE = 0 # Variable c_int '0'
SDL_MAX_LOG_MESSAGE = 4096 # Variable c_int '4096'
SDL_AUDIO_ALLOW_ANY_CHANGE = 7 # Variable c_int '7'
SDL_BUTTON_RIGHT = 3 # Variable c_int '3'
SDL_AUDIO_MASK_ENDIAN = 4096 # Variable c_int '4096'
SDL_VIDEO_DRIVER_X11_XRANDR = 1 # Variable c_int '1'
SDL_VIDEO_DRIVER_X11_XINERAMA = 1 # Variable c_int '1'
SDL_ASSERT_LEVEL = 1 # Variable c_int '1'
SDL_BUTTON_RMASK = 4 # Variable c_int '4'
SDL_HINT_RENDER_SCALE_QUALITY = 'SDL_RENDER_SCALE_QUALITY' # Variable STRING '(const char*)"SDL_RENDER_SCALE_QUALITY"'
SDL_HINT_ORIENTATIONS = 'SDL_IOS_ORIENTATIONS' # Variable STRING '(const char*)"SDL_IOS_ORIENTATIONS"'
SDL_AUDIO_DRIVER_OSS = 1 # Variable c_int '1'
SDL_WINDOWPOS_CENTERED = 805240832 # Variable c_int '805240832'
SDL_MINOR_VERSION = 0 # Variable c_int '0'
SDL_ICONV_EILSEQ = 18446744073709551613L # Variable c_ulong '-3u'
SDL_VIDEO_DRIVER_X11_DYNAMIC_XINERAMA = 'libXinerama.so.1' # Variable STRING '(const char*)"libXinerama.so.1"'
SDL_VIDEO_DRIVER_X11_XINPUT2_SUPPORTS_MULTITOUCH = 1 # Variable c_int '1'
SDL_RLEACCEL = 2 # Variable c_int '2'
SDL_BUTTON_LMASK = 1 # Variable c_int '1'
SDL_HAPTIC_LINUX = 1 # Variable c_int '1'
SDL_HINT_IDLE_TIMER_DISABLED = 'SDL_IOS_IDLE_TIMER_DISABLED' # Variable STRING '(const char*)"SDL_IOS_IDLE_TIMER_DISABLED"'
SDL_INIT_HAPTIC = 4096 # Variable c_int '4096'
SDL_INIT_VIDEO = 32 # Variable c_int '32'
SDL_HINT_RENDER_OPENGL_SHADERS = 'SDL_RENDER_OPENGL_SHADERS' # Variable STRING '(const char*)"SDL_RENDER_OPENGL_SHADERS"'
SDL_HAT_RIGHTUP = 3 # Variable c_int '3'
SDL_HAT_UP = 1 # Variable c_int '1'
SDL_VIDEO_DRIVER_X11 = 1 # Variable c_int '1'
SDL_ASSEMBLY_ROUTINES = 1 # Variable c_int '1'
SDL_HAT_DOWN = 4 # Variable c_int '4'
SDL_AUDIO_ALLOW_FORMAT_CHANGE = 2 # Variable c_int '2'
SDL_BUTTON_MIDDLE = 2 # Variable c_int '2'
SDL_AUDIO_DRIVER_DISK = 1 # Variable c_int '1'
SDL_VIDEO_DRIVER_DUMMY = 1 # Variable c_int '1'
SDL_COMPILEDVERSION = 2000 # Variable c_int '2000'
SDL_MUTEX_MAXWAIT = 4294967295L # Variable c_uint '4294967295u'
SDL_ICONV_E2BIG = 18446744073709551614L # Variable c_ulong '-2u'
SDL_IGNORE = 0 # Variable c_int '0'
SDL_THREAD_PTHREAD = 1 # Variable c_int '1'
SDL_MIX_MAXVOLUME = 128 # Variable c_int '128'
SDL_INIT_TIMER = 1 # Variable c_int '1'
SDL_HINT_RENDER_DRIVER = 'SDL_RENDER_DRIVER' # Variable STRING '(const char*)"SDL_RENDER_DRIVER"'
SDL_PREALLOC = 1 # Variable c_int '1'
SDL_HAT_RIGHT = 2 # Variable c_int '2'
SDL_ALPHA_OPAQUE = 255 # Variable c_int '255'
SDL_HINT_FRAMEBUFFER_ACCELERATION = 'SDL_FRAMEBUFFER_ACCELERATION' # Variable STRING '(const char*)"SDL_FRAMEBUFFER_ACCELERATION"'
SDL_INIT_EVERYTHING = 65535 # Variable c_int '65535'
SDL_ICONV_EINVAL = 18446744073709551612L # Variable c_ulong '-4u'
SDL_VIDEO_DRIVER_X11_HAS_XKBKEYCODETOKEYSYM = 1 # Variable c_int '1'
SDL_ENABLE = 1 # Variable c_int '1'
SDL_BUTTON_X2MASK = 16 # Variable c_int '16'
SDL_VIDEO_DRIVER_X11_DYNAMIC_XCURSOR = 'libXcursor.so.1' # Variable STRING '(const char*)"libXcursor.so.1"'
SDL_VIDEO_DRIVER_X11_DYNAMIC_XRANDR = 'libXrandr.so.2' # Variable STRING '(const char*)"libXrandr.so.2"'
SDL_PRESSED = 1 # Variable c_int '1'
SDL_AUDIO_MASK_BITSIZE = 255 # Variable c_int '255'
SDL_ICONV_ERROR = 18446744073709551615L # Variable c_ulong '-1u'
SDL_HAT_RIGHTDOWN = 6 # Variable c_int '6'
SDL_WINDOWPOS_UNDEFINED_MASK = 536805376 # Variable c_int '536805376'
SDL_SWSURFACE = 0 # Variable c_int '0'
SDL_HINT_RENDER_VSYNC = 'SDL_RENDER_VSYNC' # Variable STRING '(const char*)"SDL_RENDER_VSYNC"'
SDL_VIDEO_DRIVER_X11_SUPPORTS_GENERIC_EVENTS = 1 # Variable c_int '1'
SDL_MAJOR_VERSION = 2 # Variable c_int '2'
SDL_HAT_LEFT = 8 # Variable c_int '8'
SDL_DONTFREE = 4 # Variable c_int '4'
SDL_POWER_LINUX = 1 # Variable c_int '1'
SDL_WINDOWPOS_UNDEFINED = 536805376 # Variable c_int '536805376'
SDL_VIDEO_DRIVER_X11_XSHAPE = 1 # Variable c_int '1'
SDL_LIL_ENDIAN = 1234 # Variable c_int '1234'
SDL_CACHELINE_SIZE = 128 # Variable c_int '128'
SDL_TEXTEDITINGEVENT_TEXT_SIZE = 32 # Variable c_int '32'
SDL_BUTTON_MMASK = 2 # Variable c_int '2'
SDL_BUTTON_X1MASK = 8 # Variable c_int '8'
SDL_VIDEO_DRIVER_X11_DYNAMIC_XEXT = 'libXext.so.6' # Variable STRING '(const char*)"libXext.so.6"'
SDL_AUDIO_MASK_DATATYPE = 256 # Variable c_int '256'
SDL_RELEASED = 0 # Variable c_int '0'
SDL_MUTEX_TIMEDOUT = 1 # Variable c_int '1'
SDL_VIDEO_DRIVER_X11_DYNAMIC = 'libX11.so.6' # Variable STRING '(const char*)"libX11.so.6"'
SDL_HAT_LEFTUP = 9 # Variable c_int '9'
SDL_ALPHA_TRANSPARENT = 0 # Variable c_int '0'
SDL_JOYSTICK_LINUX = 1 # Variable c_int '1'
SDL_TEXTINPUTEVENT_TEXT_SIZE = 32 # Variable c_int '32'
SDL_THREAD_PTHREAD_RECURSIVE_MUTEX = 1 # Variable c_int '1'
SDL_HAT_LEFTDOWN = 12 # Variable c_int '12'
SDLK_SCANCODE_MASK = 1073741824 # Variable c_int '1073741824'
SDL_INIT_JOYSTICK = 512 # Variable c_int '512'
SDL_INPUT_LINUXEV = 1 # Variable c_int '1'
SDL_AUDIO_DRIVER_DUMMY = 1 # Variable c_int '1'
SDL_INIT_AUDIO = 16 # Variable c_int '16'
SDL_INIT_NOPARACHUTE = 1048576 # Variable c_int '1048576'
SDL_VIDEO_DRIVER_X11_XINPUT2 = 1 # Variable c_int '1'
SDL_BUTTON_LEFT = 1 # Variable c_int '1'
SDL_AUDIO_ALLOW_CHANNELS_CHANGE = 4 # Variable c_int '4'
SDL_BIG_ENDIAN = 4321 # Variable c_int '4321'
SDL_PATCHLEVEL = 0 # Variable c_int '0'
SDL_WINDOWPOS_CENTERED_MASK = 805240832 # Variable c_int '805240832'
SDL_VIDEO_DRIVER_X11_DYNAMIC_XINPUT2 = 'libXi.so.6' # Variable STRING '(const char*)"libXi.so.6"'
SDL_AUDIO_MASK_SIGNED = 32768 # Variable c_int '32768'
SDL_TIMER_UNIX = 1 # Variable c_int '1'
_SDL_Joystick._fields_ = [
]
class _IO_marker(Structure):
    pass
__off_t = c_long
_IO_lock_t = None
__off64_t = c_long
_IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', STRING),
    ('_IO_read_end', STRING),
    ('_IO_read_base', STRING),
    ('_IO_write_base', STRING),
    ('_IO_write_ptr', STRING),
    ('_IO_write_end', STRING),
    ('_IO_buf_base', STRING),
    ('_IO_buf_end', STRING),
    ('_IO_save_base', STRING),
    ('_IO_backup_base', STRING),
    ('_IO_save_end', STRING),
    ('_markers', POINTER(_IO_marker)),
    ('_chain', POINTER(_IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_byte),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', c_void_p),
    ('__pad2', c_void_p),
    ('__pad3', c_void_p),
    ('__pad4', c_void_p),
    ('__pad5', size_t),
    ('_mode', c_int),
    ('_unused2', c_char * 20),
]
__va_list_tag._fields_ = [
]
_IO_marker._fields_ = [
    ('_next', POINTER(_IO_marker)),
    ('_sbuf', POINTER(_IO_FILE)),
    ('_pos', c_int),
]

