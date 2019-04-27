from setuptools import setup
import sys,os
home=os.path.expanduser('~')

with open('description.txt') as f:
    long_description = f.read()

setup(
    name = 'pandasqtable',
    version = '0.1.0',
    description = 'Library for qt tables using pandas DataFrames',
    long_description = long_description,
    url='https://github.com/dmnfarrell/pandastable2',
    license='GPL v3',
    author = 'Damien Farrell',
    author_email = 'farrell.damien@gmail.com',
    packages = ['pandasqtable'],
    package_data={'pandasqtable': ['../logo.png', '../description.txt',
                                  'datasets/*.csv']},
    install_requires=['matplotlib>=2.0',
                      'pandas>=0.20',
                      'PySide2'],
                      #'xlrd>=0.9',
                      #'future'],
    entry_points = { 'gui_scripts': [
                     'dataexplore2 = pandasqtable.app:main']},
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Topic :: Software Development :: User Interfaces',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research'],
    keywords = ['spreadsheet', 'table', 'pandas', 'data analysis', 'qt'],
)
