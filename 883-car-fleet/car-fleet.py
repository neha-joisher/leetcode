class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars=[(p,s) for p, s in zip(position,speed)]
        cars.sort(reverse=True)
        stack=[]

        for p,s in cars:
            time=(float(target-p)/s)
            print(time)
            if not stack or time > stack[-1]:
                stack.append(time)  # New fleet formed
        return len(stack)
        