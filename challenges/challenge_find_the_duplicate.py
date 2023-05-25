def find_duplicate(nums):
    """
    para pegar todos sao numeros em uma lista refereencia:
    https://datascienceparichay.com/article/python-check-list-contains-only-numbers/
    """
    if not isinstance(nums, list) or not all(
        [isinstance(item, int) for item in nums]
    ):
        return False

    nums.sort()
    # baseado no código apresentado no dia 4.1
    # pelo professor Cristiano Benites e ajuda da isabela costa
    for index, num_element in enumerate(nums[:-1]):
        if num_element == nums[index + 1] and num_element >= 0:
            return num_element
    return False


print(find_duplicate([-1, -1, 2, 3, 10]))
