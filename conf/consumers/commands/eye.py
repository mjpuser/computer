import logging
import redis


logging.getLogger().setLevel(logging.INFO)

redis_client = redis.Redis(host='redis', port=6379, db=0)
x, y = redis_client.mget('offset_x', 'offset_y')
x = int(x or '0')
y = int(y or '0')
redis_client.mset({'offset_x': x, 'offset_y': y})

def update_shared_state(fn):
  def wrapper(*args, **kwargs):
    logging.info(args)
    state = fn(*args, **kwargs)
    redis_client.mset({'offset_x': state['x'], 'offset_y': state['y']})

  return wrapper


class Eye:
  state = {
    'x': x,
    'y': y,
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

