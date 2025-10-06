clearvars, clc;
mu = 5; sigma = 0.1;
n = 10000;
x_min_max = 0.5;
binSize = 0.1;
edges = mu-x_min_max:binSize:mu+x_min_max;
T = 0.01;
x = min(edges):T:edges(end);
figure(1); clf;
f = (1/sqrt(2*pi*sigma^2))*exp(-0.5*((x-mu)/sigma).^2);
plot(x,f,'color','k','LineWidth',1.3);
hold on;
X = sigma*randn(1,n)+mu;
h = histogram(X, edges, 'normalization','pdf', 'FaceColor',[0.75,0.75,0.75]);
h.Values*n
hold off;
for i=1:length(h.Values)
    % map [1, 10] to [mu-x_min_max+binSize/2, mu+x_min_max-binSize/2]
    x = ((i-1)/(length(h.Values)-1))*((mu+x_min_max-binSize/2)- ...
        (mu-x_min_max+binSize/2))+(mu-x_min_max+binSize/2);
    text(x-binSize/2, h.Values(i)+0.1, num2str(h.Values(i)*n/10));
end
grid on; set(gca, 'gridlinestyle', '--');
xlabel('x', 'fontsize', 14);
ylabel(['Gözlem sayısı (n=', num2str(n),')'], 'fontsize', 14);
% axis([-6, 2, 0, 0.6]);
% set(gca, 'xtick', -5:5);
legend('$$f_X(x)$$', 'MCS','interpreter','latex','fontsize',15);
t = title(['$$\mu$$ = ', num2str(mu), '$$\;\;\sigma$$ = ', num2str(sigma)]);
t.set('interpreter','latex','fontsize',15);