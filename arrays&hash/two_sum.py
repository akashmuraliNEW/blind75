class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array={}
        for i in range(len(nums)):
            find = nums[i]-target
            if find in array:
                return [array[find],i]
            array[nums[i]]=i
       
        else:
            return []