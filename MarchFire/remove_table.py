import sqlite3

# Connect to the database
conn = sqlite3.connect('final.db')
c = conn.cursor()

# Drop the old table
c.execute("DROP TABLE IF EXISTS emglightfixes")

# Commit the changes and close the connection
conn.commit()
conn.close()