import os
import shelve
from os import path
from collections import OrderedDict
from task import Task
from errors import TaskError

class TaskQueue:
  USER_HOME  = path.expanduser('~')
  SHELF_KEY  = 'tasks'
  SHELF_DIR  = path.join(USER_HOME, '.' + SHELF_KEY)
  SHELF_FILE = path.join(SHELF_DIR, SHELF_KEY)
  
  UNTAGGED_KEY = 'TODO'
  
  def __init__(self):
    if not os.path.exists(self.SHELF_DIR):
      os.mkdir(self.SHELF_DIR)
    self._shelf = shelve.open(self.SHELF_FILE)
    if self._shelf.has_key(self.SHELF_KEY):
      self._tasks = OrderedDict(self._shelf[self.SHELF_KEY])
    else:
      self._tasks = OrderedDict({})
  
  def push(self, args):
    task_txt = args.task_txt
    tag = args.tag
    if not self._tag_exists(tag):
      self._create_tag(tag)
    self.push_to_tag(task_txt, tag)
  
  def push_to_tag(self, task_txt, tag):
    task_pos = len(self._tasks[tag]) + 1
    self._tasks[tag].append(Task(task_txt, task_pos))
    self._sync()
  
  def remove(self, args):
    task_pos = args.task_no - 1
    tag = args.tag
    if not self._tag_exists(tag):
      raise TaskError('That tag does not exist.')
    else:
      self.remove_from_tag(task_pos, tag)
  
  def remove_from_tag(self, task_pos, tag):
    if task_pos >= len(self._tasks[tag]):
      raise TaskError('That task does not exist.')
    else:
      del(self._tasks[tag][task_pos])
      self._update_positions(tag)
      if len(self._tasks[tag]) == 0:
        del(self._tasks[tag])
      self._sync()
  
  def mark_task_done(self, task_pos, tag=UNTAGGED_KEY):
    if not self._tag_exists(tag):
      raise TaskError('That tag does not exist.')
    else:
      self.mark_task_done_from_tag(task_pos, tag)
  
  def mark_task_done_from_tag(self, task_pos, tag):
    if task_pos > len(self._tasks[tag]):
      raise TaskError('That task does not exist.')
    else:
      task = self._tasks[tag][task_pos - 1]
      task.mark_done()
      self._sync()
  
  def mark_task_todo(self, task_pos, tag=UNTAGGED_KEY):
    if not self._tag_exists(tag):
      raise TaskError('That tag does not exist.')
    else:
      self.mark_task_todo_from_tag(task_pos, tag)
  
  def mark_task_todo_from_tag(self, task_pos, tag):
    if task_pos > len(self._tasks[tag]):
      raise TaskError('That task does not exist.')
    else:
      task = self._tasks[tag][task_pos - 1]
      task.mark_todo()
      self._sync()
  
  def list(self, args):
    tasks = self._tasks
    if args.tag:
      tasks = {args.tag: self._tasks[args.tag]}
    num_tags = len(tasks)
    for idx, tag in enumerate(tasks):
      newline_needed = idx < (num_tags - 1)
      self.list_tasks_from_tag(tag, newline_needed)
  
  def list_tasks_from_tag(self, tag, newline=False):
    print(tag + ":\n")
    for task in self._tasks[tag]:
      print(task)
    if newline:
      print('')
      
  
  def clear(self):
    self._tasks = {}
    self._sync()
  
  def _tag_exists(self, tag):
    return self._tasks.has_key(tag)
  
  def _create_tag(self, tag):
    self._tasks[tag] = []
  
  def _update_positions(self, tag):
    for task in enumerate(self._tasks[tag]):
      task[1].position = task[0] + 1
  
  def _sync(self):
    self._shelf[self.SHELF_KEY] = self._tasks
    self._shelf.sync()
