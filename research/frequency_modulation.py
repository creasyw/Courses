import numpy as np
from math import pi, acos

def fm_linear(length, finitial=0.0, ffinal=0.5):
    assert length>=100, "The required length is too short."
    assert -0.5<=finitial<=0.5 and -0.5<=ffinal<=0.5, \
            "The linear slope should be between [-0.5, 0.5]"
    y = np.arange(1, length, dtype=float)
    mid = int(length/2)
    y = finitial*(y-mid)+((ffinal-finitial)/(2.*(length-1)))*((y-1)**2-(mid-1)**2)
    y = np.exp(y*pi*2j)
    return  y/y[mid]

def fm_sin(length, fmin=0.05, fmax=0.45):
    assert length>=100, "The required length is too short."
    assert -0.5<=fmin<=0.5 and -0.5<=fmax<=0.5 and fmin<fmax, \
            "The linear slope should be between [-0.5, 0.5]"
    period = length/2
    # time reference for the phase, default as N/2
    t0 = int(length/2)
    # frequency direction at T0 (-1 or +1), default as +1
    pm1 = 1
    # normalized frequency at time T0, default as 0.25
    fnorm0 = 0.25
    
    fmid = 0.5*(fmin+fmax)
    delta = 0.5*(fmax-fmin)
    phi = -pm1*acos((fnorm0-fmid)/delta)
    time = np.arange(1,length,dtype=float)-t0
    phase=2*pi*fmid*time+delta*period*(np.sin(2*pi*time/period+phi)-np.sin(phi))
    return np.exp(phase*1j)

