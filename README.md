## **PHÁT HIỆN GIAN LẬN TRONG CÁC GIAO DỊCH TRỰC TUYẾN**

## 1. Mô tả dữ liệu

#### Tải dữ liệu: https://www.kaggle.com/datasets/ealaxi/paysim1

#### Hiển thị 5 dòng đầu của dữ liệu:
![image](https://github.com/akaichi21/OnlinePaymentsFraud/assets/69575272/5a4b39a2-a19d-4d1b-b9d5-e0625336f23b)

#### Các cột dữ liệu:
- **step: đại diện cho một đơn với thời gian (1 step = 1 giờ)**
- **type: kiểu giao dịch trực tuyến**
- **amount: số lượng được giao dịch**
- **nameOrig: tên người bắt đầu giao dịch**
- **oldbalanceOrg: số dư trước giao dịch**
- **newbalanceOrig: số dư sau giao dịch**
- **nameDest: tên người nhận giao dịch**
- **oldbalanceDest: số dư ban đầu của người nhận trước giao dịch**
- **newbalanceDest: số dư mới của người nhận sau giao dịch**
- **isFraud: kiểm tra giao dịch có gian lận hay không gian lận**

#### Các kiểu giao dịch được đề cập trong dữ liệu:
![image](https://github.com/akaichi21/OnlinePaymentsFraud/assets/69575272/54356636-bf1c-46bf-b90d-d8dc3dfcafae)

**CASH_OUT: rút tiền**
**PAYMENT: thanh toán**
**CASH_IN: gửi tiền**
**TRANFER: chuyển tiền**
**DEBIT: ghi nợ**

#### Biểu đồ thể hiện sự phân bố của các loại giao dịch:
![image](https://github.com/akaichi21/OnlinePaymentsFraud/assets/69575272/490543cd-810e-4891-b4ba-886f54e0cea9)

## 2. Xây dựng mô hình

