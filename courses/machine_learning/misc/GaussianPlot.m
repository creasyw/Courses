

xm = m1(1,1);
ym = m1(1,2);
xsd = sqrt(sigma(1,1));
ysd = sqrt(sigma(2,2));
ivsig = inv(sigma);
maxsd = max(xsd, ysd);

%location of points at which x is calculated
x = xm-4*maxsd:0.1:xm+4*maxsd;
%location of points at which x is calculated
y = ym-4*maxsd:0.1:ym+4*maxsd;
% matrices used for plotting
[X, Y] = meshgrid(x,y); 
% Compute value of Gaussian pdf at each point in the grid
z=1/(2*pi*sqrt(det(sigma)))*exp(-0.5*(ivsig(1,1)*(X-xm).^2-2*ivsig(1,2)*(X-xm)*(Y-ym)+ivsig(2,2)*(Y-ym).^2));

h = surf(x,y,z);
%figure;
%contour(x,y,z)

hold on;

xm = m2(1,1);
ym = m2(1,2);

x = xm-4*maxsd:0.1:xm+4*maxsd;
y = ym-4*maxsd:0.1:ym+4*maxsd;
[X, Y] = meshgrid(x,y);
z=1/(2*pi*sqrt(det(sigma)))*exp(-0.5*(ivsig(1,1)*(X-xm).^2-2*ivsig(1,2)*(X-xm)*(Y-ym)+ivsig(2,2)*(Y-ym).^2));
h = surf(x,y,z);
%contour(x,y,z)

hold on;

xm = m3(1,1);
ym = m3(1,2);

x = xm-4*maxsd:0.1:xm+4*maxsd;
y = ym-4*maxsd:0.1:ym+4*maxsd;
[X, Y] = meshgrid(x,y);
z=1/(2*pi*sqrt(det(sigma)))*exp(-0.5*(ivsig(1,1)*(X-xm).^2-2*ivsig(1,2)*(X-xm)*(Y-ym)+ivsig(2,2)*(Y-ym).^2));
h = surf(x,y,z);
%contour(x,y,z)

view([0,0,0.1]);
axis([-5 5 -4 5]);

