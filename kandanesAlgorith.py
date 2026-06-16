#to find the maximum subaarray sum using kadane's algorithm
#solution no.53
class  Solution():
    def  maxSubArray(self,nums):
        max_sum=nums[0]
        curr_sum=0
        subarray=[]
        for i in range(0,len(nums)):
            curr_sum+=nums[i]
            subarray.append(nums[i])
            if(curr_sum>max_sum):
                max_sum=curr_sum
            if(curr_sum<0):
                curr_sum=0
                subarray=[]
        print("The maximum subarray is: ",subarray)
        print("The maximum subarray sum is: ",max_sum)
obj=Solution()
nums=list(map(int,input("enter the numbers separated by space: ").split()))
obj.maxSubArray(nums)