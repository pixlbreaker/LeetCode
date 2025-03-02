class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Gets number of unique characters of each string
        count_s = len(set(s))
        count_t = len(set(t))

        freq_s = {}
        freq_t = {}
        
        # Compares the counts
        if( not count_s == count_t):
            return False
        else:
            for i in range(len(s)):
                if not s[i] in freq_s:
                    freq_s[s[i]] = i
                
                if not t[i] in freq_t:
                    freq_t[t[i]] = i
                
                if freq_s[s[i]] != freq_t[t[i]]:
                    return False
        return True
                    