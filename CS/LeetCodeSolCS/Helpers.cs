using System;

namespace LeetCodeSolCS
{
    public struct LLNode
    {
        public int val;
        pubilc LLNode next;

	    public LLNode(int val = 0, LLNode next = null)
        {
            this.val = val;
            this.next = next;
        }

        public string ToString()
        {
            LLNode index = this;
            while(index)
            {
                Console.WriteLine(index.val);
                index = index.next;
            }
        }
    }

    public class Helpers
    {
        static LLNode ConstructLL(int[] vals)
        {
            LLNode dummy = new LLNode();
            LLNode index = dummy;

            for (int i = 0; i < vals.Length; i++)
            {
                LLNode node = new LLNode(vals[i]);
                index.next = node;
                index = index.next;
            }

            return dummy.next
        }
    }
}
