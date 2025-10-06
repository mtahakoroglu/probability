sigma = 3;
n = 100;
R = chol(sigma);
x = round(randn(n,1)*R);
histogram(x,10);
grid on; set(gca, 'gridlinestyle', '--');
xlabel('dk')
set(gca, 'xticklabel', {'56','57','58','59','0','1','2','3','4','5','6'})
set(gca, 'ytick', [1,2,8,9,16,20,22], 'yticklabel', {'1','2','8','9','16','20','22'})
ylabel('Gözlem sayısı');