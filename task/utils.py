import sys
from errors import TaskError

def safely_call(fn, *args):
  try:
    fn(*args)
  except TaskError as e:
    print(e)
    sys.exit(TaskError.ERROR_STATUS)

def color(str, color):
  codes = {
    'red':   '\033[91m',
    'green': '\033[92m',
    'end':   '\033[0m'
  }
  return codes[color] + str + codes['end']
