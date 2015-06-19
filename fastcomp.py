#!/usr/bin/env python

#
# constants

REPLACE = 'r'
INSERT = 'i'
DELETE = 'd'

MODELS = [
    (INSERT+DELETE, DELETE+INSERT, REPLACE+REPLACE),
    (DELETE+REPLACE, REPLACE+DELETE),
    (DELETE+DELETE,)
]

#
# functions

def compare(str1, str2):
    len1, len2 = len(str1), len(str2)

    if len1 < len2:
        len1, len2 = len2, len1
        str1, str2 = str2, str1

    if len1 - len2 > 2:
        return -1

    result = 3
    for model in MODELS[len1-len2]:
        idx1, idx2, cost = 0, 0, 0
        while (idx1 < len1) and (idx2 < len2):
            if str1[idx1] != str2[idx2]:
                cost += 1
                if 2 < cost:
                    break

                option = model[cost-1]
                if option == DELETE:
                    idx1 += 1
                elif option == INSERT:
                    idx2 += 1
                else:  # option == REPLACE
                    idx1 += 1
                    idx2 += 1

            else:
                idx1 += 1
                idx2 += 1

        if 2 < cost:
            continue
        elif idx1 < len1:
            if len1 - idx1 <= model[cost:].count(DELETE):
                cost += (len1 - idx1)
            else:
                continue
        elif idx2 < len2:
            if len2 - idx2 <= model[cost:].count(INSERT):
                cost += (len2 - idx2)
            else:
                continue

        if cost < result:
            result = cost

    if result == 3:
        result = -1

    return result
