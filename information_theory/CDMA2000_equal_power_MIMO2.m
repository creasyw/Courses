% this is the function to calculate the channel capacity using equal power
% allocation for CDMA2000
% MIMO
% channel g11,g12,g21,g22, slow fading, Nt=2(number of transmit antenna),Nr=2 (number of receiver antenna)
% hij is the channel gain from transmit antenna i to receive antenna j
% the equation to calculate the channel capacity is
% C=sum(log(1+lamdai^2*Pi/N0)) i=1,2 


clear all 
clc

load g11;
load g12;
load g21;
load g22;

N0=1e-4;
SNR_dB=[-20:2:40];
SNR=10.^(SNR_dB/10);
M=length(SNR_dB);
P=SNR.*N0;
H=[g11(500) g21(500);g12(500) g22(500)];
[U,S,V]=svd(H); % singular value decomposition
lamda=diag(S); % the eigenbvalues of H*Ht
N=length(lamda); % the rank of H
C=zeros(1,M);

for m=1:M
% calculate the channel capacity

   
%   N0=P./SNR(m);
    C(m)=sum(log2(1+lamda.^2*P(m)/N0/N));
    

end

figure
plot(SNR_dB,C,'r-<');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of CDMA2000 with equal power allocation MIMO(2X2)');