file_path = 'file_ops/sample_text.txt'

file = open(file= file_path)


number_of_words = 0

lines_list = file.readlines()

for line in lines_list:
    number_of_words += len(line.split())

print(number_of_words)