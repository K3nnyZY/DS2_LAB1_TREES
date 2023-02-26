class Node:
    def __init__(self, data, right = None, left = None):
        self.right =  right
        self.left = left
        self.data = data
        self.height = 1

    def __str__(self):
        return  f" {self.data}"