#!/usr/bin/python
import ctypes
import os

import ctypes
from ctypes.util import find_library

from fanotify_defines import *


libc = ctypes.cdll.LoadLibrary(find_library("c"))

fanotify_fd = libc.fanotify_init(FAN_CLOEXEC, 0)
libc.fanotify_mark(fanotify_fd, FAN_MARK_ADD | FAN_MARK_MOUNT, FAN_CLOSE_WRITE, 0, '/')

while True:
    data = os.read(fanotify_fd, 24)
    bb = ctypes.create_string_buffer(data)
    metadata = fanotify_event_metadata()
    ctypes.memmove(ctypes.addressof(metadata), ctypes.addressof(bb), len(data))
    print "event_len: %d" % metadata.event_len
    print "vers: %d" % metadata.vers
    print "fd: %d" % metadata.fd
    print "pid: %d" % metadata.pid

    filename = os.readlink("/proc/self/fd/%d" % (metadata.fd))
    print "filename: %s" % filename
    try:
        cmdline_fh = open("/proc/%d/cmdline" % metadata.pid, "r")
        cmdline = cmdline_fh.read()
        cmdline = cmdline.split(chr(0))
    except IOError:
        cmdline = []

    print "cmdline: %s" % (cmdline)
    os.close(metadata.fd)
    print "--------------------------------------------------------------------"
