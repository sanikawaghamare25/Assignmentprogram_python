'''
2. Flatten a Nested List
   - Create a function flatten_list(nested_list) that takes a nested list as input and returns a flattened list.
   - Example:  
     Input: [[1, 2], [3, [4, 5]], 6]  
     Output: [1, 2, 3, 4, 5, 6]'''


def flatten_list(nested_list):
    #a=[[1,2],[3,4]]
    flat_list=[]
    for i in nested_list:
        for item in i:
            flat_list.append(item)
    return flat_list
#nested_list=int(input("Enter the list:"))
nested_list=[[1,2,2],[4,5,6],[1,2]]
print("flatten_list:",flatten_list(nested_list))


2) 
input=[[1,2],[3,[4,5]],6]
list1=[]
for i in input:
    if type(i)==list:
        for i1 in i:
            if type(i1)==list:
                for i2 in i1:
                    list1.append(i2)
            else:
                list1.append(i1)
    else:
        list1.append(i)
print(list1)
        
