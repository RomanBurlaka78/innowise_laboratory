-- 1. CREATE TABLES
CREATE TABLE  IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL UNIQUE,
        birth_year INTEGER
    );

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

------------------------------------------------------------

-- 2. INSERT DATA

INSERT OR IGNORE INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Izabella Martinez', 2006);

INSERT OR IGNORE INTO grades (student_id, subject, grade) VALUES
(1, 'Math',88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 74),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

------------------------------------------------------------

-- 3. FIND ALL GRADES FOR A SPECIFIC STUDENT (Alice Johnson)
SELECT
    students.full_name,
    GROUP_CONCAT(grades.grade, ', ') AS grades_list
FROM grades
JOIN students ON students.id = grades.student_id
WHERE students.full_name = 'Alice Johnson'
GROUP BY students.full_name;

------------------------------------------------------------

-- 4. CALCULATE AVERAGE GRADE PER STUDENT
SELECT
    students.full_name,
    AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY students.full_name;

-- 5. LIST OF STUDENTS BORN AFTER 2004
SELECT
	id, full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 6. LIST OF SUBJECTS AND THEIR AVERAGE GRADES.
 SELECT
    subject,
    AVG(grade) AS average_grade
FROM grades
GROUP BY subject;

 -- 7. FIND THE TOP 3 STUDENTS WITH HIGHEST AVERAGE GRADES.
SELECT
    students.full_name,
    AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 3;

-- 8. SHOW ALL STUDENTS WHO HAVE SCORED BELOW 80 IN ANY SUBJECT.
SELECT DISTINCT
    students.full_name,
    grades.subject,
    grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.grade < 80;


