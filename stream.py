#!/usr/bin/python

from client import Client
from setver import Server
import sys

if __name__ == '__main__':
  if sys.argv[1] == 'client':
    Client(ip=sys.argv[2]).run()
  elif sys.argv[1] == 'server':
    Server().run()
