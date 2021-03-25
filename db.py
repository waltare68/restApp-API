import sqlite3

conn = sqlite3.connect("database.db")

print("opened database successfully")

conn.execute("CREATE TABLE students(name TEXT, branch TEXT, college TEXT,batch TEXT,program TEXT, course TEXT, firstLanguage TEXT )")
print("table created successfully")

conn.close()