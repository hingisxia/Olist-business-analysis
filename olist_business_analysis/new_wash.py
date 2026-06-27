#缺失值检查
import pandas as pd
import os

path = "/Users/apple/Desktop/archive"

for file in os.listdir(path):

    if file.endswith(".csv"):

        df = pd.read_csv(f"{path}/{file}")

        print("\n")
        print("="*50)
        print(file)

        missing = df.isnull().sum()

        missing_pct = (
            missing / len(df) * 100
        ).round(2)

        result = pd.concat(
            [missing, missing_pct],
            axis=1
        )

        result.columns = [
            "missing_count",
            "missing_pct"
        ]

        print(
            result[result["missing_count"] > 0]
        )

#重复值检查
import pandas as pd
import os

path = "/Users/apple/Desktop/archive"

for file in os.listdir(path):

    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(path,file))

        dup = df.duplicated().sum()

        print(file, "重复记录数:", dup)

# 订单状态检查

orders = pd.read_csv(
    "/Users/apple/Desktop/archive/olist_orders_dataset.csv"
)

print(
    orders["order_status"].value_counts()
)

print("\n缺失值数量：")
print(
    orders["order_status"].isnull().sum()
)

# 时间字段转换

date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(
        orders[col]
    )

print("时间字段转换完成")

#检查审核时间早于购买时间
abnormal1 = orders[
    orders["order_approved_at"]
    < orders["order_purchase_timestamp"]
]

print(
    "审核时间异常:",
    len(abnormal1)
)

#检查发货时间早于审核时间
abnormal2 = orders[
    orders["order_delivered_carrier_date"]
    < orders["order_approved_at"]
]

print(
    "发货时间异常:",
    len(abnormal2)
)

#检查签收时间早于发货时间
abnormal3 = orders[
    orders["order_delivered_customer_date"]
    < orders["order_delivered_carrier_date"]
]

print(
    "签收时间异常:",
    len(abnormal3)
)

print(
    abnormal2["order_status"]
    .value_counts()
)

print(
    abnormal3["order_status"]
    .value_counts()
)

#金额字段检查
items = pd.read_csv(
    "/Users/apple/Desktop/archive/olist_order_items_dataset.csv"
)

payments = pd.read_csv(
    "/Users/apple/Desktop/archive/olist_order_payments_dataset.csv"
)

print("价格负值:",
      (items["price"] < 0).sum())

print("运费负值:",
      (items["freight_value"] < 0).sum())

print("支付金额负值:",
      (payments["payment_value"] < 0).sum())

print("\n价格分布")
print(items["price"].describe())

print("\n支付金额分布")
print(payments["payment_value"].describe())

#检查支付金额为0的订单
payments[
    payments["payment_value"] == 0
]
print(
    len(
        payments[
            payments["payment_value"] == 0
        ]
    )
)
