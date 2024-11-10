import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('final.db')
c = conn.cursor()

# Backup the database (optional, but recommended)
conn.execute("VACUUM INTO 'backup_final.db'")

# Delete all data from the users, results, and images tables
c.execute("DELETE FROM users")
c.execute("DELETE FROM results")
c.execute("DELETE FROM images")

# Reset the auto-increment counters for the tables
c.execute("DELETE FROM sqlite_sequence WHERE name='users'")
c.execute("DELETE FROM sqlite_sequence WHERE name='results'")
c.execute("DELETE FROM sqlite_sequence WHERE name='images'")

# Commit the changes and close the connection
conn.commit()
conn.close()