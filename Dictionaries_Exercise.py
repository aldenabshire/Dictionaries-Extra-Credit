
import csv

infile = open('book of John text.txt', 'r')
csvfile = csv.reader(infile, delimiter = ' ')

dictionary = dict()

for row in csvfile:

    for word in row:

        if word in dictionary:

            dictionary[word] = dictionary[word] + 1

        else:

            dictionary[word] = 1

print()
print('Father:', dictionary['Father'])
print('God:', dictionary['God'])
print('Christ:', dictionary['Christ'])
print('Spirit:', dictionary['Spirit'])
print('spirit:', dictionary['spirit'])
print('life:', dictionary['life'])
print('man', dictionary['man'])
print()