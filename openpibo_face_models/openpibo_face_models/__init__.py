from pkg_resources import resource_filename

__version__ = '0.3.1'

def filepath(filename):
  return resource_filename(__name__, f'models/{filename}')
