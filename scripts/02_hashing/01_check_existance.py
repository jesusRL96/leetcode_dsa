import functools


def two_sum(nums: list[int], target: int) -> list[int]:
    print(f"{nums=}")
    print(f"{target=}")
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:  # This operation is O(1)!
            return [i, dic[complement]]

        dic[num] = i

    return [-1, -1]


two_sum_demo = functools.partial(two_sum, nums=[5, 2, 7, 10, 3, 9], target=8)


def repeated_character(s: str) -> str:
    print(f"{s=}")
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)

    return " "


repeated_character_demo = functools.partial(repeated_character, s="abcdeda")


# challenges
def check_is_pangram() -> bool:
    """
    check it contains all letters in the alphabet
    """
    s = list(input("enter a text:"))
    word_letters = set(s)
    return len(word_letters) == 26


def missing_number(nums: list[int]) -> int:
    print(f"{nums=}")
    nums_set = set(nums)
    for i in range(len(nums) + 1):
        if i not in nums_set:
            return i
    return -1


def missing_number_demo():
    print(missing_number([3, 0, 1]))

def counting_elements(arr: list[int]) -> int:
    print(f"{arr=}")
    arr_set = set(arr)
    ans=0
    for i in arr:
        if i+1 in arr_set:
            ans+=1
    return ans


def counting_elements_demo():
    print(counting_elements([1,2,3]))

valid_options = (
    (1, "two sum", two_sum_demo),
    (2, "repeated character", repeated_character_demo),
    (3, "C1: Check is pangram", check_is_pangram),
    (4, "C2: Missing number", missing_number_demo),
    (5, "C3: Counting elements", counting_elements_demo),
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
