'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # walk through array at each spot
    #walk through array again except current spot and append product into new array
    productArray = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if(j != i):
                product = product * arr[j]
        
        productArray.append(product)
    
    return productArray

#Goal: O(n) time and O(1) space NO DIVISION
    #need to modify given array and utilize that space
    #one pass through? not necessarily, pass through and then once again
        #first pass through calculates all possible results
        #second pass modifys original array?
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
