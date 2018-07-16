fastcomp
========

This PyPI package is deprecated and will be removed in 2019-08-01.

This package was created as a reference implementation of the mbleven
algorithm. Although the underlying algorithm is still the fastest
solution to compute Levenshtein distance under a small threshold k,
this particular implementation is not.

The slowness comes from the sore fact that it is implemented in pure
Python. A simple benchmark suggests that it is 10x-20x slower than an
equivalent implementation in C.

   $ python3 -m timeit -s 'import polyleven' 'polyleven.levenshtein("abcde", "edcba")'
   1000000 loops, best of 3: 0.359 usec per loop
   $ python3 -m timeit -s 'import fastcomp' 'fastcomp.compare("abcde", "edcba")'
   100000 loops, best of 3: 5.92 usec per loop

In short, I do not believe this library is suitable for practical use
anymore. I'd like to recommend considering the [polyleven](https://github.com/fujimotos/polyleven) library if you
are interested in a practical Python library for computing Levenshtein
distance.

Overview
--------

The fastcomp is an efficient algorithm for computing (Damerau-)
Levenshtein distance **up to two**.

Given two strings of length m and n (m <= n), the
computation requires O(1) space and O(n) time, which is
much smaller and faster than well-known [Wagner-Fisher
algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm).

Installation
------------

    $ pip install fastcomp

Usage
-----

The fastcomp.py has a function named `compare()`. It takes two strings as
arguments and returns an integer, which is...

* the exact distance between two strings (if they are within two edit
  distance)
* -1 (if they are over two edit distance away)

Therefore, the return value should be any one of 0, 1, 2 or -1.

```
>>> from fastcomp import compare
>>> compare("meet", "meat")
1
>>> compare("meet", "eat")
2
>>> compare("meet", "mars")  # distance 3
-1
```

You can also measure the similarity using [Damerau–Levenshtein 
distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
by setting transpose flag true.

```
>>> compare("meat", "meta", transpose=True)
1
>>> compare("abc", "ca", transpose=True)
2
```

Technical documentation
-----------------------

http://ceptord.net/fastcomp/
