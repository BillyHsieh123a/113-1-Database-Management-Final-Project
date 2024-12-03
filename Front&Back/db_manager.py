import psycopg2

def get_connection():
    """
    Establish and return a database connection.
    """
    return psycopg2.connect(
        dbname="DB_Final_Project",
        user="postgres",
        password="bear123321a",
        host="localhost",
    )

def execute_query(query, values=None):
    """
    Execute a query against the database.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        conn.commit()
    except Exception as e:
        raise e
    finally:
        if conn:
            conn.close()
