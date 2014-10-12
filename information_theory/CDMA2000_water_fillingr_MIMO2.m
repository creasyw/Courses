% this function is to calculate the channel capacity for CDMA2000 using
% water filling algorithm
% the channel is MIMO, slow fading, Nt=2(number of transmit antenna), Nr=2 (number of receiver antenna)
% hij is the channel gain from transmit antenna i to receive antenna j

clear all
clc

load g11
load g12
load g21
load g22

N0=1e-4;
SNR_dBH=[-20:2:40];
SNRH=10.^(SNR_dBH/10);
M=length(SNR_dBH);
Ptot=SNRH.*N0;
H=[g11(500) g21(500);g12(500) g22(500)];
[U,S,V]=svd(H); % singular value decomposition
lamda=diag(S); % the eigenbvalues of H*Ht
lamda=lamda.';
N=length(lamda); % the rank of H
C=zeros(1,M);
miu=zeros(1,M);
P=zeros(1,N);
miu=Ptot/N+N0/N*sum(1./lamda.^2);

% for m=1:M
%     
%     s=0;
%     
%     for n=1:N
%         
%         if miu(m)-N0/lamda(n)^2>0
%             s=s+1/lamda(n)^2;
%         end
%         
%     end
%     
%     miu(m)=Ptot(m)/N+N0/N*s;
%     
%     for n=1:N
%         
%         if miu(m)-N0/lamda(n)^2>0
%         
%             P(n)=miu(m)-N0/lamda(n)^2;
%             
%         else
%             
%             P(n)=0;
%             
%         end
%     end
%     
%     C(m)=sum(log2(1+lamda.^2.*P/N0));
%     
% end
% 
% figure
% plot(SNR_dBH,C,'b-*');
% xlabel('SNR(dB)');
% ylabel('channel capacity(bits/s/Hz)');
% title('channel capacity of CDMA2000 with water filling algorithm (MIMO 2X2)');


% below is to calculate the channel capacity at low SNR
% C=SNR*Gmax*log2e

% Gmax is the maximum value of lamda.^2
SNR_dBL=[-20:2:0];
SNRL=10.^(SNR_dBL/10);
Gmax=max(lamda.^2);
CL=SNRL*Gmax*log2(exp(1));
Cawgn=SNRL*log2(exp(1));


figure
plot(SNR_dBL,CL,'c-o');
hold
plot(SNR_dBL,Cawgn,'g-<');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of CDMA2000 with water filling algorithm (MIMO2) at low SNR');

            

