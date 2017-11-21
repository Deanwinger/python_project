import os
import json
from optparse import OptionParser
from threading import Timer
import re
import time
import sys
import atexit
import signal
import logging

#'#1'
CONFIG_FILE = '#'
PID_FILE =  '/tmp/alans-alarm.pid'
LOG_FILE = '/var/log/alans-alarm.log'

#'#2'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)-15s [pid:%(process)d] [thread:%(threadName)s] [%(filename)s] [%(levelname)s] %(message)s",
)
LOG = logging.getLogger(__name__)

# def main()