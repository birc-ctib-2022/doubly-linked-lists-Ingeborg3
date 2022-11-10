"""Doubly-linked lists."""

from __future__ import annotations
from typing import (
    Generic, TypeVar, Iterable,
    Callable, Protocol
)


class Comparable(Protocol):
    """Type info for specifying that objects can be compared with <."""

    def __lt__(self, other: Comparable) -> bool:
        """Less than, <, operator."""
        ...


T = TypeVar('T')
S = TypeVar('S', bound=Comparable)


class Link(Generic[T]):
    """Doubly linked link."""

    val: T
    prev: Link[T]
    next: Link[T]

    def __init__(self, val: T, p: Link[T], n: Link[T]):
        """Create a new link and link up prev and next."""
        self.val = val
        self.prev = p
        self.next = n


def insert_after(link: Link[T], val: T) -> None:
    """Add a new link containing avl after link."""
    new_link = Link(val, link, link.next)
    new_link.prev.next = new_link
    new_link.next.prev = new_link


def remove_link(link: Link[T]) -> None:
    """Remove link from the list."""
    link.prev.next = link.next
    link.next.prev = link.prev


class DLList(Generic[T]):
    """
    Wrapper around a doubly-linked list.

    This is a circular doubly-linked list where we have a
    dummy link that function as both the beginning and end
    of the list. By having it, we remove multiple special
    cases when we manipulate the list.

    >>> x = DLList([1, 2, 3, 4])
    >>> print(x)
    [1, 2, 3, 4]
    """

    head: Link[T]  # Dummy head link

    def __init__(self, seq: Iterable[T] = ()):
        """Create a new circular list from a sequence."""
        # Configure the head link.
        # We are violating the type invariants this one place,
        # but only here, so we ask the checker to just ignore it.
        # Once the head element is configured we promise not to do
        # it again.
        self.head = Link(None, None, None)  # type: ignore
        self.head.prev = self.head
        self.head.next = self.head

        # Add elements to the list, exploiting that self.head.prev
        # is the last element in the list, so appending means inserting
        # after that link.
        for val in seq:
            insert_after(self.head.prev, val)

    def __str__(self) -> str:
        """Get string with the elements going in the next direction."""
        elms: list[str] = []
        link = self.head.next
        while link and link is not self.head:
            elms.append(str(link.val))
            link = link.next
        return f"[{', '.join(elms)}]"
    __repr__ = __str__  # because why not?


# Exercises

def keep(x: DLList[T], p: Callable[[T], bool]) -> None:
    """
    Remove all elements from x that do not satisfy the predicate p.

    >>> x = DLList([1, 2, 3, 4, 5])
    >>> keep(x, lambda a: a % 2 == 0)
    >>> print(x)
    [2, 4]
    """
    ...


def reverse(x: DLList[T]) -> None:
    """
    Reverse the list x.

    >>> x = DLList([1, 2, 3, 4, 5])
    >>> reverse(x)
    >>> print(x)
    [5, 4, 3, 2, 1]
    """
    ...


def sort(x: DLList[S]) -> None:
    """
    Sort the list x.

    >>> x = DLList([1, 3, 12, 6, 4, 5])
    >>> sort(x)
    >>> print(x)
    [1, 3, 4, 5, 6, 12]
    """
    ...
