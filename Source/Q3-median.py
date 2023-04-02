import csv

# Hàm tính giá trị trung vị
def median(lst):
    n = len(lst)
    s = sorted(lst)
    if n % 2 == 0:
        # Nếu số lượng phần tử là số chẵn, chọn giá trị ở giữa
        return (s[n//2-1] + s[n//2]) / 2
    else:
        # Nếu số lượng phần tử là số lẻ, chọn giá trị ở giữa
        return s[n//2]

# Đọc tệp csv và lưu dữ liệu vào danh sách
data = []
with open('house-prices.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

# Tính giá trị trung vị của thuộc tính số
median_val = {}
for i in range(len(data[0])):
    try:
        val_list = []
        for j in range(1, len(data)):
            if data[j][i] != '':
                val_list.append(float(data[j][i]))
        if val_list:
            median_val[i] = median(val_list)
    except ValueError:
        continue

# Tính giá trị trung vị của tất cả các thuộc tính số
all_val_list = []
for i in range(1, len(data)):
    for j in range(len(data[i])):
        try:
            val = float(data[i][j])
            all_val_list.append(val)
        except ValueError:
            # Nếu giá trị không phải số, ta bỏ qua hoặc thay bằng giá trị khác tùy thích
            all_val_list.append(0)  # Thay bằng giá trị 0
            # continue  # Bỏ qua giá trị không phải số

# Tính giá trị trung vị của danh sách các giá trị số
overall_median = median(all_val_list)


# Điền giá trị còn thiếu bằng giá trị trung vị
for i in range(1, len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '':
            if j in median_val:
                data[i][j] = median_val[j]

# Ghi danh sách dữ liệu đã được cập nhật vào tệp csv
with open('Q3-median.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
