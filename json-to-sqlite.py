import json
import sqlite3

with open('activities.json') as f:
    data = json.load(f)

# print(json.dumps(data, indent=4, sort_keys=True))

conn = sqlite3.connect('helpdeskdb.db')
c = conn.cursor()
# Create table

# c.execute('''DROP TABLE IF EXISTS note''')
# c.execute('''CREATE TABLE note
#              (performed_at text, ticket_id text, performer_type text, performer_id real, id real, type text)''')

c.execute('''DROP TABLE IF EXISTS activity''')
c.execute('''CREATE TABLE activity
             (performed_at text, ticket_id real, performer_type text, 
             performer_id real, shipping_address text, shipment_date text, 
             category text, contacted_customer real, issue_type text,
             source real, status text, priority real, t_group text, 
             agent_id real, requester real, product text)''')


values_to_insert = ''
for i in range(data['metadata']['activities_count']):
    values_to_insert += ('(\'' + data['activities_data'][i]['performed_at'] + '\',' +
                         str(data['activities_data'][i]['ticket_id']) + ',' +
                         '\'' + data['activities_data'][i]['performer_type'] + '\',' +
                         str(data['activities_data'][i]['performer_id']) + ',' +
                         '\'' + data['activities_data'][i]['activity']['shipping_address'] + '\',' +
                         '\'' + data['activities_data'][i]['activity']['shipment_date'] + '\',' +
                         '\'' + data['activities_data'][i]['activity']['category'] + '\',' +
                         str(data['activities_data'][i]['activity']['contacted_customer']) + ',' +
                         '\'' + data['activities_data'][i]['activity']['issue_type'] + '\',' +
                         str(data['activities_data'][i]['activity']['source']) + ',' +
                         '\'' + data['activities_data'][i]['activity']['status'] + '\',' +
                         str(data['activities_data'][i]['activity']['priority']) + ',' +
                         '\'' + data['activities_data'][i]['activity']['group'] + '\',' +
                         str(data['activities_data'][i]['activity']['agent_id']) + ',' +
                         str(data['activities_data'][i]['activity']['requester']) + ',' +
                         '\'' + data['activities_data'][i]['activity']['product'] + '\'),'
                         )
values_to_insert = values_to_insert[:-1]


# Insert a row of data
c.execute("INSERT INTO activity VALUES" + values_to_insert)

# Save (commit) the changes
conn.commit()

c.execute('SELECT * FROM activity')
print(c.fetchall())


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
