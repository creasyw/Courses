% Source information generation
% 
% Source_gen.m
%
% w/ convolutional encoder, punturing, and interleaving.
%
% 1/2 rate encoder
% 3/4 puncture
% (10, 5) interleaver
%
% [source_bit, info_bit] = Source_gen(N_sym)
%
% input:    Nb         -- # of source bit
%
% output:   info_bit   -- bit stream of useful infomation
%                         660 useful + '000000' transition bits
%           source_bit -- bit stream of codeword

function [source_bit, info_bit] = Source_gen()

% Generation of info_bit

    info_bit = randint(1, 494);
    info_bit2 = [info_bit, zeros(1,6)];

% 1/2 rate Conv-Encoder

    trel = poly2trellis(7,[133,171]);
    codeword_1 = convenc(info_bit2, trel);

% Puncturing. Remove b3 in 'b0 b1 b2 b3';

%     codeword_2 = puncture(codeword_1);
%     L2 = length(codeword_2);

codeword_2 = codeword_1;
L2 = length(codeword_2);

% Interleaving (10, 5) Matrix

    source_bit = zeros(1,L2);
    source_bit = interleaving(
    Ni = L2 / 50;
    for ii = 1 : Ni
        index = (ii-1)*50 +1 : ii*50;
        source_bit(index) = matintrlv(codeword_2(index), 10, 5);
    end
   
return