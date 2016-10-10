import sys
if sys.version_info < (2, 6, 0):
    print('You need Python 2.6 or better to install isoweek')
    sys.exit(1)

from distutils.core import setup
setup(
    name = 'isoweek',
    version = '1.3.1',
    description = 'Objects representing a week',
    author='Gisle Aas',
    author_email='gisle@aas.no',
    url='http://github.com/gisle/isoweek',
    py_modules=['isoweek'],
    license='BSD',
    long_description=open("README.rst").read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
