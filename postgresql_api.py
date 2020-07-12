import psycopg2
import os
try:
    # db_secret = os.environ["DATABASE_URL"]
    db_secret = 'postgres://uzplahckyznmgh:fbabe63af3f79dad472f0545895e1ae2a55ee3555d7e05c751a1c1ead2bf5cac@ec2-52-200-48-116.compute-1.amazonaws.com:5432/d4uu3pblmmnd2g'
    connection = psycopg2.connect(db_secret)
    connection.set_session(autocommit=True)

    # cur = connection.cursor()
    # cur.execute("""
    # SELECT table_name
    # FROM information_schema.tables
    # WHERE table_schema='public'
    # AND table_type='BASE TABLE';
    # """)
    # rows = cur.fetchall()
    # print('Table list:')
    # for row in rows:
    #     print("   ", row[0])
    # cur.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

def get_student_data():
    
    cur = connection.cursor()
    cur.execute("SELECT first_name, last_name, age FROM student")
    rows = cur.fetchall()
    print('Student firstname')
    print(rows)
    cur.close()
    return rows

get_student_data()
