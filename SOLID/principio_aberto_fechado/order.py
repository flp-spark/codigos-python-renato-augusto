 

class Order:

    def __init__(self, amount:float):
        self.amount = amount

    def apply_fixed_discount(self, discount:float):

        if discount > self.amount :
            print("Desconto não pode ser maior que o valor do pedido")

        self.amount = self.amount - discount

    def apply_percentage_discount(self, percentage:float):

        if percentage > 100 and percentage <= 0 :
            print("Insira um percentual entre 1% e 100%")

        self.amount = self.amount - (self.amount * percentage / 100)   

    def get_amount(self):
        
        return self.amount