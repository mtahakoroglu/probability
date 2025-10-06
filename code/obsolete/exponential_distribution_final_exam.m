clearvars, clc;
lambda = 0.8;
n = 10000; % number of samples
edges = 0:12;
T = 0.01;
X = 0:T:edges(end);
%% plot histogram
figure(1); clf; set(figure(1),'Position',[273 316 528 384]);
x = exprnd(1/lambda,1,n);
% subplot(1,2,1);
h = histogram(x,edges,'FaceColor',[0.75,0.75,0.75]);
grid on; set(gca, 'gridlinestyle', '--');
xlabel('dk'); ylabel('Gözlem sayısı');
for i=1:length(h.Values)
    text((i-1)+0.3,h.Values(i)+350,num2str(h.Values(i)));
end
set(gca,'position',[0.13 0.11 0.843 0.87]);
set(gca,'FontName','Trebuchet MS','FontWeight','bold');
axis([0, edges(end), 0, n]);
set(gca, 'xtick', 0:edges(end));
titleText = ['$\lambda$ =  ' num2str(lambda)];
title(titleText, 'interpreter', 'latex', 'fontsize', 15);
%% plot normalized histogram and pdf
figure(2);
% subplot(1,2,2);
plot(X,lambda*exp(-lambda.*X),'color','k','LineWidth',1.3);
hold on;
histogram(x,edges,'normalization','pdf','FaceColor',[0.75,0.75,0.75]);
hold off;
grid on; set(gca, 'gridlinestyle', '--');
xlabel('dk'); ylabel('Gözlem sayısı (normalize)');
% set(gca,'position',[0.5466 0.13 0.4424 0.785]);
set(gca,'FontName','Trebuchet MS','FontWeight','bold');
axis([0, edges(end), 0, 1]);
set(gca, 'xtick', 0:edges(end));
titleText = ['$\lambda$ =  ' num2str(lambda)];
title(titleText, 'interpreter', 'latex', 'fontsize', 15);
legend('$$f_X(x) = \lambda e^{-\lambda x}$$','interpreter','latex','fontsize',15);
%% nümerik sonuç (simülasyon) ile teorik sonucu kıyasla
[sum(h.Values(3:end)) / n, exp(-1)]