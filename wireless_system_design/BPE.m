% Block Phase Estimate (BPE)
%
% BPE.m
% 
% Transmitted Unique Word (UW) is 10110100 = [-j, -1, j, 1];
% 
% input:  Symbol      (after down-sampling)
% Output: Symbol_BPE  (After channel compensation);
% NN:     Window (Block) size
% MM:     Step size
% kk:     # of steps

function Symbol_BPE = BPE(Symbol)

    L_UW = 40;               % length of UW
    N_sym = length(Symbol);  % # of Sym in a Burst.
    
    UW = [-1i, -1, 1i, 1];
    UW_tx = [UW, UW, UW, UW, UW, UW, UW, UW, UW, UW];
    UW_rx = Symbol(4 : 43);   
    
% (1). Phase of UW

    theta_UW = angle(mean(UW_rx .* conj(UW_tx)));
    
% (2). Window (Block) size NN, and step Size MM

    NN = 1.5 * L_UW;            % NN > L_UW;
    MM = 6;                     % MM > 1;
    kk = (N_sym - NN) / MM + 1; % # of steps
    
% (3). Non-linear transform

    zz = abs(Symbol).^2 .* exp(1i*4*angle(Symbol));
    
% (4). Estimate phase of each block
    
    theta(1:kk) = 0;
    
    for ii = 1 : kk
        index = 1+MM*(ii-1) : NN+MM*(ii-1);
        theta0 = 1/4 * angle(sum(zz(index)));
        
        temp = theta0 + pi/4 * [-4 : 3];   % Candidates of angles
        
        % For the first one, find the angle closest to theta_UW;
        % For other angles, find the angle closest to the previous one.
        
        if(ii == 1)           
            [~, Ix] = min(abs(temp - theta_UW));   % yy is useless
            theta(ii) = temp(Ix);          
        else
            [~, Ix] = min(abs(temp - theta(ii-1)));
            theta(ii) = temp(Ix);            
        end
    end
    
% (5). Linear interpolation to estimate phase of every SYMBOL

    theta2(1:N_sym) = 0.0;
    for ii = 1 : kk
        nn = 0.5*NN + MM*(ii-1);
        theta2(nn) = theta(ii);
        
        if(ii > 1)
            delta = (theta(ii) - theta(ii-1)) / MM;
            theta2(nn - [1 : MM]) = theta2(nn) - delta * [1 : MM];
        end
    end
    
    % The beginning of Burst are UW, their phases are not important.
    
    theta2(1 : NN/2-1) = theta2(NN/2);
    theta2(nn+1 : N_sym) = theta2(nn);
    
    
% (6).  Channel phase compensation.

    Symbol_BPE = Symbol .* exp(-1i*theta2);
    
return
