import csv
import json

# p. 377

# example_file = open('example.csv')
# example_reader = csv.reader(example_file)
# example_data = list(example_reader)
# print(example_data)

# p. 377-378
# print(example_data[0][0])
# print(example_data[0][1])
# print(example_data[0][2])
# print(example_data[1][1])
# print(example_data[6][1]# )

# p. 378

# exampleFile = open('example.csv')
# example_reader = csv.reader(exampleFile)
# for row in example_reader:
#     print('Row #' + str(example_reader.line_num) + ' ' + str(row))

# p. 379

# output_writer = csv.writer(output_file)
# print(output_writer.writerow(['pita', 'falafel', 'fries', 'hummus']))
# print(output_writer.writerow(['Ayo, #MYGUY', 'pita', 'falafel', 'fries']))
# print(output_writer.writerow([1, 2, 3.131592, 4]))
#
# output_file.close()

# p. 380

# csv_file = open('example.tsv', 'w', newline='')
# csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
# print(csv_writer.writerow(['apples', 'oranges', 'grapes']))
#
# print(csv_writer.writerow(['eggs', 'bacon', 'ham']))
#
# print(csv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam']))
#
# csv_file.close()

# p. 381
'''
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv. DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

p. 382
exampleFile = open('example.csv')
exampleDictReader = csv. DictReader(exampleFile, ['time', 'name',
                                                  'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])

outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
print(outputDictWriter.writerow(
    {'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'}))

print(outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'}))

print(outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':
                                 'dog'}))

outputFile.close()

p. 389


stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'


jsonDataAsPythonValue = json.loads(stringOfJsonData)

print(jsonDataAsPythonValue)

p. 390


pythonValue = {'isCat': True, 'miceCaught': 0,
               'name': 'Zophie', 'felineIQ': None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
'''
