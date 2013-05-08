% this function is to calculate the channel capacity of CDMA2000 using
% equal power allocation scheme 
% the channel is SISO, fast fading, g11
% the equation is C=1/L*sum(log(1+P/L*hl^2/N0))

clear all
clc

load g11

L=length(g11); % the number of coherent period
Aver=mean(g11.^2);
h=g11./sqrt(Aver); % channel normalization
N0=1e-4;
SNR_dB=[-20:2:40];
SNR=10.^(SNR_dB/10);
M=length(SNR_dB);
P=SNR.*N0;
Pl=P./L; % power allocation for each coherent period
C=zeros(1,M);

for m=1:M
   
    C(m)=sum(log2(1+Pl(m)*h.^2/N0))/L;
   
end

figure
plot(SNR_dB,C,'r-*');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of CDMA2000 with equal power allocation (SISO)');