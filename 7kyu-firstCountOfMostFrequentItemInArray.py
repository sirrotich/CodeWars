# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

# Example
# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5 

def most_frequent_item_count(collection):
    counter = 0
    
    for i in collection:
        freq = collection.count(i)
        print(freq)
        if freq > counter:
            counter = freq
    return(counter)