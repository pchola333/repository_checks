import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS checks;')
cur.execute('CREATE TABLE checks (id serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'day varchar (50) NOT NULL,'
                                 'amount integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO checks (name, day, amount, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Denis',
             'Sunday',
             499,
             'Spent a lot of time in the store')
            )


cur.execute('INSERT INTO checks (name, day, amount, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Mark',
             'Monday',
             530,
             'All tme on the phone')
            )

conn.commit()

cur.close()
conn.close()