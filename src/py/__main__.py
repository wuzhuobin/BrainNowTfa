from tfa import core
import sys

def main(input_xlsx, output_xlsx):
  pass
  print('main', file=sys.stderr)
  result = core(input_xlsx, output_xlsx)
  print(result[0])
  print(result[1])
  print(result[2])
  print(result[3])
  print(result[4])
  print(result[5])
  print(result[6])
  print(result[7])
  print(result[8])
  print(result[9])
  print(result[10])
  print(result[11])

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2])