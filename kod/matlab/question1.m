clear; clc;
n = 10000; % örnek sayısı (number of samples)
k = 6; % öğrenci sayısı
student = ['E','E','E','E','K','K']; % başlangıç durumu, istenildiği gibi olabilir
count = 0; % kızların yanyana geldiği durumlar
for i=1:n
    girl_index = find(student(randperm(k)) == 'K');
    if abs(girl_index(1)-girl_index(2)) == 1 % yanyana iseler sıra numaraları farkı 1 olmalı
        count = count+1;
    end
end
fprintf('Toplam %i örnekle yapılan denemede olasılık %.3f bulundu.\n', n, count/n);