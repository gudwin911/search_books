import sqlite3

a = "Хрома"
b = "Как жить вместе: романические симуляции некоторых пространств повседневности"
print(a == b)
print(b in a)
print(a in b)
print(b.split())


def test_():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # c.execute('''CREATE TABLE stocks
    #              (date text, trans text, symbol text, qty real, price real)''')
    # purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
    #              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
    #              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
    #             ]
    # c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
    conn.commit()
    conn.close()


def delete(price):
    conn = sqlite3.connect("example.db")
    c = conn.cursor()
    c.execute("delete from stocks where price = ?", (price,))
    conn.commit()
    c.close()

# delete()
# test_()

a = (1,)
print(a)
b = [2]
print(a)
print(b)