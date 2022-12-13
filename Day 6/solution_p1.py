class DistinctQueue:
    class ListNode():
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.max_length = 4
        self.window = set()

    def enqueue(self, element):
        if self.length == self.max_length:
            self.dequeue()
        self.window.add(element)
        if self.head is None:
            self.head = self.ListNode(element)
            self.tail = self.head
        else:
            self.tail.next = self.ListNode(element)
            self.tail = self.tail.next
        self.length += 1

    def dequeue(self):
        if self.length > 0:
            element = self.head.data
            self.window.discard(element)
            self.head = self.head.next
            self.length -= 1
            self.recreate_window()
            return element

    def recreate_window(self):
        curr = self.head
        while curr != None:
            self.window.add(curr.data)
            curr = curr.next

    def __str__(self):
        curr = self.head
        s = ''
        s += '['
        while curr != None:
            s += '\'' + curr.data + '\''
            curr = curr.next
            if curr != None:
                s += ', '
        s += ']'
        return s

    def __len__(self):
        return len(self.window)


with open('input.txt') as f:
    queue = DistinctQueue()
    processed = 0
    while len(queue) != queue.max_length:
        char = f.read(1)
        queue.enqueue(char)
        processed += 1
    print(processed)
