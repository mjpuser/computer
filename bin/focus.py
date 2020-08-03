#!/usr/bin/env python3

import redis
import sys
import numpy as np

redis_client = redis.Redis(host='localhost', port=6379, db=0)


class Dimensions:
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)
  
  @property
  def area(self):
    return self.x * self.y


def get_offset():
  x, y = redis_client.mget('offset_x', 'offset_y')
  return int(x), int(y)


def transform(frame, i, o):
  mask = np.ndarray((i.x, i.y))
  mask.fill(1)
  roi = np.zeros((o.x, o.y)) # region of interest
  x, y = get_offset()
  mask[y:y + o.y, x:x + o.x] = roi
  return np.ma.masked_array(frame, mask).compressed()


if __name__ == '__main__':
  i = Dimensions(*sys.argv[1].split('x')) # 100x100
  o = Dimensions(*sys.argv[2].split('x')) # 10x20

  while True:
    frame = sys.stdin.buffer.read(i.area)
    frame = np.frombuffer(frame, dtype=np.uint8).reshape((i.x, i.y,))
    out = transform(frame, i, o)
    sys.stdout.buffer.write(out.tobytes())
