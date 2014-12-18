from __future__ import print_function


def count_evens(nums):
    """Return the number of even numbers in a list of numbers"""
    return len([x for x in nums if not x % 2])


if __name__ == "__main__":
    test_values = [[0, 100, 50], [0, 30, 15], [10, 50, 20]]
    for x in test_values:
        nums = range(x[0], x[1])
        print(count_evens(nums))
        assert count_evens(nums) == x[2]

    print(u"All tests pass")
