import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    key = (S, T)
    if key in MED:
        return MED[key]
    if not S:
        res = len(T)
    elif not T:
        res = len(S)
    elif S[0] == T[0]:
        res = fast_MED(S[1:], T[1:], MED)
    else:
        delete_cost = 1 + fast_MED(S[1:], T,     MED)
        insert_cost = 1 + fast_MED(S,     T[1:], MED)
        sub_cost    = 1 + fast_MED(S[1:], T[1:], MED)
        res = min(delete_cost, insert_cost, sub_cost)
    MED[key] = res
    return res
    pass

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    dist_memo = {}
    dist = fast_MED(S, T, dist_memo)

    # 2) recursively reconstruct one optimal alignment
    align_memo = {}
    def align(s, t):
        key = (s, t)
        if key in align_memo:
            return align_memo[key]

        if not s:
            aligned = ('-' * len(t), t)
        elif not t:
            aligned = (s, '-' * len(s))
        elif s[0] == t[0]:
            aS, aT = align(s[1:], t[1:])
            aligned = (s[0] + aS, t[0] + aT)
        else:
            # compute costs of each choice
            del_cost = dist_memo.get((s[1:], t), float('inf')) + 1
            ins_cost = dist_memo.get((s, t[1:]), float('inf')) + 1
            sub_cost = dist_memo.get((s[1:], t[1:]), float('inf')) + 1

            # pick the minimum
            if sub_cost <= del_cost and sub_cost <= ins_cost:
                aS, aT = align(s[1:], t[1:])
                aligned = (s[0] + aS, t[0] + aT)
            elif del_cost <= ins_cost:
                aS, aT = align(s[1:], t)
                aligned = (s[0] + aS, '-' + aT)
            else:
                aS, aT = align(s, t[1:])
                aligned = ('-' + aS, t[0] + aT)

        align_memo[key] = aligned
        return aligned

    aS, aT = align(S, T)
    return dist, aS, aT
    pass

