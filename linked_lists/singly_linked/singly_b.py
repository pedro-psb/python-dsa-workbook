"""
Simple Singly linked without Header node

ADT:
    append
    appendLast
    pop
    popLast

    __iter__,
    __len__,
    __repr__
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, NamedTuple, TypeVar

T = TypeVar("T")


class Node(NamedTuple):
    value: Any
    next: Node | None


class Singly:
    """
    Singly linked list with no positions
    """

    def __init__(self, elements: Sequence[Any] | None = None):
        """
        Initializes linked list (optionally with a sequence)
        """
        self._size = 0
        self._head: Node | None = None

        # optional sequence initializer
        if elements:
            if isinstance(elements, Sequence):
                # initialize list in-place and in order
                # where sequence[0] = head
                self._head = Node(elements[-1], None)
                self._size += 1
                for e in reversed(elements[:-1]):
                    prev = self._head
                    self._head = Node(e, prev)
                    self._size += 1
            else:
                raise TypeError(f"elements should be a sequence, not {type(elements)}")

    def append(self, element) -> Node:
        """
        Append at the beginning
        """
        ...

    def appendLast(self, element) -> Node:
        """
        Append at the end
        """
        ...

    def pop(self) -> Node:
        """
        Pops first element
        """
        ...

    def popLast(self) -> Node:
        """
        Pops last element
        """
        ...

    def __iter__(self):
        """
        Return iterator of _Nodes
        """
        cursor = self._head
        if not cursor:
            return

        while cursor.next:
            yield cursor.value
            cursor = cursor.next
        yield cursor.value

    def __len__(self):
        return self._size

    def __repr__(self):
        repr = ""
        for value in self:
            repr += f"{value.__repr__()}, "
        return f"[{repr[:-2]}]"

# TODO implement SinglyB (extended version)
class SinglyB(Singly):
    """
    Extended version of Singly.
    Add general purpose insert, remove and find
    """

    def insertAfter(self, node: Node, value: Any):
        """
        Insert value after node
        """

    def insertBefore(self, node: Node, value: Any):
        """
        Insert value before node
        """

    def find(self, match_value: Any) -> tuple[Node, Node]:
        """
        Find node with vaue that matches @match_value and
        return tuple with (prev_node, match_node).
        """
        ...



if __name__ == "__main__":
    llist = Singly([1, 2, 3, 4])
    # for n in llist:
    #     print(n)
