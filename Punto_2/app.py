from Tree import *

# root = DNSNode(".", "0.0.0.0")
# com = DNSNode(".com", "1.1.1.1", root)
# org = DNSNode("org", "2.2.2.2", root)
# google = DNSNode("google.com", "3.3.3.3", com)
# facebook = DNSNode("facebook.com", "4.4.4.4", com)  
# print(com.child[1])

DNSsTree = DNSTree()

DNSsTree.insert(".", "0.0.0.0")
DNSsTree.insert(".com", "1.1.1.1", ".")