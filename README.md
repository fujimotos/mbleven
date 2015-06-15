# fastcomp

The fastcomp is an efficient algorithm for computating Levenshtein
distance **up to two**.

Given two strings of length m and n (m <= n), the
computation requires O(1) space and O(n) time, which is
much smaller and faster than well-known [Wagner-Fisher
algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm).

## Requirements

Python 2.6 or later

## Usage

The fastcomp.py has a function named `compare()`. It takes two strings as
arguments and returns an integer, which is...

* the exact distance between two strings (if they are within two edit
  distance)
* -1 (if they are over two edit distance away)

Therefore, the return value should be any one of 0, 1, 2 or -1.

```
>>> from fastcomp import compare
>>> compare("than", "then")
1
>>> compare("meeting", "eating")
2
>>> compare("book", "talk") # distance 3
-1
```

## Demo

http://ceptord.net/fastcomp/demo/

