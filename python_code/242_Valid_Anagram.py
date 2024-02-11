"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from time import perf_counter


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            temp = s
            for char in temp:
                if char in t:
                    s = s.replace(char, "", 1)
                    t = t.replace(char, "", 1)
                else:
                    return False
        return len(s) == 0 and len(t) == 0


start = perf_counter()
result = Solution().isAnagram(s="anagram", t="nagaram")
stop = perf_counter()
print(f"Result: {result} | Time: {stop - start}")
