import csv

delimiter = ','

# Đọc dữ liệu từ tệp csv
with open('house-prices.csv', 'r') as file:
    data = []
    for row in file:
        data.append(row.strip().split(delimiter))

# Tìm cột bị thiếu dữ liệu
missing_columns = []
num_rows = len(data)
num_cols = len(data[0])
for j in range(num_cols):
    num_missing = 0
    for i in range(num_rows):
        if data[i][j] == '':
            num_missing += 1
    if num_missing > int(num_rows*0.05):
        missing_columns.append(j)

# Loại bỏ cột bị thiếu dữ liệu
new_data = []
for row in data:
    new_row = []
    for j, value in enumerate(row):
        if j not in missing_columns:
            new_row.append(value)
    new_data.append(new_row)

# Ghi dữ liệu mới vào tệp csv
with open('Q5.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=delimiter)
    for row in new_data:
        writer.writerow(row)

