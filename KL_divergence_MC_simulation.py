# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:20:59 2018

@author: victor Zuanazzi

"""
import numpy as np

if __name__ == '__main__':
    KL_divergence_f = 0
    KL_divergence_g = 0
    mu, sigma = 0 , 1
    nu, tao = 0, 1
    sample_f = np.random.normal(mu, sigma, 10)
    sample_g = np.random.normal(nu, tao, 10)
    #print('sample_f:', sample_f)
    #print('sample_g:', sample_g)
    KL_divergence_f = (sample_f*np.log(np.abs(sample_f/sample_g))).sum()
    KL_divergence_g = (sample_g*np.log(np.abs(sample_g/sample_f))).sum()
    print('KL(f||g) =', KL_divergence_f)
    print('KL(g||f) =', KL_divergence_g)
    T_KL_f = (np.log((tao**2)/(sigma**2))-1 + (sigma**2+(mu-nu)**2)/tao**2)/2
    print('Theoretical KL(f||g) =',T_KL_f)
