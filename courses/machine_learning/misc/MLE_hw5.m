%calculate the values of mean and covariance
unbiasmu=zeros(3,2);
unbiascov = zeros(3,2,2);
for i=1:3
    unbiasmu(i,:) = mean(train(i,:,:));
    unbiascov(i,:,:)=cov(squeeze(train(i,:,:)));
end
biasmu = 24*unbiasmu/25;
biascov = 24*unbiascov/25;

%calculate the coefficients of the decision function
omiga1 = zeros(3,2,2);
omiga2 = zeros(2,3);
omiga3 = zeros(3,1);
for i=1:3
    omiga1(i,:,:)= -biascov(i,:,:)\0.5;
    omiga2(:,i)= squeeze(biascov(i,:,:))\transpose(biasmu(i,:));
    omiga3(i)= -0.5*biasmu(i,:)*inv(squeeze(biascov(i,:,:)))...
        *transpose(biasmu(i,:))-0.5...
        *log(det(squeeze(biascov(i,:,:))));
end

%classify the data via Normal Minimum Distance
datalength = length(test_clean);
disfunc = zeros(3,1);

classification1 = zeros(datalength, 1);
for i = 1:datalength
    disfunc(1) = test_clean(i,:)*transpose(squeeze(omiga1(1,:,:)))...
        *transpose(test_clean(i,:))+transpose(omiga2(:,1))...
        *transpose(test_clean(i,:))+omiga3(1);
    disfunc(2) = test_clean(i,:)*transpose(squeeze(omiga1(2,:,:)))...
        *transpose(test_clean(i,:))+transpose(omiga2(:,2))...
        *transpose(test_clean(i,:))+omiga3(2);
    disfunc(3) = test_clean(i,:)*transpose(squeeze(omiga1(3,:,:)))...
        *transpose(test_clean(i,:))+transpose(omiga2(:,3))...
        *transpose(test_clean(i,:))+omiga3(3);
    classification1(i)=find(disfunc==min(disfunc));
end

classification2 = zeros(datalength, 1);
for i = 1:datalength
    disfunc(1) = test_noisy(i,:)*transpose(squeeze(omiga1(1,:,:)))...
        *transpose(test_noisy(i,:))+transpose(omiga2(:,1))...
        *transpose(test_noisy(i,:))+omiga3(1);
    disfunc(2) = test_noisy(i,:)*transpose(squeeze(omiga1(2,:,:)))...
        *transpose(test_noisy(i,:))+transpose(omiga2(:,2))...
        *transpose(test_noisy(i,:))+omiga3(2);
    disfunc(3) = test_noisy(i,:)*transpose(squeeze(omiga1(3,:,:)))...
        *transpose(test_noisy(i,:))+transpose(omiga2(:,3))...
        *transpose(test_noisy(i,:))+omiga3(3);
    classification2(i)=find(disfunc==min(disfunc));
end

classification3 = zeros(datalength, 1);
for i = 1:datalength
    disfunc(1) = test_verynoisy(i,:)*transpose(squeeze(omiga1(1,:,:)))...
        *transpose(test_verynoisy(i,:))+transpose(omiga2(:,1))...
        *transpose(test_verynoisy(i,:))+omiga3(1);
    disfunc(2) = test_verynoisy(i,:)*transpose(squeeze(omiga1(2,:,:)))...
        *transpose(test_verynoisy(i,:))+transpose(omiga2(:,2))...
        *transpose(test_verynoisy(i,:))+omiga3(2);
    disfunc(3) = test_verynoisy(i,:)*transpose(squeeze(omiga1(3,:,:)))...
        *transpose(test_verynoisy(i,:))+transpose(omiga2(:,3))...
        *transpose(test_verynoisy(i,:))+omiga3(3);
    classification3(i)=find(disfunc==min(disfunc));
end
