from lib import event


class SalesAdded(event.Event):
    reference_no: str
    customer: str

    def __hash__(self):
        return hash(self.reference_no)


