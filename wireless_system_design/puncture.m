% Puncturing (b3 is punctured in every four bits b0-b3)

function cod_pun = puncture(code)

    L = length(code);
    
% Number of loops

    count = L/4;

% length of punctured code

    L_pun = 3*count;
    
% Length of output punctured code

    L_out = L_pun+1;
    cod_pun = zeros(1,L_out);
    
% Do puncture

for ii = 0:(count-1)
    cod_pun(ii*3+1) = code(ii*4+1);
    cod_pun(ii*3+2) = code(ii*4+2);
    cod_pun(ii*3+3) = code(ii*4+3);
end

% Add bit 0 in the last bit

    cod_pun(L_out)=0;
    
    
return