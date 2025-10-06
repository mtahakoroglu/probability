clearvars, clc;
mu = [0,0,0,-2]; sigma = [sqrt(0.2),1,sqrt(5),sqrt(0.5)];
n = 10000;
edges = -5:0.5:5;
T = 0.01;
X = -5:T:edges(end);
figure(2); clf;
for i=1:length(mu)
    subplot(2,2,i);
    f = (1/sqrt(2*pi*sigma(i)^2))*exp(-0.5*((X-mu(i))/sigma(i)).^2);
    plot(X,f,'color','k','LineWidth',1.3);
    hold on;
    x = sigma(i)*randn(1,n)+mu(i);
    histogram(x,edges,'normalization','pdf', 'FaceColor',[0.75,0.75,0.75]);
    hold off;
    grid on; set(gca, 'gridlinestyle', '--');
    xlabel('dk'); ylabel('Gözlem sayısı');
    axis([-5, 5, 0, 1]);
    set(gca, 'xtick', -5:5);
    legendText = ['$$\mu$$ = ' num2str(mu(i)) '$$\;\;\sigma^2$$ = ' num2str(sigma(i)^2)];
    legend(legendText,'interpreter','latex','fontsize',13);
end