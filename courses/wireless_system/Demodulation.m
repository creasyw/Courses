% Demodulation;
%
% Demodulation.m
% 
% (C) Shaoshu Sha, 11/02/2010
%

function [source_dem, info_dem] = Demodulation(Symbol_dns_rx, N_sym, N_UW, N_g, N_inf)

% Demodulation BPE

    for ii = 1 : N_sym
        if(abs(real(Symbol_dns_rx(ii))) >= abs(imag(Symbol_dns_rx(ii))))
            temp = sign(real(Symbol_dns_rx(ii)));
        else
            temp = 1i * sign(imag(Symbol_dns_rx(ii)));
        end
        Symbol_dem(ii) = temp;
        
        % Re-mapping from symbol to bit
        if(temp == 1)
            Burst_bit_dem(2*ii-1 : 2*ii) = [0 0];
        elseif(temp == -1)
            Burst_bit_dem(2*ii-1 : 2*ii) = [1 1];
        elseif(temp == 1i)
            Burst_bit_dem(2*ii-1 : 2*ii) = [0 1];
        elseif(temp == -1i)
            Burst_bit_dem(2*ii-1 : 2*ii) = [1 0];
        end
    end
    
    source_dem = Burst_bit_dem((N_UW+N_g)*2 + 1 : (N_UW+N_g)*2 + N_inf*2);
    L2 = length(source_dem);
    
% De-interleaving (10,5)

    codeword_2 = zeros(1,L2);
    Ni = L2 / 50;
    for nn = 1 : Ni
        index = (nn-1)*50 +1 : nn*50;
        codeword_2(index) = matdeintrlv(source_dem(index), 10, 5);
    end


% De-puncture

%     codeword_1 = depuncture(codeword_2);
 
codeword_1 = codeword_2;

% De-conv-coder

    trel = poly2trellis(7,[133,171]);
    codeword   = vitdec(codeword_1,trel,32,'term','hard');

% Cut off last 6 transition bits

    info_dem = codeword(1:494);    


return