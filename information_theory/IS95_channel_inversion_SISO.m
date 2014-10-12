% this is the function to calulate the channel capacity using channel
% inversion power control for IS-95
% SISO
% channel g11, fast fading
% the equation to calculate the channel capacity is C=1/L*sum(log(1+|hl|^2*P/N0))

clear all
clc

load g11;
L=1000; % number of coherence period
Aver=mean(g11.^2);
h=g11./sqrt(Aver); % channel normalization
SNR_dB=[-20:2:20];
SNR=10.^(SNR_dB/10);
M=length(SNR_dB);
C=zeros(1,M);

for m=1:M
% calculate the channel capacity

for l=1:1000
    
    P=1/h(l)^2; % channel inversion power control
    N0=P/SNR(m);
    C(m)=C(m)+log2(1+h(l)^2*P/N0);
    
end

C(m)=C(m)/L; % take the average
Cawgn(m)=log2(1+SNR(m)); % channel capacity of AWGN

end

figure
plot(SNR_dB,C,'r-*',SNR_dB,Cawgn,'b-o');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of IS-95 with channel converstion (SISO)');
