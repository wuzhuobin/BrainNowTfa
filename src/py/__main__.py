from tfa import core
import sys

def main(input_xlsx, output_xlsx):
  pass
  print('main', file=sys.stderr)
  result = core(input_xlsx, output_xlsx)
  print(result)


if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2])