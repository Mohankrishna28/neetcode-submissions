class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxfrequency=0
        left=0
        count = {}
        longest=0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxfrequency = max(maxfrequency, count[s[right]])
            while (right - left + 1) - maxfrequency > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
                

        