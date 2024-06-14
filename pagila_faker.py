import argparse
from actor import insert_fake_actors  
from film import insert_fake_films  
from connect import connect_db  

def main():
    parser = argparse.ArgumentParser(description='Insert fake data into Pagila database.')
    parser.add_argument('table', choices=['actor', 'film'], help='The table to insert fake data into.')
    parser.add_argument('num_records', type=int, help='The number of fake records to insert.')
    args = parser.parse_args()

    conn = connect_db()
    cur = conn.cursor()

    if args.table == 'actor':
        insert_fake_actors(cur, args.num_records)
    elif args.table == 'film':
        insert_fake_films(cur, args.num_records)

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {args.num_records} records into the {args.table} table.")

if __name__ == '__main__':
    main()
