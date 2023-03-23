import pytest

from testing.utils import transform_parametrize as param

from .singly_b import Singly

# initializing


@pytest.mark.parametrize(
    "seq",
    (
        pytest.param([1, 2, 3, 4], id="list-4"),
        pytest.param([1], id="list-1"),
        pytest.param([], id="list-empty"),
        pytest.param((1, 2, 3, 4), id="tuple"),
        pytest.param(("foo", "bar", "baz"), id="tuple-str"),
    ),
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


@pytest.mark.parametrize(
    "seq",
    (
        pytest.param([1], id="1-element"),
        pytest.param([1, 2, 3, 4, 5], id="5-elements"),
    ),
)
def test_append_and_appendLast(seq):
    sl = Singly(seq)
    assert str(sl)[1:-1] == str(seq)[1:-1]
    assert len(sl) == len(seq)


def test_append_fail():
    """Not sure what should fail"""


# removing


@pytest.mark.parametrize(
    "pop_repeats",
    (
        pytest.param(1, id="1-element"),
        pytest.param(4, id="5-elements"),
    ),
)
def test_pop_and_popLast(pop_repeats):
    ...


def test_pop_fail():
    # pop empty

    # pop after empty
    ...
