1D Cubic spline interpolation
=====================

A simple example of using some of `GSL's <http://www.gnu.org/software/gsl/>`_ C functionality.

Also, its hella faster and costs less memory than `Scipy's <http://www.scipy.org/>`_ equivalent.

Run
-------

Edit ``setup.py`` to point to your GSL libraries, etc.  Then,

::

    python setup.py build_ext --inplace

For the example,

::

    python demo.py



``demo.png`` should look something like:

.. image:: https://raw.github.com/rossfadely/cubic-spline-interpolation/master/demo.png
