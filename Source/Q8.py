import csv

# Ví dụ ta thử tính toán với cột 0 và cột 1 của tệp
col1 =0
col2 =1
# đọc dữ liệu từ tệp csv vào list
data = []
with open('house-prices.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

# thêm các tiêu đề cho các cột mới
data[0].append('Add')
data[0].append('Sub')
data[0].append('Mul')
data[0].append('Div')

# dùng vòng lặp duyệt để lấp đầy ô trống (trống ta coi như nó bằng 0)
# vòng lặp này sinh ra để tránh lỗi tính toán với ô trống
for i in range(1, len(data)):
    if data[i][col1]=="":
        (data[i][col1])=0;
    if data[i][col2]=="":
        (data[i][col2])=0;

# tính toán và thêm kết quả vào list data
for i in range(1, len(data)):
    number1 = float(data[i][col1])
    number2 = float(data[i][col2])

    add = str(number1 + number2)
    sub = str(number1 - number2)
    mul = str(number1 * number2)
    if number2 != 0:
        div = str(number1 / number2)
    else:
        div = 'NaN'
    data[i].append(add)
    data[i].append(sub)
    data[i].append(mul)
    data[i].append(div)

# ghi kết quả vào file mới
with open('Q8.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in data:
        writer.writerow(row)
