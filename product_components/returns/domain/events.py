from lib import event


class ReturnAdded(event.Event):
    reference_no: str
    customer: str

    def __hash__(self):
        return hash(self.reference_no)


