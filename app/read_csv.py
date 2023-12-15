import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
      print('***' * 5)
      print(row)


if __name__ == '__main__':
  read_csv('./app/data.csv')
