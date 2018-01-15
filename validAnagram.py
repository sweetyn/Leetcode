"""242. Valid Anagram
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false."""

def vaildAnagram(s, t):

    for x in s:
        if x in t:
            t.replace(x, "")
        else:
            return False

    return True


s = "rat"
t = "tar"

print (vaildAnagram(s, t))
#complted in 7mins
