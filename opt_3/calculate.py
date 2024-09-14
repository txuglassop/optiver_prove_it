import numpy as np
from scipy.special import comb

# function to calculate E[P | X = k]
def E_P_X(k):

    if k == 1:
        return 6

    outer_sum = 0

    for s in range(k-1, 6):
        inner_sum = np.sum([6+i for i in range(0,s+1)])

        binom_s_k = comb(s-1, k-2)

        term = (inner_sum / (s + 1)) * binom_s_k

        outer_sum += term
    
    binom_5_k = comb(5, k-1)
    return outer_sum / binom_5_k

# function to calculate P[X = k]
def P(k):
    return 1/ 6**(k-1) * comb(5,k-1) - 1/6**k * comb(5,k)

odd_k = np.array([1,3,5])
even_k = np.array([2,4,6])

E_player2 = np.sum([E_P_X(k) * P(k) for k in even_k])
E_player1 = np.sum([E_P_X(k) * P(k) for k in odd_k])

print("Player 1 expected payout:", E_player1)
print("Player 2 expected payout:", E_player2)