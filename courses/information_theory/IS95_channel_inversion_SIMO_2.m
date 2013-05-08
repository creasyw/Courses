% this is the function to calculate the channel capacity using channel
% inverstion power control for IS-95
% SIMO
% channel g11,g12, fast fading, Nr=2 (number of receiver antenna)

% the equation to calculate the channel capacity is
% C=1/L*sum(log(1+||hl||^2*P/N0)) 
% ||hl||^2=|hl1|^2+|hl2|^2

clear all 
clc

load g11;
load g12;
L=1000; % number of coherence period
Aver1=mean(g11.^2);
Aver2=mean(g12.^2);
h1=g11./sqrt(Aver1); % channel normalization
h2=g12./sqrt(Aver2); % channel normalization
SNR_dB=[-20:2:20];
SNR=10.^(SNR_dB/10);
M=length(SNR_dB);
C=zeros(1,M);

for m=1:M
% calculate the channel capacity

for l=1:L
    
    hsquare=h1(l)^2+h2(l)^2;
    P=1/hsquare; % channel inversion power control
    N0=P/SNR(m);
    C(m)=C(m)+log2(1+hsquare*P/N0);
    
end

C(m)=C(m)/L; % take the average

end

figure
plot(SNR_dB,C,'g-+');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of IS-95 with channel conversion (1X2)');