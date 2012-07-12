import sys
from errors import TaskError

def safely_call(fn, *args):
  try:
    fn(*args)
  except TaskError as e:
    print(e)
    sys.exit(TaskError.ERROR_STATUS)
