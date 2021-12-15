import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Manage Project Zomboid whitelist')
    parser.add_argument("--list-users", dest="get_users", nargs="*")
    return parser.parse_args()
