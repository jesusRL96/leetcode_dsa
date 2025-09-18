import functools


def check_word_ispalindrome() -> bool:
    word = input("enter a text to check whether it is a palindrome or not: ")
    print(f"{word=}")
    left, right = 0, len(word) - 1
    while left < right:
        if word[left].lower() != word[right].lower():
            return False
        left += 1
        right -= 1
    return True


def check_for_target(nums, target) -> bool:
    print(f"{nums=}")
    print(f"{target=}")
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False


check_for_target_demo = functools.partial(
    check_for_target, nums=[1, 2, 4, 6, 8, 9, 14, 15], target=13
)


# More than one array
def combine_sorted_arrays(array1: list, array2: list) -> list:
    print(f"{array1=}")
    print(f"{array2=}")
    ans = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] > array2[j]:
            ans.append(array2[j])
            j += 1
        else:
            ans.append(array1[i])
            i += 1
    if i < len(array1) - 1:
        ans.extend(array1[i:])
    elif j < len(array2) - 1:
        ans.extend(array2[j:])
    return ans


def is_subsequence(s: str, t: str) -> bool:
    print(f"{s=}")
    print(f"{t=}")
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


is_subsequence_demo = functools.partial(is_subsequence, s="ace", t="abcde")


combine_sorted_arrays_demo = functools.partial(
    combine_sorted_arrays, array1=[1, 4, 7, 20], array2=[3, 5, 6]
)


# challenges
def reverse_string() -> list:
    """
    Do not return anything, modify s in-place instead.
    """
    s = list(input("enter a text:"))
    print(f"input: {s=}")
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


def sorted_squares(nums: list[int]) -> list[int]:
    print(f"{nums=}")
    i = 0
    j = len(nums) - 1
    ans = []

    while i <= j:
        if nums[i] ** 2 <= nums[j] ** 2:
            ans.insert(0,nums[j]**2)
            j -= 1
        else:
            ans.insert(0,nums[i]**2)
            i += 1
    return ans


def sorted_squares_demo():
    print(sorted_squares([-5, -4, 1, 2, 5]))
    print(sorted_squares([-7, -3, 2, 3, 11]))
    print(sorted_squares([-10, -8, -6, -2, -1, 0]))
    print(sorted_squares([1, 2, 3, 4, 5, 8]))
    print(sorted_squares([-9, -7, -5, -3, -1, 2, 4, 4, 7, 10]))
    print(sorted_squares([-4,-1,0,3,10]))
    print(sorted_squares([2]))


valid_options = (
    (1, "palindrome", check_word_ispalindrome),
    (2, "check for target", check_for_target_demo),
    (3, "combine - sorted arrays", combine_sorted_arrays_demo),
    (4, "is subsequence", is_subsequence_demo),
    (5, "reverse string", reverse_string),
    (6, "sorted squares", sorted_squares_demo),
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
