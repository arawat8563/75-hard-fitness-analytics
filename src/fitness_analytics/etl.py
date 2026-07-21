import pandas as pd
from pathlib import Path
from sqlalchemy import text
from src.fitness_analytics.database import get_engine


BASE_DIR = Path(__file__).resolve().parents[2]


def load_workout_csv():

    file_path = BASE_DIR / "data" / "raw" / "workouts.csv"

    df = pd.read_csv(file_path)

    print("Workout data loaded successfully!")
    print(df.head())

    df["workout_date"] = pd.to_datetime(
        df["workout_date"],
        dayfirst=True
    )

    df["notes"] = df["notes"].fillna("")

    print("\nUpdated data types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    return df


def check_exercises():

    engine = get_engine()

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT COUNT(*) FROM exercises")
        )

        count = result.fetchone()

        print("\nExercises in database:")
        print(count)


def load_workouts_to_database(df):

    engine = get_engine()

    with engine.begin() as connection:

        # Check if workout session already exists
        check_query = text("""
            SELECT id
            FROM workout_sessions
            WHERE date = :date
            AND workout_type = :workout_type;
        """)


        existing_session = connection.execute(
            check_query,
            {
                "date": df["workout_date"].iloc[0],
                "workout_type": df["workout_type"].iloc[0]
            }
        ).fetchone()


        if existing_session:

            session_id = existing_session[0]

            print(
                "Workout session already exists. Using existing session."
            )


        else:

            session_query = text("""
                INSERT INTO workout_sessions
                (
                    date,
                    workout_type
                )
                VALUES
                (
                    :date,
                    :workout_type
                )
                RETURNING id;
            """)


            session_result = connection.execute(
                session_query,
                {
                    "date": df["workout_date"].iloc[0],
                    "workout_type": df["workout_type"].iloc[0]
                }
            )


            session_id = session_result.fetchone()[0]


        # Insert workout sets

        for _, row in df.iterrows():

            exercise_query = text("""
                SELECT id
                FROM exercises
                WHERE exercise_name = :exercise_name;
            """)


            exercise_result = connection.execute(
                exercise_query,
                {
                    "exercise_name": row["exercise_name"]
                }
            )


            exercise_id = exercise_result.fetchone()[0]


            set_query = text("""
                INSERT INTO workout_sets
                (
                    workout_session_id,
                    exercise_id,
                    set_number,
                    reps,
                    weight_kg,
                    rir,
                    notes
                )
                VALUES
                (
                    :workout_session_id,
                    :exercise_id,
                    :set_number,
                    :reps,
                    :weight_kg,
                    :rir,
                    :notes
                )
                ON CONFLICT
                (
                    workout_session_id,
                    exercise_id,
                    set_number
                )
                DO NOTHING;
            """)


            connection.execute(
                set_query,
                {
                    "workout_session_id": session_id,
                    "exercise_id": exercise_id,
                    "set_number": row["set_number"],
                    "reps": row["reps"],
                    "weight_kg": row["weight_kg"],
                    "rir": row["rir"],
                    "notes": row["notes"]
                }
            )


    print("Workout data loaded into database successfully!")


if __name__ == "__main__":

    workout_df = load_workout_csv()

    check_exercises()

    load_workouts_to_database(workout_df)