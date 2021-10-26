def binary_search(list_exp, item):
    low = 0
    high = len(list_exp) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list_exp[mid]
        # finding and the way to find
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    # if not
    return None