# Write a recursive function that takes in a string and returns the string reversed

def reverse_string(test_string):
    if len(test_string) == 0 or len(test_string) ==1:
        return test_string
    else:
        return test_string[len(test_string) -1] + reverse_string(test_string[:len(test_string) -1])

test_string= "hello"

print(reverse_string(test_string))