
input = x_verynosie;

m1 = [-3,1];
m2 = [1,-2];
m3 = [3,2.5];
sigma = [1.6,0; 0,1.6];
len = length (input);

for i=1:len
    dis1 = ((input(i,1)-m1(1,1))^2+(input(i,2)-m1(1,2))^2)^0.5;
    dis2 = ((input(i,1)-m2(1,1))^2+(input(i,2)-m2(1,2))^2)^0.5;
    dis3 = ((input(i,1)-m3(1,1))^2+(input(i,2)-m3(1,2))^2)^0.5;
    if dis1==dis2==dis3
        input(i,3)='1,2,3';
    elseif dis1==dis2 && dis2 ~= dis3
        input(i,3)='1,2';
    elseif dis2==dis3 && dis2 ~= dis1
        input(i,3)='2,3';        
    elseif dis1==dis3 && dis2 ~= dis1
        input(i,3)='1,3';    
    elseif dis1 < dis2 && dis1 < dis3
        input(i,3)=1;
    elseif dis2 < dis1 && dis2 < dis3
        input(i,3)=2;
    elseif dis3 < dis1 && dis3 < dis2
        input(i,3)=3;
    end
end

for i=1:len
    if input(i,3)==1
        plot(input(i,1),input(i,2),'.r');
        hold on;
    elseif input(i,3)==2
        plot(input(i,1),input(i,2),'.g');
        hold on;
    elseif input(i,3)==3
        plot(input(i,1),input(i,2),'.b');
        hold on;
    end
end