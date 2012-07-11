class Task(object):
  def __init__(self, text, position):
    self.text, self.position = text, position
  
  def __repr__(self):
    return '%d. %r' % (self.position, self.text)