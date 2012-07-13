class Task(object):
  STATUS_DONE = 'DONE'
  STATUS_TODO = 'TODO'
  
  def __init__(self, text, position):
    self.text, self.position = text, position
    self.status = self.STATUS_TODO
  
  def mark_done(self):
    self.status = self.STATUS_DONE
  
  def mark_todo(self):
    self.status = self.STATUS_TODO
  
  def __repr__(self):
    return '%d. %s %s' % (self.position, self._status_str(), self.text)
  
  def _status_str(self):
    return {
      self.STATUS_DONE: '✓',
      self.STATUS_TODO: '✗'
    }[self.status]
      