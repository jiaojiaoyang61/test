import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--verbose", action="store_true")
group.add_argument("--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))


# python parser_exclusive.py 4 2 
# python parser_exclusive.py 4 2 --quiet
# python parser_exclusive.py 4 2 --verbose
# python parser_exclusive.py 4 2 --verbose --quiet