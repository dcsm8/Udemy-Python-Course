data_file = open('csv_data.txt', 'r')

data_content = [line.strip() for line in data_file.readlines()]
data_file.close()
data_content = data_content[1:]

for item in data_content:
    name, age, university, degree = item.split(',')
    print(f'{name.capitalize()} is {age}, studying {degree.title()} at {university.title()}')

sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)
