import json
import logging

import pika

from core.models import Order, OrderItem

QUEUE = "order-created-queue"


class OrderCreatedListener:
    logger = logging.getLogger()

    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="broker"))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=QUEUE)
        self.channel.basic_consume(
            queue=QUEUE, on_message_callback=self.save_order, auto_ack=True
        )

    def save_order(self, channel, method, properties, body):
        order_payload = json.loads(body)

        (order, created) = Order.objects.update_or_create(
            order_code=order_payload["order_code"],
            defaults={"customer_code": order_payload["customer_code"]},
        )

        [
            OrderItem.objects.create(
                order=order,
                price=item["price"],
                product=item["product"],
                quantity=item["quantity"],
            )
            for item in order_payload["items"]
        ]

        if created:
            self.logger.info("Order created successfully")
        else:
            self.logger.info(f"Order {order.id} updated successfully")

    def start(self):
        self.logger.info(f"Listening for messages in queue {QUEUE}")
        self.channel.start_consuming()
