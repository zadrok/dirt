#!/usr/bin/python

import socket
import os
import struct
import hashlib
import numpy as np
import cv2
import pickle
import time

class Client(object):

  def __init__(self):
    super(Client, self).__init__()
    self.buffsize = 1024
    self.compressionQuility = 60
    self.port = 8080
    self.host = '192.168.0.73'
    self.fps = 5
    self.framePeriod = 1.0/self.fps


  def imgEncode(self,img,quality):
    encode_param = [cv2.IMWRITE_JPEG_QUALITY, quality]
    result, encimg = cv2.imencode('.jpg', img, encode_param)
    return encimg


  def imgDecode(self,img):
    return cv2.imdecode(img, 1)


  def receiveFile(self, sender):
    received = 0
    chunks = []
    while received < 4:
      data = sender.recv(4 - received)
      received += len(data)
      chunks.append(data)
    fsize = struct.unpack('!I', b''.join(chunks))[0]

    received = 0
    chunks = []
    while received < fsize:
      data = sender.recv(min(fsize - received, self.buffsize))
      received += len(data)
      chunks.append(data)
    file = b''.join(chunks)

    received = 0
    chunks = []
    while received < 64:
      data = sender.recv(64 - received)
      received += len(data)
      chunks.append(data)
    sha512 = b''.join(chunks)
    hash_ok = hashlib.sha512(file).digest() == sha512
    if hash_ok:
      pass
      # print('Hash is ok')
    else:
      print('Hash is not ok')

    return pickle.loads(file)


  def run(self):
    addr = (self.host, self.port)
    sock = socket.socket()
    sock.connect(addr)
    print('Connected to', addr)

    while(True):
      start = time.time()
      file = self.receiveFile(sock)
      frame = self.imgDecode(file)
      cv2.imshow('Client',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      time.sleep(max(self.framePeriod - (time.time() - start), 0))

    sock.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
  client = Client()
  client.run()
