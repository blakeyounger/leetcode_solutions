class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(height) - 1
        maxArea = 0
        while leftPtr < rightPtr:
            newArea = min(height[leftPtr], height[rightPtr]) * (rightPtr-leftPtr)
            if newArea > maxArea:
                maxArea = newArea
            
            #maxArea = max(maxArea, newArea)

            if height[leftPtr] > height[rightPtr]:
                rightPtr -= 1
            else:
                leftPtr += 1
        
        return maxArea

