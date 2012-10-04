import numpy as np
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion

def detect_peak (spectrum):
    """
    Takes an spectrum and detect the peaks usingthe local maximum filter.
    Returns a boolean mask of the peaks (i.e. 1 when
    the pixel's value is the neighborhood maximum, 0 otherwise)
    """
    # Define an 8-connected neighborhood
    #side_length = min(spectrum.shape)*2
    side_length = 5
    neighborhood = generate_binary_structure(2,2)
    # Apply local maximum filter to generate the mask that contains the peaks, 
    # whose values are set to be 1. Meanwhile, the background is set to be 0.
    
    #local_max = maximum_filter(spectrum, footprint=neighborhood)==spectrum
    local_max = maximum_filter(spectrum, size=(side_length,1))==spectrum
    background = (spectrum==0)
    
    # Erode the background in order to successfully subtract it form local_max, 
    # otherwise a line will appear along the background border 
    # (artifact of the local maximum filter)
    eroded_background = binary_erosion(background, structure=neighborhood, border_value=1)
    # local peaks in boolean matrix format
    peaks = local_max-eroded_background
    return peaks*spectrum

def detect_peak_1 (spectrum):
    """
    Return the local maximum of the given array.
    The data type of both input and output are numpy.ndarray
    """
    end = np.hstack((spectrum,spectrum[-1]))
    fir = np.hstack((spectrum[0],spectrum))
    mask = [end[k]>=fir[k] for k in range(len(end))]
    return spectrum*mask[:-1]*(np.ones(len(spectrum))-mask[1:])

def spread (spectrum, profile=4.):
    """
    Each point (maxima) in X is "spread" (convolved) with the profile.
    Return the pointwise max of all of these.
    "profile" is a scalar, it's the SD of a gaussian used as the spreading function.
    """
    w = int(4*profile)
    profile = np.exp([-0.5*((k/profile)**2) for k in range(-w, w+1)])
    spectrum = detect_peak_1(spectrum)
    output = np.zeros(spectrum.shape)
    if spectrum.ndim!=1:
        lensptr = len(spectrum[0])
    else:
        lensptr = len(spectrum)
    for i in np.nonzero(spectrum)[0]:
        EE = [0 for k in range(i+1)]+[v for v in profile]
        if len(EE)<=lensptr:
            EE = EE+[0 for k in range(lensptr+1-len(EE))]
            EE = EE[1:lensptr+1]
        else:
            EE[lensptr]=0
            EE = EE[1:lensptr+1]
        EE = np.array(EE)
        output = np.maximum(output, spectrum[i]*EE)
    return output


