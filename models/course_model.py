from src.database.database import DatabaseManager

class CourseModel:
    def __init__(self):
        self.db = DatabaseManager()

    def add_course(self, name, code, credits):
        query = '''
        INSERT INTO courses (name, code, credits)
        VALUES (?, ?, ?)
        '''
        params = (name, code, credits)
        return self.db.execute_query(query, params)

    def get_all_courses(self):
        query = 'SELECT * FROM courses'
        return self.db.fetch_all(query)

    def get_course_by_id(self, course_id):
        query = 'SELECT * FROM courses WHERE id = ?'
        return self.db.fetch_one(query, (course_id,))

    def update_course(self, course_id, name, code, credits):
        query = '''
        UPDATE courses 
        SET name=?, code=?, credits=?
        WHERE id=?
        '''
        params = (name, code, credits, course_id)
        return self.db.execute_query(query, params)

    def delete_course(self, course_id):
        query = 'DELETE FROM courses WHERE id = ?'
        return self.db.execute_query(query, (course_id,))