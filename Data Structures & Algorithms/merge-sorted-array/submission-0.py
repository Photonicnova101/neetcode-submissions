class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for x in range(1,n+1):
            nums1[-x]=nums2[x-1]
        for i in range(len(nums1)):
            j=i-1
            while(j>=0 and nums1[j+1]<nums1[j]):
                temp=nums1[j+1]
                nums1[j+1]=nums1[j]
                nums1[j]=temp
                j-=1
            
        