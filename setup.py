from setuptools import setup

version = '0.1dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'django-extensions',
    'django-nose',
    ],

tests_require = [
    'nose',
    'coverage',
    'mock',
    ]

setup(name='spoc-base',
      version=version,
      description="Base nens_djangoapp contains common functionalities for SPOC.",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='Alexandr Seleznev',
      author_email='alexandr.seleznev@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['spoc_base'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
