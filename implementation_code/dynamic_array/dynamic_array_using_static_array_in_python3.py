"""
This python module implements dynamic array using static array.

Static Array: An array of fixed capacity. It doesn't allow deletion, insertion, and append.
A static array occupy a contiguous block of memory.


Raw array used here is from a built-in library called ctypes of python module.
py_object is all python objects.
(size * ctypes.py_object)() creates a python static array with python object type.

example:
(c_int*16)() creates an int array of size 16.
"""

from typing import Any
import ctypes


class DynamicArray:
    """Implement dynamic array in python3, similar to python List."""

    def __init__(self) -> None:
        """
        Initialize a dynamic aray with default size 1.
        """
        self._n = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    @staticmethod
    def _make_array(new_capacity: int) -> Any:
        """
        Return a new array with new capacity.
        Args:
            new_capacity: size of static array.

        Returns:
            A static array with new_capacity number of elements.

        """
        return (new_capacity * ctypes.py_object)()

    def __len__(self) -> int:
        """

        Returns: number of elements stored in the array.

        """
        return self._n

    def __getitem__(self, index: int) -> Any:
        """
        Return element at the index.
        Args:
            index: int, index of the element.

        Returns: element at the index.
        """
        if 0 <= index < self._n:
            return self._array[index]
        raise IndexError(f"Index {index} is out of bounds.")

    def _resize(self, new_capacity: int) -> None:
        """
        Resize the internal static array to new capacity.
        Args:
            new_capacity: int, the size of the array.

        Returns: None
        """
        new_array = self._make_array(new_capacity)

        for index in range(self._n):
            new_array[index] = self._array[index]

        self._array = new_array
        self._capacity = new_capacity

    def insert_at(self, element: Any, index: int) -> None:
        """
        Insert the item at the specified index.
        Args:
            element: generic python object.
            index: int, index of the python object.

        Returns: None.
        """
        if 0 <= index <= self._n:
            if self._n == self._capacity:
                self._resize(new_capacity=2 * self._capacity)

            for ind in range(self._n - 1, index - 1, -1):
                self._array[ind + 1] = self._array[ind]

            self._array[index] = element
            self._n += 1
            return
        raise IndexError(f"Index {index} is not between 0 and {self._n}.")

    def append(self, element: Any) -> None:
        """
        Add an element at the end of the array.
        Args:
            element: generic python object.

        Returns: None.
        """
        return self.insert_at(element=element, index=self._n)

    def remove_at(self, index: int) -> None:
        """
        Deletes element from the specified index value.
        Args:
            index: int, index of the array.

        Returns: None.

        """
        if 0 <= index < self._n:

            for ind in range(index, self._n - 1):
                self._array[ind] = self._array[ind + 1]

            self._array[self._n - 1] = None
            self._n -= 1
            return
        raise IndexError(f"Index {index} is not between 0 and {self._n-1}.")

    def delete(self) -> None:
        """
        Delete item at the end of the array.
        Returns:
            None
        """
        self.remove_at(index=self._n - 1)

    def __repr__(self) -> str:
        """Allow print string."""
        string_list = ["[", str(self._array[0])]
        for ind in range(1, self._n):
            string_list.append(",")
            string_list.append(str(self._array[ind]))
        string_list.append("]")
        return "".join(string_list)


if __name__ == "__main__":
    my_array = DynamicArray()

    assert len(my_array) == 0

    my_array.append(1)
    my_array.append(5)

    assert len(my_array) == 2

    my_array.delete()

    assert my_array[0] == 1

    my_array.insert_at("yes", 0)
    my_array.insert_at("No", 2)

    assert len(my_array) == 3
    assert my_array[1] == 1
    assert my_array[2] == "No"

    my_array.remove_at(0)
    assert my_array[0] == 1
    assert len(my_array) == 2

    my_array.append(10)
    my_array.append("my_love")
    my_array.insert_at("my_future", 0)
    my_array.insert_at("yes", 5)
    my_array.insert_at(14, 4)
    assert len(my_array) == 7
    assert my_array[6] == "yes"

    my_array.remove_at(4)
    assert my_array[4] == "my_love"
