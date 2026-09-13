class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        ret=[]
        for num in nums1:
            index = nums2.index(num)
            if index+1>=len(nums2):
                ret.append(-1)
            for i in range(index+1,len(nums2)):
                if nums2[i]>num:
                    ret.append(nums2[i])
                    break
                elif i==len(nums2)-1:
                    ret.append(-1)
        if len(ret)!=len(nums1):
            ret.append(-1)

        return ret
            
