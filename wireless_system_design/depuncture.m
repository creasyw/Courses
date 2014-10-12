% Depuncturing, add b3(bit 0) after every b0-b2

function Code = depuncture(Cod_pun)

% Length of unpunctured input code

    L = length(Cod_pun);
    
% Number of loops

    count = (L-1)/3;

% Length of depunctured output code

    L_out = 4*count;

    Code = zeros(1,L_out);

    for ii = 0:(count-1)
        Code(ii*4+1) = Cod_pun(ii*3+1);
        Code(ii*4+2) = Cod_pun(ii*3+2);
        Code(ii*4+3) = Cod_pun(ii*3+3);
    
        % add bit 0 in the fourth bit
        Code(ii*4+4)=0;
    end

return