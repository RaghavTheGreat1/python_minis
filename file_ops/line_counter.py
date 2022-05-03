file_name = 'sample_text.txt'

file = open(file= file_name)


number_of_lines = 0

for line in file:
    number_of_lines += 1

print(number_of_lines)