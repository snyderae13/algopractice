# Write an algorithm that takes in an unsorted integer array and finds a pair with a given sum

def find_pair(lst,target):
    sorted_list = sorted(lst)
    left = 0
    right = len(sorted_list) -1

    while left < right:
        if sorted_list[left] + sorted_list[right] == target:
            return(sorted_list[left], sorted_list[right])

        if sorted_list[left] + sorted_list[right] < target:
            left = left+1
        else:
            right = right -1
    return ('no pairs sum to the target')

sample_list=[5, 10, 4, 7, 6, 2]
print(find_pair(sample_list, 9))