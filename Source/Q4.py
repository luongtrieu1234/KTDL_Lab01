import csv

delimiter = ','

# Đọc dữ liệu từ tệp csv
with open('house-prices.csv', 'r') as file:
    data = []
    for row in file:
        data.append(row.strip().split(delimiter))

# Loại bỏ hàng bị thiếu dữ liệu
new_data = []
for row in data:
    num_missing = 0
    for value in row:
        if value == '':
            num_missing += 1
    if num_missing <= int(len(row)*0.05):
        new_data.append(row)

# Ghi dữ liệu mới vào tệp csv
with open('Q4.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=delimiter)
    for row in new_data:
        writer.writerow(row)
