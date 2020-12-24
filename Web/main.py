import eel
# E:/5th Semester/Fall 2020/ALGO/Sir Zeshan/Dynamic-Programming-Algorithms-/Web
# eel.init('E:/5th Semester/Fall 2020/ALGO/Sir Zeshan/Dynamic-Programming-Algorithms-/Web')
eel.init('C:/Users/Zaeem Ahmed/Desktop/algo project/Dynamic-Programming-Algorithms-/Web')

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
    A = f.readline()
    B = f.readline()

    m = len(A) 
    n = len(B) 

    Z = [[0 for x in range(n+1)] for x in range(m+1)] 

    for i in range(m+1):     
        for j in range(n+1): 
            if i == 0 or j == 0: 
                Z[i][j] = 0
            elif A[i-1] == B[j-1]: 
                Z[i][j] = Z[i-1][j-1] + 1
            else: 
                Z[i][j] = max(Z[i-1][j], Z[i][j-1]) 

    ind = Z[m][n] 
  
    lcs = [""] * (ind+1) 
    lcs[ind] = "" 

    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        if A[i-1] == B[j-1]: 
            lcs[ind-1] = A[i-1] 
            i-=1
            j-=1
            ind-=1

        elif Z[i-1][j] > Z[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    return lcs
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def SCS(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    str1 = f.readline()
    str2 = f.readline()
 
    d_p = [[None for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if not i:
                d_p[i][j] = j
            elif not j:
                d_p[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                d_p[i][j] = d_p[i - 1][j - 1] + 1
            else:
                d_p[i][j] =1 + min(d_p[i - 1][j], d_p[i][j - 1])

    sc_len = d_p[len(str1)][len(str2)]
    # for printing purpose
    sc_str = [ None for _ in range(sc_len)]
    i, j = len(str1), len(str2)

    while i > 0 and j > 0 :
        if str1[i - 1] == str2[j - 1]:
            sc_str[sc_len - 1] = str1[i - 1]
            i = i - 1
            j = j - 1
            sc_len = sc_len - 1
        
        elif d_p[i][j - 1] < d_p[i - 1][j]:
            sc_str[sc_len - 1] = str2[j - 1]
            j = j - 1
            sc_len = sc_len - 1
        else:
            sc_str[sc_len - 1] = str1[i - 1]
            i = i - 1
            sc_len = sc_len - 1
    while i > 0:
        sc_str[sc_len - 1] = str1[i - 1]
        i = i - 1
        sc_len = sc_len - 1
    while j > 0:
        sc_str[sc_len - 1] = str2[j - 1]
        j = j - 1
        sc_len = sc_len - 1        

    sc_str = "".join(map(str, sc_str))
    return sc_str


# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def editDistance(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    A = f.readline()
    B = f.readline()
    len_A = len(A)
    len_B = len(B)
    d_p = [[0 for x in range(len_B + 1)] for x in range(len_A + 1)]

    for i in range(len_A + 1):
        for j in range(len_B + 1):
            if i == 0:
                d_p[i][j] = j

            elif j == 0:
                d_p[i][j] = i

            elif A[i-1] == B[j-1]:
                d_p[i][j] = d_p[i-1][j-1]

            else:
                d_p[i][j] = 1 + min(d_p[i][j-1],	 
								d_p[i-1][j],	 
								d_p[i-1][j-1]) 
                                
    return d_p[len_A][len_B]
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def LIS(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    X = [int(x) for x in next(f).split(' ')]
    
    L = [[] for _ in range(len(X))]

    L[0].append(X[0])
 

    for i in range(1, len(X)):
 
        for j in range(i):
 
            if X[j] < X[i] and len(L[j]) > len(L[i]):
                L[i] = L[j].copy()

        L[i].append(X[i])

    j = 0

    for i in range(len(X)):
        if len(L[j]) < len(L[i]):
            j = i

    return L[j]
    
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def matrixChain(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    p = [int(x) for x in next(f).split(' ')]
    len_arr = len(p)
    arr = []
    for i in range(0,len_arr):
        arr.append(p[i])
    len_arr = len(arr) - 1
    m_arr = matrixChainOrder(arr, len_arr)
    print("\nOptimal Cost is :", m_arr[0][len_arr - 1])
    return m_arr[0][len_arr - 1]

 
def matrixChainOrder(p, len_arr):
 
    m_arr = [[0 for i in range(len_arr)] 
            for i in range (len_arr)]
 
    for l in range (2, len_arr + 1):
        for i in range (len_arr - l + 1):
            j = i + l - 1

            m_arr[i][j] = float('Inf')
            for k in range (i, j):
                q = (m_arr[i][k] + m_arr[k + 1][j] +
                    (p[i] * p[k + 1] * p[j + 1]))
                if (q < m_arr[i][j]):
                    m_arr[i][j] = q
 
                    m_arr[j][i] = k + 1
    return m_arr

# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def Knapsack(inputFile):
    f = open("Test Cases/" + inputFile, "r")

    arrw = [int(x) for x in next(f).split(' ')]
    arrv = [int(y) for y in next(f).split(' ')]
    tot_W = f.readline()
    tot_W = int(tot_W)

    len_arr = len(arrv)
    wt_arr = []
    val_arr = []
    for i in range(0,len_arr):
        wt_arr.append(arrw[i])
    for i in range(0,len_arr):
        val_arr.append(arrv[i])
    
    kanp = [[0 for x in range(tot_W + 1)] for x in range(len_arr + 1)] 

    for i in range(len_arr + 1): 
        for w_index in range(tot_W + 1): 
            if i == 0 or w_index == 0: 
                kanp[i][w_index] = 0
            elif wt_arr[i-1] <= w_index: 
                kanp[i][w_index] = max(val_arr[i-1] 
						+ kanp[i-1][w_index-wt_arr[i-1]], 
							kanp[i-1][w_index]) 
            else: 
                kanp[i][w_index] = kanp[i-1][w_index] 
            
    return kanp[len_arr][tot_W] 
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def Partition(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    p = [int(x) for x in next(f).split(' ')]
    n = len(p)
    arr_ele = []
    for i in range(0,n):
        arr_ele.append(p[i])

    n = len(arr_ele)
    sum = 0
    i, j = 0, 0

    for i in range(n):
        	sum += arr_ele[i]
    
    if sum % 2 != 0:
        return False
    
    partition = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

    for i in range(0, n + 1):
    	partition[0][i] = True

    for i in range(1, sum // 2 + 1):
        partition[i][0] = False

    for i in range(1, sum // 2 + 1):
        for j in range(1, n + 1):
            partition[i][j] = partition[i][j - 1]
            if i >= arr_ele[j - 1]:
                partition[i][j] = (partition[i][j] or
							partition[i - arr_ele[j - 1]][j - 1])
                            
    return partition[sum // 2][n]
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def rodcutting(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    # p = f.readline().split(' ')
    INT_MIN = -32767
    arrlength = [int(x) for x in next(f).split(' ')]
    arrPrice = [int(y) for y in next(f).split(' ')]
    W = f.readline()
 
    n = int(W)

    x = len(arrPrice)
    
    T = [0] * (n + 1)
 
    for i in arrlength:
        for j in range(1, i + 1):
            T.append(max(T[i], arrPrice[j - 1] + T[i - j - 1]))
            
    return max(T)

# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def coinChange(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    arr = [int(x) for x in next(f).split(' ')]
    req_ch = f.readline()
    req_ch = int(req_ch)
    m = len(arr)
    coin_arr = []
    for i in range(0,m):
        coin_arr.append(arr[i])
    T = [0] * (req_ch + 1)
 
    for i in range(1, req_ch + 1):

        T[i] = float('inf')

        for coin in range(len(coin_arr)):
            if i - coin_arr[coin] >= 0:
                res = T[i - coin_arr[coin]]
 
                if res != float('inf'):
                    T[i] = min(T[i], res + 1)

    return T[req_ch]
 
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def Word_Break(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    word_arr = f.readline().split(' ')
    word = f.readline()
    word_arr[-1] = word_arr[-1].rstrip("\n")
    if Break_Word(word_arr, word):
        return("String can be segmented")
    else:
        return("String can't be segmented")

 
def Break_Word(word_arr, word):
 
    if not word:
        return True
 
    for i in range(1, len(word) + 1):
 
        prefix = word[:i]

        if prefix in word_arr and Break_Word(word_arr, word[i:]):
            return True
 
    return False

eel.start('index.html')