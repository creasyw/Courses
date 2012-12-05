% Rician Flat Fading
%
% Rician.m
%
% (C) Shaoshu Sha, 11-27-2010
%
% -------------------------------
% 
% Rician flat fading consists of 2 parts
% 1. Line of Sight;          relative magnitude is "1"
% 2. Rayleigh flat fading;   relative magnitude is "A"
%
% fading = Rician(K_dB, dt, fd_m)
%
% Input:   K_dB  : Rician factor in dB
%          dt    : Time step, delta_t
%          fd_m  : Maximum Doppler shift
%          N_sym : # of symbols after upsampling.
%
% Output:  fading: Channel data.
%



function [fading, Rayleigh] = Rician2(K_dB, dt, fd_m, N_sym)

%     clear
%     clc
%     close all
%     
%     
%     dt = 5e-3;
%     K_dB = 7;
%     fd_m = 20;
%     N_sym = 546 * 16;
%     
% Generation of Rayleigh Flat Fading
    
    N = 200;
    M = (N/2 - 1) / 2;
    c = sqrt(2/M);
    Wm = 2*pi*fd_m;
    
    t0 = rand * (N/10);

    t = t0 + [0 : N_sym-1] * dt;
    
    g_I = 0;
    g_Q = 0;
    
    for n = 1 : M
        a_n = (2*pi*n - pi + (2*pi*rand - pi)) / (4*M);
        pha_1 = 2*pi*rand - pi;
        pha_2 = 2*pi*rand - pi;
        g_I = g_I + cos(Wm*t*cos(a_n) + pha_1);
        g_Q = g_Q + cos(Wm*t*sin(a_n) + pha_2);
    end
    g_I = g_I * c;
    g_Q = g_Q * c;
    
    Rayleigh = (g_I + g_Q *1i) / sqrt(2);
    
%     Ray = Rayleigh;
%      
%     m_ray = mean(Rayleigh)
%     var_ray = var(Rayleigh)
%  
%     figure
%     subplot(2,1,1)
%     plot(abs(Ray));
%     
%     subplot(2,1,2)
%     plot(unwrap(angle(Ray)))
%     
%     figure;
%     step = 0.1; range = 0: step : 3;
%     r = abs(Ray);
%     h = hist(r, range);
%     fr_ap = h / (step*sum(h));
%     fr = (range*2) .* exp(-range.^2);
%     plot(range, fr_ap, 'ko', range, fr, 'k'); grid;
%  

% Generation of Rician flat fading
    
    A = 10^(-K_dB/20); 
    B = 1 / sqrt(1 + A^2);
    LOS = (ones(1, N_sym) + 1i * ones(1, N_sym)) / sqrt(2);
    fading = B * ( LOS + A * Rayleigh );
    
       
return