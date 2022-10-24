class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int

        Problem 2405
        Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
        Return the minimum number of substrings in such a partition.
        Note that each character should belong to exactly one substring in a partition.
        """
        substrings = []
        substring = ""
        for char in s:
            if char in substring:
                substrings.append(substring)
                substring = char
            else:
                substring += char
        substrings.append(substring)

        return len(substrings)


sol = Solution()
print(sol.partitionString("ssssss"))
