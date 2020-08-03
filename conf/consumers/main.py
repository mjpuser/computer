import aiormq
import asyncio
import logging
from commands import consumer

logging.getLogger().setLevel(logging.INFO)


async def connect():
  return await aiormq.connect('amqp://guest:guest@rabbitmq/%2F')


def ack(func):
  async def ack(message):
    try:
      await func(message)
    except Exception as e:
      logging.info('Rejecting message')
      await message.channel.basic_reject(message.delivery.delivery_tag, requeue=False)
    else:
      await message.channel.basic_ack(message.delivery.delivery_tag)
  return ack


async def main():
  conn = await connect()
  channel = await conn.channel()
  c = consumer.Consumer()
  tag = await channel.basic_consume(c.queue, ack(c.consume))
  logging.info(f'Started {type(c).__name__} consumer binded to {c.queue} queue')


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.run_forever()
