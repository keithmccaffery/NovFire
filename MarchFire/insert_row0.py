import sqlite3

# Connect to the database
conn = sqlite3.connect('final.db')
c = conn.cursor()

# Insert a row with fault_id 0
c.execute("INSERT INTO fireExfixes (fault_id, inspect, fault, remedy) VALUES (?, ?, ?, ?)", (0, 'Fire extinguisher sound but want record status and image', 'No fault', 'No action required'))

# Commit the changes and close the connection
conn.commit()
conn.close()