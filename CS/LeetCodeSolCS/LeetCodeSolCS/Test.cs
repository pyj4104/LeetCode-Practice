using System;
using System.Collections.Generic;

namespace LeetCodeSolCS
{
    public class Test<T>
    {
        private List<List<object>> tests;
        public delegate string ToStr(T result);

        public Test()
        {
            this.tests = new List<List<object>>();
        }

        public void RunTest(Delegate f, ToStr toString)
        {
            foreach (List<object> test in tests)
            {
                string inputs = "";
                foreach (object item in test)
                {
                    inputs = inputs + item.ToString() + " ";
                }
                Console.WriteLine("Testing " + inputs);
                T result = (T) f.DynamicInvoke(test.ToArray());
                Console.WriteLine(toString(result));
                Console.WriteLine("---");
            }
        }

        public void AddTest(List<object> test)
        {
            this.tests.Add(test);
        }

        public void AddTests(List<List<object>> tests)
        {
            foreach(List<object> test in tests)
            {
                this.AddTest(test);
            }
        }
    }
}
