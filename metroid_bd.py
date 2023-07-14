import sqlite3

con = sqlite3.connect('metroid')
cur = con.cursor()

def criar():
    sql = '''
    CREATE TABLE Metroid(Titulo text, Diretor text, Ano_de_Lancamento text, Console text)
    '''
    cur.execute(sql)

    con.commit()

def gravar():
    sql = 'INSERT INTO Metroid VALUES("Metroid", "Yoshio Sakamoto", "08/15/1987", "NES")'

    cur.execute(sql)

    con.commit()


def gravar_multi():
    sql = [
         ("Metroid II: Return of Samus", "Hiroji Kiyotake", "11/21/1991", "Gameboy"),
         ("Super Metroid", "Yoshio Sakamoto", "03/19/1994", "Super Nintendo"),
         ("Metroid Zero Mission", "Yoshio Sakamoto", "02/09/2004", "Gameboy Advance"),
         ("Metroid Fusion", "Yoshio Sakamoto", "11/18/2002", "Gameboy Advance"),
         ("Metroid Other M", "Yoshio Sakamoto", "08/31/2010", "Nintendo Wii"),
         ("Metroid Samus Return", "Yoshio Sakamoto", "09/15/2017", "Nintendo 3ds"),
         ("Metroid Dread", "Yoshio Sakamoto", "10/08/2021", "Nintendo Switch")
        ]

    cur.executemany('INSERT INTO Metroid VALUES(?, ?, ?, ?)', sql)

    con.commit()
