'''
Created on 2014/9/25/

@author: kepler-moment
'''

#get edit distance between str1 and str2
def editDistance(str1,str2):
    s1 = '0' + str(str1)
    s2 = '0' + str(str2)
    len1 = len(s1)
    len2 = len(s2)
    dp = [0] * max(len1,len2)
    for i in range(len2):
        dp[i] = i
    for i in range(1,len1):
        dp[0] = i - 1;
        tmp1 = dp[0];
        for j in range(1,len2):
            tmp2 = dp[j];
            if s1[i] == s2[j]:
                s = 0
            else:
                s = 1
            dp[j] = min(tmp1 + s,1 + min(tmp2,dp[j - 1]));
            tmp1 = tmp2;
    return dp[len2 - 1];
