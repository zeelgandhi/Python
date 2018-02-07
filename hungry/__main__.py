import argparse


parser = argparse.ArgumentParser(prog="hungry")
parser.add_argument('--user_id',type = int)

args = parser.parse_args()

print(args)
print(args.user_id)