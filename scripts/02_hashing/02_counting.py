import functools
from collections import defaultdict


def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


find_longest_substring_demo = functools.partial(find_longest_substring, s="eceba", k=2)


def intersection(nums: list[list[int]]) -> list[int]:
    counts = defaultdict(int)
    for arr in nums:
        for x in arr:
            counts[x] += 1

    n = len(nums)
    ans = []
    for key in counts:
        if counts[key] == n:
            ans.append(key)

    return sorted(ans)


intersection_demo = functools.partial(
    intersection, nums=[[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
)


def are_occurrences_equal(s: str) -> bool:
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    frequencies = counts.values()
    return len(set(frequencies)) == 1


are_occurrences_equal_demo = functools.partial(are_occurrences_equal, s="abacbc")


def subarray_sum(nums: list[int], k: int) -> int:
    """find the number of subarrays whose sum is equal to k."""
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


subarray_sum_demo = functools.partial(subarray_sum, nums=[1, 2, 1, 2, 1], k=3)


def number_of_subarrays(nums: list[int], k: int) -> int:
    """Find the number of subarrays with exactly k odd numbers in them"""
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


number_of_subarrays_demo = functools.partial(
    number_of_subarrays, nums=[1, 1, 2, 1, 1], k=3
)


# challenges
def max_number_of_balloons(text):
    balloon = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
    forming_word_frequency = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
    ans = 0
    for l in text:
        if l in balloon:
            forming_word_frequency[l] += 1
    return min(*[v / balloon[k] for k, v in forming_word_frequency.items()])
    """
        b = text.count('b')
        a = text.count('a')
        o = text.count('o')//2
        l = text.count('l')//2
        n = text.count('n')
        return min(b,a,l,o,n)
        """


max_number_of_balloons_demo = functools.partial(
    max_number_of_balloons, text="loonbalxballpoon"
)


def find_max_length(nums):
    """
    Contiguous array
    """
    count = 0
    max_length = 0
    hash_table = {0: 0}
    for index, num in enumerate(nums, 1):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in hash_table:
            max_length = max(max_length, index - hash_table[count])
        else:
            hash_table[count] = index
    return max_length

find_max_length_demo = functools.partial(
    find_max_length, nums=[0,1,1,1,1,1,0,0,0]
)


valid_options = (
    (1, "find longest substring", find_longest_substring_demo),
    (2, "intersection", intersection_demo),
    (3, "are occurrences equal", are_occurrences_equal_demo),
    (4, "subarray sum", subarray_sum_demo),
    (5, "number of subarray", number_of_subarrays_demo),
    (6, "c1: max number of 'balloon'", number_of_subarrays_demo),
    (7, "c2: find max length", find_max_length_demo),
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
