import sys
import argparse
from utils import safely_call
from taskqueue import TaskQueue

def push_task(queue, args):
  txt = args.task_txt
  if txt == None:
    txt = sys.stdin.read().strip()
  tasks = txt.split('\n')
  for task_txt in tasks:
    queue.push(task_txt)

def remove_task(queue, args):
  safely_call(queue.remove, args.task_no)

def list_tasks(queue, args):
  queue.list()

def clear_tasks(queue, args):
  queue.clear()

# def mark_task_done(queue, args):
#   queue.mark_task_done(args.task_no)

class Parser(object):
  def __init__(self):
    self._queue = TaskQueue()
    
    self._main_parser = argparse.ArgumentParser()
    self._sub_parsers = self._main_parser.add_subparsers()
    
    # push sub-command
    self._push_parser = self._sub_parsers.add_parser('push')
    self._push_parser.add_argument('task_txt', nargs='?')
    self._push_parser.set_defaults(func=push_task)
    
    # rm sub-command
    self._rm_parser = self._sub_parsers.add_parser('rm')
    self._rm_parser.add_argument('task_no', type=int)
    self._rm_parser.set_defaults(func=remove_task)
    
    # list sub-command
    self._list_parser = self._sub_parsers.add_parser('list')
    self._list_parser.set_defaults(func=list_tasks)
    
    # clear sub-command
    self._list_parser = self._sub_parsers.add_parser('clear')
    self._list_parser.set_defaults(func=clear_tasks)
    
    # done sub-command
    # self._done_parser = self._sub_parsers.add_parser('done')
    # self._done_parser.add_argument('task_no', type=int)
    # self._list_parser.set_defaults(func=mark_task_done)
  
  def run(self):
    args = self._main_parser.parse_args()
    args.func(self._queue, args)
    
