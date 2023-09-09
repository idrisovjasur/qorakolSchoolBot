import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            phone varchar(255),
            maktab_raqami int NOT NULL ,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    def create_table_lang(self):
            sql = """
            CREATE TABLE Lang (
                id int UNIQUE NOT NULL,
                language varchar(10) NOT NULL
                );
    """
            self.execute(sql, commit=True)

    def create_table_teacher(self):
            sql = """
            CREATE TABLE Teacher (
                science varchar(30) UNIQUE NOT NULL ,
                first_name varchar(255) NOT NULL,
                last_name varchar(30) NOT NULL ,
                phone varchar(255) NOT NULL ,
                ielts varchar(30),
                stage varchar(30),
                age varchar(30)
                );
    """
            self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str,maktab_raqami: int,phone: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, maktab_raqami, phone) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, maktab_raqami, phone), commit=True)

    def add_lang(self, id: int, language: str):
            sql = """
            INSERT INTO Lang(id, language) VALUES(?, ?)
            """
            self.execute(sql, parameters=(id, language), commit=True)
    def add_teacher(self, science: str, first_name: str,last_name: str,phone: str,ielts: str=None,stage: str=None,age: str=None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Teacher(science,first_name, last_name, phone,ielts,stage,age) VALUES(?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(science,first_name,last_name,phone,ielts,stage,age), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_lang(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Lang WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    def select_teacher(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Teacher WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_330(self):
        return self.execute("SELECT COUNT(*) FROM Users WHERE maktab_raqami = 330;", fetchone=True)
    def count_131(self):
        return self.execute("SELECT COUNT(*) FROM Users WHERE maktab_raqami = 131;", fetchone=True)
    def count_165(self):
        return self.execute("SELECT COUNT(*) FROM Users WHERE maktab_raqami = 165;", fetchone=True)


    def delete_teacher(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "DELETE FROM Teacher WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True,commit=True)

    def delete_users(self, **kwargs):
        sql = "DELETE FROM Users"
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True,commit=True)

    def update_user_lang(self,lang ,id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Lang SET language=? WHERE id=?
        """
        return self.execute(sql, parameters=(lang, id), commit=True)


# def logger(statement):
#     print(f"""
# _____________________________________________________
# Executing:
# {statement}
# _____________________________________________________
# """)