input_value = input("Enter the value:  ")
seperate = input_value.split(',')

convert_list =[int (num) for num in seperate]
convert_tuple=tuple(convert_list)
print(convert_list)
print(convert_tuple)