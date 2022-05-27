# Write an algorithm that checks if a string contains another string.
#If it does, return True; otherwise, return False
#Example: When checking if string "Hello world" contains "Hello", the function should return True. If checking if string contains "Bye", the function should return False.



def find_string(str, word):
    return(word in str)

sample_str = "Hello World"
chosen_str = "Bye"

print(find_string(sample_str, sample_str))