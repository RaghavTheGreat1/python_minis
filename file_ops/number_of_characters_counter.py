file_path = 'file_ops/sample_text.txt'

file = open(file= file_path)


number_of_chars = 0

for line in file.readlines():
    number_of_chars += len(line)

print(number_of_chars)