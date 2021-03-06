import sqlite3

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# import openfoodfacts

connection = sqlite3.connect('pantry.db')

def setup_database():
    # Product table create statement
    product_query = '''CREATE TABLE IF NOT EXISTS products (
                        barcode TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        unit TEXT NOT NULL
                    );'''
    # Stock table create statement
    stock_query = '''CREATE TABLE IF NOT EXISTS stock (
                        barcode TEXT PRIMARY KEY,
                        quantity REAL,
                        FOREIGN  KEY (barcode)
                            REFERENCES products (barcode)
                    );'''

    # Create tables products and stock
    connection.execute(product_query)
    connection.execute(stock_query)

def decode_image(file):
    image = cv2.imread(file)
    decode_obj = pyzbar.decode(image)

    if not decode_obj:
        return None
   
    print(str(decode_obj[0].data))
    return str(decode_obj[0].data)

def get_stock():
    select_query = ''' SELECT stock.barcode, name, unit, quantity
                       FROM stock
                       LEFT JOIN products
                       ON stock.barcode = products.barcode
                   '''

    cursor = connection.cursor()
    cursor.execute(select_query)

    return cursor.fetchall()

def add_product_to_database(product):
    insert_query = '''INSERT INTO products (barcode, name, unit)
                      VALUES (?, ?, ?)
                   '''

    cursor = connection.cursor()
    cursor.execute(insert_query, (product['barcode'], product['name'], product['unit']))
    connection.commit()

def get_product(barcode):
    product = {}
    select_query = ''' SELECT products.barcode, name, unit, quantity
                       FROM products
                       LEFT JOIN stock
                       ON products.barcode = stock.barcode
                       WHERE products.barcode=?
                   '''
    cursor = connection.cursor()
    cursor.execute(select_query, (barcode,))
    result = cursor.fetchone()

    print(barcode)

    if result is None:
        result = openfoodfacts.products.get_product(barcode)
        print(result)
        result = result.get('product')
        quantity = result.get('quantity')

        product['barcode'] = barcode
        product['name'] = result.get('product_name')
        qty_split = quantity.split()
        if len(qty_split) > 2:
            product['unit'] = qty_split[1].upper()
        else:
            product['unit'] = ''
        product['quantity'] = 0 # (quantity.split())[0]
        add_product_to_database(product)

    else:
        print(result[3])
        product['barcode'] = result[0]
        product['name'] = result[1]
        product['unit'] = result[2]
        if result[3] is None:
            product['quantity'] = 0
        else:
            product['quantity'] = result[3]

    return product

def insert_stock(product):
    create_query = '''INSERT INTO stock (barcode, quantity)
                      VALUES (?, ?)
                   '''

    cursor = connection.cursor()
    cursor.execute(create_query, (product['barcode'], product['quantity']))
    connection.commit()


def update_stock_table(product):
    update_query = '''UPDATE stock
                      SET quantity = ?
                      WHERE barcode = ?
                   '''

    cursor = connection.cursor()
    cursor.execute(update_query, (product['quantity'], product['barcode']))
    connection.commit()

def delete_from_stock(product):
    delete_query = '''DELETE FROM stock
                      WHERE stock.barcode = ?
                   '''

    cursor = connection.cursor()
    cursor.execute(delete_query, (product['barcode'],))
    connection.commit()

def get_product_from_stock(barcode):
    select_query = '''SELECT *
                      FROM stock
                      WHERE barcode=?
                   '''

    cursor = connection.cursor()
    cursor.execute(select_query, (barcode,))

    return cursor.fetchone()

def update_stock(product, quantity):
    product['quantity'] = quantity
    if product['quantity'] == 0:
        # The given product has been used and it's no longer avaliable
        delete_from_stock(product)
        return

    result = get_product_from_stock(product['barcode'])
    if result is None:
        # A product has been added to the stock
        insert_stock(product)
    else:
        # More has been added or used
        update_stock_table(product)
