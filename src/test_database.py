from fitness_analytics.database import get_engine


engine = get_engine()

try:
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()

except Exception as e:
    print("Connection failed:")
    print(e)