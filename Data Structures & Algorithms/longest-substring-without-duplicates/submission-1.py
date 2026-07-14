class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in ch:
                ch.remove(s[left])
                left+=1
            ch.add(s[right])
            length = right - left +1
            longest = max(longest,length)
        return longest
                
            
        