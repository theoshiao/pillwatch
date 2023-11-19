import psycopg2
# Update connection string information 

# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
host = "pilldb-public.postgres.database.azure.com"
dbname = "user"
user = "pillwatch_admin"
password = "Broceries123"
sslmode = "require"
# Construct connection string

# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string) 
print("Connection established")
cursor = conn.cursor()
# Drop previous table of same name if one exists

# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
cursor.execute("DROP TABLE IF EXISTS pills;")
print("Finished dropping table (if existed)")
# Create a table

# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
cursor.execute("CREATE TABLE pills (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table")
# Insert some data into the table

# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
cursor.execute("INSERT INTO pills (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO pills (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO pills (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted 3 rows of data")
# Clean up

# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
conn.commit()
cursor.close()
conn.close()