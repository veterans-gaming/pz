import database
import argparse
from prettytable import PrettyTable
from pprint import pprint
#import args


def parse_args():
    parser = argparse.ArgumentParser(description='Manage Project Zomboid whitelist')
    parser.add_argument("--list-users", dest="get_users", nargs="*")
    return parser.parse_args()


def main(arguments):
    whitelist_table = database.WhitelistTable("../servertest.db")
    print(arguments.get_users)
    whitelist_columns = whitelist_table.get_table_headers()
    t = PrettyTable(whitelist_columns)
    if not arguments.get_users:
        for row in whitelist_table.get_users():
            t.add_row(row)
    else:
        for row in whitelist_table.get_users(arguments.get_users):
            t.add_row(row)
    #t._max_width = {"password": 6}
    t.del_column("password")
    print(t)

    #pprint(whitelist_table.get_users())
    #user = whitelist_table.get_user("admin")
    #print(user[0])
    #if user:
    #    whitelist_table.edit_user(user[0], username="admin1")
    #pprint(whitelist_table.get_users())

    """
    user = User(username="lol", password="lol")
    user.exists()
    user.change_password("lol2")
    user.create()
    """


if __name__ == '__main__':
    main(parse_args())
