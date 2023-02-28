"""Simple Singly linked without Header node
ADT:
    insertAfter
    removeAfter
    __iter__ and __next__

"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class PositionError(Exception):
    pass


class NotFoundError(Exception):
    pass


class SingleLinkedList:
    """Generic implementation of single linked list with no header and no tail"""

    @dataclass
    class Node:
        value: Any
        next: SingleLinkedList.Node | None

    def __init__(self, elements: list[Any] | None = None):
        self._length = 0
        self._head: SingleLinkedList.Node | None = None

    def insertAtHead(self, element: Any) -> None:
        """Insert element at the head of the list in O(1)"""
        # insert in head in log(1)
        new_node = SingleLinkedList.Node(element, None)
        new_node.next = self._head
        self._head = new_node
        self._length += 1
        return

    def insertAfter(self, position: int, element: Any) -> None:
        """Insert element after valid 0-index position in O(n)"""
        pos = self._validatePosition(position)

        # insert first element in log(1)
        if not self._head:
            self._head = SingleLinkedList.Node(element, None)
            self._length += 1
            return

        # insert in random pos in log(n)
        # - check whether is the first element
        try:
            old_prev_node = self.getNodeAt(pos - 1)
        except PositionError:
            old_prev_node = self._head

        old_node = self.getNodeAt(pos)
        old_next_node = old_node.next
        new_node = SingleLinkedList.Node(element, old_next_node)

        old_prev_node.next = new_node
        self._length += 1

    def removeAfter(self, position: int) -> SingleLinkedList.Node:
        """Remove element after any position.
        Position 0 means at beginning
        O(1) for HEAD or log(n) for other positions
        """
        pos = self._validatePosition(position)
        if self._isEmpty():
            raise PositionError("list is empty")

        # remove from head in log(1)
        node = None
        if pos == 0:
            node = self._head.next  # type: ignore because cannot be empty
            if self._length == 1:
                self._head.next = None  # type: ignore because cannot be empty
                self._length -= 1
                return node  # type: ignore because cannot be empty
            self._head.next = node.next  # type: ignore because cannot be empty
            self._length -= 1
            return node  # type: ignore because cannot be empty

        # remove from random in log(n)
        # - check if is last
        prev_node = self.getNodeAt(pos - 1)
        node = prev_node.next
        if node:
            if node:
                prev_node.next = node.next if node.next else None  # type: ignore
                self._length -= 1
            return node  # type: ignore
        raise PositionError("The position provided is the last. Cannot remove after it")

    def getNodeAt(self, position: int) -> SingleLinkedList.Node:
        """Traverse in log(n) and get node at specified position"""
        pos = self._validatePosition(position)
        for i, node in enumerate(self):
            if i == pos:
                return node
        raise NotFoundError("Could not find node at given position")

    def printAll(self):
        """Traverse list and print each node in log(n)"""
        print("[", end="")
        for node in self:
            print(node.value, end="")
            print("," if node.next else "", end="")
        print("]")

    def _isEmpty(self):
        """Return whether the list is empty"""
        return not bool(self._length)

    def _validatePosition(self, position: int):
        """Check if position (index 0) is valid"""
        if not isinstance(position, int):
            raise PositionError("position must be an integer")
        if self._isEmpty():
            raise PositionError("list is empty")
        if (position >= self._length) or position < 0:
            raise PositionError(f"position {position} is not valid")
        return position

        # len   pos   valid
        # 0     0       ok
        # 1     0       ok
        # 1     1       ok
        # 1     2       x

    # def __getitem__(self, i):
    #     if self._isEmpty() or len(self) <= i < 0:
    #         raise KeyError
    #     return self.getNodeAt(i)

    def __iter__(self):
        cursor = self._head
        try:
            if not cursor:
                raise IndexError
            while True:
                yield cursor
                if not cursor.next:
                    raise IndexError
                cursor = cursor.next
        except IndexError:
            return

    # def __next__(self):
    #     if self._cursor:
    #         current_element = self._cursor
    #         self._cursor = self._cursor.next
    #         return current_element
    #     raise StopIteration

    def __len__(self):
        return self._length
