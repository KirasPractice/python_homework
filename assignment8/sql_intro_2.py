import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = "SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price FROM line_items li JOIN products p ON li.product_id = p.product_id"
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())
    
    df['total'] = df['quantity'] * df['price']
    print(df.head())
    
    df_grouped = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    })
    print(df_grouped.head())
    
    df_grouped = df_grouped.sort_values('product_name')
    
    df_grouped.to_csv('order_summary.csv')
    print("Data wrote to order_summary.csv")