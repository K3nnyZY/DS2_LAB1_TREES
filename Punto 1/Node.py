class Node:

    def __init__(self, user_id, user_name) -> None:
        
        self.user_id = user_id
        self.user_name = user_name
        self.left = None
        self.right = None
        self.level = 1

    def __str__(self) -> str:
        return f"Node value: {self.user_id}"