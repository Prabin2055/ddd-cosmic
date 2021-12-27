from lib import event


class CategoryAdded(event.Event):
    product_name: str
    category: str

    def __hash__(self):
        return hash(self.category)

