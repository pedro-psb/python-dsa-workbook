"""Simple Singly linked without Header
ADT:
    insertAfter
    removeAfter
    __iter__ and __next__

"""
from typing import Any, NamedTuple

import pytest
from singly_a import NotFoundError, PositionError
from singly_a import SingleLinkedList as L


class Item(NamedTuple):
    value: Any
    position: int


@pytest.mark.parametrize(
    ("item_list", "final_len"),
    (
        # nobreak
        pytest.param([Item("foo", 0)], 1, id="one item at beginning"),
        pytest.param([Item("foo", 0), Item("bar", 0)], 2, id="two items at beginning"),
        pytest.param([Item("foo", 0), Item("end", 1)], 2, id="one item at the end"),
        pytest.param(
            [Item("foo", 0), Item("bar", 0), Item("middle", 1)],
            3,
            id="one item at the middle",
        ),
    ),
)
def test_insertion(item_list: list[Item], final_len):
    l = L()
    for item in item_list:
        l.insertAfter(item.position, item.value)
    assert len(l) == final_len


@pytest.mark.parametrize(
    ("item_list"),
    (
        # nobreak
        pytest.param([Item("foo", -1)], id="negative position"),
        pytest.param([Item("foo", 1)], id="out of range (initially empty)"),
        pytest.param(
            [Item("foo", 0), Item("bar", 2)], id="out of range (initially populated)"
        ),
    ),
)
def test_insertion_failures(item_list: list[Item]):
    l = L()
    with pytest.raises(PositionError):
        for item in item_list:
            l.insertAfter(item.position, item.value)


@pytest.mark.parametrize(
    ("position_list", "final_len"),
    (
        # nobreak
        pytest.param([0], 2, id="one item at beginning"),
        pytest.param([0, 0], 1, id="two items at beginning"),
        pytest.param([2], 2, id="one item at the end"),
        pytest.param([1], 2, id="one item at the middle"),
        pytest.param([0, 0, 0], 0, id="all from beginning"),
    ),
)
def test_remove(position_list, final_len):
    l = L()
    l.insertAfter(0, "foo")
    l.insertAfter(0, "bar")
    l.insertAfter(0, "spam")
    for position in position_list:
        l.removeAfter(position)
    assert len(l) == final_len


@pytest.mark.parametrize(
    ("position_list"),
    (
        # nobreak
        pytest.param([-1], id="negative position"),
        pytest.param([3], id="out of range"),
        pytest.param([0] * 4, id="no element left (empty list)"),
    ),
)
def test_remove_failures(position_list):
    l = L()
    l.insertAfter(0, "foo")
    l.insertAfter(0, "bar")
    l.insertAfter(0, "spam")
    with pytest.raises(PositionError):
        for position in position_list:
            l.removeAfter(position)


def test_traverse_in_order(filled_list):
    pass


def test_traverse_in_reverse_order(filled_list):
    pass
