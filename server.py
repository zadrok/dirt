#!/usr/bin/python

import socket
import os
import struct
import hashlib
import numpy as np
import cv2
import pickle
import time

class Server(object):

  def __init__(self):
    super(Server, self).__init__()
    self.buffsize = 1024
    self.compressionQuility = 60
    self.port = 8080
    self.host = 'localhost'
    self.fps = 5
    self.framePeriod = 1.0/self.fps


  def imgEncode(self,img,quality):
    encode_param = [cv2.IMWRITE_JPEG_QUALITY, quality]
    result, encimg = cv2.imencode('.jpg', img, encode_param)
    return encimg


  def imgDecode(self,img):
    return cv2.imdecode(img, 1)


  def getChunck(self, file, i):
    s = i
    n = i + self.buffsize
    return n, file[s:n]


  def sendFile(self, file, receiver):
    file = pickle.dumps(file)
    fsize = struct.pack('!I', len(file))
    receiver.send(fsize)
    i = 0
    while True:
      i, chunk = self.getChunck(file, i)
      if not chunk:
        break
      receiver.send(chunk)
    i = 0
    hash = hashlib.sha512()
    while True:
      i, chunk = self.getChunck(file, i)
      if not chunk:
        break
      hash.update(chunk)
    receiver.send(hash.digest())


  def run(self):
    cap = cv2.VideoCapture(0)
    addr = (self.host, self.port)
    sock = socket.socket()
    sock.bind(addr)
    sock.listen(5)
    client, addr = sock.accept()
    print('Got connection from:', addr)

    while(True):
      start = time.time()
      ret, frame = cap.read()
      file = self.imgEncode(frame,self.compressionQuility)
      self.sendFile(file, client)
      cv2.imshow('Server',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      time.sleep(max(self.framePeriod - (time.time() - start), 0))

    client.close()
    sock.close()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
  server = Server()
  server.run()
