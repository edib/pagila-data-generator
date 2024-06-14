from faker import Faker
from psycopg2 import sql
from extensions import generate_fulltext, generate_special_features


fake = Faker()

# Sahte verileri 'film' tablosuna ekleme fonksiyonu
def insert_fake_films(cur, num_records):
    for _ in range(num_records):
        title = fake.catch_phrase()
        description = fake.text()
        release_year = fake.year()
        language_id = fake.random_int(min=1, max=6)
        rental_duration = fake.random_int(min=3, max=7)
        rental_rate = fake.random_int(min=1, max=10)
        length = fake.random_int(min=60, max=180)
        replacement_cost = fake.random_int(min=10, max=30)
        rating = fake.random_element(elements=('G', 'PG', 'PG-13', 'R', 'NC-17'))   
        special_features = generate_special_features()
        fulltext = generate_fulltext(10) 
        
        
        cur.execute(
            sql.SQL("""INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, fulltext) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""),
            [title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, fulltext]
        )