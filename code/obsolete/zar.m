clc, clearvars;
n = 500; % örnek sayısı - sample size
maxNumber = 6;
x = randi(6,[n,1]);
T = 0.01;
edges = 0.5:1:maxNumber+0.5;
X = 0:T:edges(end);
figure(1); clf;
subplot(1,2,1);
histogram(x,edges,'FaceColor',[0.75,0.75,0.75]);
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x'); ylabel('gözlem'); title('histogram');
subplot(1,2,2);
histogram(x,edges,'normalization','pdf','FaceColor',[0.75,0.75,0.75]);
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x'); title('normalize edilmiş histogram');
axis([0 edges(end) 0 0.2]);