'''
    A database connection context manager module
'''
import sqlite3, logging
logging.basicConfig(filename='task24.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DatabaseConnection:
    '''
        Connection manager for sqlite3 and postgres\n
        Won't be implementing postgres
    '''
    logger = logging.getLogger(__name__) #class level logger
    
    def __init__(self,db_path):
        self.dbpath = db_path
        
    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.dbpath)
            self.cursor = self.conn.cursor()
        except sqlite3.OperationalError as e:
            self.logger.error(e)
            raise
        except Exception as e:
            self.logger.error(e)
        else:
            return self

    def execute(self,query):
        '''
            Execute the query with the open cursor
        '''
        success,tries = False,3
        while not success and tries > 0:
            try:
                self.logger.info(f"Executing {query}")
                response = self.cursor.execute(query)
            except sqlite3.NotSupportedError as e:
                self.logger.error(e)
                self.conn.rollback()
                tries -= 1
            except sqlite3.ProgrammingError as e:
                self.logger.error(e)
                self.conn.rollback()
                tries -= 1
            except sqlite3.IntegrityError as e:
                self.logger.error(e)
                self.conn.rollback()
                tries -= 1
            except Exception as e:
                self.logger.error(e)
            else:
                self.conn.commit()
                success = True
                return response
    
    def __exit__(self, exc_type, exc, tb):
        self.conn.close()
    
if __name__ == "__main__":
    with DatabaseConnection('test.db') as db:
        response = db.execute('PRAGMA table_info(users)')
        print(response.fetchall())