"""This module outlines how to implement a simple max heap from scratch in python3 API."""
from typing import List


class MaxHeap:
    """This is the implementation of max heap for int elements.
     n stands for the number of elements in the heap."""

    def __init__(self, array: List[int]) -> None:
        self.max_heap = self._heapify(array)

    def _heapify(self, array: List[int]) -> List[int]:
        """time o(n), space o(1)

        the approach:
        if you use sink up then the time would be n*log2(n)

        but if you use sink down then you will get o(n)

        1) place the element as it is in the array.
        2) start with the lowest parent nodes then start to use sink down
        to get the element to the right place

        to preserve the min heap property:
        1) complete binary tree
        2) any parent node is >= either children nodes.
        """
        last_parent_index = (len(array) - 2) // 2

        for curr_index in range(last_parent_index, -1, -1):
            self._sink_down(
                curr_index=curr_index,
                last_index=len(array) - 1,
                array=array
            )
        return array

    def peak(self) -> int:
        """time o(1), space o(1)"""
        return self.max_heap[0]

    def _sink_down(self, curr_index: int, last_index: int, array: List[int]) -> None:
        """time o(log2n), space o(1)

        the relationship between curr_index to child nodes:
        left_child = curr_index * 2 + 1
        right_child = curr_index * 2 + 2

        keep compare curr_index with max(left child, right child) until:
        1) it hit the leaf node index
        2) or the curr_index is >= max(left child, right child).
        """
        left_child_index = 2 * curr_index + 1
        while left_child_index <= last_index:
            right_child_index = 2 * curr_index + 2 if left_child_index < last_index else -1
            if right_child_index != -1 and array[right_child_index] > array[left_child_index]:
                index_to_swap = right_child_index
            else:
                index_to_swap = left_child_index
            if array[index_to_swap] > array[curr_index]:
                self._swap_element(
                    array=array,
                    index_a=index_to_swap,
                    index_b=curr_index
                )
                curr_index = index_to_swap
                left_child_index = 2 * index_to_swap + 1
            else:
                break

    def _sink_up(self, curr_index: int, array: List[int]) -> None:
        """time o(log2n), space o(1)

        the relationship between curr_index to parent node:
        parent_node = (curr_index-1)//2

        keep compare current index to the parent node until:
        1) it hit node at index 0.
        2) or the parent node >= curr index.
        """
        parent_index = (curr_index - 1) // 2
        while curr_index > 0 and array[parent_index] < array[curr_index]:
            self._swap_element(array=array,
                               index_a=parent_index,
                               index_b=curr_index,
                               )
            curr_index = parent_index
            parent_index = (curr_index - 1) // 2

    def push(self, element: int) -> None:
        """time o(log2n), space o(1)

         Approach:
        1. Add new element to the last position
        2. sink up to get the element to the right place
         to preserve the min heap property:
        1) complete binary tree
        2) any parent node is >= either children nodes.
        """
        self.max_heap.append(element)
        self._sink_up(
            curr_index=len(self.max_heap) - 1,
            array=self.max_heap
        )

    def pop(self) -> int:
        """time o(log2n), space o(1)

        Approach:
        1. swap last element with element at index zero.
        2. pop the last element (aka element zero)
        3. sink down the last element to the right place
        to preserve the min heap property:
        1) complete binary tree
        2) any parent node is >= either children nodes.
        """
        if self.max_heap:
            self._swap_element(array=self.max_heap,
                               index_a=0,
                               index_b=len(self.max_heap) - 1)
            element_to_remove = self.max_heap.pop()
            self._sink_down(curr_index=0,
                            last_index=len(self.max_heap) - 1,
                            array=self.max_heap)
            return element_to_remove
        return -1

    @staticmethod
    def _swap_element(array: List[int], index_a: int, index_b: int) -> None:
        """time o(1) space o(1)"""
        array[index_a], array[index_b] = array[index_b], array[index_a]


if __name__ == "__main__":
    max_heap = MaxHeap(array=[12, 10, 5, 11])
    assert max_heap.max_heap == [12, 11, 5, 10]
    max_heap.push(element=100)
    assert max_heap.max_heap == [100, 12, 5, 10, 11]
    max_heap.pop()
    assert max_heap.max_heap == [12, 11, 5, 10]
    assert max_heap.peak() == 12
    max_heap.push(element=5)
    assert max_heap.max_heap == [12, 11, 5, 10, 5]
