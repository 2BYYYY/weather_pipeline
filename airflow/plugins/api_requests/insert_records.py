from api_request import mock_data, fetch_data
import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="db",
            user="db_user",
            password="db_password",
            # if local: host=localhost port=5000 (follow the docker compose file)
            host="db",
            port=5432
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

def create_table(conn: object):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
                       
        """)
        conn.commit()
        print("table was created")
    except Exception as e:
        print(f"Failed to create table: {e}")
        raise

def insert_records(conn: object, data: dict):
    try:
        cursor = conn.cursor()
        location = data['location']
        weather = data['current']
        cursor.execute("""
            INSERT INTO dev.raw_weather_data(
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                inserted_at,
                utc_offset)
                VALUES(%s, %s, %s, %s, %s, NOW(), %s)
            """,(
                location['name'],
                weather['temperature'],
                weather['weather_descriptions'][0],
                weather['wind_speed'],
                location['localtime'],
                location['utc_offset']

            ))
        conn.commit()
        print("Data inserted")
    except Exception as e:
        print(f"Data was unsuccessful: {e}")

def insert_records_main():
    try:
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occured during execution {e}")
    finally:
        if "conn" in locals():
            conn.close()
            print("Database closed")

def test_import_insert():
    print("imported successful")

if __name__ == "__main__":
    insert_records_main()