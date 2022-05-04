file_path = 'file_ops/sample_text.txt'

file = open(file=file_path)

letter_to_count = input("Enter the letter to count: ")

number_of_letters = 0

lines_list = file.readlines()

for line in lines_list:
    list_of_words = line.split(" ")
    for word in list_of_words:
        number_of_letters += word.count(letter_to_count)

print(number_of_letters)
