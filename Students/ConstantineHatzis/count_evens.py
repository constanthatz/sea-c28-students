from __future__ import print_function


def count_evens(nums):
    return len([x for x in nums if not x % 2])


if __name__ == "__main__":
    nums = range(100)
    num_evens = count_evens(nums)
    print(num_evens)
