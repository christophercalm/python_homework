#Rotate a string by a number shift

rotate_string = input("Enter a string: ")
shift = eval(input("Enter the numberic shift: ")) % len(rotate_string)

new_string = rotate_string.split(rotate_string[:shift])
