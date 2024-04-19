from repositories.db import get_pool
from psycopg.rows import dict_row


#get all the rooms
def get_all_courses():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT 
                                course_id,
                                course_name
                            FROM
                                courses;
                           ''')
            return cursor.fetchall()