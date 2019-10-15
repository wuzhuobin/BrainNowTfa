import sys
import tfa
from tfa import cli
import argparse

# def core(input_xlsx, output_xlsx):
#   pass
#   tfa.core(input_xlsx, output_xlsx)

# def summary(input_xlsx, output):
#   print(input_xlsx)
#   print(output)
#   tfa.summary(input_xlsx, output)
#   pass


# def main():
#   pass
#   print('main', file=sys.stderr)
#   parser = argparse.ArgumentParser(description='Brain Now TFA program.')
#   parser.add_argument('-c', '--core', nargs=2)
#   parser.add_argument('-s', '--summary', nargs='+')
#   args = parser.parse_args()
#   if isinstance(args.core, list) and len(args.core) == 2:
#     pass
#     core(args.core[0], args.core[1])
#   elif isinstance(args.summary, list) and len(args.summary) > 1:
#     pass
#     summary(args.summary[0:-1], args.summary[-1])
#   else:
#     parser.print_help()

if __name__ == '__main__':
  cli.main()