# Write a recursive function that takes in a number and returns the sum of the numbers from 0 to the number.
# Example: if the input is 5, the expected output would be 15 (5+4+3+2+1 = 15).

def sum_of_all_numbers(num):
    if num == 0 or num == 1:
        return num
    else:
        return num + sum_of_all_numbers(num-1)

n = 5

print(sum_of_all_numbers(n))

# this is creating a kind of loop where until num becomes either 1 or 0 it will contine to be added to the original num and then decrement by 1. 