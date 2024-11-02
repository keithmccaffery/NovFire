import sqlite3

# Connect to the database
conn = sqlite3.connect('final.db')
c = conn.cursor()

# Add a timestamp column
c.execute("ALTER TABLE results ADD COLUMN timestamp DATETIME")

# Commit the changes and close the connection
conn.commit()
conn.close()