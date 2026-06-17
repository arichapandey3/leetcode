class Solution(object):
    def maxArea(self, height):
        i=0
        n=len(height)-1
        m=0
        while(i<n):
            m=max(m,min(height[i],height[n])*(n-i))
            if(height[i]<height[n]):
                i+=1
            else:
                n-=1
        return m
