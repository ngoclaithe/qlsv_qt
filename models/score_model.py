from src.database.database import DatabaseManager

class ScoreModel:
    def __init__(self):
        self.db = DatabaseManager()

    def add_score(self, student_id, course_id, score):
        query = '''
        INSERT INTO scores (student_id, course_id, score)
        VALUES (?, ?, ?)
        '''
        params = (student_id, course_id, score)
        return self.db.execute_query(query, params)

    def get_all_scores(self):
        query = '''
        SELECT scores.id, students.name, courses.name, scores.score
        FROM scores
        JOIN students ON scores.student_id = students.id
        JOIN courses ON scores.course_id = courses.id
        '''
        return self.db.fetch_all(query)

    def get_score_by_id(self, score_id):
        query = '''
        SELECT scores.id, students.name, courses.name, scores.score
        FROM scores
        JOIN students ON scores.student_id = students.id
        JOIN courses ON scores.course_id = courses.id
        WHERE scores.id = ?
        '''
        return self.db.fetch_one(query, (score_id,))

    def update_score(self, score_id, student_id, course_id, score):
        query = '''
        UPDATE scores SET student_id=?, course_id=?, score=?
        WHERE id=?
        '''
        params = (student_id, course_id, score, score_id)
        return self.db.execute_query(query, params)

    def delete_score(self, score_id):
        query = 'DELETE FROM scores WHERE id = ?'
        return self.db.execute_query(query, (score_id,))

    def get_students_for_dropdown(self):
        query = 'SELECT id, name FROM students'
        return self.db.fetch_all(query)

    def get_courses_for_dropdown(self):
        query = 'SELECT id, name FROM courses'
        return self.db.fetch_all(query)

    def get_student_average_score(self, student_id):
        query = '''
        SELECT AVG(score) as avg_score 
        FROM scores 
        WHERE student_id = ?
        '''
        return self.db.fetch_one(query, (student_id,))

    def get_course_average_score(self, course_id):
        query = '''
        SELECT AVG(score) as avg_score 
        FROM scores 
        WHERE course_id = ?
        '''
        return self.db.fetch_one(query, (course_id,))