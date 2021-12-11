import psycopg2
import matplotlib.pyplot as plt
import matplotlib

con = psycopg2.connect(
  database="ternytska01_DB",
  user="postgres",
  password="shwartz",
  host="localhost",
  port="5432"
)


query_1 = '''
create view GameGeekRanking as
SELECT game_name, ROUND(AVG(geek_ranking),2)
FROM collection INNER JOIN board_game USING(game_id)
GROUP BY game_name
'''

query_2 = '''
create view CountGameInCollections as
SELECT game_name, COUNT(game_id) 
FROM collection INNER JOIN board_game USING(game_id)
GROUP BY game_name
'''

query_3 = '''
create view CountGamesForAge as
SELECT age, COUNT(game_id)
FROM collection INNER JOIN geek USING(geek_id)
GROUP BY age
ORDER BY age;
'''



with con:
    cur = con.cursor()
    cur.execute('DROP VIEW IF EXISTS GameGeekRanking')

    cur.execute(query_1)

    cur.execute('SELECT * FROM GameGeekRanking')

    data_name = []
    data_values = []
    for line in cur:
        data_name.append(line[0])
        data_values.append(line[1])
    for i in range(len(data_name)):
        data_name[i] = data_name[i].replace(' ','')
    plt.bar(data_name, data_values, width=0.5)
    plt.xticks(rotation=80)
    plt.xlabel('Ігри')
    plt.ylabel('Середня оцінка')
    plt.show()
    print("Запит 1")
    for i in range(len(data_name)) :
        print("Назва гри =", data_name[i])
        print("Середня оцінка =", data_values[i], "\n")

    cur.execute('DROP VIEW IF EXISTS CountGameInCollections')

    cur.execute(query_2)

    cur.execute('SELECT * FROM CountGameInCollections')
    data_name = []
    data_values = []
    data_percentage = []
    for line in cur:
        data_name.append(line[0])
        data_values.append(line[1])
    for i in range(len(data_name)):
        data_name[i] = data_name[i].replace(' ','')
    for i in range(len(data_values)):
        data_percentage.append(data_values[i]/sum(data_values)*100)
    fig1, ax1 = plt.subplots()
    colors = ['#001eff','#00e5ff','#00ffa2','#ff8000','#ff0000','#ff00d0','#6200ff','#1eff00','#ccff00','#ffee00','#787878']
    ax1.pie(data_percentage, labels=data_name, autopct='%1.1f%%', colors = colors)
    plt.show()
    print("Запит 2")
    for i in range(len(data_name)) :
        print("Назва гри =", data_name[i])
        print("Кількість в колекціях =", data_values[i], "\n")

    cur.execute('DROP VIEW IF EXISTS CountGamesForAge')

    cur.execute(query_3)

    cur.execute('SELECT * FROM CountGamesForAge')
    data_name = []
    data_values = []
    for line in cur:
        data_name.append(line[0])
        data_values.append(line[1])


    fig, ax = plt.subplots()
    ax.plot(data_name, data_values, )

    plt.xlabel('Вік')
    plt.ylabel('Кількість ігор')
    plt.xticks(data_name)
    plt.xticks(rotation=300)
    plt.show()
    print("Запит 3")
    for i in range(len(data_name)) :
        print("Вік =", data_name[i])
        print("Кількість ігор =", data_values[i], "\n")

