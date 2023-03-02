class Node:
    def __init__(self, user_name, user_id) -> None:
        self.user_name = user_name
        self.user_id = user_id
        self.left = None
        self.right = None
        self.height = 1