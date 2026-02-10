import sqlite3

def run_app():
    conn = sqlite3.connect('users_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS people 
                      (id INTEGER PRIMARY KEY, name TEXT, city TEXT)''')

    user_data = [('Arjun', 'Mumbai'), 
                 ('Priya', 'Delhi'), 
                 ('Ishaan', 'Bangalore')]
    
    cursor.executemany("INSERT INTO people (name, city) VALUES (?, ?)", user_data)
    conn.commit()
    cursor.execute("UPDATE people SET city = ? WHERE name = ?", ('Chennai', 'Ishaan'))
    cursor.execute("DELETE FROM people WHERE name = ?", ('Priya',))
    conn.commit()
    cursor.execute("SELECT * FROM people")
    rows = cursor.fetchall()

    print(f"{'ID':<5} {'Name':<20} {'City':<15}")
    print("-" * 40)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15}")

    conn.close()

if __name__ == "__main__":
    run_app()