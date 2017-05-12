from setuptools import setup, find_packages

VERSION = '0.1'

requires = [
    'pytest',
    'pytest-cov',
    'pyramid_debugtoolbar',
    'alembic',
    'docopt',
    'lxml',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_tm',
    'python-dateutil',
    'pyyaml',
    'requests',
    'SQLAlchemy',
    'transaction',
    'velruse',
]

setup(name='spacedate',
      version=VERSION,
      description='Zee Spaeshdate',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = spacedate.application:main

      [console_scripts]
      runtests = spacedate.scripts.runtests:main
      """,
      )
