import eel

eel.init('E:/5th Semester/Fall 2020/ALGO/Sir Zeshan/Dynamic-Programming-Algorithms-/Web')

@eel.expose
def showInput(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    input = f.read()
    f.close()
    return input

# -----------------------------------------------------------------------------------------------------------------------
@eel.expose
def LCS(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    X = f.readline()
    Y = f.readline()

    # find the length of the strings 
    m = len(X) 
    n = len(Y) 

    L = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Following steps build L[m+1][n+1] in bottom up fashion. Note 
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # Following code is used to print LCS 
    index = L[m][n] 
  
    # Create a character array to store the lcs string 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
  
    # Start from the right-most-bottom-most corner and 
    # one by one store characters in lcs[] 
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        # If current character in X[] and Y are same, then 
        # current character is part of LCS 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    return lcs
#end of function lcs 

# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def SCS(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    str1 = f.readline()
    str2 = f.readline()
 
    dp = [[None for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if not i:
                dp[i][j] = j
            elif not j:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] =1 + min(dp[i - 1][j], dp[i][j - 1])

    sc_len = dp[len(str1)][len(str2)]
    # for printing purpose
    scstr = [ None for _ in range(sc_len)]
    i, j = len(str1), len(str2)

    while i > 0 and j > 0 :
        if str1[i - 1] == str2[j - 1]:
            scstr[sc_len - 1] = str1[i - 1]
            i -= 1
            j -= 1
            sc_len -= 1
        
        elif dp[i][j - 1] < dp[i - 1][j]:
            scstr[sc_len - 1] = str2[j - 1]
            j -= 1
            sc_len -= 1
        else:
            scstr[sc_len - 1] = str1[i - 1]
            i -= 1
            sc_len -= 1
    while i > 0:
        scstr[sc_len - 1] = str1[i - 1]
        i -= 1
        sc_len -= 1
    while j > 0:
        scstr[sc_len - 1] = str2[j - 1]
        j -= 1
        sc_len -= 1        

    scstr = "".join(map(str, scstr))
    return scstr

eel.start('index.html')