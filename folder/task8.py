import sys
import itertools
import random
from functools import reduce
from itertools import accumulate
import math
from typing import List


class Solution:

    def dominantIndex(self, nums):
        max1 = 0
        max2 = 0
        idxOfMax1 = 0

        for i, n in enumerate(nums):
            if n >= max1:
                max2 = max1
                max1 = n
                idxOfMax1 = i
            elif n > max2:
                max2 = n

        return idxOfMax1 if max1 >= max2 * 2 else -1

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        N, M = len(matrix), len(matrix[0])
        row, column, direction = 0, 0, 1
        result = []

        while row < N and column < M:
            result.append(matrix[row][column])
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)

            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                if direction:
                    row += column == M - 1
                    column += column < M - 1
                else:
                    column += row == N - 1
                    row += row < N - 1
                direction = 1 - direction
            else:
                row = new_row
                column = new_column

        return result

    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum, right_sum, index = 0, sum(nums), -1

        for key, num in enumerate(nums):
            if left_sum == right_sum - num:
                return key
            right_sum -= num
            left_sum += num

        return index

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        haystack = haystack.split(needle)
        return len(haystack[0]) if len(haystack) > 1 else -1

    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

    def removeElement(self, nums: List[int], val: int) -> int:
        deletes = 0
        for i in range(len(nums)):
            if val == nums[i]:
                deletes += 1
            else:
                nums[i - deletes] = nums[i]
        return len(nums) - deletes

    def romanToInt(self, s: str) -> int:
        result_number, prevous_number = 0, 0
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for symbol in s[::-1]:
            if mapping[symbol] >= prevous_number:
                result_number += mapping[symbol]
            else:
                result_number -= mapping[symbol]
            prevous_number = mapping[symbol]
        return result_number

    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix

    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int("".join(map(str, digits))) + 1)))

    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n % 2 != 0:
                count += 1
            n = n >> 1
        return count

    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)

    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + (high % 2 and low % 2)

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0

    def subtractProductAndSum(self, n: int) -> int:
        suma, mult = 0, 1
        while n > 0:
            digit = n % 10
            suma += digit
            mult *= digit
            n //= 10
        return mult - suma

    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def maxSubArray(self, A: List[int]) -> int:
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec not in store:
                store[nums[i]] = i
            else:
                return [store[sec], i]

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted list of numbers in-place and returns the new length.
        Uses a set to keep track of seen numbers for efficient duplicate detection.
        """
        if len(nums) <= 1:  # Handle empty or single-element lists
            return len(nums)

        seen = {nums[0]}  # Initialize set with the first element
        write_index = 1  # Index to overwrite duplicates, starting from the second element

        for read_index in range(1, len(nums)):
            if nums[read_index] not in seen:
                nums[write_index] = nums[read_index]  # Overwrite if the element is new
                seen.add(nums[read_index])  # Add the new element to the seen set
                write_index += 1  # Move to the next write position

        return write_index  # New length of the de-duplicated list

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

def main():
    solution = Solution()

    # Test cases for various methods
    print("Dominant Index:", solution.dominantIndex([3, 6, 1, 0]))  # Output: 1
    print("Find Diagonal Order:", solution.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [1,2,4,7,5,3,6,8,9]
    print("Find Middle Index:", solution.findMiddleIndex([2, 3, -4, 1, 4, 0]))  # Output: 3
    print("strStr:", solution.strStr("hello", "ll"))  # Output: 2
    print("Is Palindrome:", solution.isPalindrome(121))  # Output: True
    print("Remove Element:", solution.removeElement([3, 2, 2, 3], 3))  # Output: 2 (since the array becomes [2,2])
    print("Roman to Int:", solution.romanToInt("MCMXCIV"))  # Output: 1994
    print("Longest Common Prefix:", solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print("Plus One:", solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print("Hamming Weight:", solution.hammingWeight(0b11111111111111111111111111111101))  # Output: 31
    print("Average Salary:", solution.average([4000, 3000, 1000, 2000]))  # Output: 2500.0
    print("Count Odds:", solution.countOdds(3, 7))  # Output: 3
    print("Length of Last Word:", solution.lengthOfLastWord("Hello World"))  # Output: 5
    print("Is Valid Parentheses:", solution.isValid("()[]{}"))  # Output: True
    print("Subtract Product and Sum:", solution.subtractProductAndSum(234))  # Output: 15
    print("Max Subarray:", solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print("Two Sum:", solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print("Remove Duplicates:", solution.removeDuplicates([1, 1, 2]))  # Output:
    print("Search Insert Position:", solution.searchInsert([1, 3, 5, 6], 5))  # Output: 2

if __name__ == "__main__":
    main()


