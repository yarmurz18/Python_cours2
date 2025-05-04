import json
import time

from config import get_connection
import pika


def process_new_message(channel: pika.adapters.blocking_connection.BlockingChannel, method, properties, body):
    data = json.loads(body)
    event = data.get("event")
    user_id = data.get("user_id")
    print(f"Новий лог: {event}, user_id: {user_id}")
    time.sleep(1)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def consume_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message,
    )
    channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_logs(channel)


if __name__ == "__main__":
    main()
