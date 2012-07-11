import sys
import argparse
from . import taskqueue

def push_task(queue, args):
  txt = args.task_txt
  if txt == None:
    txt = sys.stdin.read().strip()
  queue.push(txt)

def list_tasks(queue, args):
  queue.list()

def clear_tasks(queue, arts):
  queue.clear()

class Parser(object):
  def __init__(self):
    self._queue = taskqueue.TaskQueue()
    
    self._main_parser = argparse.ArgumentParser()
    self._sub_parsers = self._main_parser.add_subparsers()
    
    # push sub-command
    self._push_parser = self._sub_parsers.add_parser('push')
    self._push_parser.add_argument('task_txt', nargs='?')
    self._push_parser.set_defaults(func=push_task)
    
    # list sub-command
    self._list_parser = self._sub_parsers.add_parser('list')
    self._list_parser.set_defaults(func=list_tasks)
    
    # clear sub-command
    self._list_parser = self._sub_parsers.add_parser('clear')
    self._list_parser.set_defaults(func=clear_tasks)
  
  def run(self):
    args = self._main_parser.parse_args()
    args.func(self._queue, args)
    
