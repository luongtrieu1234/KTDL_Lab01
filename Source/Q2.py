import csv
import io

# Đọc dữ liệu từ file và lưu vào một mảng
data = []
with open("house-prices.csv", "r") as f:
    for line in f:
        data.append(line.strip().split(","))

# Khai báo biến đếm số dòng bị thiếu dữ liệu và duyệt qua từng dòng
missing_row_count = 0
for row in data:
    if any([cell == "" for cell in row]):
        missing_row_count += 1

# Ghi số dòng bị thiếu dữ liệu vào file text
with io.open("Q2.txt", mode="w", encoding="utf-8") as f:
    f.write(str(missing_row_count))
