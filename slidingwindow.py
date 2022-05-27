def maxSum(arr,WindowSize):
    arraySize = len(arr)
    if(arraySize<= WindowSize):
        print("invalid operation")
        return -1
    
    window_sum = sum([arr[i] for i in range(WindowSize)]) # sum of first window
    max_sum = window_sum

    for i in range(arraySize-WindowSize):  # we compute the sum by removing the first element of the previous window and adding the last element of our current window
        window_sum = window_sum - arr[i] + arr[i + WindowSize] # our window sum is equal to our current window sum minus the first element of the previous window, plus the element from our new window
        max_sum = max(window_sum,max_sum) # get our max sum between current value and our just calculated value and then return the max sum 
    
    return max_sum

arr = [80,-50,90,100]
k = 2
answer = maxSum(arr, k) # 190
print(answer)