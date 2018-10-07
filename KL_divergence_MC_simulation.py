# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:20:59 2018

@author: victor Zuanazzi

"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def plot_2_normal_distributions(means, stds):
    #Plot distributions:    
    mu, nu = means
    sigma, tau = stds
    n = 100
    x = np.linspace(-5, 8, n)

    p = norm.pdf(x, loc = mu, scale = sigma)
    q = norm.pdf(x, loc = nu, scale = tau)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, p, label="$p$, $\mu={0}, \sigma={1}$".format(mu, sigma))
    plt.plot(x, q, label="$q$, $v={0}, t={1}$".format(nu, tau)) # nu and tau are not recognized as latex symbols
    plt.ylabel("PDF of normal")
    plt.xlabel("$x$")
    plt.legend();
    plt.show();
    
def MC_KL_divergence(p1, p2):
    assert len(p1) == len(p2)
    n = len(p1)
    
    return (np.log(p1/p2)).sum()/n



if __name__ == '__main__':
    
    mu, sigma = 0 , 1
    nu, tau = 0, 2
    means = mu, nu
    stds = sigma, tau
    plot_2_normal_distributions(means, stds)
    
    for size in [10, 1000, 10000, 1000000]:
        print 'size: ',size
        # draw n samples from p(x)
        x = np.random.normal(size = size, loc = mu, scale = sigma)
        f = norm.pdf(x, loc = mu, scale = sigma)
        g = norm.pdf(x, loc = nu, scale = tau)
        #print('x: ', x)
        #print('f: ', f)
        #print('g: ', g)
        
        theoretical_fg = (np.log(tau**2/sigma**2) -1 + (sigma**2 +(mu - nu)**2)/(tau**2))/2
        mc_fg = MC_KL_divergence(f, g)
        
        print("Theoretical KL(f || g) \t= {0}\nMonte Carlo KL(f || g) \t= {1}".format(theoretical_fg, mc_fg))
        # draw n samples from q(x)
        x = np.random.normal(size = size, loc = nu, scale = tau)
        f = norm.pdf(x, loc = mu, scale = sigma)
        g = norm.pdf(x, loc = nu, scale = tau)
        
        theoretical_gf = (np.log(sigma**2) - np.log(tau**2) -1 + (tau**2 +(mu - nu)**2) / (sigma**2))/2
        mc_gf = MC_KL_divergence(g, f)
        
        print("Theoretical KL(g || f) \t= {0}\nMonte Carlo KL(g || f) \t= {1}".format(theoretical_gf, mc_gf))
        # sanity check
        print( MC_KL_divergence(f, f) == MC_KL_divergence(g, g) ==0) 

