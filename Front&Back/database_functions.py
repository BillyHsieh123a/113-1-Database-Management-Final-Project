def show_user_profile(user_id):
    conn = None
    cur = None

    try:
        # Establish database connection
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        cur = conn.cursor()

        # Execute the UPDATE query
        cur.execute(
            """
            SELECT user_id, user_name, user_description, profile_pic, 
                         profile_background, birthday, email, country, 
                         language, fund, filtering, notification, cookies
            FROM public."user"
            WHERE 
                user_id = %s
            """,
            (user_id,)
        )

        # Check if any rows were updated
        if cur.rowcount == 0:
            print("No user found with the specified user_id.")
            return []
        
        user_data = cur.fetchall()

        # Commit the transaction
        conn.commit()
        return user_data

    except OperationalError as e:
        print(f"Database connection error: {e}")
        return []
    except IntegrityError as e:
        print(f"Integrity error (e.g., duplicate or invalid data): {e}")
        return []
    except DataError as e:
        print(f"Invalid input data: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
    finally:
        # Cleanup resources
        if cur:
            try:
                cur.close()
            except Exception as cleanup_error:
                print(f"Error closing cursor: {cleanup_error}")
        if conn:
            try:
                conn.close()
            except Exception as cleanup_error:
                print(f"Error closing connection: {cleanup_error}")