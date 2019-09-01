import sys
import tfa
import argparse

def core(input_xlsx, output_xlsx):
  pass
  print('core', file=sys.stderr)
  result = tfa.core(input_xlsx, output_xlsx)
  print(result[0])
  print(result[1][0])
  print(result[1][1])
  print(result[1][2])
  print(result[1][3])
  print(result[1][4])
  print(result[1][5])
  print(result[1][6])

def summary(input_xlsx, output):
  tfa.summary(input_xlsx, output)
  pass


def main():
  pass
  print('main', file=sys.stderr)
  parser = argparse.ArgumentParser(description='Brain Now TFA program.')
  parser.add_argument('-c', '--core', nargs=2)
  parser.add_argument('-s', '--summary', nargs=2)
  args = parser.parse_args()
  if isinstance(args.core, list) and len(args.core) == 2:
    pass
    core(args.core[0], args.core[1])
  elif isinstance(args.summary, list) and len(args.summary) == 2:
    pass
    summary(args.summary[0], args.summary[1])
  else:
    parser.print_help()

if __name__ == '__main__':
  main()