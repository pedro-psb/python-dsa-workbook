"""Support for dict argument form for @pytest.mark.parametrize

eg:
@pytest.mark.parametrize({
    "argnames": ("arg1", "arg2"),
    "test-a": ("a", "b"),
    "test-b": ("foo", "bar"),
})

"""
import pytest

from testing.utils import ParametrizeError, transform_parametrize

params = transform_parametrize


# sample usage
#
# @pytest.mark.parametrize(
#     **{
#         "argnames": "a,b,result",
#         "argvalues": (
#             (1, 1, 2),
#             (2, 2, 4),
#         ),
#         "ids": ("test-a", "test-b"),
#     }
# )
# def test_unpack_sample(a, b, result):
#     assert result == a + b
#
#
# @pytest.mark.parametrize(
#     **params(
#         {
#             "argnames": ("a", "b", "result"),
#             "test-a": (1, 1, 2),
#             "test-b": (1, 1, 2),
#         }
#     )
# )
# def test_transform_parametrize_usage(a, b, result):
#     assert result == a + b


@pytest.mark.parametrize(
    ("in_form", "out_form"),
    (
        (
            {
                "argnames": ("a", "b"),
                "test-a": ("foo", "bar"),
                "test-b": (1, 2),
            },
            {
                "argnames": ("a", "b"),
                "argvalues": (
                    ("foo", "bar"),
                    (1, 2),
                ),
                "ids": ("test-a", "test-b"),
            },
        ),
        (
            {
                "argnames": "a,b",
                "test-a": ("foo", "bar"),
                "test-b": (1, 2),
            },
            {
                "argnames": "a,b",
                "argvalues": (
                    ("foo", "bar"),
                    (1, 2),
                ),
                "ids": ("test-a", "test-b"),
            },
        ),
    ),
    ids=["argnames-as-tuple", "argnames-as-str"],
)
def test_transform_parametrize(in_form, out_form):
    assert out_form == transform_parametrize(in_form)


@pytest.mark.parametrize(
    "incorrect_form",
    (
        {
            "test-a": ("foo", "bar"),
            "test-b": (1, 2),
        },
        {
            "argnames": ("foo", "bar"),
        },
        {
            "argnames": ("foo", "bar"),
            "test-a": "not-sequence",
        },
        {
            "argnames": ("foo", "bar"),
            "test-a": 123,
        },
    ),
    ids=["no-arg-name", "only-one-record", "no-sequence--str", "no-sequence--int"],
)
def test_transform_parametrize_fail(incorrect_form):
    with pytest.raises(ParametrizeError):
        transform_parametrize(incorrect_form)
