clc, clearvars;
n = 100000; % örnek sayısı - sample size
minNumber = 4;
maxNumber = 9;
x = minNumber + (maxNumber-minNumber)*rand(1,n);
T = 0.2;
edges = minNumber:T:maxNumber;
X = 0:T:edges(end);
figure(1); clf;
histogram(x,edges,'FaceColor',[0.75,0.75,0.75]);
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x','FontSize',15); ylabel('gözlem','FontSize',15); title('histogram');
set(gca,'xtick',[0:12]);
axis([0 12 0 5000]);
figure(2); clf;
histogram(x,edges,'normalization','pdf','FaceColor',[0.75,0.75,0.75]);
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x'); title('normalize edilmiş histogram');
axis([3 10 0 0.25]);