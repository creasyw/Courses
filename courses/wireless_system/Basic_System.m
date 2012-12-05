% Main program for System
% 
% 1st part is TX (Transmission)
% 2nd part is RX (Receiver) and detection;
%
% Main.m
% (c) Shaoshu Sha 10-21-2010, shaoshu.sha@mavs.uta.edu

% trel=poly2trellis(7,[133,171]);
% code=convenc(source,trel);
%-----
% deco=vitdec(code,trel,32,'term','hard');

clear
close all
clc

N_g = 3;                       % # of Guard
N_UW = 40;                      % # of Unique Word
N_inf = 500;                    % # of information
N_sym = N_g*2 + N_UW + N_inf;   % # of Symbols

N_burst = 100;  % # of bursts to average each SNR 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  
% System Calibration
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

SNR_n = Sys_cali(N_sym)


%=======================================================

SNR = [1 : 7];   % Signal-to-Noise ratio

for count = 1 : 7    % for different SNR

    Kn(count)  = 10.^((SNR_n - SNR(count))/20);
   
    for rr = 1 : N_burst   % # Burst for each SNR
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % 1st Part: Transmitter
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % Step 1: Burst Generation : Bit domain

        [Burst_bit, info_bit] = Burst(N_g, N_UW, N_inf, N_g); 
        Symbol = modulation(Burst_bit);
    
    % Step 2: Modulation and pulse shapping: Symbol domain

        [Symbol_tx, N_sym_ups] = Transmitter(Burst_bit);

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % 2nd Part: Channel
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    % Add Rician fading
    
        K_dB = 7;
        fd_m = 20;
        dt = 5e-8;
        [Rice, Ray] = Rician2(K_dB, dt, fd_m, N_sym_ups);     
        Symbol_rx = Symbol_tx .* Rice;
        
    % Add AWGN Noise   
%         Noise  = Kn(count) * (randn(1,N_sym_ups) + i*randn(1,N_sym_ups));
%         Symbol_rx = Symbol_tx + Noise;
        
        Symbol_rx = awgn(Symbol_rx, SNR(count));
        
%         Symbol_rx = Symbol_tx;

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % 3rd Part: Receiver front end
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        Symbol_dns_rx = Receiver(Symbol_rx, N_sym_ups);

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % 4th Part: Demodulation
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % Block Phase Estimate (BPE) to estimate the effect of AWGN Noise.

        Symbol_BPE_rx = BPE(Symbol_dns_rx);
    
        [source_dem, info_dem] = Demodulation(Symbol_BPE_rx, N_sym, N_UW, N_g, N_inf);
    
        BER(rr) = mean(abs(info_dem - info_bit));
    end
    
    % Average BER for N_burst Burst
    BER_avg(count) = mean(BER);
    
end

% Theoretical value by Q-function
gamma = 1 ./ Kn;
BER_the = 0.5 * erfc(gamma/sqrt(2));

figure
semilogy(SNR, BER_avg,'b-*',SNR, BER_the, 'rs-')
















