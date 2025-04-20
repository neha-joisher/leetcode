class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left_height=[0]*len(height)
        right_height=[0]*len(height)
        left_Max=0
        right_Max=0
        for i in range(1,len(height)):
            left_height[i]=max(left_Max,height[i-1])
            left_Max=left_height[i]
        for i in range(len(height)-2,-1,-1):
            right_height[i]=max(right_Max,height[i+1])
            right_Max=right_height[i]
        max_water=0
        for i in range(len(height)):
            max_water+=max(0,min(left_height[i],right_height[i])-height[i])
        return max_water