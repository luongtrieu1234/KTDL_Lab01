import csv

# đặt tên tệp csv để bình thường hóa và tạo biến "index_attribute" để chỉ định index của cột muốn bình thường hóa
filename = "house-prices.csv"
output_filename = "Q7-minmax.csv"
index_attribute = 0  #ví dụ ở đây là index cột 0 là Id

# đọc tệp csv bằng module csv và lưu dữ liệu vào danh sách các hàng
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

# tìm giá trị nhỏ nhất và lớn nhất của cột được chỉ định bằng biến "index_attribute"
min_value = float('inf')
max_value = -float('inf')
for row in rows:
    try:
        value = float(row[index_attribute])
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    except ValueError:
        pass  

# duyệt qua danh sách các hàng và thực hiện bình thường hóa
for row in rows[1:]:  # bỏ qua hàng đầu tiên chứa tiêu đề
    try:
        value = float(row[index_attribute])
        normalized_value = (value - min_value) / (max_value - min_value)
        row[index_attribute] = normalized_value    
    except ValueError:
        pass  

# ghi dữ liệu mới đã bình thường hóa và chuyển đổi thành số nguyên vào một tệp csv mới
with open(output_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
