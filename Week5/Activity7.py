# Week 5 Activity 7 — Library OOP:
# Inheritance: Book, Magazine → LibraryItem
# Encapsulation: protected (_attr), private (__attr), and properties for safe access.

from typing import List


class LibraryItem:
    """
    Base (parent) class for anything the library can lend.
    Encapsulation:
      - _title, _author are 'protected' by convention (single underscore).
      - __checked_out is 'private' (double underscore → name-mangling).
    """

    def __init__(self, title: str, author: str) -> None:
        self._title = title
        self._author = author
        self.__checked_out = False  # private: only methods inside LibraryItem can mutate directly

    # ---- Read-only properties expose protected data without giving callers a raw attribute handle.
    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    # ---- Controlled accessors for the private flag (encapsulation in action).
    @property
    def is_checked_out(self) -> bool:
        return self.__checked_out

    def check_out(self) -> None:
        """Mark this item as checked out (uses private state)."""
        self.__checked_out = True

    def check_in(self) -> None:
        """Mark this item as returned (uses private state)."""
        self.__checked_out = False

    # ---- Polymorphic method: subclasses override to add details.
    def display_details(self) -> str:
        status = "Checked out" if self.is_checked_out else "Available"
        return f"'{self.title}' by {self.author} — {status}"


class Book(LibraryItem):
    """Child class: inherits attributes/behavior from LibraryItem."""
    # No extra fields needed for this exercise; just override the display.
    def display_details(self) -> str:
        # super() lets us reuse the parent’s implementation and extend it.
        base = super().display_details()
        return f"Book — {base}"


class Magazine(LibraryItem):
    """
    Child class: adds 'issue_frequency' with validation via property.
    Demonstrates encapsulation with a controlled setter.
    """

    def __init__(self, title: str, author: str, issue_frequency: str) -> None:
        super().__init__(title, author)  # initialize inherited fields
        self._issue_frequency = ""       # protected storage for the property
        self.issue_frequency = issue_frequency  # go through the setter for validation

    @property
    def issue_frequency(self) -> str:
        return self._issue_frequency

    @issue_frequency.setter
    def issue_frequency(self, value: str) -> None:
        allowed = {"daily", "weekly", "monthly", "quarterly", "annual"}
        v = value.strip().lower()
        if v not in allowed:
            raise ValueError(f"issue_frequency must be one of {sorted(allowed)}")
        self._issue_frequency = v

    def display_details(self) -> str:
        base = super().display_details()
        return f"Magazine — {base} — Issue: {self.issue_frequency.capitalize()}"


class Library:
    """
    Aggregates LibraryItem objects (composition).
    Encapsulation:
      - _items is protected; methods provide the safe public API.
    """

    def __init__(self) -> None:
        self._items: List[LibraryItem] = []

    def add_item(self, item: LibraryItem) -> None:
        """Add any LibraryItem (Book or Magazine) to the collection."""
        self._items.append(item)

    def remove_item_by_title(self, title: str) -> bool:
        """
        Remove first item with matching title.
        Returns True if removed, False if not found.
        """
        for i, it in enumerate(self._items):
            if it.title == title:
                del self._items[i]
                return True
        return False

    def display_all(self) -> str:
        """Return a newline-separated list of all item details."""
        if not self._items:
            return "Library is empty."
        return "\n".join(it.display_details() for it in self._items)


# ---------------- Demo / Manual test ----------------
if __name__ == "__main__":
    lib = Library()

    b1 = Book("Clean Code", "Robert C. Martin")
    b2 = Book("The Pragmatic Programmer", "Andrew Hunt & David Thomas")
    m1 = Magazine("Nature", "Editorial Board", "weekly")
    m2 = Magazine("National Geographic", "Editorial Board", "monthly")

    lib.add_item(b1)
    lib.add_item(b2)
    lib.add_item(m1)
    lib.add_item(m2)

    # Try a checkout to show private-state usage via methods.
    b1.check_out()

    print(lib.display_all())
    # Remove an item, then show again
    lib.remove_item_by_title("Nature")
    print("\nAfter removing 'Nature':")
    print(lib.display_all())
