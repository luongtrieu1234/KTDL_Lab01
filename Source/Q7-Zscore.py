import csv
import math 

# đặt tên tệp csv để bình thường hóa và tạo biến "index_attribute" để chỉ định index của cột muốn bình thường hóa
filename = "house-prices.csv"
output_filename = "Q7-Zscore.csv"
index_attribute = 0

# đọc tệp csv bằng module csv và lưu dữ liệu vào danh sách các hàng
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

# tạo danh sách các giá trị của thuộc tính muốn chuẩn hóa
data = []
for row in rows[1:]:  # bỏ qua hàng đầu tiên chứa tiêu đề
    try:
        value = float(row[index_attribute])
        data.append(value)
    except ValueError:
        pass 

# tính giá trị trung bình (mean) và độ lệch chuẩn (standard deviation) của thuộc tính muốn chuẩn hóa
#mean = statistics.mean(data)
#stdev = statistics.stdev(data)
# tính giá trị trung bình (mean) và độ lệch chuẩn (standard deviation) của thuộc tính muốn chuẩn hóa
mean = sum(data) / len(data)
stdev = math.sqrt(sum([(x - mean) ** 2 for x in data]) / (len(data) - 1))


# duyệt qua danh sách các hàng và thực hiện chuẩn hóa Z-score
for row in rows[1:]:  # bỏ qua hàng đầu tiên chứa tiêu đề
    try:
        value = float(row[index_attribute])
        z_score = (value - mean) / stdev
        row[index_attribute] = z_score
    except ValueError:
        pass  

# ghi dữ liệu mới đã chuẩn hóa Z-score vào một tệp csv mới
with open(output_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
