def quick_sort(string_list, start, end):
    if start < end:
        p = partition(string_list, start, end)
        quick_sort(string_list, start, p - 1)
        quick_sort(string_list, p + 1, end)

    return string_list


# baseado no course
def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = (
                string[delimiter],
                string[index],
            )

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)
    # elif len(first_string) != len(second_string):
    #     return (first_string, first_string, False)

    list_1 = list(first_string.lower())
    list_2 = list(second_string.lower())
    first_str_list = "".join(
        quick_sort(list_1, 0, len(list_1) - 1)
    )
    second_str_list = "".join(
        quick_sort(list_2, 0, len(list_2) - 1)
    )

    test_anagram = first_str_list == second_str_list
    print(first_str_list, second_str_list, test_anagram)
    return (first_str_list, second_str_list, test_anagram)


print(is_anagram("", "perdaaaa"))
