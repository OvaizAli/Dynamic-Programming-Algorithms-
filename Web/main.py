import eel

eel.init('C:/Users/Zaeem Ahmed\Desktop/algo project/Dynamic-Programming-Algorithms-/Web')

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

# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def editDistance(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    str1 = f.readline()
    str2 = f.readline()
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	# Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j # Min. operations = j

			# If second string is empty, only option is to
			# remove all characters of second string
            elif j == 0:
                dp[i][j] = i # Min. operations = i

			# If last characters are same, ignore last char
			# and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

			# If last character are different, consider all
			# possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
								dp[i-1][j],	 # Remove
								dp[i-1][j-1]) # Replace
                                
    return dp[m][n]
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def LIS(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    p = [int(x) for x in next(f).split(' ')]
    # p = int(p)
    # p = p.split(' ')
    n = len(p)
    arr = []
    for i in range(0,n):
        arr.append(p[i])
    n = len(arr)
    lis = [1]*n 

	# Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1

	# Initialize maximum to 0 to get 
	# the maximum of all LIS 
    maximum = 0

	# Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
    
    return maximum 
    
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def matrixChain(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    # p = f.readline().split(' ')
    arr = [int(x) for x in next(f).split(' ')]
    # p = int(p)
    # p = p.split(' ')
    n = len(arr)
    p = []
    for i in range(0,n):
        p.append(arr[i])

    m = [[0 for x in range(n)] for x in range(n)] 
    for i in range(1, n): 
        m[i][i] = 0

	# L is chain length. 
    for L in range(2, n): 
        for i in range(1, n-L + 1): 
            j = i + L-1
            m[i][j] = 99999999 
            for k in range(i, j): 

				# q = cost / scalar multiplications 
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j] 
                if q < m[i][j]: 
                    m[i][j] = q 
    
    return m[1][n-1] 

# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def Knapsack(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    # p = f.readline().split(' ')
    arrw = [int(x) for x in next(f).split(' ')]
    arrv = [int(y) for y in next(f).split(' ')]
    W = f.readline()
    W = int(W)
    # p = int(p)
    # p = p.split(' ')
    n = len(arrv)
    wt = []
    val = []
    for i in range(0,n):
        wt.append(arrw[i])
    for i in range(0,n):
        val.append(arrv[i])
    
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

	# Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
						+ K[i-1][w-wt[i-1]], 
							K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
            
    return K[n][W] 
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def Partition(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    p = [int(x) for x in next(f).split(' ')]
    # p = int(p)
    # p = p.split(' ')
    n = len(p)
    arr = []
    for i in range(0,n):
        arr.append(p[i])

    n = len(arr)
    sum = 0
    i, j = 0, 0

	# calculate sum of all elements
    for i in range(n):
        	sum += arr[i]
    
    if sum % 2 != 0:
        return False
    
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

	# initialize top row as true
    for i in range(0, n + 1):
    	part[0][i] = True

	# initialize leftmost column,
	# except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

	# fill the partition table in
	# bottom up manner
    for i in range(1, sum // 2 + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
							part[i - arr[j - 1]][j - 1])
                            
    return part[sum // 2][n]
# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def rodcutting(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    # p = f.readline().split(' ')
    arrw = [int(x) for x in next(f).split(' ')]
    arrv = [int(y) for y in next(f).split(' ')]
    W = f.readline()
    L = int(W)
    # p = int(p)
    # p = p.split(' ')
    n = len(arrv)
    val = []
    price = []
    for i in range(0,n):
        val.append(arrw[i])
    for i in range(0,n):
        price.append(arrv[i])

	# Build the table val[] in bottom up manner and return 
	# the last entry from the table 
    for i in range(1, n+1): 
        max_val = -32767
        for j in range(i): 
            max_val = max(max_val, price[j] + val[i-j-1]) 
        val[i] = max_val 
        
    return val[n] 

# ------------------------------------------------------------------------------------------------------------------------
@eel.expose
def coinChange(inputFile):
    f = open("Test Cases/" + inputFile, "r")
    # p = f.readline().split(' ')
    arr = [int(x) for x in next(f).split(' ')]
    n = f.readline()
    n = int(n)
    m = len(arr)
    S = []
    for i in range(0,m):
        S.append(arr[i])

    table = [[0 for x in range(m)] for x in range(n+1)] 

	# Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1

	# Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m): 

			# Count of solutions including S[j] 
        	x = table[i - S[j]][j] if i-S[j] >= 0 else 0

			# Count of solutions excluding S[j] 
        	y = table[i][j-1] if j >= 1 else 0

			# total count 
        	table[i][j] = x + y 
            
    return table[n][m-1] 

# ------------------------------------------------------------------------------------------------------------------------
# @eel.expose
# def (inputFile):

eel.start('index.html')