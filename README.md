mbleven
=======

mbleven is a fast, memory-efficient algorithm to compute k-bounded
Levenshtein distance.

If the upper-bound parameter k is small (especially k=1,2), this
algorithm runs much faster than the Wagner-Fischer algorithm.

For details, see [the documentation](https://ceptord.net/fastcomp/index.html).


IMPORTANT NOTICE
----------------

This is a proof-of-concept implementation to show how mbleven algorithm
works. If you are searching for a practical library to compute Levenshtein
distance, please take a look at [polyleven](
https://github.com/fujimotos/polyleven).


Installation
------------

Clone this repository and run setup.py

    $ git clone https://github.com/fujimotos/mbleven
    $ cd mbleven
    $ sudo python setup.py install


Usage
-----

This module provides a function named `compare()`. It takes two strings
as arguments and returns an integer, which is...

* the exact distance between two strings (if they are within two edit
  distance)
* -1 (if they are over two edit distance away)

Therefore, the return value should be any one of 0, 1, 2 or -1.

```python
>>> from mbleven import compare
>>> compare("meet", "meat")
1
>>> compare("meet", "eat")
2
>>> compare("meet", "mars")  # distance 3
-1
```

You can also measure the similarity using Damerau-Levenshtein distance
by setting `transpose` flag true.

```python
>>> compare("meat", "meta", transpose=True)
1
>>> compare("abc", "ca", transpose=True)
2
```
