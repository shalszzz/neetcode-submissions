class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s)==1:
            return True

        first=0
        
        mystr=s.lower()
        mystr=mystr.replace(" ","")
        last=len(mystr)-1

        while(first<=last):

            if not mystr[first].isalnum():
                first+=1
                continue

            if not mystr[last].isalnum():
                last-=1
                continue
                
            if mystr[first]!=mystr[last]:
                return False

            first+=1
            last-=1
        return True
        