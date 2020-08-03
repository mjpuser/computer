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
    command_type = headers.get('type', b'').decode('utf-8')
    command_name = headers.get('name', b'').decode('utf-8')

    try:
      payload = json.loads(message.body.decode('utf-8'))
    except json.JSONDecodeError as e:
      payload = []
    reducer = REDUCERS.get(command_type)

    if reducer is None:
      logging.error(f'Invalid command {command_type}.  Message headers: {headers}')
      raise ValueError()

    command = getattr(reducer, command_name)
    if command is None:
      logging.error(f'Invalid command {command_type}.{command_name}.  Message headers: {headers}')
      raise ValueError()

    logging.info(f'Running command: {command_type}.{command_name}')
    command(*payload)