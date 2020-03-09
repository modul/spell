import yaml
from pkg_resources import resource_listdir, resource_stream
from os.path import splitext, join

NAME = "spell"
VERSION = "0.1.0"
DATADIR = 'tables'
DEFAULTTABLE = 'itu'

__table_files = resource_listdir(__name__, DATADIR)
__table_names = list(map(lambda f: splitext(f)[0], __table_files))

TABLES = dict(zip(__table_names, [join(DATADIR, f) for f in __table_files]))


class Speller:

  def __init__(self, tableName=DEFAULTTABLE):
    self.table = tableName

  @property
  def table(self):
    return self._table

  @table.setter
  def table(self, name):
    with resource_stream(__name__, TABLES[name]) as s:
      self._table = yaml.safe_load(s)

  def spell(self, word, delimiter=', '):
    return delimiter.join(
      self[letter] if letter in self
      else letter
      for letter in word)

  def __getitem__(self, key):
    letter = self.table[key.upper()]
    return key.islower() and letter.lower() or letter.upper()

  def __contains__(self, key):
    return key.upper() in self.table


def main():
  import argparse

  parser = argparse.ArgumentParser(description='Spell text using a spelling alphabet')
  parser.add_argument('text', nargs='+', help='text to be spelled')
  parser.add_argument('--version', '-v', action='version', version=f'%(prog)s {VERSION}')
  parser.add_argument('--table', '-t', choices=__table_names, default=DEFAULTTABLE, help='spelling table to use')

  args = parser.parse_args()

  speller = Speller(args.table)

  for word in args.text:
    print(speller.spell(word))
