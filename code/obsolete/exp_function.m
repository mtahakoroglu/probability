clearvars, clc;
T = 0.01;
x = -1:T:0;
figure(1);
plot(x,exp(x),'k-','LineWidth',1.3);
grid on; set(gca,'gridlinestyle','--','FontSize',16);
xlabel('x','FontSize',15); ylabel('f(x)','FontSize',15);
leg = legend('$$f(x) = e^x$$','interpreter','latex');
set(leg,'fontsize',20,'Location','northwest');