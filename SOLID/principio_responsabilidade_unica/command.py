# Aqui é onde processa os os pedidos(orders)

from principio_responsabilidade_unica.order import Order
from principio_responsabilidade_unica.order_processor_service import ProcessOrderService

new_order = Order(
    uuid = '554310-2568-e59021-u3748-5h2970',
    amount = 300
)

new_order_process = ProcessOrderService()
new_order_process.process_order(new_order)