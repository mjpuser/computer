import logging

logging.getLogger().setLevel(logging.INFO)


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

  def down(self):
    self.state['y'] = min(self.y_max, self.state['y'] + 1)
  
  def right(self):
    self.state['x'] = min(self.x_max, self.state['x'] + 1)
  
  def left(self):
    self.state['x'] = max(0, self.state['x'] - 1)

