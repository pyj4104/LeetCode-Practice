using System;
using System.Collections.Generic;

namespace LeetCodeSolCS
{
    public class LLNode
    {
        public int val;
        public LLNode next;

	    public LLNode(int val = 0, LLNode next = null)
        {
            this.val = val;
            this.next = next;
        }

        public override string ToString()
        {
            LLNode index = this;
            string retVal = "Start -> ";
            while(index != null)
            {
                retVal = retVal + index.val.ToString() + " -> ";
                index = index.next;
            }
            retVal += "End";

            return retVal;
        }
    }

    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;

        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public class DisplayMethods
    {
        public static string PrintInt(int num)
        {
            return num.ToString();
        }

        public static string PrintIntArr(int[] nums)
        {
            string retVal = "";
            foreach (int num in nums)
            {
                retVal += num + " ";
            }
            return retVal;
        }

        public static string PrintIntMatrix(int[,] matrix)
        {
            string retVal = "";
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    retVal += matrix[i, j];
                }
                retVal += "\n";
            }
            return retVal;
        }

        public static void PrintIntBTreeBFS(TreeNode head, string indent = "", bool last = true)
        {
            Console.Write(indent);
            if (last)
            {
                Console.Write("└─ ");
                indent += "  ";
            }
            else
            {
                Console.Write("├─ ");
                indent += "| ";
            }
            Console.WriteLine(head.val);

            var children = new List<TreeNode>();
            if (head.left != null)
                children.Add(head.left);
            if (head.right != null)
                children.Add(head.right);

            for (int i = 0; i < children.Count; i++)
                PrintIntBTreeBFS(children[i], indent, i == children.Count - 1);
        }

        public static void PrintIntBTreeDFS(TreeNode head, ref string retVal)
        {
            retVal += head.val.ToString() + " ";
            if (head.left != null)
            {
                PrintIntBTreeDFS(head.left, ref retVal);
            }
            if (head.right != null)
            {
                PrintIntBTreeDFS(head.right, ref retVal);
            }
        }
    }

    public class Helpers
    {
        public static LLNode ConstructLL(int[] vals)
        {
            LLNode dummy = new LLNode();
            LLNode index = dummy;

            for (int i = 0; i < vals.Length; i++)
            {
                LLNode node = new LLNode(vals[i]);
                index.next = node;
                index = index.next;
            }

            return dummy.next;
        }

        public static TreeNode ConstructBTree(int?[] vals)
        {
            int i = 0;
            TreeNode currentNode = null;

            TreeNode root = new TreeNode((int)vals[i]);
            i++;

            Queue<TreeNode> insertionOrder = new Queue<TreeNode>();

            insertionOrder.Enqueue(root);

            while(i < vals.Length)
            {
                if(currentNode == null || currentNode.right != null)
                {
                    currentNode = insertionOrder.Dequeue();
                }

                TreeNode newNode = null;

                if (vals[i] != null)
                {
                    newNode = new TreeNode((int)vals[i]);
                    insertionOrder.Enqueue(newNode);
                }

                if(currentNode.left == null)
                {
                    currentNode.left = newNode;
                }
                else
                {
                    currentNode.right = newNode;
                }

                i++;
            }


            return root;
        }
    }

    public class TestTestClass
    {
        Func<int, int, int> times;
        public TestTestClass()
        {
            times = (x, y) => x* y;
        }

        public void TestFunc()
        {
            List<object> test1 = new List<object> { 5, 6 };

            Test<int> testClass = new Test<int>();
            testClass.AddTest(test1);

            testClass.RunTest(this.times, DisplayMethods.PrintInt);
        }
    }
}
