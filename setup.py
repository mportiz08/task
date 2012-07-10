from setuptools import setup
import task

setup(
  name='task',
  version=task.__version__,
  description=task.__doc__.strip(),
  author=task.__author__,
  license=task.__license__,
  packages=['task'],
  entry_points={
    'console_scripts': [
      'task = task.__main__:main'
    ]
  }
)
