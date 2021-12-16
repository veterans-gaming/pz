import sqlite3
import sys


class WhitelistTable:

    def __init__(self, db="servertest.db"):
        self.conn = sqlite3.connect(db)

    def __contains__(self, item: str) -> bool:
        if self.get_user(item): return True

    def get_table_headers(self) -> list:
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
        cursor = self.conn.cursor()
        return cursor.execute(sql_query).fetchall()

    def add_user(self, username="", password="", access=None):
        """should return ID on success, None on failure"""
        if self.get_user(username):
            print("User already exists")
            self.conn.close()
            sys.exit()
        if password == "":
            password = "changeme"
        if access is None:
            access = "NULL"
        cursor = self.conn.cursor()
        sql_query = """
            INSERT INTO whitelist
                (username, password, admin, moderator, banned, encryptedPwd, pwdEncryptType, accesslevel, transactionID, displayName)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        cursor.execute(sql_query, (username, password, "false", "false", "false", "false", 1, "", 0, username))
        self.conn.commit()

    def _edit_user(self, uid: int, **kwargs) -> None:
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

    def get_user_id(self, username: str) -> str:
        return self.get_user(username)[0]

    def change_password(self, username: str, password: str):
        cursor = self.conn.cursor()
        uid = self.get_user_id(username)
        self._edit_user(uid, password=password, encryptedPwd=False, pwdEncryptType=1)

    def delete_user(self, username="", uid=-1):
        if uid < 0:
            if not username:
                raise ValueError("Username cant be NULL if UID is not present")
            uid = self.get_user_id(username)
        cursor = self.conn.cursor()
        sql_query = "DELETE FROM whitelist WHERE id = ?"
        cursor.execute(sql_query, (uid,))
        self.conn.commit()


