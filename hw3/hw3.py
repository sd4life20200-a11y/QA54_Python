def print_list_reverse(lst):
    if not isinstance(lst, list) or not lst:
        print("Wrong list")
        return
    print(lst[::-1])

print_list_reverse([1, 2, 3])



def is_valid_point(point):
    if point is None or point == ():
        return None
    if not isinstance(point, tuple):
        return False
    if len(point) != 2:
        return False
    if not isinstance(point[0], (int, float)) or not isinstance(point[1], (int, float)):
        return False
    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))



def print_sublist_reverse(lst, start, finish):
    if not isinstance(lst, list) or not lst:
        print("Wrong args")
        return

    if not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
        return

    if start < 0 or finish >= len(lst):
        print("Wrong args")
        return

    if start > finish:
        print("Wrong args")
        return

    result = lst[:start] + lst[start:finish + 1][::-1] + lst[finish + 1:]

    print(result)


print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)

print_sublist_reverse(None, 1, 3)
print_sublist_reverse([], 1, 3)
print_sublist_reverse("hello", 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse([1, 2, 3], 0, "2")
print_sublist_reverse([1, 2, 3], 0, 5)
print_sublist_reverse([1, 2, 3], 2, 0)