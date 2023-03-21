import sqlite3

db = sqlite3.connect('DB/farmBLG.sqlite')
sql = db.cursor()

def medication_check(name_medicine):
    request = """SELECT count_request FROM medicines WHERE name == (?)"""
    count_request = sql.execute(request, (name_medicine,)).fetchone()
    return add_new(name_medicine) if count_request is None else increase(name_medicine)

def add_new(name_medicine):
    try:
        medicine_id = sql.execute("SELECT MAX(medicine_id) FROM medicines").fetchone()[0] + 1
        sqlite_insert_query = """INSERT INTO medicines (medicine_id, name, count_request) VALUES (?, ?, ?);"""
        data = (medicine_id, name_medicine, 1)
        sql.execute(sqlite_insert_query, data)
        db.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def increase(name_medicine):
    try:
        data = sql.execute("SELECT * FROM medicines WHERE name == (?)", (name_medicine, )).fetchone()
        sqlite_insert_query = """UPDATE medicines SET count_request = ? WHERE medicine_id = ?;"""
        sql.execute(sqlite_insert_query, (data[2] + 1, data[0],))
        db.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
