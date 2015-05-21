'''Wrapper for fanotify.h

Generated with:
/usr/bin/ctypesgen.py -a /usr/include/linux/fanotify.h -o fanotify_defines.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

# /usr/include/asm-generic/int-ll64.h: 19
for _lib in _libs.values():
    try:
        __s8 = (c_char).in_dll(_lib, '__s8')
        break
    except:
        pass

__u8 = c_ubyte # /usr/include/asm-generic/int-ll64.h: 20

__u16 = c_ushort # /usr/include/asm-generic/int-ll64.h: 23

# /usr/include/asm-generic/int-ll64.h: 25
for _lib in _libs.values():
    try:
        __s32 = (c_int).in_dll(_lib, '__s32')
        break
    except:
        pass

__u32 = c_uint # /usr/include/asm-generic/int-ll64.h: 26

# /usr/include/asm-generic/int-ll64.h: 32
for _lib in _libs.values():
    try:
        __s64 = (c_long).in_dll(_lib, '__s64')
        break
    except:
        pass

__u64 = c_ulonglong # /usr/include/asm-generic/int-ll64.h: 33

# /usr/include/linux/posix_types.h: 26
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'fds_bits',
]
struct_anon_1._fields_ = [
    ('fds_bits', c_ulong * (1024 / (8 * sizeof(c_long)))),
]

__kernel_fd_set = struct_anon_1 # /usr/include/linux/posix_types.h: 26

__kernel_sighandler_t = CFUNCTYPE(UNCHECKED(None), c_int) # /usr/include/linux/posix_types.h: 29

__kernel_key_t = c_int # /usr/include/linux/posix_types.h: 32

__kernel_mqd_t = c_int # /usr/include/linux/posix_types.h: 33

__kernel_old_uid_t = c_ushort # /usr/include/asm/posix_types_64.h: 10

__kernel_old_gid_t = c_ushort # /usr/include/asm/posix_types_64.h: 11

__kernel_old_dev_t = c_ulong # /usr/include/asm/posix_types_64.h: 14

__kernel_long_t = c_long # /usr/include/asm-generic/posix_types.h: 14

__kernel_ulong_t = c_ulong # /usr/include/asm-generic/posix_types.h: 15

__kernel_ino_t = __kernel_ulong_t # /usr/include/asm-generic/posix_types.h: 19

__kernel_mode_t = c_uint # /usr/include/asm-generic/posix_types.h: 23

__kernel_pid_t = c_int # /usr/include/asm-generic/posix_types.h: 27

__kernel_ipc_pid_t = c_int # /usr/include/asm-generic/posix_types.h: 31

__kernel_uid_t = c_uint # /usr/include/asm-generic/posix_types.h: 35

__kernel_gid_t = c_uint # /usr/include/asm-generic/posix_types.h: 36

__kernel_suseconds_t = __kernel_long_t # /usr/include/asm-generic/posix_types.h: 40

__kernel_daddr_t = c_int # /usr/include/asm-generic/posix_types.h: 44

__kernel_uid32_t = c_uint # /usr/include/asm-generic/posix_types.h: 48

__kernel_gid32_t = c_uint # /usr/include/asm-generic/posix_types.h: 49

__kernel_size_t = __kernel_ulong_t # /usr/include/asm-generic/posix_types.h: 71

__kernel_ssize_t = __kernel_long_t # /usr/include/asm-generic/posix_types.h: 72

__kernel_ptrdiff_t = __kernel_long_t # /usr/include/asm-generic/posix_types.h: 73

# /usr/include/asm-generic/posix_types.h: 80
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'val',
]
struct_anon_2._fields_ = [
    ('val', c_int * 2),
]

__kernel_fsid_t = struct_anon_2 # /usr/include/asm-generic/posix_types.h: 80

__kernel_off_t = __kernel_long_t # /usr/include/asm-generic/posix_types.h: 86

__kernel_loff_t = c_longlong # /usr/include/asm-generic/posix_types.h: 87

__kernel_time_t = __kernel_long_t # /usr/include/asm-generic/posix_types.h: 88

__kernel_clock_t = __kernel_long_t # /usr/include/asm-generic/posix_types.h: 89

__kernel_timer_t = c_int # /usr/include/asm-generic/posix_types.h: 90

__kernel_clockid_t = c_int # /usr/include/asm-generic/posix_types.h: 91

__kernel_caddr_t = String # /usr/include/asm-generic/posix_types.h: 92

__kernel_uid16_t = c_ushort # /usr/include/asm-generic/posix_types.h: 93

__kernel_gid16_t = c_ushort # /usr/include/asm-generic/posix_types.h: 94

__le16 = __u16 # /usr/include/linux/types.h: 27

__be16 = __u16 # /usr/include/linux/types.h: 28

__le32 = __u32 # /usr/include/linux/types.h: 29

__be32 = __u32 # /usr/include/linux/types.h: 30

__le64 = __u64 # /usr/include/linux/types.h: 31

__be64 = __u64 # /usr/include/linux/types.h: 32

__sum16 = __u16 # /usr/include/linux/types.h: 34

__wsum = __u32 # /usr/include/linux/types.h: 35

# /usr/include/linux/fanotify.h: 96
for _lib in _libs.values():
    try:
        response = (__u32).in_dll(_lib, 'response')
        break
    except:
        pass

__const = c_int # <command-line>: 5

# <command-line>: 8
try:
    CTYPESGEN = 1
except:
    pass

# /usr/include/stdc-predef.h: 19
try:
    _STDC_PREDEF_H = 1
except:
    pass

# /usr/include/stdc-predef.h: 41
try:
    __STDC_IEC_559__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 49
try:
    __STDC_IEC_559_COMPLEX__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 54
try:
    __STDC_ISO_10646__ = 201103L
except:
    pass

# /usr/include/stdc-predef.h: 57
try:
    __STDC_NO_THREADS__ = 1
except:
    pass

# /usr/include/asm/bitsperlong.h: 5
try:
    __BITS_PER_LONG = 64
except:
    pass

# /usr/include/linux/posix_types.h: 22
try:
    __FD_SETSIZE = 1024
except:
    pass

__kernel_old_uid_t = __kernel_old_uid_t # /usr/include/asm/posix_types_64.h: 12

__kernel_old_dev_t = __kernel_old_dev_t # /usr/include/asm/posix_types_64.h: 15

# /usr/include/linux/fanotify.h: 7
try:
    FAN_ACCESS = 1
except:
    pass

# /usr/include/linux/fanotify.h: 8
try:
    FAN_MODIFY = 2
except:
    pass

# /usr/include/linux/fanotify.h: 9
try:
    FAN_CLOSE_WRITE = 8
except:
    pass

# /usr/include/linux/fanotify.h: 10
try:
    FAN_CLOSE_NOWRITE = 16
except:
    pass

# /usr/include/linux/fanotify.h: 11
try:
    FAN_OPEN = 32
except:
    pass

# /usr/include/linux/fanotify.h: 13
try:
    FAN_Q_OVERFLOW = 16384
except:
    pass

# /usr/include/linux/fanotify.h: 15
try:
    FAN_OPEN_PERM = 65536
except:
    pass

# /usr/include/linux/fanotify.h: 16
try:
    FAN_ACCESS_PERM = 131072
except:
    pass

# /usr/include/linux/fanotify.h: 18
try:
    FAN_ONDIR = 1073741824
except:
    pass

# /usr/include/linux/fanotify.h: 20
try:
    FAN_EVENT_ON_CHILD = 134217728
except:
    pass

# /usr/include/linux/fanotify.h: 23
try:
    FAN_CLOSE = (FAN_CLOSE_WRITE | FAN_CLOSE_NOWRITE)
except:
    pass

# /usr/include/linux/fanotify.h: 26
try:
    FAN_CLOEXEC = 1
except:
    pass

# /usr/include/linux/fanotify.h: 27
try:
    FAN_NONBLOCK = 2
except:
    pass

# /usr/include/linux/fanotify.h: 30
try:
    FAN_CLASS_NOTIF = 0
except:
    pass

# /usr/include/linux/fanotify.h: 31
try:
    FAN_CLASS_CONTENT = 4
except:
    pass

# /usr/include/linux/fanotify.h: 32
try:
    FAN_CLASS_PRE_CONTENT = 8
except:
    pass

# /usr/include/linux/fanotify.h: 33
try:
    FAN_ALL_CLASS_BITS = ((FAN_CLASS_NOTIF | FAN_CLASS_CONTENT) | FAN_CLASS_PRE_CONTENT)
except:
    pass

# /usr/include/linux/fanotify.h: 36
try:
    FAN_UNLIMITED_QUEUE = 16
except:
    pass

# /usr/include/linux/fanotify.h: 37
try:
    FAN_UNLIMITED_MARKS = 32
except:
    pass

# /usr/include/linux/fanotify.h: 39
try:
    FAN_ALL_INIT_FLAGS = ((((FAN_CLOEXEC | FAN_NONBLOCK) | FAN_ALL_CLASS_BITS) | FAN_UNLIMITED_QUEUE) | FAN_UNLIMITED_MARKS)
except:
    pass

# /usr/include/linux/fanotify.h: 44
try:
    FAN_MARK_ADD = 1
except:
    pass

# /usr/include/linux/fanotify.h: 45
try:
    FAN_MARK_REMOVE = 2
except:
    pass

# /usr/include/linux/fanotify.h: 46
try:
    FAN_MARK_DONT_FOLLOW = 4
except:
    pass

# /usr/include/linux/fanotify.h: 47
try:
    FAN_MARK_ONLYDIR = 8
except:
    pass

# /usr/include/linux/fanotify.h: 48
try:
    FAN_MARK_MOUNT = 16
except:
    pass

# /usr/include/linux/fanotify.h: 49
try:
    FAN_MARK_IGNORED_MASK = 32
except:
    pass

# /usr/include/linux/fanotify.h: 50
try:
    FAN_MARK_IGNORED_SURV_MODIFY = 64
except:
    pass

# /usr/include/linux/fanotify.h: 51
try:
    FAN_MARK_FLUSH = 128
except:
    pass

# /usr/include/linux/fanotify.h: 53
try:
    FAN_ALL_MARK_FLAGS = (((((((FAN_MARK_ADD | FAN_MARK_REMOVE) | FAN_MARK_DONT_FOLLOW) | FAN_MARK_ONLYDIR) | FAN_MARK_MOUNT) | FAN_MARK_IGNORED_MASK) | FAN_MARK_IGNORED_SURV_MODIFY) | FAN_MARK_FLUSH)
except:
    pass

# /usr/include/linux/fanotify.h: 67
try:
    FAN_ALL_EVENTS = (((FAN_ACCESS | FAN_MODIFY) | FAN_CLOSE) | FAN_OPEN)
except:
    pass

# /usr/include/linux/fanotify.h: 75
try:
    FAN_ALL_PERM_EVENTS = (FAN_OPEN_PERM | FAN_ACCESS_PERM)
except:
    pass

# /usr/include/linux/fanotify.h: 78
try:
    FAN_ALL_OUTGOING_EVENTS = ((FAN_ALL_EVENTS | FAN_ALL_PERM_EVENTS) | FAN_Q_OVERFLOW)
except:
    pass

# /usr/include/linux/fanotify.h: 82
try:
    FANOTIFY_METADATA_VERSION = 3
except:
    pass

# /usr/include/linux/fanotify.h: 100
try:
    FAN_ALLOW = 1
except:
    pass

# /usr/include/linux/fanotify.h: 101
try:
    FAN_DENY = 2
except:
    pass

# /usr/include/linux/fanotify.h: 103
try:
    FAN_NOFD = (-1)
except:
    pass

# /usr/include/linux/fanotify.h: 106
class struct_fanotify_event_metadata(Structure):
    pass

# /usr/include/linux/fanotify.h: 106
try:
    FAN_EVENT_METADATA_LEN = sizeof(struct_fanotify_event_metadata)
except:
    pass

# /usr/include/linux/fanotify.h: 108
def FAN_EVENT_NEXT(meta, len):
    return (len - (meta.contents.event_len))

# /usr/include/linux/fanotify.h: 112
def FAN_EVENT_OK(meta, len):
    return (((len >= FAN_EVENT_METADATA_LEN) and (((meta.contents.event_len).value) >= FAN_EVENT_METADATA_LEN)) and (((meta.contents.event_len).value) <= len))

fanotify_event_metadata = struct_fanotify_event_metadata # /usr/include/linux/fanotify.h: 106

# No inserted files

