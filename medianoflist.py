#problen no.4
class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        x=len(nums1)
        if(x%2==0):
            m=x%2
            n=m-1
            result=nums1[m]+nums1[n]
            result=float(result)/2
            return result
        else:
            m=x%2
            if(m==x):
                return nums1[x-1]
            else:
                return nums1[m]
obj=Solution()
x=[1,2,3,4,5]
y=[6,7,8,9,10,11,12,13,14,15,16,17]
print(obj.findMedianSortedArrays(x,y))
