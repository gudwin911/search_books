import sqlite3
import xlsxwriter


def add_book_to_db(lst):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    try:
        c.execute('''create table items
        (id integer unique, name text, price real)''')
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("""insert into items values(?, ?, ?)""", lst)
    except sqlite3.IntegrityError:
        pass
    conn.commit()
    c.close()
    print("Book is added: %s" % lst)

shop = "lavka"


def create_bookshop_in_db(shop_name):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    try:
        c.execute('''create table %s
                (id integer unique, name text, price real)''' % shop_name)
    except sqlite3.OperationalError:
        pass
    conn.commit()
    c.close()


def print_data(table_name):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute('select * from %s order by id' % table_name)
    for row in c:
        print(row)


def add_book_to_db2(shop_name, lst):
    # all 3 columns for now
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    try:
        c.execute("insert into %s values(?, ?, ?)" % shop_name, (lst[0], lst[1], lst[2]))
    except sqlite3.IntegrityError:
        pass
    conn.commit()
    c.close()
    print("Book is added: %s" % lst)


def delete(shop_name, id):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("delete from %s where id = ?" % (shop_name), (id,))
    conn.commit()
    c.close()

# delete(shop)
# create_bookshop_in_db(shop)
# add_book_to_db2(shop, [6, "book6", 150])
print_data(shop)


def get_book_name_from_db(id):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("select name from lavka where id = ?", (id,))
    for name in c:
        return name
    c.close()


wb = xlsxwriter.Workbook("price_analysis.xlsx")
ws = wb.add_worksheet("prices")
ws.write("A1", str(get_book_name_from_db(1)))
wb.close()
