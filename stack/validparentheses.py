class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenDict ={ '}' : '{', ')':'(', ']':'['}
     