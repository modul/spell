import yaml

TABLES = {
  'german': 'german.yaml',
  'itu': 'itu.yaml'
}

class Speller:

  def __init__(self, tableName):
    self.table = tableName

  @property
  def table(self):
    return self._table
  
  @table.setter
  def table(self, name):
    with open(TABLES[name]) as fp:
      self._table = yaml.safe_load(fp)
  
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


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Spell text using a spelling alphabet')
  parser.add_argument('text', nargs='+', help='text to be spelled')
  parser.add_argument('--table', '-t', choices=['german', 'itu'], default='german', help='spelling table to use')

  args = parser.parse_args()

  speller = Speller(args.table)

  for word in args.text:
    print(speller.spell(word))
