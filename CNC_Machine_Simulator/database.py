import sqlite3

def save_simulation_data(inputs, tool_path):
    conn = sqlite3.connect('simulations.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS simulations
                      (id INTEGER PRIMARY KEY, inputs TEXT, tool_path TEXT)''')
    cursor.execute("INSERT INTO simulations (inputs, tool_path) VALUES (?, ?)",
                   (str(inputs), str(tool_path)))
    conn.commit()
    conn.close()
