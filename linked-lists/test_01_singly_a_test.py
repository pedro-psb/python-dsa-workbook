import pytest
from _01_singly_a import SingleLinkedList as L


class TestInstantiate:
    def test_no_args(self):
        l = L()
        assert len(l) == 0

    def test_one_arg(self):
        pass

    def test_multiple_arg(self):
        pass

    # fail
    def test_wrong_args(self):
        pass


class TestAppend:
    def test_append(self):
        pass


class TestRemove:
    def test_remove(self):
        pass


class TestGeneral:
    pass
