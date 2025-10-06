clearvars, clc;
lambda = [3,2,1,1/2,1/5,1/10];
n = 10000;
edges = 0:12;
T = 0.01;
X = 0:T:edges(end);
x = zeros(6,n);
%% plot histogram
figure(1); clf; set(gcf,'Position',1e3*[0.0218,0.1074,1.5072,0.6544]);
for i=1:length(lambda)
    subplot(2,3,i);
    x(i,:) = exprnd(1/lambda(i),1,n);
    histogram(x(i,:),edges,'FaceColor',[0.75,0.75,0.75]);
    grid on; set(gca, 'gridlinestyle', '--');
    xlabel('dk'); ylabel('Gözlem sayısı');
    axis([-0.5, 12.5, 0, n]);
    set(gca, 'xtick', 0:12);
    titleText = ['$\lambda$ =  ' num2str(lambda(i))];
    title(titleText, 'interpreter', 'latex', 'fontsize', 15);
end
%% plot normalized histogram and pdf
figure(2); clf; set(gcf,'Position',1e3*[0.0218,0.1074,1.5072,0.6544]);
for i=1:length(lambda)
    subplot(2,3,i);
    plot(X,lambda(i)*exp(-lambda(i).*X),'color','k','LineWidth',1.3);
    hold on;
    histogram(x(i,:),edges,'normalization','pdf','FaceColor',[0.75,0.75,0.75]);
    hold off;
    grid on; set(gca, 'gridlinestyle', '--');
    xlabel('dk'); ylabel('Gözlem');
    axis([-0.5, 12.5, 0, 1]);
    set(gca, 'xtick', 0:12);
    titleText = ['$\lambda$ =  ' num2str(lambda(i))];
    title(titleText, 'interpreter', 'latex', 'fontsize', 15);
    legend('$$f_X(x) = \lambda e^{-\lambda x}$$','interpreter','latex','fontsize',15);
end