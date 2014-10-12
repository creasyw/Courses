% Burst.m
%
% Burst Builder.
%
% The output is bit not symbol
%
% QPSK is used, so, 1 symbol = 2 bits
%
% For Unique Word, Baker code is used: 10110100;
%
% Burst(N_g, N_uw, N_info);
% N_g:     # of symbols of guard, for both head and tail.
% N_uw:    # of symbols of Unique Word.
% N_info:  # of symbols of information.


function [Bst_bit, info] = Burst(N_g1, N_uw, N_info, N_g2)

    n = 2;  % 2 bits / symbol

    guard_1 = ones(1, N_g1*n);
    guard_2 = ones(1, N_g2*n);
    baker = [1 0 1 1 0 1 0 0];
    UW = [baker,baker,baker,baker,baker,baker,baker,baker,baker,baker];

    [source, info] = Source_gen;

    Bst_bit = [guard_1, UW, source, guard_2];

return
