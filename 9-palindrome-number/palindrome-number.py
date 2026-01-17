class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        rev = ""
        for i in s:
            rev = i + rev
        if (rev==s):
            return True
        else:
            return False