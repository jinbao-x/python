#!/usr/bin/python2
import time
from __future__ import print_function
for i in range(101):
    print("\r{:2}%".format(i),end='')
    time.sleep(0.5)
