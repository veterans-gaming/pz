import database
from prettytable import PrettyTable
from pprint import pprint
import args


def display(headers: list, rows: list, display_password=False):
    t = PrettyTable(headers)
    t.add_rows(rows)
    if not display_password:
        t.del_column("password")
    print(t)


def get_users(whitelist_table, users: list):
    if users:
        rows = whitelist_table.get_users(users)
    else:
        rows = whitelist_table.get_users()
    return rows


def main(arguments):
    whitelist_table = database.WhitelistTable("../servertest.db")

    if arguments.cmd == "list":
        whitelist_columns = whitelist_table.get_table_headers()
        rows = get_users(whitelist_table, arguments.users)
        display(whitelist_columns, rows, arguments.show_password)
    elif arguments.cmd == "adduser":
        arg_list = [arguments.username]
        if arguments.password:
            arg_list.append(arguments.password)
        if arguments.accesslevel:
            arg_list.append(arguments.accesslevel)
        whitelist_table.add_user(*arg_list)
    elif arguments.cmd == "deluser":
        whitelist_table.delete_user(uid=int(arguments.uid))



if __name__ == '__main__':
    main(args.parse_args())
