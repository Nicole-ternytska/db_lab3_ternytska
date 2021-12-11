import csv
import decimal
import psycopg2

con = psycopg2.connect(
  database="ternytska01_DB",
  user="postgres",
  password="shwartz",
  host="localhost",
  port="5432"
)


INPUT_CSV_FILE = 'bgg_dataset.csv'

query_0 = '''
CREATE TABLE game_new
(
    game_id character(10)NOT NULL,
    game_name character(255) NOT NULL,
    rating numeric(8,2) NOT NULL,
    CONSTRAINT pk_game_new PRIMARY KEY (game_id)
)
'''

query_1 = '''
DELETE FROM game_new
'''

query_2 = '''
INSERT INTO game_new (game_id, game_name, rating) VALUES (%s, %s, %s)
'''


with con:
    cur = con.cursor()
    cur.execute(query_0)
    cur.execute(query_1)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf, delimiter=";")
        for idx, row in enumerate(reader):
            if (idx > 10):
                break
            print(row)
            values = (idx, row['Name'], row['Rating Average'].replace(",", "."))
            cur.execute(query_2, values)


    con.commit()
