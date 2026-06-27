class Solution:
    def reverse(self, x: int) -> int:

        mini = -int(math.pow(2,31))
        maxi = int(math.pow(2,31))
        res=0

        while x:

            digit= int(math.fmod(x,10))
            x=int(x/10)

            if(res>maxi//10 or (res==maxi//10 and digit>=maxi%10)):
                return 0

            if(res<mini//10 or (res==mini//10 and digit<=mini%10)):
                return 0

            res=(res*10)+digit
        return res

        