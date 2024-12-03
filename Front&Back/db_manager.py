import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )

def execute_query(conn, query, params=None):
    with conn.cursor() as cur:
        cur.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
            return cur.fetchall()
        conn.commit()

def close_db(conn):
    conn.close()
