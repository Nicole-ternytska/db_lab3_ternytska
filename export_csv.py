import csv
import psycopg2

con = psycopg2.connect(
  database="ternytska01_DB",
  user="postgres",
  password="shwartz",
  host="localhost",
  port="5432"
)


OUTPUT_FILE_T = 'ternytska_DB_{}.csv'

TABLES = [
    'play_time',
    'board_game',
    'geek',
    'collection',
    'game_new',
]


with con:
    cur = con.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])

 
