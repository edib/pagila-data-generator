from faker import Faker
from psycopg2 import sql

fake = Faker()

# Sahte verileri 'actor' tablosuna ekleme fonksiyonu
def insert_fake_actors(cur, num_records):
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        cur.execute(
            sql.SQL("INSERT INTO actor (first_name, last_name) VALUES (%s, %s)"),
            [first_name, last_name]
        )
