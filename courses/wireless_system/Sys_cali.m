
%*********************************************************
% System Calibration
%
% Sys_cali.m
%
% (C) Shaoshu Sha, 11-11-2010
%
% Calibrate average signal power and noise power.
%
% 10  Bursts are used to calculate SIGNAL power.
% 100 Noises --------------------- NOISE power
%
% Output:
%           SNR_n    : Normalized SNR (converges to ZERO)
%           Sigma_S2 : SIGNAL Power
%           Sigma_n2 : NOISE Power
%
% Input:
%           N_sym    : # of Original Symbol.
%
%*********************************************************

function [SNR_n, Sigma_S2, Sigma_n2] = Sys_cali(N_sym)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% 1st Part: NOISE power Calibration
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    N_sym_ups = 16 * N_sym;
    
    for nn = 1 : 100
        temp = randn(1,N_sym_ups) + i * randn(1,N_sym_ups); 
        
        % Apply temp noise to Receiver front end.
        temp2 = Receiver(temp, N_sym_ups);              
        
        % Calculate noise power after Receriver front end.
        Sigma2(nn) = mean(real(temp2).^2 + imag(temp2).^2);
    end
      
    Sigma_n2 = mean(Sigma2);
    
    Noise = temp;
       

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% 2nd Part: SIGNAL power Calibration
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    for rr = 1 : 10    % 10 Burst
        % Step 1: Burst Generation : Bit domain
        [Burst_bit, info_bit] = Burst(3, 40, 500, 3); 
    
        % Step 2: Modulation and pulse shapping: Symbol domain
        [Symbol_tx, N_sym_ups] = Transmitter(Burst_bit);

        % Step 3: Add AWGN noise
%         Noise = randn(1,N_sym_ups) + i * randn(1,N_sym_ups);
        Symbol_rx = Symbol_tx;
    
        % Step 4: Receiver front end (Match Filter, Downsmapling)
        Symbol_dns_rx = Receiver(Symbol_rx, N_sym_ups);

        % step 5: Calibartion of Signal power -- symbol domain
        Sigma_SI2(rr) = mean(real(Symbol_dns_rx).^2);
        Sigma_SQ2(rr) = mean(imag(Symbol_dns_rx).^2);
    end

    Sigma_S2 = 2 * mean(Sigma_SI2 + Sigma_SQ2);    % This is power

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% 3rd Part: Normalized SNR -- without effect of Kn
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% SNR = 10*log(Sigma_S2 / Sigma_n2 / (Kn)^2);
%     = 10*log(Sigma_S2 / Sigma_n2) - 20*log(Kn);
%     = SNR_n - 20*log(Kn);

    SNR_n = 10*log(Sigma_S2 / Sigma_n2);
    
return

    
    

