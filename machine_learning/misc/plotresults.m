
for i=1:datalength
    if classification3(i)==1
        plot(test_verynoisy(i,1),test_verynoisy(i,2),'.r');
        hold on;
    elseif classification3(i)==2
        plot(test_verynoisy(i,1),test_verynoisy(i,2),'xg');
        hold on;
    elseif classification3(i)==3
        plot(test_verynoisy(i,1),test_verynoisy(i,2),'+b');
        hold on;
    end
end