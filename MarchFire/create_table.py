import sqlite3

# Connect to the database
conn = sqlite3.connect('final.db')
c = conn.cursor()

# Drop the existing table
c.execute("DROP TABLE IF EXISTS fireExfixes")

# Create table
c.execute('''
    CREATE TABLE fireExfixes (
        fault_id INTEGER PRIMARY KEY AUTOINCREMENT,
        inspect TEXT,
        fault TEXT,
        remedy TEXT
    )
''')

# List of tuples, each tuple represents a row
data = [
    ('The extinguisher should be conspicuous, readily accessible and in its assigned location as per your fire safety plan. Check that the location sign is at the correct height and is visible', 'Accessibility Signage Inadequate', 'Install accessibility signage'), 
    ('Ensure that the anti-tamper device is intact and positioned to serve its purpose', 'Anti-tamper seal faulty', 'Install anti-tamper seal '), 
    ('Ensure that the extinguisher is clean and the operating instructions are legible', 'Exterior & instructions illegible', 'Replace fire extinguisher'), 
    ('Check that the maintenance record tag or label is securely attached by the required means and that the extinguisher has a unique means of identification.', 'Maintenance record label/tag missing', 'Replace missing maintenance record label/tag '), 
    ('Check that the exterior surface and all attachments are not damaged and free of corrosion and is not pitted.', 'External damage', 'Replace fire extinguisher'), 
    ('Ensure that the hose & nozzle attachment are securely fitted, is free from obstruction and has no sign of damage or deterioration.', 'Outlet hose assembly faulty', 'Replace fire extinguisher'), 
    ('If a pressure indicator is fitted ensure that it is legible, registering with in the operating range and is operating correctly.', 'Pressure indicator faulty', 'Replace fire extinguisher'), 
    ('Check that the support bracket is appropriate, securely attached to a suitable structure and the fire extinguisher is easily removed', 'Support bracket faulty', 'Install suitable support bracket '), 
    ('Weigh the extinguisher to determine that it is fully charged', 'Not fully charged', 'Replace fire extinguisher'), 
    ('Determine, where possible and without discharging any contents that the actuating device is free from damage and corrosion and moves freely.', 'Actuating device faulty', 'Replace fire extinguisher'),
    ('Invert the extinguisher and ensure that the powder remains free flowing','Powder not free flowing','Replace fire extinguisher'),
    ('Check that the extinguisher is not due for a hydrostatic test','Extinguisher due for hydrostatic test','Replace fire extinguisher'),
    ('Determine, hat the internal discharge tube and strainer (where fitted) provide clear passage and are securely attached. "water & foam only (gas container type)"','Internal Components faulty','Replace fire extinguisher')
]

# Insert rows
for row in data:
    c.execute("INSERT INTO fireExfixes (inspect, fault, remedy) VALUES (?, ?, ?)", row)

# Commit the changes and close the connection
conn.commit()
conn.close()