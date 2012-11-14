from distutils.core import setup, Extension

extmod = Extension('_cubic_spline_interp_1d',
                   include_dirs = ['/usr/local/gsl/include'], # e.g.
                   libraries = ['gsl'],
                   library_dirs = ['/usr/local/gsl/lib'], # e.g.
                   sources = ['_cubic_spline_interp_1d.c'])

setup (ext_modules = [extmod])
