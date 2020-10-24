using System;
using System.Collections.Generic;
using System.Text;

namespace LeetCodeSolCS.Qs.SearchRange
{
    public class Solution
    {
        private int[] bSearch(int[] nums, int target, Func<int, int, bool> f)
        {
            //Init Vars with default vals
            int l, r, mid;

            l = 0;
            r = nums.Length;

            //Find lIndex
            while (l < r)
            {
                mid = (l + r) / 2;
                if (f(nums[mid], target))
                {
                    l = mid + 1;
                }
                else
                {
                    r = mid;
                }
            }
            return new int[] { l, r };
        }

        public int[] SearchRange(int[] nums, int target)
        {
            if(nums == null || nums.Length == 0)
            {
                return new int[] { -1, -1 };
            }

            int lIndex, rIndex;
            int[] retVal = new int[2];

            //Lambda Func
            Func<int, int, bool> findLeftMost = (x, t) => x < t;
            Func<int, int, bool> findRightMost = (x, t) => x <= t;

            int[] temp = this.bSearch(nums, target, findLeftMost);

            lIndex = (temp[0] < nums.Length) && (nums[temp[0]] == target) ? temp[0] : -1;
            
            if(lIndex == -1)
            {
                return new int[] { -1, -1 };
            }

            temp = this.bSearch(nums, target, findRightMost);

            rIndex = nums[temp[1]-1] == target ? temp[1] - 1 : -1;

            return new int[] { lIndex, rIndex };
        }
    }
}
