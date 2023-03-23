from __future__ import annotations
from typing import NamedTuple, Any

# TODO[faq]: how to reprsent empty list?
# eg:
# - can be: [Obj, ...] or exactly []
# - cannot be: [None, ...]

# nodes
class Node(NamedTuple):
    """
    Tree Node
    """
    value: Any
    parent: Node | None
    children: list[Node] | None

    @property
    def siblings(self) -> list[Node]:
        if self.parent:
            # TODO return (parent.children - this.node)
            return self.parent.children # type: ignore -- can't be emtpy
        return []

class NamedNode(Node):
    """
    Named Tree Node
    """
    name: str


# trees

class Tree:
    """
    General purpose tree
    """

if __name__ == "__main__":
    root = Node("foo", None, None)
