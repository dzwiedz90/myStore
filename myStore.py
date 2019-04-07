import tkinter
import databaseActions



#Creates new objects with program windows
class Create_Window(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master.title("myStore")
        self.master.geometry("315x200")
        self.master.resizable(0, 0)

        #Creates window with list of products
        products_window = lambda: Create_Window.products_window(self)
        products_button = tkinter.Button(master, text = "Lista produktów", command = products_window, width=15, height=2).place(x = 25, y = 25)

        #Creates window with list of orders
        orders_window = lambda: Create_Window.orders_window(self)
        orders_button = tkinter.Button(master, text = "Lista zamówień", command = orders_window, width=15, height=2).place(x = 175, y = 25)

        # Creates window for adding products to database
        adding_window = lambda: Create_Window.edit_product(self)
        adding_button = tkinter.Button(master, text="Edycja produktów", command=adding_window, width=20, height=2).place(
            x=80, y=85)


    def products_window(self, event=None):
        #Create new window
        new_window = tkinter.Toplevel(self)
        new_window.title("Lista produktów")
        new_window.geometry("815x300")
        new_window.resizable(0, 0)

        def create_window():
            global new_products
            new_products = tkinter.Frame(new_window)
            new_products.pack()

        create_window()

        def refresh_products():
            new_products.destroy()
            create_window()
            fill_products_data()

        # Print labels in window
        def fill_products_data():
            # Download data from database
            data = databaseActions.read_products()

            id_label = tkinter.Label(new_products, text="id", pady=7, bg="white", relief="groove", width=10)
            id_label.grid(row=0, column=0)
            product_name_label = tkinter.Label(new_products, text="Nazwa produktu", pady=7, bg="white", relief="groove",
                                               width=45)
            product_name_label.grid(row=0, column=1)
            price_label = tkinter.Label(new_products, text="Cena", pady=7, bg="white", relief="groove", width=20)
            price_label.grid(row=0, column=2)
            in_magazine_label = tkinter.Label(new_products, text="W magazynie", pady=7, bg="white", relief="groove",
                                              width=15)
            in_magazine_label.grid(row=0, column=3)
            tkinter.Button(new_products, text="Odśwież", command=refresh_products, width=20, height=2).grid(row=0,
                                                                                                            column=4)

            row = 1
            x = 0
            column = 0
            y = 0
            for i in range(len(data)):
                for a in range(4):

                    id_text = tkinter.Label(new_products, text=data[x][y], pady=7)
                    id_text.grid(row=row, column=column)

                    product_text = tkinter.Label(new_products, text=data[x][y], pady=7)
                    product_text.grid(row=row, column=column)

                    price_text = tkinter.Label(new_products, text=data[x][y], pady=7)
                    price_text.grid(row=row, column=column)

                    in_text = tkinter.Label(new_products, text=data[x][y], pady=7)
                    in_text.grid(row=row, column=column)
                    if y == 3:
                        y = 0
                    else:
                        y += 1

                    if column == 3:
                        column = 0
                    else:
                        column += 1

                row += 1
                x += 1

        fill_products_data()


    def orders_window(self, event=None):
        def create_window():
            global new_orders
            new_orders = tkinter.Toplevel(self)
            new_orders.title("Lista zamówień")
            new_orders.geometry("1210x300")
            new_orders.resizable(0, 0)

        create_window()

        def refresh_orders():
            new_orders.destroy()
            create_window()
            fill_orders_data()

        def fill_orders_data():
            # Download data from database
            data = databaseActions.read_orders()

            id_label = tkinter.Label(new_orders, text="id", pady=7, bg="white", relief="groove", width=7)
            id_label.grid(row=0, column=0)
            name_label = tkinter.Label(new_orders, text="Imię", pady=7, bg="white", relief="groove", width=17)
            name_label.grid(row=0, column=1)
            surname_label = tkinter.Label(new_orders, text="Nazwisko", pady=7, bg="white", relief="groove", width=20)
            surname_label.grid(row=0, column=2)
            city_label = tkinter.Label(new_orders, text="Miasto", pady=7, bg="white", relief="groove", width=20)
            city_label.grid(row=0, column=3)
            postcode_label = tkinter.Label(new_orders, text="Kod pocztowy", pady=7, bg="white", relief="groove", width=10)
            postcode_label.grid(row=0, column=4)
            street_label = tkinter.Label(new_orders, text="Ulica i nr domu", pady=7, bg="white", relief="groove", width=30)
            street_label.grid(row=0, column=5)
            product_label = tkinter.Label(new_orders, text="Produkt", pady=7, bg="white", relief="groove", width=25)
            product_label.grid(row=0, column=6)
            price_label = tkinter.Label(new_orders, text="Cena", pady=7, bg="white", relief="groove", width=15)
            price_label.grid(row=0, column=7)
            tkinter.Button(new_orders, text="Odśwież", command=refresh_orders, width=20, height=2).grid(row=0, column=8)


            # Print labels in window
            row = 1
            x = 0
            column = 0
            y = 0
            for i in range(len(data)):
                for a in range(8):


                    id_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    id_text.grid(row=row, column=column)

                    name_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    name_text.grid(row=row, column=column)

                    surname_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    surname_text.grid(row=row, column=column)

                    city_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    city_text.grid(row=row, column=column)

                    postcode_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    postcode_text.grid(row=row, column=column)

                    street_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    street_text.grid(row=row, column=column)

                    product_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    product_text.grid(row=row, column=column)

                    price_text = tkinter.Label(new_orders, text=data[x][y], pady=7)
                    price_text.grid(row=row, column=column)
                    if y == 7:
                        y = 0
                    else:
                        y += 1

                    if column == 7:
                        column = 0
                    else:
                        column += 1

                row += 1
                x += 1

        fill_orders_data()


    def edit_product(self, event=None):
        # Create new window
        new = tkinter.Toplevel(self)
        new.title("Edycja produktów")
        new.geometry("1000x300")
        new.resizable(0, 0)

        #Adding new product
        tkinter.Label(new, text="Dodawanie nowego produktu").grid(row=0, pady = 7, sticky="W")
        tkinter.Label(new, text="Nazwa produktu").grid(row=1, pady = 7, sticky="W")
        tkinter.Label(new, text="Cena").grid(row=2, pady = 7, sticky="W")
        tkinter.Label(new, text="Ilość").grid(row=3, pady = 7, sticky="W")

        product_name_entry = tkinter.Entry(new)
        price_entry = tkinter.Entry(new)
        in_magazine_entry = tkinter.Entry(new)

        product_name_entry.grid(row=1, column=1, pady = 7)
        price_entry.grid(row=2, column=1, pady = 7)
        in_magazine_entry.grid(row=3, column=1, pady = 7)


        def add_new():
            product_name = str(product_name_entry.get())
            price = str(price_entry.get())
            in_magazine = str(in_magazine_entry.get())

            databaseActions.add_products(product_name, price, in_magazine)

            product_name_entry.delete(0, tkinter.END)
            price_entry.delete(0, tkinter.END)
            in_magazine_entry.delete(0, tkinter.END)

        tkinter.Button(new, text = "Zapisz", command = add_new).grid(row = 5, column = 1, sticky = "W", pady = 7)


        #Editing existing product
        tkinter.Label(new, text="Edycja istniejącego produktu").grid(row=0, column = 4, pady=7, sticky="W", ipadx = 20)
        tkinter.Label(new, text="id produktu").grid(row=1, column = 4, pady=7, sticky="W", ipadx = 20)
        tkinter.Label(new, text="Nazwa produktu").grid(row=2, column = 4, pady=7, sticky="W", ipadx = 20)
        tkinter.Label(new, text="Cena").grid(row=3, column = 4, pady=7, sticky="W", ipadx = 20)
        tkinter.Label(new, text="Ilość").grid(row=4, column = 4, pady=7, sticky="W", ipadx = 20)

        id_edit_entry = tkinter.Entry(new)
        product_edit_entry = tkinter.Entry(new)
        price_edit_entry = tkinter.Entry(new)
        in_magazine_edit_entry = tkinter.Entry(new)

        id_edit_entry.grid(row=1, column=5, pady=7)
        product_edit_entry.grid(row=2, column=5, pady=7)
        price_edit_entry.grid(row=3, column=5, pady=7)
        in_magazine_edit_entry.grid(row=4, column=5, pady=7)

        def edit_existing():
            id_edit_name = int(id_edit_entry.get())
            product_edit_name = str(product_edit_entry.get())
            price_edit = str(price_edit_entry.get())
            in_magazine_edit = str(in_magazine_edit_entry.get())

            databaseActions.edit_existing(id_edit_name, product_edit_name, price_edit, in_magazine_edit)

            id_edit_entry.delete(0, tkinter.END)
            product_edit_entry.delete(0, tkinter.END)
            price_edit_entry.delete(0, tkinter.END)
            in_magazine_edit_entry.delete(0, tkinter.END)

        tkinter.Button(new, text = "Zapisz", command = edit_existing).grid(row = 5, column = 5, sticky = "W", pady = 7)

        #Deleting existing product
        tkinter.Label(new, text="Usuwanie istniejącego produktu").grid(row=0, column=7, pady=7, sticky="W", ipadx=20)
        tkinter.Label(new, text="id produktu").grid(row=1, column=7, pady=7, sticky="W", ipadx=20)

        id_delete_entry = tkinter.Entry(new)

        id_delete_entry.grid(row=1, column=8, pady=7)

        def delete_existing():
            id_delete_name = int(id_delete_entry.get())

            databaseActions.delete_existing(id_delete_name)

            id_delete_entry.delete(0, tkinter.END)

        tkinter.Button(new, text="Zapisz", command=delete_existing).grid(row=5, column=8, sticky="W", pady=7)


app = Create_Window()
app.grid()

app.mainloop()