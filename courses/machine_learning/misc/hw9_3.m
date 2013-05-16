clear all;

% Create random rectangle
P1 = [2,0.5]; P2 = [0,0];
P3 = [4,0]; 

% Random fill points
n = 5000; % the total number of fill points
s = rand(n,1); t = rand(n,1);
P = repmat(P1,n,1) + s*(P2-P1)+t*(P3-P1);
len = length(P(:,2));
for i=1:len
    if P(i,2)<0
        P(i,2)=-P(i,2);
    end
end

pxx=P(:,1).';
pdfx_approx=Parzen_gauss_kernel(pxx,0.1,-2,5);
plot(-2:0.1:5,pdfx_approx,'b');

% Plot it
% R = [P1;P2;P3;P1];
% figure(1);
% plot(R(:,1),R(:,2),'b-',P(:,1),P(:,2),'r.');
% grid on;
% set(gca,'ytick',-.4:.2:1);
% axis([-1,5,-0.4,1]);

% px = knn_density_estimate(pxx,5, -2,6,0.1); 
% plot(px);

% Parzen Windows Estimation
% px=zeros(len,)
% for i =1:len
%     for j = 1:i
%         px(i)
%     end
% end
% 
% =========
% [f,xi] = ksdensity(P(:,1));
% figure(2);
% plot(xi,f);
