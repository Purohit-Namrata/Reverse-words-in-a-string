class Solution:
    def reverse_words(self,s:str)->str:
        words=s.split(" ")
        words.reverse()
        words=' '.join(words)
        return words
s=Solution()
print(s.reverse_words("the sky is blue"))
    



