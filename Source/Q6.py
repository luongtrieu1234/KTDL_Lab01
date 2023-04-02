import csv

delimiter = ','

# Đọc bảng dữ liệu từ tệp csv
with open('house-prices.csv', 'r') as file:
    data = []
    csv_reader = csv.reader(file, delimiter=delimiter)
    for row in csv_reader:
        data.append(row)

# Xác định các mẫu không trùng lặp
new_data = []
for row in data:
    if row not in new_data:
        new_data.append(row)

# Ghi các mẫu không trùng lặp vào một tệp csv mới
with open('Q6.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=delimiter)
    for row in new_data:
        csv_writer.writerow(row)


