#!/usr/bin/python

from client import Client
from server import Server
import sys

if __name__ == '__main__':
  if sys.argv[1] == 'client':
    if len( sys.argv ) == 3:
      Client(ip=sys.argv[2]).run()
    else:
      Client().run()
  elif sys.argv[1] == 'server':
    Server().run()
