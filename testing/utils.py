from typing import Any, Sequence


class ParametrizeError(Exception):
    """Error in the transform_parametrize function"""


def transform_parametrize(in_form: dict[str, Any]) -> dict:
    """takes dict-form test and transform to pytest parametrize form for dict unpacking"""

    argnames = in_form.get("argnames")
    argvalues = tuple(in_form.values())[1:]
    ids = tuple([key for key in in_form.keys() if key != "argnames"])

    # validate
    if len(in_form) < 2:
        raise ParametrizeError(
            "in_form should contain 'argnames' and at least one other record"
        )

    if not argnames:
        raise ParametrizeError("in_form should contain the key 'argnames'")

    if not isinstance(argnames, (Sequence, str)):
        raise ParametrizeError("in_form['argnames'] should be a Sequence or str")

    for value in argvalues:
        if not isinstance(value, Sequence) or isinstance(value, str):
            raise ParametrizeError(
                "in_form['test-x'] should be of type Sequence (tuple, list, ...)"
            )

    return {"argnames": argnames, "argvalues": argvalues, "ids": ids}
