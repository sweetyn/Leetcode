"""Given a string, find the first non-repeating character in it
and return it's index. If it doesn't exist, return -1.

s = "leetcode"
return 0.

s = "loveleetcode",
return 2."""


class Solution(object):
    def firstUniqChar(self, s):

        #Options1
        for i in range(len(s)):
            if s[i] not in s[i+1:]:
                return i

        #Options2
        # i=0
        # for x in s:
        #     i += 1
        #     if x not in s[i:]:
        #         return s.index(x)

        return -1

s = "loveleetcode"

sol = Solution()
print(sol.firstUniqChar(s))
