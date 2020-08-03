import logging
from multiprocessing import shared_memory


offset = shared_memory.SharedMemory(
  'computer_offset', create=True, size=8)

logging.getLogger().setLevel(logging.INFO)


def update_shared_state(fn):
  def wrapper(*args, **kwargs):
    logging.info(args)
    state = fn(*args, **kwargs)


  return wrapper


class Eye:
  state = {
    'x': 0,
    'y': 0,
  }

  def __init__(self, x_max=200, y_max=200):
    self.x_max = x_max
    self.y_max = y_max

  def up(self):
    self.state['y'] = max(0, self.state['y'] - 1)
    return self.state

  def down(self):
    self.state['y'] = min(self.y_max, self.state['y'] + 1)
    return self.state
  
  def right(self):
    self.state['x'] = min(self.x_max, self.state['x'] + 1)
    return self.state
  
  def left(self):
    self.state['x'] = max(0, self.state['x'] - 1)
    return self.state

