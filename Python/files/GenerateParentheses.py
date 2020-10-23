class BinTreeNode:
    def __init__(self, val: str):
        self.key = val
        self.left = None
        self.right = None
        self.isValid = True
        self.isLeaf = False

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % (self.key + " " + str(self.isValid) + " " + str(self.isLeaf))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % (self.key + " " + str(self.isValid) + " " + str(self.isLeaf))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % (self.key + " " + str(self.isValid) + " " + str(self.isLeaf))
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % (self.key + " " + str(self.isValid))
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 0:
            return True

        retVal1 = []
        paranList = {'(': 0, ')': 0}
        head = BinTreeNode("")
        self.BuildTreeBU(head, 2*n, paranList)
        self.GenerateAnswer(head, '', retVal1)

        retVal2 = []
        paranList2 = {'(': 0, ')': 0}
        head2 = BinTreeNode("")
        self.BuildTree(head2, 2*n, paranList2, '', retVal2)

        print(retVal1, retVal2)

    def BuildTreeBU(self, head: BinTreeNode, n: int, usedList: {}):
        if n == 0:
            head.isLeaf = True
            if usedList["("] - usedList[")"] != 0:
                head.isValid = False
        else:
            if usedList[")"] > usedList["("]:
                head.isValid = False
                return None

            n -= 1

            usedList[")"] += 1
            head.right = BinTreeNode(val = ")")
            self.BuildTreeBU(head.right, n, usedList)

            usedList[")"] -= 1

            usedList["("] += 1
            head.left = BinTreeNode(val = "(")
            self.BuildTreeBU(head.left, n, usedList)

            usedList["("] -= 1

    def GenerateAnswer(self, head:BinTreeNode, val: str, retVal = []):
        if not head.isValid:
            return ""

        val += head.key

        if head.isLeaf:
            retVal.append(val)
        else:
            self.GenerateAnswer(head.left, val, retVal)
            self.GenerateAnswer(head.right, val, retVal)

    def BuildTree(self, head: BinTreeNode, n: int, usedList: {}, val: str, retVal = []):
        val += head.key
        if n == 0:
            if usedList["("] - usedList[")"] != 0:
                return ""
            else:
                retVal.append(val)
        else:
            if usedList[")"] > usedList["("]:
                return ""
            else:
                n -= 1
                usedList[")"] += 1
                head.right = BinTreeNode(val = ")")
                self.BuildTree(head.right, n, usedList, val, retVal)

                usedList[")"] -= 1

                usedList["("] += 1
                head.left = BinTreeNode(val = "(")
                self.BuildTree(head.left, n, usedList, val, retVal)

                usedList["("] -= 1

s = Solution()
tcs = [1, 2, 3, 4]
for tc in tcs:
    s.generateParenthesis(tc)