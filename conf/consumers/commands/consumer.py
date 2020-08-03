import json
import logging

from . import eye

logging.getLogger().setLevel(logging.INFO)



REDUCERS = {
  'eye': eye.Eye()
}


class Consumer:
  queue = 'commands'

  async def consume(self, message):
    headers = message.header.properties.headers
    command_type = headers['type'].decode('utf-8')
    command_name = headers['name'].decode('utf-8')
    payload = json.loads(message.body.decode('utf-8'))
    reducer = REDUCERS.get(command_type)

    if reducer is None:
      logging.error(f'Invalid command {command_type}.  Message headers: {headers}')

    command = getattr(reducer, command_name)
    if command is None:
      logging.error(f'Invalid command {command_type}.{command_name}.  Message headers: {headers}')

    logging.info(f'Running command: {command_type}.{command_name}')
    command(*payload)