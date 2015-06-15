#!/usr/bin/env python

#
# constants

REPLACE = 'r'
INSERT = 'i'
DELETE = 'd'


#
# functions

def compare(str1, str2):
    len1, len2 = len(str1), len(str2)
    if len1 < len2:
        len1, len2 = len2, len1
        str1, str2 = str2, str1

    if len1 - len2 == 0:
        models = (INSERT+DELETE, DELETE+INSERT, REPLACE+REPLACE)
    elif len1 - len2 == 1:
        models = (DELETE+REPLACE, REPLACE+DELETE)
    elif len1 - len2 == 2:
        models = (DELETE+DELETE,)
    else:
        return -1

    res = 3
    for model in models:
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
                cost = cost + (len2 - idx2)
            else:
                continue

        if cost < res:
            res = cost

    if res == 3:
        res = -1

    return res
