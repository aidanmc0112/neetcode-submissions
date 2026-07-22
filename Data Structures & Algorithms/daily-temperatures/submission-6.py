class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #output = []
        #for i in range (0, len(temperatures)):
         #   count = 0
          #  for j in range (i+1, len(temperatures)):
           #     count +=1
            #    if temperatures[j] > temperatures[i]:
             #       break
              #  else:
               #     if j == len(temperatures)-1:
                #        count = 0
            #output.append(count)
        #return output
        n = len(temperatures)
        result = [0] * n
        stack = []          
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result
