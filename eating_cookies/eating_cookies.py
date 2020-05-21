'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = None):
    #base case of 0 cookies#
    if n == 0:
        return 1
    #base case of negative values
    elif n < 0:
        return 0
    #skip calculations, we already know this answer
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        #if we don't have cache started, initialize
        if not cache:
            cache = [0 for _ in range(n+1)]
        #save answer of permutations for n, into cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
