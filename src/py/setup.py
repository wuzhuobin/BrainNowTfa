from setuptools import *

setup(
  name='tfa',
  version='0.0.1',
  author='wuzhuobin',
  packages=find_packages(),
  install_requires=[
    'numpy',
    'pandas',
    'xlrd',
    'scipy',
    'openpyxl',
    'xlwt',
  ],
  entry_points = {
    'console_scripts': ['tfa=tfa.cli:main'],
  }
)
