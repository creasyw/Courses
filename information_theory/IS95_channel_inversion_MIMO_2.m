% this is the function to calculate the channel capacity using channel
% inverstion power control for IS-95
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

% Aver11=mean(g11.^2);
% Aver12=mean(g12.^2);
% Aver21=mean(g21.^2);
% Aver22=mean(g22.^2);
% h11=g11./sqrt(Aver11); % channel normalization
% h12=g12./sqrt(Aver12); % channel normalization
% h21=g21./sqrt(Aver21); % channel normalization
% h22=g22./sqrt(Aver22); % channel normalization
SNR_dB=[-20:2:20];
SNR=10.^(SNR_dB/10);
M=length(SNR_dB);

 H=[g11(500) g21(500);g12(500) g22(500)];
 [U,S,V]=svd(H); % singular value decomposition
 lamda=diag(S); % the eigenbvalues of H*Ht
 N=length(lamda); % the rank of H
 P=1./lamda.^2; % channel inversion power control
 C=zeros(1,M);

for m=1:M
% calculate the channel capacity


    
   
    N0=P./SNR(m);
    C(m)=sum(log2(1+lamda.^2.*P./N0));
    

end

figure
plot(SNR_dB,C,'r-<');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of IS-95 with channel conversion (2X2)');