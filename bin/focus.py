#!/usr/bin/env python3

import sys
import numpy as np


BYTES_PER_PIXEL = 1


class Dimensions:
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)
  
  @property
  def area(self):
    return self.x * self.y


def transform(frame, i, o, offset):
  mask = np.ndarray((i.x, i.y))
  mask.fill(1)
  roi = np.zeros((o.x, o.y)) # region of interest
  mask[offset.y:offset.y + o.y, offset.x:offset.x + o.x] = roi
  return np.ma.masked_array(frame, mask).compressed()


if __name__ == '__main__':
  i = Dimensions(*sys.argv[1].split('x')) # 100x100
  o = Dimensions(*sys.argv[2].split('x')) # 10x20
  offset = Dimensions(0, 0,)

  while True:
    frame = sys.stdin.buffer.read(i.area)
    frame = np.frombuffer(frame, dtype=np.uint8).reshape((i.x, i.y,))
    out = transform(frame, i, o, offset)
    sys.stdout.buffer.write(out.tobytes())
