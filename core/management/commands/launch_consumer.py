import sys, os
from typing import Any

from django.core.management.base import BaseCommand

from core.queue_consumer import OrderCreatedListener


class Command(BaseCommand):
    help = "Starts the queue consumer"

    def handle(self, *args: Any, **options: Any) -> str | None:
        try:
            self.stdout.write("Starting queue consumer...")
            listener = OrderCreatedListener()
            listener.start()
        except KeyboardInterrupt:
            print("Interrupted")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
