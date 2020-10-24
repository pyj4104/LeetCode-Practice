from queue import Queue
from .basicClasses.Helper import TestSuites, List

class Trie:
    def __init__(self, val: str, children: [str], wordLen: int):
        self.val = val
        self.children = {}
        self.wordLen = wordLen
        for i, child in enumerate(children):
            remaining = children[:i]
            if i+1 < len(children):
                remaining += children[i+1:]
            self.children[child] = Trie(child, remaining, wordLen)

    def checkStr(self, s: str, index: int):
        if not self.children:
            return (True, index)
        chars = s[:self.wordLen]
        if chars in self.children:
            result = self.children[chars].checkStr(s[self.wordLen:], index)
            return result
        else:
            return (False, index)

    def __repr__(self, level=0) -> str:
        ret = "\t"*level+repr(self.val)+"\n"
        for child in self.children:
            ret += self.children[child].__repr__(level+1)
        return ret

class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        if not len(s):
            return []

        if not words:
            return []

        head = Trie("", words, len(words[0]))
        totLength = len(words[0])*len(words)

        retVal = []

        for i in range(len(s)-totLength+1):
            #strToCheck.append((i, s[i:i+totLength]))
            results = head.checkStr(s[i:i+totLength], i)
            if results[0]:
                retVal.append(results[1])

        return retVal


