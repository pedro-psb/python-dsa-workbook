from typing import Any
from dataclasses import dataclass



# @dataclass
# class Node:
#     value: str
#     next: Node

class Node:
    def __init__(self, value: str, next: Node):
        self._value = value
        self._node = node


class SingleLinkedList:
    """Raw implementation of single linked list"""

    def __init__(self):
        self._length = 0
        self._head = None

    def insert(self, element: Any) -> None:
        """Insert element in the front of the list, so it becomes the HEAD"""

    def remove(self) -> Any:
        """Remove element in HEAD"""

    def __len__(self):
        return self._length

if __name__=="__main__":
    l = SingleLinkedList()
    print(len(l))

