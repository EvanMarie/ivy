# local
import ivy
from typing import Union
from ivy.framework_handler import current_framework as _cur_framework


def bitwise_and(x1: Union[ivy.Array, ivy.NativeArray],
                x2: Union[ivy.Array, ivy.NativeArray])\
        -> ivy.Array:
    """
    Computes the bitwise AND of the underlying binary representation of each element x1_i of the input array x1 with
    the respective element x2_i of the input array x2.

    :param x1: first input array. Should have an integer or boolean data type.
    :param x2: second input array. Must be compatible with x1 (see Broadcasting). Should have an integer or
               boolean data type.
    :return: an array containing the element-wise results. The returned array must have a data type determined
             by Type Promotion Rules.
    """
    return _cur_framework(x1, x2).bitwise_and(x1, x2)


def isfinite(x: Union[ivy.Array, ivy.NativeArray])\
        -> ivy.Array:
    """
    Tests each element x_i of the input array x to determine if finite (i.e., not NaN and not equal to positive
    or negative infinity).

    :param x: input array. Should have a numeric data type.
    :return: an array containing test results. An element out_i is True if x_i is finite and False otherwise.
             The returned array must have a data type of bool.
    """
    return _cur_framework(x).isfinite(x)


def isnan(x: Union[ivy.Array, ivy.NativeArray])\
        -> Union[ivy.Array, ivy.NativeArray]:
    """
    Returns boolean map at locations where the input is not a number (nan).

    :param x: Input array.
    :type x: array
    :return: Boolean values for where the values of the array are nan.
    """
    return _cur_framework(x).isnan(x)


def less(x1: Union[ivy.Array, ivy.NativeArray],x2: Union[ivy.Array, ivy.NativeArray], f: ivy.Framework = None)\
        -> ivy.Array:
    """
    Computes the truth value of x1_i < x2_i for each element x1_i of the input array x1 with the respective 
    element x2_i of the input array x2.

    :param x1: Input array.
    :type x1: array
    :param x2: Input array.
    :type x2: array
    :param f: Machine learning framework. Inferred from inputs if None.
    :type f: ml_framework, optional
    :return: an array containing the element-wise results. The returned array must have a data type of bool.
    """
    return _cur_framework(x1,f=f).less(x1,x2)   


def cos(x: Union[ivy.Array, ivy.NativeArray])\
        -> ivy.Array:
    """
    Computes trigonometric cosine element-wise.

    :param x: Input array, in radians (2*pi radian equals 360 degrees).
    :return: The cosine of x element-wise.
    """
    return _cur_framework(x).cos(x)


def logical_not(x: Union[ivy.Array, ivy.NativeArray])\
        -> ivy.Array:
    """
    Computes the truth value of NOT x element-wise.

    :param x: Input array.
    :return: Boolean result of the logical NOT operation applied element-wise to x.
    """
    return _cur_framework(x).logical_not(x)
