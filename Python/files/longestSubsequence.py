"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""
def longestSubsequence(t1: str, t2: str) -> int:
    if not t1 or not t2:
        return 0
    ansTable = [[0]*len(t1) for i in range(len(t2))]
    
    initVal = 0
    for i in range(len(t1)):
        if t1[i] == t2[0]:
            initVal += 1
        ansTable[0][i] = initVal
    
    initVal = 0
    for j, char in enumerate(t2):
        if t1[0] == char:
            initVal += 1
        ansTable[j][0] = initVal
    
    for i in range(1, len(t1)):
        for j in range(1, len(t2)):
            if t1[i] == t2[j]:
                ansTable[j][i] = ansTable[j-1][i-1]+1
            else:
                ansTable[j][i] = max(ansTable[j][i-1], ansTable[j-1][i])
    
    print2DTable(ansTable)
    
    return ansTable[len(t2)-1][len(t1)-1]

def print2DTable(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

print(longestSubsequence('abcde', 'ace'))
print(longestSubsequence('bsbi', 'kb'))