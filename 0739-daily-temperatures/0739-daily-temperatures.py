class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        n = len(temperatures)
        stack = []
        res = [0]*n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res
                 
        
        
        
        
        
        
        
        # stack = []
        # res = []
        # res[0] = 0
        # # stack.push(1)

        # n = len(temperatures)

        # for i in range(n - 1,0,-1):
        #     if temperatures[i] < temperatures[i+1]:
        #         stack.push(1)
        #     if stack:
        #         day = stack.pop()
        #         res.append(day)
        #         stack.push
            
            
