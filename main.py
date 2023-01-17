from dataclasses import dataclass


@dataclass
class Data:
    """The class stores an ascending sequence and borders"""

    ascending_sequence: list
    borders: tuple

    def __len__(self):
        return len(self.ascending_sequence)

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return len(self.ascending_sequence) > len(other)


def check_ascending_sequence(sequence: list[int]) -> bool:
    """Checks if a sequence is strictly increasing"""
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True


def generates_all_sublists_of_list(sequence: list[int]) -> list[dict]:
    """
    Returns a list of dictionaries, each containing a
    strictly increasing sublist and its bounds in the main list
    """
    new_list = []
    for len_substr in range(len(sequence)):
        for i in range(len(sequence) - len_substr):
            temp_list = sequence[i : i + len_substr + 1]
            if check_ascending_sequence(temp_list):
                new_list.append(
                    Data(ascending_sequence=temp_list, borders=(i, i + len_substr))
                )
    return new_list


def get_bounds_strictly_monotonic_sub_max_len(sequence: list[int]) -> tuple:
    """
    Returns the bounds of a strictly monotonic
    subsegment of the maximum length of the given list
    """
    all_sublists_of_list = generates_all_sublists_of_list(sequence)
    return max(all_sublists_of_list).borders


if __name__ == "__main__":
    print(get_bounds_strictly_monotonic_sub_max_len([-3, 2, 3, 4, 5, 6, 7, 7, 8]))
    print(
        get_bounds_strictly_monotonic_sub_max_len([-1, -1, -1, -1, -1, -1, -1, -1, -1])
    )
