import csv

filename_input = "house-prices.csv"
filename_output = "Q3-mode.csv"
delimiter = ","
missing_values = ["", "NULL", "NaN"] # Giá trị bị thiếu cần điền

# Bước 1: Đọc dữ liệu từ tệp CSV vào danh sách list
data = []
with open(filename_input, "r") as file:
    for row in file:
        fields = row.strip().split(delimiter)
        data.append(fields)

# Bước 2: Tìm các thuộc tính thiếu giá trị
num_cols = len(data[0])
missing_cols = []
for i in range(num_cols):
    values = [row[i] for row in data if row[i] not in missing_values]
    if len(values) != len(data):
        missing_cols.append((i, values))

# Bước 3: Tìm giá trị mode của các thuộc tính thiếu giá trị
modes = []
for col, values in missing_cols:
    freqs = {value: values.count(value) for value in set(values)}
    mode_value = max(freqs, key=freqs.get)
    modes.append((col, mode_value))

# Bước 4: Điền giá trị mode vào các ô Trống
for row in data:
    for col, mode_value in modes:
        if row[col] in missing_values:
            row[col] = mode_value

# Bước 5: Lưu kết quả vào têp CSV
with open(filename_output, "w") as file:
    for row in data:
        file.write(delimiter.join(row) + "\n")
