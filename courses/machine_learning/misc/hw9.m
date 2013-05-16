clear all;

n = 4096; % <-- Choose the desired number of points, preferably large
p1 = [1.1,1.9]; p2 = [4.2,1.2]; p3 = [6.3,2.9];
p4 = [4.8,5.1]; p5 = [0.9,3.8]; % The five pentagon vertices

a23 = abs(det([p2-p1;p3-p1])); % Twice the triangles' areas
a34 = abs(det([p3-p1;p4-p1]));
a45 = abs(det([p4-p1;p5-p1]));
sa = a23+a34+a45;
a = a23/sa; b = (a23+a34)/sa; % Normalize cumulative areas
r = rand(n,1); % Use this to select the triangle
s = sqrt(rand(n,1)); s2 = [s,s]; % Use these to select
t = rand(n,1); t2 = [t,t]; % points within a triangle
pa = (r<=a)*p2 + ((a<r)&(r<=b))*p3 + (b<r)*p4; % Generalized vertices
pb = (r<=a)*p3 + ((a<r)&(r<=b))*p4 + (b<r)*p5;
p = (1-s)*p1 + s2.*((1-t2).*pa + t2.*pb); % The random points

c = [p1;p2;p3;p4;p5;p1]; % Plot the pentagon in red
plot(c(:,1),c(:,2),'ro',c(:,1),c(:,2),'r-',...
     p(:,1),p(:,2),'y.') % Plot random points as yellow dots
axis equal
