clear all; close all; clc;
n = 100;
x = round(20+randn(n,1));
%% plot
figure(1); set(gcf, 'position', [82.6000  217.0000  531.2000  375.2000]);
h = histogram(x,'FaceColor',[0.75,0.75,0.75]);
grid on; set(gca, 'gridlinestyle', '--', 'position', [0.0798 0.1128 0.9040 0.8661]);
xlabel('yaş'); ylabel('öğrenci sayısı');
xlim([min(x)-0.5,max(x)+0.5]); ylim([0,n/2]);
for i=1:length(h.Values)
    text(min(x)+i-1-0.15, h.Values(i)+2, sprintf('%i',h.Values(i)), 'FontSize', 14);
end
figure(2);
stem(min(x):max(x),h.Values,'k.','LineWidth',1.2);
grid on; set(gca, 'gridlinestyle', '--');
xlabel('yaş'); ylabel('öğrenci sayısı');
xlim([min(x)-0.5,max(x)+0.5]); ylim([0,n/2]);