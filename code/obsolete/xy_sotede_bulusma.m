clear all; close all; clc;
w = 25; % bekleme zamanı
n = 60000; % number of samples
xy = 60*rand(n,2);
tic;
m = sum(abs(xy(:,1)-xy(:,2)) <=w);
toc
fprintf('Olasılık (analitik) = %.5f\n', (w*(120-w))/(60*60))
fprintf('Olasılık (nümerik) = %.5f\n', m/n)