import json
import psycopg2

con = psycopg2.connect(
  database="ternytska01_DB",
  user="postgres",
  password="shwartz",
  host="localhost",
  port="5432"
)
TABLES = [
    'play_time',
    'board_game',
    'geek',
    'collection',
    'game_new',
]
data = {}
with con:

    cur = con.cursor()
    
    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table_name] = rows

with open('ternytska.json', 'w') as outf:
    json.dump(data, outf, default = str)
    