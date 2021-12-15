import database
from prettytable import PrettyTable
from pprint import pprint
import args


def main(arguments):
    whitelist_table = database.WhitelistTable("../servertest.db")
    whitelist_columns = whitelist_table.get_table_headers()
    t = PrettyTable(whitelist_columns)
    if not arguments.get_users:
        for row in whitelist_table.get_users():
            t.add_row(row)
    else:
        for row in whitelist_table.get_users(arguments.get_users):
            t.add_row(row)
    # t._max_width = {"password": 6}
    t.del_column("password")
    print(t)


if __name__ == '__main__':
    main(args.parse_args())
