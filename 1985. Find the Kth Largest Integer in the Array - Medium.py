class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=list(map(int,nums))
        nums.sort()
        i=0-k
        return(str(nums[i]))
