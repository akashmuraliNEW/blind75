class Solution: 
    def isPalindrome(self, s: str) -> bool:
        newStr =''
        for i in s:
           if i.isalnum():
            newStr+=i.lower()
        print(newStr)
        return newStr == newStr[::-1]
obj=Solution()
print(obj.isPalindrome('aka'))