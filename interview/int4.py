 # Write a recursive function that takes in a list of strings and returns the words capitalized.

def capitalize_strings(test_list):
    if len(test_list) == 0:
        return " "
    else:
        return (f"{test_list[0].upper()} {capitalize_strings(test_list[1:])}")

sample_list = ['pandas', 'monkeys', 'koalas', 'kangaroos']
print(capitalize_strings(sample_list))
        
      