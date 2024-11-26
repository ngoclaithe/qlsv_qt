from src.database.database import DatabaseManager

class StudentModel:
    def __init__(self):
        self.db = DatabaseManager()

    def add_student(self, name, code, birthday, gender, email, phone):
        query = '''
        INSERT INTO students (name, code, birthday, gender, email, phone)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        params = (name, code, birthday, gender, email, phone)
        return self.db.execute_query(query, params)

    def get_all_students(self):
        query = 'SELECT * FROM students'
        return self.db.fetch_all(query)

    def get_student_by_id(self, student_id):
        query = 'SELECT * FROM students WHERE id = ?'
        return self.db.fetch_one(query, (student_id,))

    def update_student(self, student_id, name, code, birthday, gender, email, phone):
        query = '''
        UPDATE students 
        SET name=?, code=?, birthday=?, gender=?, email=?, phone=?
        WHERE id=?
        '''
        params = (name, code, birthday, gender, email, phone, student_id)
        return self.db.execute_query(query, params)

    def delete_student(self, student_id):
        query = 'DELETE FROM students WHERE id = ?'
        return self.db.execute_query(query, (student_id,))