from _01_singly_a import SingleLinkedList as L


class TestShouldSucced:
    # init
    def test_instantiate__no_args(self):
        l = L()
        assert len(l) == 0

    def test_instantiate__one_arg(self):
        pass

    def test_instantiate__multiple_arg(self):
        pass

    # append
    def test_append(self):
        pass

    # remove
    def test_remove(self):
        pass

    # general


class TestShouldFail:
    def test_instantiate_with_wrong_args(self):
        pass
