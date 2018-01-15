"""Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution
and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2"""


class Solution(object):
    def twoSum(self, numbers, target):

        result = ""
        temp_dict = {}

        for i in range(len(numbers)):
            if numbers[i] < target:
                if numbers[i] in temp_dict:
                    result = "index1=" + str(temp_dict[numbers[i]])+ ", " + "index2=" + str(i+1)
                    return result
                else:
                    temp_dict[target - numbers[i]] = i+1


numbers = [2, 5, 7, 11, 15]
target = 9

sol = Solution()
print (sol.twoSum(numbers, target))