file_path = 'file_ops/sample_text.txt'

file = open(file= file_path)

number_of_lines = 0

for line in file:
    number_of_lines += 1    

print(number_of_lines)