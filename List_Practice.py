# Python program to swap first and last element of the list using inbuilt function   append() ,Insert(),pop().
# Input : [12, 35, 9, 56, 24] Output : [24, 35, 9, 56, 12] 
# def swap(input_list):
    

#     last_element_tempVarible=input_list.pop()
#     first_tempVarible=input_list.pop(0)

#     input_list.append(first_tempVarible)
#     input_list.insert(0,last_element_tempVarible)
#     return input_list
# input_list=[12,35,9,56,24]
# swap(input_list)
# print(swap(input_list))



def Assigning_same():
    
    input_list=[28,35,9,56,24]
    input_list[0],input_list[-1]=input_list[-1],input_list[0]
    # return input_list
    print(input_list)


Assigning_same()
# print(Assigning_same(input_list))
