from typing import Any, Sequence


class ParametrizeError(Exception):
    """Error in the transform_parametrize function"""

# TODO: add support for parsing str arganames. Eg ("arg1,arg2")
# TODO: add support for: {case-a: "unique_arg"} over {case-a: ["unique-arg"]}
def transform_parametrize(in_form: dict[str, Any]) -> dict:
    """
    Takes dict-form test and transform to pytest parametrize form for dict unpacking

    @in_form: dict

    """

    argnames = in_form.get("argnames")
    # if isinstance(argnames, str):
    #     raise ParametrizeError("str parsing ('arg1, arg2, ...') not implemented yet")
    # if not isinstance(argnames, Sequence):
    #     raise ParametrizeError("should be sequence")

    # arglen = len(argnames)
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

    # if arglen > 1:
    for value in argvalues:
        if not isinstance(value, Sequence) or isinstance(value, str):
            raise ParametrizeError(
                "in_form['test-x'] should be of type Sequence (tuple, list, ...)"
            )

    return {"argnames": argnames, "argvalues": argvalues, "ids": ids}
