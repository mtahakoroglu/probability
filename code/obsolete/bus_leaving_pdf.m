clf;
lambda = [3,2,1,1/2,1/5,1/10];
n = 10000;
edges = 0:12;
T = 0.01;
X = 0:T:edges(end);
figure(1);
for i=1:length(lambda)
    subplot(2,3,i);
    x = exprnd(1/lambda(i),1,n);
    histogram(x,edges,'FaceColor',[0.75,0.75,0.75]);
    grid on; set(gca, 'gridlinestyle', '--');
    xlabel('dk'); ylabel('Gözlem sayısı');
    axis([-0.5, 12.5, 0, 10000])
    set(gca, 'xtick', 0:12);
    titleText = ['$\lambda$ =  ' num2str(lambda(i))];
    title(titleText, 'interpreter', 'latex', 'fontsize', 15);
end
% set(gca, 'ytick', [2,3,5,6,11,18,27,45,81], 'yticklabel', {'2','3','5','6','11','18','27','45','81'});
% text(0.3,53,'51'); text(1.3,33,'31'); text(2.3,22,'20');
% text(3.3,12,'10'); text(4.3,10,'8'); text(5.3,7,'5'); 
% text(6.3,8,'6'); text(7.3,6,'4'); text(8.3,5,'3'); 
% text(9.3,3,'1'); text(10.3,3,'1');
% text(5.3,9,'7');
% text(6.3,7,'5'); text(7.3,4,'2'); text(8.3,3,'1');