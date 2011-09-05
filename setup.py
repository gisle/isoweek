from distutils.core import setup
setup(
    name = 'isoweek',
    version = '0.1.0',
    description = 'Objects representing a week',
    author='Gisle Aas',
    author_email='gisle@aas.no',
    url='http://github.com/gisle/isoweek',
    py_modules=['isoweek'],
    license='LICENSE.txt',
    long_description=open("README.rst").read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
