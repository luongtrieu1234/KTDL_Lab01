import csv
import io

# Đọc dữ liệu từ file và lưu vào một mảng dữ liệu
data = []
with open("house-prices.csv", "r") as f:
    for line in f:
        data.append(line.strip().split(","))

# Tìm chỉ số của các cột bị thiếu giá trị
missing_columns = []
for i in range(len(data[0])):
    # Kiểm tra xem cột thứ i có chứa giá trị thiếu không
    if any([row[i] == "" for row in data]):
        missing_columns.append(i)

# Lưu tên các cột bị thiếu giá trị vào file txt
column_names = data[0]
missing_column_names = [column_names[i] for i in missing_columns]
with io.open("Q1.txt", mode="w", encoding="utf-8") as f:
    f.write("\n".join(missing_column_names))

