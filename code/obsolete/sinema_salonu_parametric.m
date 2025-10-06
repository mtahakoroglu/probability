clear all; close all; clc;
n = 1e5;
k = 4;
together = 0;
for i=1:n
    seat = randi(k*k, 1, 2);
    while (seat(1) == seat(2))
        seat(2) = randi(k*k);
    end
    if (abs(seat(1)-seat(2)) == 1) && (ceil(seat(1)/k) == ceil(seat(2)/k))
        together = together+1;
    end
end
fprintf('Olasılık (analitik) = %.5f\n', ((k-2)/k)*(2/(k*k-1))+(2/k)*(1/(k*k-1)));
fprintf('Olasılık (nümerik) = %.5f\n', together/n);

