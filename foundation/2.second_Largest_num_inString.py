# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

# An alphanumeric string is a string consisting of lowercase English letters and digits.

 

# Example 1:

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
# Example 2:

# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters and digits.

def finder(s):
    temp = list(s)
    contain_num = []
    repeat = False
    [contain_num.append(x) for x in temp if x.isnumeric()]
    for i in range(0,len(contain_num)):
        for x in range(1,len(contain_num)):
            if contain_num[i] != contain_num[x]:
                contain_num.remove(max(contain_num))
                return int(max(contain_num))
            else:
                return -1
    else:
        return -1

       

print(finder('dfa12321afd')) # 2
print(finder('abc1111')) # -1
print(finder('abc')) # -1
print(finder('ck077')) # -1