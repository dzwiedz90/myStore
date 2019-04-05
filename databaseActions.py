import sqlite3



# Definition that create database and place data into tables
def create_database():
    #connection with database
    conn = sqlite3.connect('bear.db')


    #create tables
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS clients;")
    cur.execute("""
		CREATE TABLE IF NOT EXISTS clients (
		    id INTEGER PRIMARY KEY ASC,
			name varchar(250) NOT NULL,
			surname varchar(250) NOT NULL,
			city varchar(250) NOT NULL,
			post_code varchar(250) NOT NULL,
			street_home_number varchar(250) NOT NULL,
			pesel BIGINT NOT NULL
		)""")
    cur.execute("DROP TABLE IF EXISTS products;")
    cur.execute("""
		CREATE TABLE IF NOT EXISTS products (
			id INTEGER PRIMARY KEY ASC,
			product_name varchar(250) NOT NULL,
			price varchar(250) NOT NULL,
			in_magazine varchar(250) NOT NULL
		)""")
    cur.execute("DROP TABLE IF EXISTS orders;")
    cur.execute("""
    		CREATE TABLE IF NOT EXISTS orders (
    			id INTEGER PRIMARY KEY ASC,
    			client_id INTEGER NOT NULL,
    			product_id INTEGER NOT NULL,
    			FOREIGN KEY(client_id) REFERENCES clients(id)
    			FOREIGN KEY(product_id) REFERENCES products(id)
    		)""")


    #tuple containing data about products
    clients_data = (
        (None, 'Tomasz', 'Nowak', 'Poznań', '60-320', 'Bukowska 1/2', '53515564843'),
        (None, 'Alfred', 'Szymczak', 'Gorzów Wlkp.', '66-400', 'Stilonowa 13/8', '74300625537'),
        (None, 'Jan', 'Kowalski', 'Warszawa', '01-020', 'Marszałowska 121/12', '38300020761')
    )

    #insert into table clients
    cur.executemany('INSERT INTO clients VALUES(?, ?, ?, ?, ?, ?, ?);', clients_data)


    #tuple containing data about products
    products_data = (
        (None, 'Komputer', '2099.99', '2'),
        (None, 'Kabel HDMI', '49.99', '8'),
        (None, 'Monitor Full HD', '599.99', '4'),
        (None, 'Klawiatura Logitech', '99.99', '2'),
        (None, 'Trackball', '156.99', '1'),
        (None, 'Gra', '89.99', '7')
    )

    #insert into table products
    cur.executemany('INSERT INTO products VALUES(?,?,?,?)', products_data)


    #tuple containing data about orders
    orders_data = (
        (None, '1', '1'),
        (None, '1', '2'),
        (None, '1', '3'),
        (None, '2', '4'),
        (None, '3', '1'),
    )

    #insert into table orders
    cur.executemany('INSERT INTO orders VALUES(?,?,?)', orders_data)

    #commit data to database
    conn.commit()
    conn.close()

#Function to read data from products table
def read_products():
    #connection with database
    conn = sqlite3.connect('bear.db')

    #select data from table
    cur = conn.cursor()
    cur.execute("SELECT * from products;")

    products_data = cur.fetchall()
    '''
    for x in products_data:
        print('\n')
        print('id: ', x[0], )
        print('product_name: ', x[1], )
        print('price: ', x[2], )
        print('in_magazine: ', x[3], )
    '''
    conn.close()
    return products_data


#Function to read data from orders table
def read_orders():
    #connection with database
    conn = sqlite3.connect('bear.db')

    # select data from table
    cur = conn.cursor()
    cur.execute("SELECT orders.id, clients.name, clients.surname, clients.city, clients.post_code, clients.street_home_number, products.product_name, products.price from orders INNER JOIN clients ON orders.client_id = clients.id INNER JOIN products ON orders.product_id = products.id;")

    orders_data = cur.fetchall()
    '''
    for x in orders_data:
        print('\n')
        print('id_zamówienia: ', x[0], )
        print('Imię: ', x[1], )
        print('Nazwisko: ', x[2], )
        print('Miasto: ', x[3], )
        print('Kod pocztowy: ', x[4], )
        print('Ulica i nr domu: ', x[5], )
        print('Nazwa produktu: ', x[6], )
        print('Cena: ', x[7], )
    '''
    conn.close()
    return orders_data


#Fucntion thanks to which user can add products to table products.
def add_products(name, price, quantity):
    # connection with database
    conn = sqlite3.connect('bear.db')

    name = str(name)
    price = str(price)
    quantity = str(quantity)

    cur = conn.cursor()

    # tuple containing data about products
    products_data = [
        (None, name, price, quantity)
    ]

    # insert into table products
    cur.executemany('INSERT INTO products VALUES(?,?,?,?)', products_data)

    # commit data to database
    conn.commit()
    conn.close()


def edit_existing(id, name, price, quantity):
    # connection with database
    conn = sqlite3.connect('bear.db')

    id = int(id)
    name = str(name)
    price = str(price)
    quantity = str(quantity)

    products_data = [(name, price, quantity, id)]

    cur = conn.cursor()

    # insert into table products
    cur.executemany("""UPDATE products SET product_name = ?, price = ?, in_magazine = ? WHERE id = ?""", products_data)

    # commit data to database
    conn.commit()
    conn.close()


def delete_existing(id):
    # connection with database
    conn = sqlite3.connect('bear.db')

    id = int(id)

    products_data = [(id)]

    cur = conn.cursor()

    # insert into table products
    cur.execute('DELETE FROM products WHERE id = ?', products_data)

    # commit data to database
    conn.commit()
    conn.close()

create_database()
