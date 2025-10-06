clc, clearvars;
n = [120, 1200, 12000]; % örnek sayısı - sample size
maxNumber = 6;
x1 = randi(6,[n(1),1]);
x2 = randi(6,[n(2),1]);
x3 = randi(6,[n(3),1]);
T = 0.01;
edges = 0.5:1:maxNumber+0.5;
X = 0:T:edges(end);
figure(1); clf; set(gcf, "Position", [400, 350, 700, 200]);
subplot(1,3,1);
h = histogram(x1,edges,'FaceColor',[0.75,0.75,0.75]);
for i=1:length(h.Values)
    text((i-1)+0.6,h.Values(i)+1.6,num2str(h.Values(i)));
end
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x'); ylabel('gözlem'); title(['n = ', num2str(n(1))]);
set(gca, 'position', [0.05    0.1860    0.2789    0.7135]);
subplot(1,3,2);
h = histogram(x2,edges,'FaceColor',[0.75,0.75,0.75]);
for i=1:length(h.Values)
    text((i-1)+0.55,h.Values(i)+15,num2str(h.Values(i)));
end
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x'); title(['n = ', num2str(n(2))]);
set(gca, 'position', [0.37    0.1860    0.2789    0.7135]);
subplot(1,3,3);
h = histogram(x3,edges,'FaceColor',[0.75,0.75,0.75]);
for i=1:length(h.Values)
    text((i-1)+0.55,h.Values(i)+320,num2str(h.Values(i)));
end
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x'); title(['n = ', num2str(n(3))]);
set(gca, 'position', [0.71    0.1860    0.2789    0.7135]);