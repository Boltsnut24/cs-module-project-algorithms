'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # seen = [0] * len(arr)

    # for i in range(len(arr)):
    #     seen[arr[i]] = seen[arr[i]] + 1

    # index = 0
    # while index < len(seen):
    #     if(seen[index] != 2 and seen[index] != 0):
    #         return index
    #     index = index + 1
    ####################################
    res = arr[0]
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    
    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")