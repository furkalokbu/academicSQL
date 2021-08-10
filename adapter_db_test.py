import psycopg2

conn = psycopg2.connect(
    database="academicDB",
    user="postgres",
    password="postgres",
    host="postgresdb.cqh8zx545xp6.eu-central-1.rds.amazonaws.com",
    port='5432'
)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS superheroes")
cur.execute("DROP TABLE IF EXISTS traffic_light")

conn.commit()

cur.execute("CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, strength int);")
cur.execute("INSERT INTO super")

cur.close()
conn.close()
