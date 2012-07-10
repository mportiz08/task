from . import task

class TaskQueue:
  def __init__(self):
    self._tasks = []
  
  def push(self, task_txt):
    self.push(Task(task_txt))
  
  def push(self, task):
    self._tasks.append(task)
    print(self._tasks)
