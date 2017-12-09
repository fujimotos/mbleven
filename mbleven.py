#!/usr/bin/env python

#
# constants

REPLACE = 'r'
INSERT = 'i'
DELETE = 'd'
TRANSPOSE = 't'

MODELS = [
    (INSERT+DELETE, DELETE+INSERT, REPLACE+REPLACE),
    (DELETE+REPLACE, REPLACE+DELETE),
    (DELETE+DELETE,)
]

MODELS_T = [
    (TRANSPOSE+TRANSPOSE, TRANSPOSE+REPLACE, REPLACE+TRANSPOSE),
    (DELETE+TRANSPOSE, TRANSPOSE+DELETE),
    tuple()
]

#
# functions

def compare(str1, str2, transpose=False):
    len1, len2 = len(str1), len(str2)

    if len1 < len2:
        len1, len2 = len2, len1
        str1, str2 = str2, str1

    if len1 - len2 > 2:
        return -1

    models = MODELS[len1-len2]
    if transpose:
        models += MODELS_T[len1-len2]

    res = 3
    for model in models:
        cost = _checkmodel(str1, str2, len1, len2, model)
        if cost < res:
            res = cost

    if res == 3:
        res = -1

    return res


def _checkmodel(str1, str2, len1, len2, model):
    """Check if the model can transform str1 into str2"""

    idx1, idx2 = 0, 0
    cost, pad = 0, 0
    while (idx1 < len1) and (idx2 < len2):
        if str1[idx1] != str2[idx2 - pad]:
            cost += 1
            if 2 < cost:
                return cost

            option = model[cost-1]
            if option == DELETE:
                idx1 += 1
            elif option == INSERT:
                idx2 += 1
            elif option == REPLACE:
                idx1 += 1
                idx2 += 1
                pad = 0
            else:  # option == TRANSPOSE
                if (idx2 + 1) < len2 and str1[idx1] == str2[idx2+1]:
                    idx1 += 1
                    idx2 += 1
                    pad = 1
                else:
                    return 3
        else:
            idx1 += 1
            idx2 += 1
            pad = 0

    return cost + (len1 - idx1) + (len2 - idx2)
