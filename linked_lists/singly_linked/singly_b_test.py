import pytest

from testing.utils import transform_parametrize as param

from .singly_b import SinglyLL as Singly

# initializing


@pytest.mark.parametrize(
    **param(
        {
            "argnames": "seq",
            "list-0": [1, 2, 3, 4],
            "list-1": [1],
            "list-4": [],
            "tuple": (1, 2, 3, 4),
            "tuple": ("foo", "bar", "baz"),
        }
    )
)
def test_init(seq):
    sl = Singly(seq)
    assert str(sl)[1:-1] == str(seq)[1:-1]
    assert len(sl) == len(seq)


def test_init_fail():
    # not a sequence
    with pytest.raises(TypeError) as type_err:
        Singly({1, 2, 3, 4})  # type: ignore
    assert type_err.match("should be")


# appending


def test_append():
    ...


def test_appendLast():
    ...


def test_append_fail():
    ...


# removing


def test_pop():
    ...


def test_popLast():
    ...


def test_pop_fail():
    ...
