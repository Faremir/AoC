from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(name = 'AoC',
      version = '1.19.05.1',
      url = 'https://jircode.com',
      license = 'GNU 3',
      author = 'faremir',
      author_email = 'faremir@jircode.com',
      description = 'Advent of Code solutions',

      long_description = long_description,
      long_description_content_type = "text/markdown",
      packages = ['Y19', 'Y19', 'utils']
      )
