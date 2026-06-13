from __future__ import annotations

from app.core.models import Order, OrderStatus


class ExecutionAdapterAgent:
    def __init__(self, settings):
        self.settings = settings

    def execute(self, order: Order) -> Order:
        order.status = OrderStatus.OPEN
        return order
