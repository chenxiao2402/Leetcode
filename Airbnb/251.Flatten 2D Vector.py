# https://leetcode.com/problems/flatten-2d-vector/
#
# Design and implement an iterator to flatten a 2d vector.
# It should support the following operations: next and hasNext.
#
# Example:
#
# Vector2D
# iterator = new
# Vector2D([[1, 2], [3], [4]]);
#
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
#
# Notes:
# Please remember to RESET your class variables declared in Vector2D,
# as static/class variables are persisted across multiple test cases.
# Please see here for more details.
#
#
# You may assume that next() call will always be valid, that is,
# there will be at least a next element in the 2d vector when next() is called.
#
# Follow up:
# As an added challenge,
# try to code it using only iterators in C++ or iterators in Java.
from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = []
        for one_line in v:
            for element in one_line:
                self.v.append(element)

    def next(self) -> int:
        return self.v.pop(0)

    def hasNext(self) -> bool:
        return self.v != []

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()


iterator = Vector2D([[],[3]])

print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
