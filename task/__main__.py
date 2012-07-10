#!/usr/bin/env python
from . import cli

def main():
  parser = cli.Parser()
  parser.run()

if __name__ == '__main__':
  main()
