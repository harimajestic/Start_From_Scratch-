class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        s2 =s1[::-1]
        return s1==s2
