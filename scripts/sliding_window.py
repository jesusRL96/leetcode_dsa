import functools


def find_subarray_length(nums, k):
    """find the length of the longest subarray whose sum is less than or equal to k"""
    # curr is the current sum of the window
    print(f"{nums=} {k=}")
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans


find_subarray_length_demo = functools.partial(
    find_subarray_length, nums=[3, 1, 2, 7, 4, 2, 1, 1, 5], k=8
)


def find_ones_subarray_length(s):
    """find the length of the longest substring achievable that contains only 1 by flipping at most on '0' to '1'"""
    # curr is the current number of zeros in the window
    print(f"{s=}")
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


find_ones_subarray_length_demo = functools.partial(
    find_ones_subarray_length, s="1101100111"
)


def num_subarray_product_lt_k(nums: list[int], k: int) -> int:
    """return the number of subarrays where the product of all the elements in the subarray is strictly less than k"""
    print(f"{nums=} {k=}")
    if k <= 1:
        return 0

    ans = left = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1

        ans += right - left + 1

    return ans


num_subarray_product_lt_k_demo = functools.partial(
    num_subarray_product_lt_k, nums=[10, 5, 2, 6], k=100
)


# Fixed window size
def find_best_subarray(nums, k):
    """find the sum of the subarray with the largest sum whose length is k"""
    print(f"{nums=} {k=}")
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)

    return ans


find_best_subarray_demo = functools.partial(
    find_best_subarray, nums=[3, -1, 4, 12, -8, 5, 6], k=4
)


# Challenges
def maximum_average_subarray(nums, k):
    """Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value"""
    print(f"{nums=} {k=}")
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = float(curr) / k
    for i in range(k, len(nums)):
        curr = curr - nums[i - k] + nums[i]
        ans = max(ans, float(curr) / k)
    return ans


def maximum_average_subarray_demo():
    print(maximum_average_subarray([-5, -4, 12, 2, 5], 4))
    print(maximum_average_subarray([1, 12, -5, -6, 50, 3], 4))


def longest_ones(nums, k):
    """return the maximum number of consecutive 1's in the array if you can flip at most k 0's"""
    print(f"{nums=} {k=}")
    left = curr = zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        curr = max(curr, right - left + 1)
    return curr


def longest_ones_demo():
    print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    print(longest_ones([0, 0, 0, 1], 3))


# Menu
valid_options = (
    (1, "find subarray length", find_subarray_length_demo),
    (2, "find max ones substring", find_ones_subarray_length_demo),
    (3, "get subarrays product less than k", num_subarray_product_lt_k_demo),
    (4, "best subarray", find_best_subarray_demo),
    (5, "c1: maximum average subarray", maximum_average_subarray_demo),
    (6, "c2: find longest ones subarray", longest_ones_demo),
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
