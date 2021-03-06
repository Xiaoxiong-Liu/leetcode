"""
合并两个有序数组
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/8/sorting-and-searching/52/

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        
        hint 逆序填充
        """
        i = m-1
        j = n-1
        p = m+n-1
        while i >= 0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
        if j>=0:
            for x in range(j+1):
                nums1[x] = nums2[x]
        
        # 重点是逆序填充 review 2018.08.28
# 2018.09.20 因为要求是在位的，所以需要逆序填充。
