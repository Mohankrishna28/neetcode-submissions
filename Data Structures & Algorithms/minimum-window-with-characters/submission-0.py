class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tcount = {}
        for ch in t:
            tcount[ch] = tcount.get(ch, 0) + 1
        window = {}
        have = 0
        need = len(tcount)
        res = [-1, -1]
        resLen = float("inf")
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in tcount and window[char] == tcount[char]:
                have += 1
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in tcount and window[s[left]] < tcount[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""

            
