"""
 @SEU(master);@ZZULI(bachelor)
 author:CuiXuan
 email:873059043@qq.com
 If you find any errors, please let me know.
 If you have any better solution, please let me know.

 Solution Using time 52ms
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        l=0;r=len(nums)-1;pos=0
        while l<=r:
            mid=(l+r)>>1
            if target==nums[mid]:return mid
            elif target>nums[mid]:l=mid+1;pos=mid+1
            else:r=mid-1;pos=mid
        return pos