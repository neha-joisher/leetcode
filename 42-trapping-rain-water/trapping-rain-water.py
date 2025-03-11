class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall=right_wall=0
        n=len(height)
        left_max=[0]*n
        right_max=[0]*n

        for i in range(n):
            left_max[i]=left_wall
            if height[i]>left_wall:
                left_wall=height[i]

        for i in range(n-1, -1, -1):
            right_max[i]=right_wall
            if height[i]>right_wall:
                right_wall=height[i]

        res=0
        for i in range(n):
           pot_water=min(left_max[i],right_max[i])
           res=res+max(0,pot_water-height[i])
        return res




        