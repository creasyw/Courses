% this function is to calculate the channel capacity of CDMA2000 using
% equal power allocation scheme 
% the channel is MISO, fast fading, g11,g21,g31,g41, Nt=4
% the equation is C=1/L*sum(log(1+(|h1|^2+|h2|^2+|h3|^2+|h4|^2)*SNR/4)) when transmitter
% does not know the channels.
% C=1/L*sum(log(1+(|h1|^2+|h2|^2+|h3|^2+|h4|^2)*SNR)) when transmitter knows the channels


clear all
clc

load g11
load g21
load g31
load g41

L=length(g11); % the number of coherent period
Aver11=mean(g11.^2);
Aver21=mean(g21.^2);
Aver31=mean(g31.^2);
Aver41=mean(g41.^2);
h11=g11./sqrt(Aver11); % channel normalization
h21=g21./sqrt(Aver21); % channel normalization
h31=g31./sqrt(Aver31); % channel normalization
h41=g41./sqrt(Aver41); % channel normalization
N0=1e-4;
SNR_dB=[-20:2:40];
SNR=10.^(SNR_dB/10);
M=length(SNR_dB);
P=SNR.*N0;
Pl=P./L; % power allocation for each coherent period
C=zeros(1,M);

for m=1:M
   
%     C(m)=sum(log2(1+Pl(m)*(h11.^2+h21.^2+h31.^2+h41.^2)/N0/4))/L; % channel is not known by transmitter
    C(m)=sum(log2(1+Pl(m)*(h11.^2+h21.^2+h31.^2+h41.^2)/N0))/L; % channel is known by transmitter
   
end

figure
plot(SNR_dB,C,'c-o');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of CDMA2000 with equal power allocation (MISO4) CSI');
% title('channel capacity of CDMA2000 with equal power allocation (MISO4) CSIR');