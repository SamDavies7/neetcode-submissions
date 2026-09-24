class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       seen = {ch: 0 for ch in s}
       l =maxFreq=best= 0
       
       for r, ch in enumerate(s):
            seen[ch] += 1
            maxFreq = max(maxFreq, seen[ch])
            if (r - l + 1) - maxFreq > k:
                seen[s[l]] -= 1
                l += 1
            best = max(best,r - l + 1)
       return best
        
