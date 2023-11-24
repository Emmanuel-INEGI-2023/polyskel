from setuptools import setup


setup(
    name='Squeletor.py',                    # package name
    version='0.1',                          # version
    description='Package Description',      # short description
    author='INEGI',
    maintainer='Emmanuel Rodriguez Garcia',
    url='http://www.inegi.org.mx',               # package URL
    install_requires=["euclid3 == 0.1","Pillow >= 7.0.0"],                    # list of packages this package depends
                                            # on.
    packages=['shapefile','argparse','re'],              # List of module names that installing
                                            # this package will provide.
)