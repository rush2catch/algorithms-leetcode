class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next



temp1 = Node(93)
print(temp1.get_data())
temp1.set_data(39)
print(temp1.get_data())
temp2 = Node(100)
print(temp2.data)
temp1.set_next(temp2)
print(temp1.next.data)