import sqlite3

# Connect to the database
conn = sqlite3.connect('final.db')
c = conn.cursor()

# Create a new table with the desired structure
c.execute('''
    CREATE TABLE new_results (
        user_id INTEGER,
        asset TEXT,
        fault_id INTEGER,
        fault TEXT,
        remedy TEXT,
        comment TEXT,
        image_url TEXT
    )
''')

# Copy the data from the old table to the new one
c.execute('''
    INSERT INTO new_results (user_id, asset, fault_id, fault, remedy, comment, image_url)
    SELECT user_id, door, fault_id, fault, remedy, comment, image_url FROM results
''')

# Delete the old table
c.execute("DROP TABLE results")

# Rename the new table to the old table's name
c.execute("ALTER TABLE new_results RENAME TO results")

# Commit the changes and close the connection
conn.commit()
conn.close()