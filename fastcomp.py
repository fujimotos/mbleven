#!/usr/bin/env python

def compare(str1, str2):
    replace, insert, delete = 'r', 'i', 'd'

    L1, L2  = len(str1), len(str2)
    if L1 < L2:
        L1, L2 = L2, L1
        str1, str2 = str2, str1

    if L1 - L2 == 0:
        models = (insert+delete, delete+insert, replace+replace)
    elif L1 - L2 == 1:
        models = (delete+replace, replace+delete)
    elif L1 - L2 == 2:
        models = (delete+delete,)
    else:
        return -1

    res = 3
    for model in models:
        i, j, c = 0, 0, 0
        while (i < L1) and (j < L2):
            if str1[i] != str2[j]:
                c = c+1
                if 2 < c:
                    break
                
                cmd = model[c-1]
                if cmd == delete:
                    i = i+1
                elif cmd == insert:
                    j = j+1
                else:
                    assert cmd == replace
                    i,j = i+1, j+1
            else:
                i,j = i+1, j+1

        if 2 < c:
            continue
        elif i < L1:
            if L1-i <= model[c:].count(delete):
                c = c + (L1-i)
            else:
                continue
        elif j < L2:
            if L2-j <= model[c:].count(insert):
                c = c + (L2-j)
            else:
                continue

        if c < res:
            res = c

    if res == 3:
        res = -1
    return res

def test():
    assert compare("abc", "abc") == 0      # Same
    assert compare("abc", "abcd") == 1     # Insertion
    assert compare("abc", "abd") == 1      # Substitute
    assert compare("abc", "bc") == 1       # Delete
    assert compare("abcde", "acdfe") == 2  # Distance 2 and L1-L2 = 0
    assert compare("acdfe", "abcde") == 2   
    assert compare("abc", "bcd") == 2
    assert compare("bcd", "abc") == 2       
    assert compare("abc", "ade") == 2      
    assert compare("abc", "eabf") == 2     # Distance 2 and L1-L2 = 1
    assert compare("abc", "ebfc") == 2   
    assert compare("abc", "a") == 2        # Distance 2 and L1-L2 = 2
    assert compare("c", "abc") == 2   
    assert compare("abcde", "bcdgf") == -1 # Distance 3
    assert compare("abc", "efg") == -1 
    assert compare("abc", "") == -1        # Comparing with Null string
    assert compare("", "abc") == -1     
    assert compare("", "ab") == 2        
    assert compare("", "a") == 1
    assert compare("", "") == 0
    return

if __name__ == "__main__":
    test()
