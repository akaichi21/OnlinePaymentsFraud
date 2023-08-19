# Xử lý dữ liệu, xây dựng mô hình và dự đoán kết quả

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Đọc dữ liệu
data = pd.read_csv('credit_card.csv')

# Chuyển các kiểu giao dịch về dạng số
data["type"] = data["type"].map({"CASH_OUT": 1, "PAYMENT": 2,
                                 "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5})

# Chuyển các giá trị của cột "isFraud" về dạng chữ để tiện nhận biết
# "isFraud" cho biết giao dịch đó phải gian lận không
data["isFraud"] = data["isFraud"].map({0: "No Fraud", 1: "Fraud"})

# Chia dữ liệu ra tập huấn luyện và tập kiểm thử
X = np.array(data[["type", "amount", "oldbalanceOrg", "newbalanceOrig"]])
y = np.array(data[["isFraud"]])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=21)

# Huấn luyện mô hình
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Đánh giá mô hình
print("Đánh giá độ chính xác của mô hình: ", model.score(X_test, y_test))

# Sử dụng mô hình để dự đoán kết quả mới
new_transactions = np.array([[2, 21.00, 42.00, 21.00]])
print("Kết quả của giao dịch ['type': 'PAYMENT', 'amount': 21.00, 'oldbalanceOrg': 42.00, 'newbalanceOrig': 21.00]: ", model.predict(new_transactions))






