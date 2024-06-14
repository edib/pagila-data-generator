import psycopg2

# PostgreSQL bağlantı ayarları
DB_NAME = "pagila"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "10.11.12.13"

# PostgreSQL veritabanına bağlantı
def connect_db():
    return psycopg2.connect(
        dbname=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        host=DB_HOST
    )
