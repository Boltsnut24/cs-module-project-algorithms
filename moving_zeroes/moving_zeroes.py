'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #split 0's into one array and non-zero into another
    zeroArr = []
    nonZeroArr = []
    for i in range(len(arr)):
        if(arr[i] == 0):
            zeroArr.append(0)
        else:
            nonZeroArr.append(arr[i])
            
    #merge the arrays
    return nonZeroArr + zeroArr
    



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")