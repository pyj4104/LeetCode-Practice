class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.repeatable = False
        self.next = None
        self.req = 0

    def __str__(self):
        retVal = str(self.val) + " " + str(self.repeatable)
        return retVal

class Automata:
    def __init__(self, p: str) -> None:
        self.allChar = {}
        for i in range(97, 123):
            self.allChar[chr(i)] = i

        self.head = Node(p[0])
        index = self.head
        for char in p[1:]:
            if char == "*":
                index.repeatable = True
            else:
                if char == index.val:
                    index.req += 1
                else:
                    newNode = Node(char)
                    index.next = newNode
                    index = index.next

    def __str__(self):
        retVal = "\nStart\n"
        i = self.head
        while i is not None:
            retVal = retVal + str(i) + "\n"
            i = i.next
        return retVal

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            if s == "":
                return True
            else:
                return False
            
        myAutomata = Automata(p)

        i = myAutomata.head

        strIndex = 0

        while strIndex < len(s):
            char = s[strIndex]
            if i:
                # Matches
                if i.val == char or i.val == ".":
                    if i.req != 0:
                        i.req -= 1
                    else:
                        if not i.repeatable:
                            i = i.next
                # Does not match
                else:
                    if i.repeatable == True:
                        i = i.next
                        strIndex -= 1
                    else:
                        return False
            else:
                return False
            strIndex += 1

        while i:
            if i.repeatable and i.req == 0:
                i = i.next
            else:
                break
        if i:
            return False

        return True

s = Solution()
tests = [
            ["aa", "a"],\
            ["aa", "a*"],\
            ["ab", ".*"],\
            ["aab", "c*a*b"],\
            ["mississippi", "mis*is*p*."],\
            ["aaa", "a*a"],\
            ["aaa",]
        ]
for test in tests:
    #s.isMatch(test[0], test[1])
    print(s.isMatch(test[0], test[1]))
'''print(s.isMatch("a", "a"))
print(s.isMatch("a", "a*"))
print(s.isMatch("a", "."))
print(s.isMatch("aaa", ".*"))
print(s.isMatch("aaa", ".*"))
print(s.isMatch("aaa", ".*"))
print(s.isMatch("aaa", ".*"))
print(s.isMatch("aaa", ".*"))'''




