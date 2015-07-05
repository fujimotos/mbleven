fastcomp
========

The fastcomp is an efficient algorithm for computing Levenshtein
distance **up to two**.

Given two strings of length m and n (m <= n), the
computation requires O(1) space and O(n) time, which is
much smaller and faster than well-known [Wagner-Fisher
algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm).

Installation
------------

Clone this repository and simply run setup.py (Python 2.6 or later required).

```
$ git clone https://github.com/fujimotos/fastcomp.git
$ cd fastcomp
$ python setup.py install
$ python -m unittest discover tests  # running test (optional)
```

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

Demo
----

http://ceptord.net/fastcomp/demo/

Technical documentation
-----------------------

http://fujimotos.github.io/fastcomp/ (for developers)
