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


def create_table_teachers():
    conn = connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
    teacher_id INTEGER UNIQUE  PRIMARY KEY,
    kurs_id INTEGER,
    full_name VARCHAR (150), 
    image_path VARCHAR (100), 
    staji INTEGER , 
    Portfolio VARCHAR(255)
    )
    """)

    conn.commit()
    conn.close()


def get_teachers_by_kursid(kurs_id):
    conn = connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT * from teachers
        where kurs_id = {kurs_id}
        """)

    data = cursor.fetchall()
    return data


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


def checkadmin(telegram_id):
    conn = connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT * from users
        WHERE telegram_id ='{telegram_id}'
        """)
    data = cursor.fetchone()
    # print(data)
    if data[6] == 'admin':
        return True
    else:
        return False
    conn.close()


def add_user(fname, lname, t_id, full_name='', phone=''):
    conn = connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO users (telegram_id,first_name,last_name,full_name, phone_number)
        VALUES ('{t_id}', "{fname}", "{lname}", '{full_name}', '{phone}')
        """)
    conn.commit()
    conn.close()
def add_course(kurs_nomi, narxi, davomiyligi, amaliyot, hafta, soat, technology):
    conn = connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO kurslar (kurs_nomi, narxi, davomiyligi, amaliyot, hafta, soat, technalogy)
        VALUES ("{kurs_nomi}", {narxi}, {davomiyligi}, {amaliyot}, {hafta}, {soat}, "{technology}")
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


def get_course_detail(course_id):
    conn = connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"""
                SELECT * from kurslar
                where kurs_id = {course_id}
                """)
    data = cursor.fetchone()
    return data
