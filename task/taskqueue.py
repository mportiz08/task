import os
import shelve
from os import path
from . import task

class TaskQueue:
  USER_HOME  = path.expanduser('~')
  SHELF_KEY  = 'tasks'
  SHELF_DIR  = path.join(USER_HOME, '.' + SHELF_KEY)
  SHELF_FILE = path.join(SHELF_DIR, SHELF_KEY)
  
  def __init__(self):
    if not os.path.exists(self.SHELF_DIR):
      os.mkdir(self.SHELF_DIR) # TEST ME
    self._shelf = shelve.open(self.SHELF_FILE)
    if self._shelf.has_key(self.SHELF_KEY):
      self._tasks = self._shelf[self.SHELF_KEY]
    else:
      self._tasks = []
  
  def push(self, task_txt):
    self._tasks.append(task.Task(task_txt))
    self._sync()
  
  def list(self):
    for task in self._tasks:
      print(task)
  
  def _sync(self):
    self._shelf[self.SHELF_KEY] = self._tasks
    self._shelf.sync()
