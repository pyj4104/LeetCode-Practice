class Solution:
    class Trie:
        class Node:
            def __init__(self, val: str):
                self.name = val
                self.quantity = 0
                self.children = {}

            def add(self, val: str):
                self.quantity += 1
                if not val == "":
                    if val[0] not in self.children:
                        self.children[val[0]] = Solution.Trie.Node(val[0])
                    self.children[val[0]].add(val[1::])

            def chckStr(self, numWords) -> str:
                if self.quantity != numWords:
                    return ""
                retVal = self.name
                for item in self.children:
                    retVal += self.children[item].chckStr(numWords)
                return retVal

            def __str__(self) -> str:
                retVal = ''
                retVal += self.name + ", " + str(self.quantity) + '\n'
                for child in self.children.values():
                    retVal += child.__str__()
                return retVal

        def __init__(self):
            self.heads = {}

        def add(self, s: str):
            if s == "":
                self.heads[s] = 1
                return

            if s[0] not in self.heads:
                self.heads[s[0]] = Solution.Trie.Node(s[0])
            self.heads[s[0]].add(s[1::])

        def chckStr(self, numWords) -> str:
            if len(self.heads) > 1:
                return ""
            for item in self.heads:
                if item != "":
                    return self.heads[item].chckStr(numWords)
                else:
                    return ""

        def __str__(self) -> str:
            retVal = ''
            for head in self.heads:
                if head != "":
                    retVal += head + ": " + '\n' + self.heads[head].__str__()
                else:
                    retVal += "'': None"
            return retVal

    def longestCommonPrefix(self, strs: [str]) -> str:
        if strs == []:
            return ""
        tree = Solution.Trie()
        for item in strs:
            tree.add(item)
        return tree.chckStr(len(strs))

s = Solution()
testCases = [\
            ['ho', 'he', 'hi'],\
            ['dog', 'racecar', 'car'],\
            ["flower","flow","flight"],\
            ["", "hi"],\
            ["", ""]
            ]
for testCase in testCases:
    print(s.longestCommonPrefix(testCase))

