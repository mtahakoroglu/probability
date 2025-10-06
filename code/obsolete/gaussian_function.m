clearvars, clc;
T = 0.01;
x = -5:T:5;
mu = [0,0,0,-2]; sigma = [sqrt(0.2),1,sqrt(5),sqrt(0.5)]; color = {'k','r','b','g'};
%%
figure(1); clf;
hold on;
legendText = {'','','',''};
for i=1:length(mu)
    f = (1/sqrt(2*pi*sigma(i)^2))*exp(-0.5*((x-mu(i))/sigma(i)).^2);
    plot(x,f,color{i},'linewidth',1.3);
    legendText{i} = ['$$\mu$$ = ' num2str(mu(i)) '$$\;\;\sigma^2$$ = ' num2str(sigma(i)^2)];
end
hold off;
grid on; set(gca,'gridlinestyle','--');
xlabel('x','FontSize',14,'interpreter','latex');
ylabel('$f_X(x)$','FontSize',14,'interpreter','latex');
legend(legendText{1},legendText{2},legendText{3},legendText{4},...
    'interpreter','latex','fontsize',13);
axis([-5, 5, 0, 1]);
set(gca,'XTick',-5:5);