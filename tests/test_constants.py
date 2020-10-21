# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:25:02 2020

@author: raula
"""

import numpy as np

from simple_functions import pi


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_pi(self):
        '''Test computation of pi'''
        my_pi = pi(2)
        assert np.isclose(my_pi, np.pi, atol=1e-12)