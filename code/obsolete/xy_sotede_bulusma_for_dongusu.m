clear all; close all; clc;
waitTime = 15;
n = 50000;
xy = 60*rand(n,2);
e = abs(xy(:,1)-xy(:,2));
m = 0;
tic;
for i=1:length(e)
    if e(i) <=15
        m = m+1;
    end
end
toc
fprintf('Olasılık (analitik) = %.5f\n', 7/16)
fprintf('Olasılık (nümerik) = %.5f\n', m/n)