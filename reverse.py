#problem no.7
class Solution(object):
    def reverse(self, x):
        sum=0
        if(x<0):
            m=-(x)
            temp=m
            while(temp>0):
                a=temp%10
                sum=sum*10+a
                temp=temp//10
            return -sum
        else:
            temp=x
            while(temp>0):
                a=temp%10
                sum=sum*10+a
                temp=temp//10
        return sum
obj=Solution()
n=-123
print(obj.reverse(n))

        