import itertools
import multiprocessing
import sys


state = multiprocessing.shared_memory.SharedMemory(
  'computer_state',
  create=True,
  size=1024)


initial = {
  'offset.x': 0,
  'offset.y': 0
}



def reducer(state, payload):
  print(payload)
  return state


if __name__ == '__main__':
  state = initial
  for action in sys.stdin.readlines():
    state = reducer(state, action)
