import argparse
from . import taskqueue

def push_task(queue, args):
  queue.push(args.task_txt)

def list_tasks(queue, args):
  queue.list()

class Parser(object):
  def __init__(self):
    self._queue = taskqueue.TaskQueue()
    
    self._main_parser = argparse.ArgumentParser()
    self._sub_parsers = self._main_parser.add_subparsers()
    
    self._push_parser = self._sub_parsers.add_parser('push')
    self._push_parser.add_argument('task_txt')
    self._push_parser.set_defaults(func=push_task)
    
    self._list_parser = self._sub_parsers.add_parser('list')
    self._list_parser.set_defaults(func=list_tasks)
  
  def run(self):
    args = self._main_parser.parse_args()
    args.func(self._queue, args)
    
