-- 75 Hard Fitness Analytics Database Schema


DROP TABLE IF EXISTS workout_sets;
DROP TABLE IF EXISTS workout_sessions;
DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS daily_checkin;
DROP TABLE IF EXISTS body_metrics;
DROP TABLE IF EXISTS cardio_sessions;


CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    exercise_name VARCHAR(100) NOT NULL,
    muscle_group VARCHAR(50)
);


CREATE TABLE workout_sessions (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    workout_type VARCHAR(50)
);


CREATE TABLE workout_sets (
    id SERIAL PRIMARY KEY,
    workout_session_id INT REFERENCES workout_sessions(id),
    exercise_id INT REFERENCES exercises(id),
    set_number INT,
    reps INT,
    weight_kg DECIMAL(5,2),
    rir INT
);


CREATE TABLE daily_checkin (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    day_number INT NOT NULL,
    workout_1_completed BOOLEAN,
    workout_2_completed BOOLEAN,
    outdoor_workout_completed BOOLEAN,
    water_litres DECIMAL(3,1),
    diet_completed BOOLEAN,
    reading_completed BOOLEAN,
    progress_photo_completed BOOLEAN
);


CREATE TABLE body_metrics (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    weight_kg DECIMAL(5,2),
    waist_cm DECIMAL(5,2),
    chest_cm DECIMAL(5,2),
    bodyfat_percentage DECIMAL(5,2)
);


CREATE TABLE cardio_sessions (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    activity_type VARCHAR(50),
    distance_km DECIMAL(5,2),
    duration_minutes INT,
    average_heart_rate INT
);