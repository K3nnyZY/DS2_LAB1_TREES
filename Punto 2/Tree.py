from Node import *
class DNSTree:
    def __init__(self):
        self.root = None

    def insert(self, name, ip, parent=None):
        if self.root is None:
            self.root = DNSNode(name, ip, parent)
        else:
            self.root.addChild(self)