import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('final.db')
c = conn.cursor()

# Drop the existing users_old table if it exists
c.execute("DROP TABLE IF EXISTS users_old")

# Step 1: Rename the existing table
c.execute("ALTER TABLE users RENAME TO users_old")

# Step 2: Create a new table with the correct schema, allowing NULL values for the hash column temporarily
c.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    hash TEXT
)
""")

# Step 3: Copy the data from the old table to the new table
c.execute("""
INSERT INTO users (id, username)
SELECT id, username
FROM users_old
""")

# Step 4: Drop the old table
c.execute("DROP TABLE users_old")

# Step 5: Update the schema to enforce the NOT NULL constraint on the hash column
c.execute("""
CREATE TABLE users_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    hash TEXT NOT NULL
)
""")

c.execute("""
INSERT INTO users_new (id, username, hash)
SELECT id, username, hash
FROM users
""")

c.execute("DROP TABLE users")
c.execute("ALTER TABLE users_new RENAME TO users")

# Commit the changes and close the connection
conn.commit()
conn.close()