class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sd = {}
        td = {}
        
        for a, b in zip(s, t):
            sd[a] = sd.get(a, 0) + 1
            td[b] = td.get(b, 0) + 1
        
        for key, value in sd.items():
            if value != td.get(key, 0):
                return False
        
        return True