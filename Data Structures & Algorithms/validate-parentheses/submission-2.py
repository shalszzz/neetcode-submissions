class Solution:
    def isEmpty(self, stack):
        if not stack:
            return True
        return False 

    def isMatch(self, current, popped):
        if popped=="(" and current==")":
            return True
        if popped=="[" and current=="]":
            return True
        if popped=="{" and current=="}":
            return True
        return False

    def isValid(self, s: str) -> bool:
        start=s[0]
        if start=="]" or start=="}" or start==")":
            return False 
        if len(s)==1:
            return False

        mystack=[]

        for i in s:
            

            if i=="(" or i=="[" or i=="{":
                mystack.append(i)

            elif i==")" or i=="]" or i=="}":
                if self.isEmpty(mystack):
                    return False
                    
                elif not self.isMatch(i,mystack.pop()):
                    print("here2")
                    return False

        if not self.isEmpty(mystack):
            return False        
        return True
            
            
            



        
        