% Receiver
%
% Receiver.m
% 
% (C) Shaoshu Sha, 11/02/2010
%
% [Symbol_dns_rx] = Receiver(Symbol_rx, N_sym_ups)
%
% Symbol_dns_rx: Received Symbol after down-sampling -- Symbol Domain
% 

function [Symbol_dns_rx] = Receiver(Symbol_rx, N_sym_ups)

% Step 1: Match Filter

    Symbol_rx_I = real(Symbol_rx);
    Symbol_rx_Q = imag(Symbol_rx);
    
    filter = rcosine(1, 16, 'sqrt', 0.35); 
    N_filter = length(filter);
    
    Symbol_rx_I = conv(Symbol_rx_I, filter);
    Symbol_rx_Q = conv(Symbol_rx_Q, filter);
    
    Symbol_rx = Symbol_rx_I + j* Symbol_rx_Q;
    
% Step 2: Cut off
    Symbol_ups_rx = Symbol_rx((N_filter-1)/2 +1 : (N_filter-1)/2 + N_sym_ups);
    
% Step 3: Down Sampling
    Symbol_dns_rx = downsample(Symbol_ups_rx, 16);
    

    
return