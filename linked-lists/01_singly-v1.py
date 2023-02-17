from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class SingleLinkedList:
    """Generic implementation of single linked list with no tail"""

    @dataclass
    class Node:
        value: str
        next: SingleLinkedList.Node | None

    def __init__(self):
        self._length = 0
        self._head: SingleLinkedList.Node | None = None

    def insertAt(self, position: int, element: Any) -> None:
        """Insert element at any valid position. O(1) for HEAD or log(n) for other positions"""
        pos = self._validatePosition(position)
        # insert first element in log(1)
        if not self._head:
            self._head = SingleLinkedList.Node(element, None)
            self._length += 1
            return

        # insert in head in log(1)
        if pos == 0:
            new_node = SingleLinkedList.Node(element, None)
            new_node.next = self._head
            self._head = new_node
            self._length += 1
            return

        # insert in random pos in log(n)
        prev_old_node = self.getNodeAt(pos - 1)
        new_node = SingleLinkedList.Node(element, None)
        new_node.next = prev_old_node.next
        prev_old_node.next = new_node
        self._length += 1

    def removeAt(self, position: int) -> SingleLinkedList.Node:
        """Remove element at any position. O(1) for HEAD or log(n) for other positions"""
        pos = self._validatePosition(position)
        if not self._head:
            raise Exception("list is empty")

        # remove from head in log(1)
        node = None
        if pos == 0:
            node = self._head
            self._head = self._head.next
            self._length -= 1
            return node

        # remove from random in log(n)
        prev_node = self.getNodeAt(pos - 1)
        node = prev_node.next
        prev_node.next = node.next  # type: ignore
        self._length -= 1
        return node  # type: ignore

    def getNodeAt(self, position: int) -> SingleLinkedList.Node:
        """Traverse in log(n) and get node at specified position"""
        pos = self._validatePosition(position)
        for i, node in enumerate(self):
            if i == pos:
                return node
        raise Exception("Could not find node at given position")

    def printAll(self):
        """Traverse list and print each node in log(n)"""
        print("[", end="")
        for node in self:
            print(node.value, end="")
            print("," if node.next else "", end="")
        print("]")

    def _isEmpty(self):
        """Return whether the list is empty"""
        return bool(self._length)

    def _validatePosition(self, position: int):
        """Check if position is valid"""
        if not isinstance(position, int):
            raise Exception("position must be an integer")
        if position > self._length or position < 0:
            raise Exception("position is not valid")
        return position

    def __iter__(self):
        self._cursor = self._head
        return self

    def __next__(self):
        if self._cursor:
            current_element = self._cursor
            self._cursor = self._cursor.next
            return current_element
        raise StopIteration

    def __len__(self):
        return self._length


if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.insertAt(0, "foo")
    ll.insertAt(0, "bar")
    ll.printAll()