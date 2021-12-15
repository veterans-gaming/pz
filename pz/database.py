import sqlite3


class WhitelistTable:

    def __init__(self, db="servertest.db"):
        self.conn = sqlite3.connect(db)

    def __contains__(self, item: str) -> bool:
        if self.get_user(item): return True

    def get_table_headers(self):
        cursor = self.conn.execute("SELECT * FROM whitelist")
        return [description[0] for description in cursor.description]

    def get_user(self, username: str) -> tuple:
        cursor = self.conn.cursor()
        return cursor.execute("SELECT * FROM whitelist WHERE username = ?", (username,)).fetchone()

    def get_users(self, users=None) -> list:
        if users is not None:
            users = ', '.join(f"'{u}'" for u in users)
            sql_query = f"SELECT * FROM whitelist WHERE username IN ({users})"
        else:
            sql_query = "SELECT * FROM whitelist"
        print(sql_query)
        cursor = self.conn.cursor()
        return cursor.execute(sql_query).fetchall()

    def add_user(self, username: str):
        """should return ID on success, None on failure"""
        pass

    def edit_user(self, uid: int, **kwargs):
        cursor = self.conn.cursor()
        if kwargs:
            sql_query = f"UPDATE whitelist SET "
            value_length = len(kwargs)
            value_length -= 1
            for i, (k, v) in enumerate(kwargs.items()):
                if i < value_length:
                    sql_query += f"{k} = '{v}', "
                else:
                    sql_query += f"{k} = '{v}' "
            sql_query += f"WHERE id = {uid}"
            cursor.execute(sql_query)
        self.conn.commit()

    def get_user_id(self, username):
        return self.get_user(username)[0]

    def change_password(self):
        pass
