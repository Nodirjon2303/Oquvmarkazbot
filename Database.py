from sqlite3 import connect


def create_table_users():


    conn = connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER UNIQUE  PRIMARY KEY,
    telegram_id VARCHAR (55),
    first_name  VARCHAR (255), 
    last_name VARCHAR (255), 
    full_name VARCHAR (255), 
    phone_number VARCHAR (25)
    )
    """)

    conn.commit()
    conn.close()
def create_table_kurslar():


    conn = connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kurslar(
    kurs_id INTEGER UNIQUE  PRIMARY KEY,
    kurs_nomi VARCHAR (185), 
    narxi INTEGER, 
    davomiyligi INTEGER , 
    amaliyot integer default 0,
    hafta integer default 3,
    soat REAL default 2.0,
    technalogy VARCHAR (255)
    )
    """)

    conn.commit()
    conn.close()





def checkuser(telegram_id):


    conn = connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT * from users
        WHERE telegram_id ='{telegram_id}'
        """)
    data = cursor.fetchone()
    if data:
        return False
    else:
        return True
    conn.close()

def add_user(fname, lname,t_id, full_name='', phone=''):
    conn = connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO users (telegram_id,first_name,last_name,full_name, phone_number)
        VALUES ('{t_id}', "{fname}", "{lname}", '{full_name}', '{phone}')
        """)
    conn.commit()
    conn.close()


def get_course_name():
    conn = connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"""
            SELECT kurs_id, kurs_nomi from kurslar
            """)
    data = cursor.fetchall()
    return data