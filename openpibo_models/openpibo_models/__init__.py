from pkg_resources import resource_filename

__version__ = '0.4.7'

def filepath(filename):
  return resource_filename(__name__, f'models/{filename}')
