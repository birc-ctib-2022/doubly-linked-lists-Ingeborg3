# Doubly linked lists

Here's a way to implement a link in a doubly-linked list:

```python
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
```

and functions for adding a new link or removing an existing one:

```python
def insert_after(link: Link[T], val: T) -> None:
    """Add a new link containing avl after link."""
    new_link = Link(val, link, link.next)
    new_link.prev.next = new_link
    new_link.next.prev = new_link


def remove_link(link: Link[T]) -> None:
    """Remove link from the list."""
    link.prev.next = link.next
    link.next.prev = link.prev
```

The functions assume that we always have non-`None` links before and after the links we manipulate. We can assure that if we have dummy elements at both ends of the list. I have done that, but with a twist: I use the same link at both ends, thus creating a so-called *circular list*.

```python
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
        self.head = Link(None, None, None)
        self.head.prev = self.head
        self.head.next = self.head
        for val in seq:
            insert_after(self.head.prev, val)
```

When you want to iterate through a list, start at its `head.next` and continue until you get back to `head`, then you are done. See `src/lists.py` for details, where the `__str__()` method gives you an example of this.

To get a little practise on how to manipulate such structures, do these exercises:

**Exercise:** Write a function, `keep` that takes a list `x` and a predicate `p` and update `x` in a similar way that

```python
x = [a for a in x if p(a)]
```

would do for a built-in list.

**Exercise:** Write a function `reverse()` that reverses a list.

**Exercise:** Write a function `sort()` that sorts a list.
