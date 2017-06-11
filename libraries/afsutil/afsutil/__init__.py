"""Utility classes to build, install, and setup OpenAFS."""

__version__ = '0.6.6'

def print_version(**kwargs):
    import sys
    sys.stdout.write("afsutil version {0}\n".format(__version__))
