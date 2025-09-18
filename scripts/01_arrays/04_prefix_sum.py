import functools
import math


def answer_queries(nums, queries, limit):
    """return a boolean array that represents the answer to each query.
    A query is true if the sum of the subarray from x to y is less than limit, or false otherwise
    """
    print(f"{nums=}")
    print(f"{queries=}")
    print(f"{limit=}")
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans


answer_queries_demo = functools.partial(
    answer_queries, nums=[1, 6, 3, 2, 7, 2], queries=[[0, 3], [2, 5], [2, 4]], limit=13
)


def ways_to_split_array(nums: list[int]) -> int:
    """find the number of ways to split the array into two parts so that the first section
    has a sum greater than or equal to the sum of the second section"""
    n = len(nums)
    print(f"{nums=}")

    prefix = [nums[0]]
    for i in range(1, n):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    for i in range(n - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1

    return ans


ways_to_split_array_demo = functools.partial(ways_to_split_array, [10, 4, -8, 7])


# Challenges
def running_sum_array(nums: list[int]):
    print(f"{nums=}")
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] + nums[i])
    return prefix


running_sum_array_demo = functools.partial(running_sum_array, nums=[3, 1, 2, 10, 1])


def min_start_value(nums: list[int]):
    print(f"{nums=}")
    ans = 1

    def validate_number(number):
        prefix = [number]
        for i in range(0, len(nums)):
            prefix.append(prefix[i] + nums[i])
            if prefix[i + 1] < 1:
                return False
        return True

    is_valid = False
    while not is_valid:
        is_valid = validate_number(ans)
        if is_valid:
            break
        ans += 1
    return ans


def min_start_value_prefix_total_approach(nums: list[int]):
    print(f"{nums=}")
    min_val = 0
    total = 0
    # Iterate over the array and get the minimum step-by-step total.
    for num in nums:
        total += num
        min_val = min(min_val, total)

    return -min_val + 1


def min_start_value_demo():
    min_start_value = min_start_value_prefix_total_approach
    print(min_start_value(nums=[-3, 2, -3, 4, 2]))
    print(min_start_value(nums=[1, 2]))
    print(min_start_value(nums=[1, -2, -3]))


def get_averages(nums: list[int], k: int):
    print(f"{nums=}")
    print(f"{k=}")
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] + nums[i])
    print(f"{prefix=}")

    ans = []
    for i in range(len(nums)):
        if i < k or i >= len(nums) - k:
            ans.append(-1)
        else:
            ans.append((prefix[i + k] - prefix[i - k] + nums[i - k]) // ((k * 2) + 1))
    return ans


def get_averages_demo():
    print(get_averages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
    print(get_averages(nums=[100000], k=0))
    print(get_averages(nums=[8], k=100000))


valid_options = (
    (1, "answer queries", answer_queries_demo),
    (2, "ways to split array", ways_to_split_array_demo),
    (3, "c1: running sum of arrays", running_sum_array_demo),
    (4, "c2: min start value", min_start_value_demo),
    (5, "c3: get averages", get_averages_demo),
)


def menu():
    input_f = None
    while input_f not in [x[0] for x in valid_options]:
        print(
            f"""Choose the method to test:\n{"\n".join([str(x[0]) + ". " + x[1].capitalize() for x in valid_options])} """
        )
        input_f = int(input("Choose a valid option: "))
    return int(input_f)


if __name__ == "__main__":
    choosen = menu()
    dict_menu = {x[0]: x[2] for x in valid_options}
    print(f"ans = {dict_menu[choosen]()}")
