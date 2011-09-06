from distutils.core import setup
setup(
    name = 'isoweek',
    version = '0.2.0',
    description = 'Objects representing a week',
    author='Gisle Aas',
    author_email='gisle@aas.no',
    url='http://github.com/gisle/isoweek',
    py_modules=['isoweek'],
    license='BSD',
    long_description=open("README.rst").read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
