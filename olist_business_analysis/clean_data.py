#读取所有表
import pandas as pd
import os

raw_path = "/Users/apple/Desktop/olist_project/raw_data"
clean_path = "/Users/apple/Desktop/olist_project/clean_data"

#处理orders
orders = pd.read_csv(
    f"{raw_path}/olist_orders_dataset.csv"
)

date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

orders.to_csv(
    f"{clean_path}/orders_clean.csv",
    index=False
)

print("orders完成")

#处理products
products = pd.read_csv(
    f"{raw_path}/olist_products_dataset.csv"
)
##品类缺失
products["product_category_name"] = (
    products["product_category_name"]
    .fillna("unknown")
)
##数值字段
fill_cols = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty"
]

for col in fill_cols:

    products[col] = (
        products.groupby(
            "product_category_name"
        )[col]
        .transform(
            lambda x: x.fillna(
                x.median()
            )
        )
    )

    products[col] = (
        products[col]
        .fillna(
            products[col].median()
        )
    )
##保存
products.to_csv(
    f"{clean_path}/products_clean.csv",
    index=False
)

print("products完成")

#处理geolocation
geo = pd.read_csv(
    f"{raw_path}/olist_geolocation_dataset.csv"
)

geo = geo.drop_duplicates()

geo.to_csv(
    f"{clean_path}/geolocation_clean.csv",
    index=False
)

print("geo完成")

#其余表直接保存
import os
import pandas as pd

processed_files = [
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_geolocation_dataset.csv"
]

for file in os.listdir(raw_path):

    if file.endswith(".csv") and file not in processed_files:

        df = pd.read_csv(
            os.path.join(raw_path, file)
        )

        clean_name = (
            file
            .replace(".csv", "")
            .replace("olist_", "")
            + "_clean.csv"
        )

        df.to_csv(
            os.path.join(clean_path, clean_name),
            index=False
        )

        print(f"{clean_name} 保存完成")