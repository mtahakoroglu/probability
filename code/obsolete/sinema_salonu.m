clear all; close all; clc;
n = 1e5;
together = 0;
for i=1:n
    seat = randi(100, 1, 2);
    while (seat(1) == seat(2))
        seat(2) = randi(100);
    end
    if (abs(seat(1)-seat(2)) == 1) && (ceil(seat(1)/10) == ceil(seat(2)/10))
        together = together+1;
    end
end
fprintf('Olasılık (analitik) = %.5f\n', 1/55);
fprintf('Olasılık (nümerik) = %.5f\n', together/n);

