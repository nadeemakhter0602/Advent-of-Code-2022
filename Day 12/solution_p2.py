class Queue:
    class ListNode():
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, element):
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
            self.head = self.head.next
            self.length -= 1
            return element

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
        return self.length


with open('input.txt') as f:
    grid = []
    initial_states = []
    goal_state = (0, 0)
    lines = f.read().split('\n')
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[0])):
            if lines[i][j] == 'E':
                goal_state = (i, j)
                row.append('z')
            elif lines[i][j] == 'S' or lines[i][j] == 'a':
                initial_states.append((i, j))
                row.append('a')
            else:
                row.append(lines[i][j])
        grid.append(row)
    shortest_distance = float('inf')
    for initial_state in initial_states:
        queue = Queue()
        queue.enqueue((initial_state, 0))
        visited = set()
        current_shortest = float('inf')
        print('Traversing with initial state :', initial_state)
        while len(queue) > 0:
            current_state, distance = queue.dequeue()
            if current_state in visited:
                continue
            visited.add(current_state)
            if current_state == goal_state:
                current_shortest = distance
                break
            i, j = current_state
            if len(grid) > i - 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i - 1][j]):
                queue.enqueue(((i - 1, j), distance + 1))
            if len(grid) > i + 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i + 1][j]):
                queue.enqueue(((i + 1, j), distance + 1))
            if len(grid[0]) > j - 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i][j - 1]):
                queue.enqueue(((i, j - 1), distance + 1))
            if len(grid[0]) > j + 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i][j + 1]):
                queue.enqueue(((i, j + 1), distance + 1))
        if shortest_distance > current_shortest:
            shortest_distance = current_shortest
    print(shortest_distance)
