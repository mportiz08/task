import argparse
from . import taskqueue

def push(queue, args):
  queue.push(args.task_txt)

class Parser(object):
  def __init__(self):
    self._queue = taskqueue.TaskQueue()
    
    self._main_parser = argparse.ArgumentParser()
    self._sub_parsers = self._main_parser.add_subparsers()
    
    self._push_parser = self._sub_parsers.add_parser('push')
    self._push_parser.add_argument('task_txt')
    self._push_parser.set_defaults(func=push)
  
  def run(self):
    args = self._main_parser.parse_args()
    args.func(self._queue, args)
    
