class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
if __name__ == '__main__':
    s = Solution()
    s.isAnagram('racecar', '')