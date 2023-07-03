import sqlite3
import json
import uuid

conn = sqlite3.connect("database/details.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS buttons
                  (id TEXT PRIMARY KEY,
                   column INTEGER NOT NULL,
                   row INTEGER NOT NULL,
                   img_passive TEXT NOT NULL,
                   img_active TEXT NOT NULL,
                   command TEXT NOT NULL,
                   status INTEGER NOT NULL)''')

def addButtonDB(column, row, imgPassiveName, imgActiveName, commandInfo, status, id=None):
    if id == None:
        id = str(uuid.uuid4())

    # converting command from dict to json
    commandJson = json.dumps(commandInfo)
    cursor.execute("INSERT INTO buttons (id, column, row, img_passive, img_active, command, status) VALUES (?, ?, ?, ?, ?, ?, ?);", (id, column, row, imgPassiveName, imgActiveName, commandJson, status))
    conn.commit()

# this function used only if database is empty
def adddButtonsDB(buttons):
    for button in buttons:
        id = button
        info = button.grid_info()
        column = info['column']
        row = info['row']
        cursor.execute("INSERT INTO buttons (id, column, row) VALUES (?, ?, ?);", (str(id), column, row))
        conn.commit()

def saveChangesToDb(buttons):
    updateButtons(buttons)
    deleteButtonsNotInList(buttons)

def updateButtons(buttons):
    for button in buttons:
        id = button.id
        info = button.grid_info()
        column = info['column']
        row = info['row']

        cursor.execute('UPDATE buttons SET column=?, row=? WHERE id=? AND (column != ? OR row != ?)',
                    (column, row, id, column, row))

def deleteButtonsNotInList(buttons):
    buttonIds = fetchButtonIdsFromDb()
    for buttonId in buttonIds:
        if not any(button.id == buttonId for button in buttons):
            cursor.execute("DELETE FROM buttons WHERE id=?", (buttonId,))
    conn.commit()

def fetchButtonIdsFromDb():
    cursor.execute("SELECT id FROM buttons")
    return [row[0] for row in cursor.fetchall()]

# returns buttons info in json format
def getButtonsDB():
    cursor.execute('SELECT id, column, row, img_passive, img_active, command, status FROM buttons')
    rows = cursor.fetchall()
    data = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        data.append(d)

    jsonData = json.dumps(data)
    return jsonData