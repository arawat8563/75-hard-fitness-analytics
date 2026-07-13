-- 75 Hard Fitness Analytics Database Schema


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


CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    workout_type VARCHAR(50),
    exercise VARCHAR(100),
    sets INT,
    reps INT,
    weight_kg DECIMAL(5,2)
);


CREATE TABLE body_metrics (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    weight_kg DECIMAL(5,2),
    waist_cm DECIMAL(5,2),
    chest_cm DECIMAL(5,2),
    bodyfat_percentage DECIMAL(5,2)
);


CREATE TABLE cardio (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    activity_type VARCHAR(50),
    distance_km DECIMAL(5,2),
    duration_minutes INT,
    average_heart_rate INT
);

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';