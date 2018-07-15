class Shape:
    edge = 0

    def set_edge(self, e):
        self.edge = e
    def display(self):
        for i in range(self.edge):
            for j in range(i + 1):
                print('* ', end='')
            print("")

n = int(input())

tri = Shape()
tri.set_edge(n)
tri.display()