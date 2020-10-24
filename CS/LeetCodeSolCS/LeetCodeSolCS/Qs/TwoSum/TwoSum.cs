using System;
using System.Collections;
using System.Collections.Generic;

namespace LeetCodeSolCS.Qs.TwoSum {
    public class Solution {
        public int[] TwoSum(int[] nums, int target) {
            int[] retVal = { 0, 0 };

            Dictionary<int, int> table = new Dictionary<int, int>();
            for(int i = 0; i < nums.Length; i++) {
                table[target - nums[i]] = i;
            }

            for(int i = 0; i < nums.Length; i++) {
                if (table.ContainsKey(nums[i])) {
                    if (i != (int) table[nums[i]]) {
                        retVal[0] = i;
                        retVal[1] = table[nums[i]];
                        return retVal;
                    }
                }
            }
            return retVal;
        }
    }
}
