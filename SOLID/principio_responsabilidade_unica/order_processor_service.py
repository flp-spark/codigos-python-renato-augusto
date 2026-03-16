# classe que processa o pedido(order)

from order import Order

class ProcessOrderService():

    def process_order(self, order:Order):
        
        self.check_inventory(order)
        self.calculate_total(order)
        self.process_payment(order)

    def check_inventory(self, order:Order):
        pass
        # Logica para verirficar o estoque

    def calculate_total(self, order:Order):
        pass
        # Logica para calcular o total

    def process_payment(self, order:Order):
        pass
        # Logica para processar o pagamento
