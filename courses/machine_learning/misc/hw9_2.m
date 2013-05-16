clear all;

% Create random rectangle
P1 = randn(1,2); P2 = randn(1,2);
P4 = P1 + 2*rand*(P2-P1)*[0 1;-1 0]; % Right angle corners
P3 = P4-P1+P2;

% Random fill points
n = 50; % <-- choose the total number of fill points
s = rand(n,1); t = rand(n,1);
P = repmat(P1,n,1) + s*(P2-P1)+t*(P4-P1);

% Plot it
R = [P1;P2;P3;P4;P1];
plot(R(:,1),R(:,2),'m-',P(:,1),P(:,2),'r.')
axis equal