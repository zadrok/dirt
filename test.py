import socket
import os
import struct
import hashlib
import numpy as np
import cv2
import pickle
import time
import zlib


quality = 20
level = 9


cap = cv2.VideoCapture(0)
ret, frame = cap.read()

encode_param = [cv2.IMWRITE_JPEG_QUALITY, quality]
result, encimg = cv2.imencode('.jpg', frame, encode_param)

file = pickle.dumps(encimg)
imgZ = zlib.compress( frame, level )

newFrame = cv2.imdecode(encimg, 1)

print( "file " + str( len( file ) ) )
print( "imgZ " + str( len( imgZ ) ) )

cv2.imshow('frame',newFrame)

while (True):
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()
