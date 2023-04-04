import sqlite3
import json
conn = sqlite3.connect("database/details.db")
cursor = conn.cursor()


cursor.execute(
    """ CREATE TABLE IF NOT EXISTS buttons(id text PRIMARY KEY, column int NOT NULL, row int NOT NULL); """)

# this function used only if database is empty
def adddButtonsDB(buttons):
    for button in buttons:
        id = button
        info = button.grid_info()
        column = info['column']
        row = info['row']
        cursor.execute("INSERT INTO buttons (id, column, row) VALUES (?, ?, ?);", (str(id), column, row))
        conn.commit()


def saveChagnesDB(buttons):
    for button in buttons:
        id = str(button)
        info = button.grid_info()
        column = info['column']
        row = info['row']
        cursor.execute('UPDATE buttons SET column=?, row=? WHERE id=? AND (column != ? OR row != ?)',
                    (column, row, id, column, row))
    conn.commit()

# returns buttons info in json format
def getButtonsDB():
    cursor.execute('SELECT id, column, row FROM buttons')
    rows = cursor.fetchall()
    data = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        data.append(d)

    jsonData = json.dumps(data)
    return jsonData
