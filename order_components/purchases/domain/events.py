from lib import event


class PurchaseAdded(event.Event):
    purchase_no: str
    date: int

    def __hash__(self):
        return hash(self.purchase_no)

