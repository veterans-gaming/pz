import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Manage Project Zomboid whitelist')
    subparsers = parser.add_subparsers(title="Commands", dest="cmd")

    list_parser = subparsers.add_parser("list", help="List users in the whitelist")
    list_parser.add_argument("--users", nargs="*", default=[], dest="users")
    list_parser.add_argument("--show-password", action="store_true", default=False, dest="show_password")

    adduser_parser = subparsers.add_parser("adduser", help="Add users to the whitelist")
    adduser_parser.add_argument("username", help="Player username")
    adduser_parser.add_argument("--password", dest="password", type=str)
    adduser_parser.add_argument("--accesslevel", choices=["player", "moderator", "admin"])

    deluser_parser = subparsers.add_parser("deluser", help="Delete users from the whitelist")
    deluser_parser.add_argument("uid", help="Player UID")

    #parser.add_argument("list", nargs="?", default=[])
    #parser.add_argument("adduser", nargs="?")
    #parser.add_argument("--password", type=str)
    #parser.add_argument("--accesslevel", type=str)
    return parser.parse_args()
