import csv

# Đọc tệp csv và lưu dữ liệu vào danh sách
data = []
with open('house-prices.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

# Tính giá trị trung bình của thuộc tính số
mean_val = {}
for i in range(len(data[0])):
    try:
        sum_val = 0
        cnt_val = 0
        for j in range(1, len(data)):
            if data[j][i] != '':
                sum_val += float(data[j][i])
                cnt_val += 1
        if cnt_val > 0:
            mean_val[i] = sum_val / cnt_val
        else:
            sum_all = 0
            cnt_all = 0
            for j in range(1, len(data)):
                for k in range(len(data[j])):
                    if k not in mean_val and data[j][k] != '':
                        sum_all += float(data[j][k])
                        cnt_all += 1
            overall_mean = sum_all / cnt_all
            mean_val[i] = overall_mean
    except ValueError:
        continue

# Điền giá trị còn thiếu bằng giá trị trung bình
for i in range(1, len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '':
            if j in mean_val:
                data[i][j] = mean_val[j]
            


# Ghi danh sách dữ liệu đã được cập nhật vào tệp csv
with open('Q3-mean.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
