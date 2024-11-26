from src.database.database import DatabaseManager

class ClassModel:
    def __init__(self):
        self.db = DatabaseManager()

    def add_class(self, name, code, course_id):
        query = '''
        INSERT INTO classes (name, code, course_id)
        VALUES (?, ?, ?)
        '''
        params = (name, code, course_id)
        return self.db.execute_query(query, params)

    def get_all_classes(self):
        query = '''
        SELECT classes.id, classes.name, classes.code, courses.name 
        FROM classes 
        JOIN courses ON classes.course_id = courses.id
        '''
        return self.db.fetch_all(query)

    def get_class_by_id(self, class_id):
        query = '''
        SELECT classes.id, classes.name, classes.code, courses.name 
        FROM classes 
        JOIN courses ON classes.course_id = courses.id
        WHERE classes.id = ?
        '''
        return self.db.fetch_one(query, (class_id,))

    def update_class(self, class_id, name, code, course_id):
        query = '''
        UPDATE classes 
        SET name=?, code=?, course_id=?
        WHERE id=?
        '''
        params = (name, code, course_id, class_id)
        return self.db.execute_query(query, params)

    def delete_class(self, class_id):
        query = 'DELETE FROM classes WHERE id = ?'
        return self.db.execute_query(query, (class_id,))

    def get_courses_for_dropdown(self):
        query = 'SELECT id, name FROM courses'
        return self.db.fetch_all(query)