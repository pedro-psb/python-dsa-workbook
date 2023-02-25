"""Simple Singly linked without Header
ADT:
    insertAfter
    removeAfter
    __iter__ and __next__

"""
import pytest
from _01_singly_a import SingleLinkedList as L


@pytest.fixture
def empty_list() -> L:
    return L()


class TestInstantiate:
    def test_no_args(self, empty_list: L):
        assert len(empty_list) == 0

    def test_one_arg(self):
        # l = L("foo")
        # assert len(l) == 1
        pass

    def test_multiple_arg(self):
        pass

    # fail
    def test_wrong_args(self):
        pass


class TestInsert:
    def test_one_at_beginning(self):
        l = L()
        l.insertAfter(0, "foo")
        assert len(l) == 1

    def test_sequence_at_beginning(self):
        l = L()
        l.insertAfter(0, "foo")
        l.insertAfter(0, "bar")
        l.insertAfter(0, "baz")
        assert len(l) == 3

    def test_one_at_end(self):
        l = L()
        l.insertAfter(0, "foo")
        l.insertAfter(1, "bar")
        l.insertAfter(2, "spam")
        assert len(l) == 3

    def test_one_at_middle(self):
        l = L()
        l.insertAfter(0, "foo")
        l.insertAfter(0, "bar")
        l.insertAfter(0, "spam")
        l.insertAfter(1, "middle")
        assert len(l) == 4

    def test_invalid_beyond_end__empty(self):
        l = L()
        with pytest.raises(Exception):
            l.insertAfter(1, "foo")

    def test_invalid_beyond_end__populated(self):
        l = L()
        l.insertAfter(0, "foo")
        with pytest.raises(Exception):
            l.insertAfter(2, "bar")

    def test_invalid_before_beginning(self):
        l = L()
        l.insertAfter(0, "foo")
        with pytest.raises(Exception):
            l.insertAfter(-1, "bar")


@pytest.fixture
def filled_list() -> L:
    l = L()
    l.insertAfter(0, "foo")
    l.insertAfter(0, "bar")
    l.insertAfter(0, "spam")
    return l


class TestRemove:
    def test_one_at_beginning(self, filled_list: L):
        filled_list.removeAfter(0)
        assert len(filled_list) == 2

    def test_subsequent_at_beginning(self, filled_list: L):
        filled_list.removeAfter(0)
        filled_list.removeAfter(0)
        assert len(filled_list) == 1

    def test_one_at_end(self, filled_list: L):
        filled_list.removeAfter(3)
        assert len(filled_list) == 2

    def test_one_at_middle(self, filled_list: L):
        filled_list.removeAfter(2)
        assert len(filled_list) == 2


class TestIteration:
    def test_traverse_in_order(self, filled_list):
        pass

    def test_traverse_in_reverse_order(self, filled_list):
        pass

    pass
