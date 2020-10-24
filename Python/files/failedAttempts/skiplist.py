class Skiplist:
    class Node:
        def __init__(self, val: int):
            self.val = val
            self.next = None
            self.prev = None
            self.up = None
            self.down = None

    class Level:
        def __init__(self, lvl: int):
            self.lvl = lvl
            self.lvlHead = None

    def __init__(self):
        self.head = None
        self.pAddDenom = 2
        self.height = 0

    def search(self, target: int) -> bool:
        # Start at the head
        # there is nothing, return false
        # if there is something
            # if current value is what's being trying to be found return true

    def add(self, num: int) -> None:
        
    def erase(self, num: int) -> bool:
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)