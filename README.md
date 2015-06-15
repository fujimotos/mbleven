# fastcomp
fastcomp.py is an efficient algorithm for computating Levenshtein distance up to *two*. Given two strings of length m and n (m <= n), the computation requires O(1) space and O(n) time, which is much smaller and faster than well-known Wagner-Fisher algorithm.

It is mainly targeted at the use in spell checkers, where considering words within two edit distance suffices. 

## Documentation

http://ceptord.net/fastcomp/

## Demo

http://ceptord.net/fastcomp/demo/
