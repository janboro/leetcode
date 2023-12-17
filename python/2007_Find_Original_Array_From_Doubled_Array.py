class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]

        Problem 2007
        An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.
        Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.
        """
        original = []
        if len(changed) % 2 == 0 and len(changed) <= 10**5:
            while len(changed) > 0:
                num = max(changed)
                if num % 2 == 0 and num / 2 in changed:
                    changed.remove(num)
                    changed.remove(num / 2)
                    original.append(int(num / 2))
                else:
                    return []
        return original


sol = Solution()
print(sol.findOriginalArray([1, 3, 4, 2, 6, 8]))
print(sol.findOriginalArray([6, 3, 0, 1]))
a = [0, 0, 0]
print(sol.findOriginalArray(a))
