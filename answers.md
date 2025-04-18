# CMPS 2200 Assignment 3
## Answers

**Name:**___Anh Pham______________________


Place all written answers from `assignment-03.md` here for easier grading.

1a) First, we find the largest power of 2 that is less than or equal to N by  

2^⌊log_2(N)⌋. Then, we subtract that value from N and repeat until N reaches 0. \
def coins(N):\
coins = [] \
while N > 0:\
    coin = 2 ** int(math.floor(math.log2(N)))\
    coins.append(coin)\
    N -= coin  # Subtract the coin value from N.\
return coins\

The greedy algorithm simply always picks the highest coin value (a power of 2) that is no more than the remaining amount. Start by finding the largest power of 2 less than or equal to N, subtract it from N, and then repeat the process with the new value. This is equivalent to writing N in binary where each picked coin represents a 1 in the binary form.

1b) The algorithm is optimal because it makes the best immediate choice at each step (the largest coin available), ensuring that you use as few coins as possible. This is supported by the fact that if you didn’t use the largest coin possible, no combination of smaller coins could add up to that value. Also, after subtracting the chosen coin, the remaining amount is a smaller instance of the same problem, which can be solved in the same way. This confirms both the greedy choice property and the optimal substructure property.

1c) The algorithm has O(logN) work because it deals with about as many coins as there are binary digits in N. Since each coin selection depends on the previous subtraction, the operations are sequential, meaning the span (or the longest chain of dependent steps) is also O(logN).

2a) Greedy could fail in the following scenario: if the coins are only 1, 3, and 4 units, and you need to make 6. If you follow the “take the biggest coin you can” rule, you grab 4 (leaving 2) and then two 1’s (three coins total). But you could’ve just taken two 3’s, using only two coins. Greedy fails here.

2b) The problem has optimal substructure so whatever the last coin you put in for a total of n, the rest of the coins must form the best possible way to make up the remaining amount. If that smaller piece weren’t done with the fewest coins, you could swap in a better combination and improve the overall solution. So every optimal solution for n is built by choosing one coin and then solving the smaller problem optimally.

2c) def min_coins(denoms, N):\
    best = [0] + [float('inf')]*N\
    for x in range(1, N+1):\
        best[x] = min((best[x-d] for d in denoms if d <= x), default=float('inf')) + 1\
    return best[N] if best[N] != float('inf') else None \
    
Whether you build the table from the bottom up or use a top‑down memoized recursion, you end up computing the answer for each amount 1 through N exactly once. For each amount you try up to k different coins, so in total you perform about N×k checks, that’s your total work, theta(N⋅k). And since each amount depends on strictly smaller amounts and you scan through the coins one by one, the longest chain of dependent steps is also proportional to N⋅k, giving a span of theta(N⋅k).