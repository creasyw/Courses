% Transmitter
%
% Transmitter.m
% 
% (C) Shaoshu Sha, 11/02/2010
%
% [Symbol_tx, N_sym_ups] = Transmitter(Burst_bit)
%
% Symbol_tx: output -- symbol domain
% N_sym_ups: output -- # of output symbols after upsampling;
%
% Burst_bit: input  -- Bit domain

function [Symbol_tx, N_sym_ups] = Transmitter(Burst_bit)
  

% Step 1: Modulation: QPSK Mapping

    Symbol = modulation(Burst_bit);
    N_Sym = length(Symbol);

% Step 2: upsample: 16 samples / symbol

    Symbol_ups = upsample(Symbol, 16);
    N_sym_ups = length(Symbol_ups);

% Step 3: Pulse Shaping

% Raised Cosine FIR filter is used with roll-off factor = 0.35
% and 'sqrt' type.

    filter = rcosine(1, 16, 'sqrt', 0.35); 
    N_filter = length(filter);

% pulse shaping for IN-Phase Channel

    Symbol_ups_I = conv(real(Symbol_ups), filter);

% pulse shaping for Quardrature Channel

    Symbol_ups_Q = conv(imag(Symbol_ups), filter);

% Cut off the redundent head and tail symbols

    Symbol_tx_I = Symbol_ups_I((N_filter-1)/2 +1 : (N_filter-1)/2 + N_sym_ups);
    Symbol_tx_Q = Symbol_ups_Q((N_filter-1)/2 +1 : (N_filter-1)/2 + N_sym_ups);

% Combine REAL and IMAGINARY part.

    Symbol_tx = Symbol_tx_I + i * Symbol_tx_Q;
 

    return;
    