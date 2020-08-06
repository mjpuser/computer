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

i = None
o = None

def get_offset():
  x, y = redis_client.mget('offset_x', 'offset_y')
  return max(min(int(x), i.x - o.x), 0), max(min(int(y), i.y - o.y), 0)


def transform(frame, i, o):
  mask = np.ndarray((i.y, i.x))
  mask.fill(1)
  roi = np.zeros((o.y, o.x)) # region of interest
  x, y = get_offset()
  mask[y:y + o.y, x:x + o.x] = roi
  return np.ma.masked_array(frame, mask).compressed()


if __name__ == '__main__':
  i = Dimensions(*sys.argv[1].split('x')) # 100x100
  o = Dimensions(*sys.argv[2].split('x')) # 10x20

  while True:
    BYTES_PER_PIXEL = 4
    frame = sys.stdin.buffer.read(i.area * BYTES_PER_PIXEL)
    frame = np.frombuffer(frame, dtype=np.uint32).reshape((i.y, i.x,))
    out = transform(frame, i, o)
    sys.stdout.buffer.write(out.tobytes())
