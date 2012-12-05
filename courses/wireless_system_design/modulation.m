% QPSK Modulation 
%
% Modulation.m
%
% Bit to Symbol Mapping
%
% 00 -->  1
% 01 -->  j
% 11 --> -1
% 10 --> -j
%
% sysmbol = modulation(Burst)
%
% Burst:    The Burst data (bits) to be modulated
% N_burst:  # of bits in the Burst.

function symbol = modulation(Burst)

    N_burst = length(Burst);

% Error detection
    if (N_burst == 0)
        error('NO data in the Burst !');
        return;
    elseif (mod(N_burst,2) ~= 0)
        error('Data should have even number of bits');
        return
    end

% Loop in a step of 2 bits
    for ii = 1 : 2 : N_burst - 1
        temp = Burst(ii : ii+1);
        nn = (ii+1)/2;   % index for symbel
    
        if     (temp == [0 0])
            symbol(nn) = 1;
        elseif (temp == [0 1])
            symbol(nn) = 0+j;
        elseif (temp == [1 1])
            symbol(nn) = -1;
        elseif (temp == [1 0])
            symbol(nn) = 0-j;
        else
            error('Burst is not in Binary Format !')
            return
        end
    end
    
return
    

