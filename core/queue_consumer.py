import json
import logging

import pika

QUEUE = "order-created-queue"


class OrderCreatedListener:
    logger = logging.getLogger()

    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="broker"))

        self.channel = connection.channel()

        self.channel.queue_declare(queue=QUEUE)

        self.channel.basic_consume(
            queue=QUEUE, on_message_callback=self.callback, auto_ack=True
        )

    def callback(self, channel, method, properties, body):
        self.logger.info(json.loads(body))

    def start(self):
        self.logger.info(f"Listening for messages in queue {QUEUE}")
        self.channel.start_consuming()
