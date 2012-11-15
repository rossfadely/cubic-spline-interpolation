import ctypes 
import numpy as np
import matplotlib.pyplot as pl

from ctypes import c_double,c_long,c_int,POINTER

def _load_cubic_spline_interp_1d(dll_path,function_name):
    """
    This reads in the compiled interpolation library
    """
    dll = ctypes.CDLL(dll_path,mode=ctypes.RTLD_GLOBAL)
    func = dll.cubic_spline_interp_1d
    func.argtypes = [c_long,c_long,POINTER(c_double),
                     POINTER(c_double),POINTER(c_double),
                     POINTER(c_double),POINTER(c_int)]
    return func

cubic_interp=_load_cubic_spline_interp_1d('./_cubic_spline_interp_1d.so',
                                          'cubic_spline_interp_1d')

if __name__ == '__main__':
    """
    In the example below, note the 'float64' and
    'int32'...
    """
    x = np.random.rand(10).astype('float64') * 2. * np.pi
    y = np.sin(x).astype('float64')

    ind = np.argsort(x)
    x = x[ind]
    y = y[ind]
    x_p = x.ctypes.data_as(POINTER(c_double))
    y_p = y.ctypes.data_as(POINTER(c_double))

    Nnew = 30
    xnew = np.random.rand(Nnew).astype('float64')
    xnew *= 2.4 * np.pi
    xnew -= 0.2 * np.pi
    xnew_p = xnew.ctypes.data_as(POINTER(c_double))
    
    ynew  = np.zeros(xnew.shape[0])
    ynew_p = ynew.ctypes.data_as(POINTER(c_double))

    mask = np.zeros(Nnew).astype('int32')
    mask_p = mask.ctypes.data_as(POINTER(c_int))

    cubic_interp(x.shape[0],xnew.shape[0],x_p,y_p,xnew_p,ynew_p,mask_p)

    fig = pl.figure()
    pl.plot(x,y,'bo',label='Reference')
    pl.plot(xnew,ynew,'ro',label='Interpolated')
    ind = mask==1
    pl.plot(xnew[ind],ynew[ind],'ko',alpha=0.2,ms=10,label='Masked')
    pl.legend()
    pl.xlabel('x values')
    pl.ylabel('y values')
    fig.savefig('demo.png')
