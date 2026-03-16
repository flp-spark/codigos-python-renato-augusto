# Codigo sobre principio de responsabilidade unica

class Order:

    def __init__(self, uuid:str, amount:float):

        self._uuid = uuid
        self._amount = amount

    def get_uuid(self) -> str:

        return self._uuid
    
    def get_amount(self) -> float:

        return self._amount