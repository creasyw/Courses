% this function is to calculate the channel capacity for CDMA2000 using
% water filling algorithm 
% the channel is SISO, fast fading, g11
% the equation is C=1/L*sum(log(1+|hl|^2*Pl/N0))
% where Pl=1/lamda-N0/|hl^2|
% total power P=1/L*sum(Pl)

clear all
clc

load g11

L=length(g11);  % the number of coherent period
Aver=mean(g11.^2);
h=g11./sqrt(Aver); % channel normalization
N0=1e-4;
SNR_dBH=[-10:2:40];
SNRH=10.^(SNR_dBH/10);
M=length(SNR_dBH);
Ptot=SNRH.*N0;  % total power
C=zeros(1,M);
P=zeros(1,L);
lamda=zeros(1,M);
lamda=1./(Ptot+N0*sum(1./h.^2)/L);

% for m=1:M
%     
%     for l=1:L
%         
%         if 1/lamda(m)-N0/h(l)^2>0            
%             P(l)=1/lamda(m)-N0/h(l)^2;
%         else
%             P(l)=0;
%         end
%     end
%     
%     C(m)=sum(log2(1+h.^2.*P/N0))/L;
%     
% end

for m=1:M
    
    s=0;
 

    for l=1:L
              
        if 1/lamda(m)-N0/h(l)^2>0  
            s=s+1/h(l)^2;
        end
      
    end
    
    lamda(m)=1/(Ptot(m)+N0*s/L);
    
   for l=1:L
        
        if 1/lamda(m)-N0/h(l)^2>0            
            P(l)=1/lamda(m)-N0/h(l)^2;
        else
            P(l)=0;
        end
    end
    
    C(m)=sum(log2(1+h.^2.*P/N0))/L;
   
end

figure
plot(SNR_dBH,C,'r-*');
xlabel('SNR(dB)');
ylabel('channel capacity(bits/s/Hz)');
title('channel capacity of CDMA2000 with water filling algorithm (SISO) at High SNR');
hold

% below is to calculate the channel capacity at low SNR
% C=SNR*Gmax*log2e

% Gmax is the maximum value of the square of channel gain
% SNR_dBL=[-20:2:0];
% SNRL=10.^(SNR_dBL/10);
% Gmax=max(h.^2);
% CL=SNRL*Gmax*log2(exp(1));
% 
% plot(SNR_dBL,CL,'b-o');
% 
% 
% Cawgn=SNRL*log2(exp(1));
% plot(SNR_dBL,Cawgn,'g-<');
% 
% title('channel capacity of CDMA2000 with water filling algorithm (SISO) at low SNR');





