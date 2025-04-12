import psycopg2

PGHOST = 'ep-calm-glitter-a5dfzo2h-pooler.us-east-2.aws.neon.tech'
PGDATABASE = 'neondb'
PGUSER = 'neondb_owner'
PGPASSWORD = 'npg_KWxI6gc0tHhf'
PORT = 5432

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS topic (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL
            );
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL
            );
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                user_id INTEGER REFERENCES users(id),
                topic_id INTEGER REFERENCES topic(id)
            );
            """
        cursor.execute(query)

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        #query_insert = 'INSERT INTO topic (name) VALUES (%s) RETURNING id, name'
        #topics = [
        #    ('IT',),
        #    ('Мандрівки',),
        #    ('Музика',)
        #]
        #cursor.executemany(query_insert, topics)

        #query_insert = 'INSERT INTO users (name) VALUES (%s) RETURNING id, name'
        #users = [
        #    ('Max',),
        #    ('Max',),
        #    ('Alex',),
        #]
        #cursor.executemany(query_insert, users)

        query_insert = 'INSERT INTO posts (name,  topic_id, user_id) VALUES (%s, %s, %s)'
        posts = [
            ('IT', 4, 1),
            ('Мандрівки', 5, 2),
            ('Музика', 6, 3),
        ]
        cursor.executemany(query_insert, posts)