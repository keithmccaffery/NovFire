import sqlite3

# Connect to your SQLite database
# Replace 'final.db' with the path to your database file if necessary
conn = sqlite3.connect('final.db')

# Create a cursor object
c = conn.cursor()

# Execute the SQL command to add a column
c.execute("ALTER TABLE results ADD COLUMN image_url TEXT")

# Commit the changes and close the connection
conn.commit()
conn.close()