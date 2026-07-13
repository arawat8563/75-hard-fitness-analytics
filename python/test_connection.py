from sqlalchemy import create_engine, text

username = "postgres"
password = "1526"
host = "localhost"
port = "5432"

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/postgres"
)

try:
    connection = engine.connect()

    result = connection.execute(
        text("SELECT datname FROM pg_database;")
    )

    print("Databases visible to Python:")

    for row in result:
        print(row)

    connection.close()

except Exception as e:
    print(e)