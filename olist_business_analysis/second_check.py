#表间关联一致性检验
import pandas as pd

orders = pd.read_csv(
"/Users/apple/Desktop/archive/olist_orders_dataset.csv"
)

items = pd.read_csv(
"/Users/apple/Desktop/archive/olist_order_items_dataset.csv"
)

orphan_orders = items[
    ~items["order_id"].isin(
        orders["order_id"]
    )
]

print(
    "孤儿订单记录数:",
    len(orphan_orders)
)

payments = pd.read_csv(
"/Users/apple/Desktop/archive/olist_order_payments_dataset.csv"
)

orphan_payment = payments[
    ~payments["order_id"].isin(
        orders["order_id"]
    )
]

print(
    "支付表孤儿记录:",
    len(orphan_payment)
)

reviews = pd.read_csv(
"/Users/apple/Desktop/archive/olist_order_reviews_dataset.csv"
)

orphan_reviews = reviews[
    ~reviews["order_id"].isin(
        orders["order_id"]
    )
]

print(
    "评价表孤儿记录:",
    len(orphan_reviews)
)

customers = pd.read_csv(
"/Users/apple/Desktop/archive/olist_customers_dataset.csv"
)

orphan_customer = orders[
    ~orders["customer_id"].isin(
        customers["customer_id"]
    )
]

print(
    "客户孤儿记录:",
    len(orphan_customer)
)

products = pd.read_csv(
"/Users/apple/Desktop/archive/olist_products_dataset.csv"
)

orphan_product = items[
    ~items["product_id"].isin(
        products["product_id"]
    )
]

print(
    "商品孤儿记录:",
    len(orphan_product)
)

sellers = pd.read_csv(
"/Users/apple/Desktop/archive/olist_sellers_dataset.csv"
)

orphan_seller = items[
    ~items["seller_id"].isin(
        sellers["seller_id"]
    )
]

print(
    "商家孤儿记录:",
    len(orphan_seller)
)

#字段值域合法性检验
print(
    reviews["review_score"]
    .value_counts()
    .sort_index()
)
print(
    reviews[
        ~reviews["review_score"]
        .isin([1,2,3,4,5])
    ]
)

print(
    payments["payment_type"]
    .unique()
)

print(
    items["price"]
    .describe()
)

print(
    items["freight_value"]
    .describe()
)
print(
    (items["freight_value"] < 0)
    .sum()
)

cols = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for col in cols:

    print(
        col,
        (products[col] <= 0).sum()
    )
abnormal_weight = products[
    products["product_weight_g"] <= 0
]

print(abnormal_weight[
    [
        "product_id",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]
])
print(
    abnormal_weight[
        [
            "product_id",
            "product_weight_g"
        ]
    ]
)