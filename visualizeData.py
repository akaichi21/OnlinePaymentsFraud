# Tìm hiểu và biểu diễn dữ liệu

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('credit_card.csv')

print("Hiển thị 5 dòng đầu tiên của dữ liệu: \n", data.head())

print("\nĐếm các cột dữ liệu rỗng: \n", data.isnull().sum())

print("\nThống kê số lượng của mỗi loại giao dịch được đề cập trong dữ liệu: \n", data.type.value_counts())

print("\nBiểu đồ tỷ lệ phân bố của mỗi loại giao dịch: \n")

type = data["type"].value_counts()
transactions = type.index
quantity = type.values

plt.pie(quantity, labels = transactions, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.title("Sự phân bố của các loại giao dịch")
plt.legend(title = "Các giao dịch:", loc='upper left')
plt.show()



