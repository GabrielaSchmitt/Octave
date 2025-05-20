# Gráficos 2D

x = -2*pi:.1:2*pi
#y = cos(x)
#plot(x,y, '--hm')

subplot(2,2,1)
plot(x, cos(x))

subplot(2,2,2)
plot(x, x.^2)

subplot(2,2,3)
plot(x, x.^3)

subplot(2,2,4)
plot(x, tan(x))

# Gráficos 3D
# curvas no espaço, malhas e superfícies

#plot3(x,y,z)
#[X,Y]=meshgrid(x,y)  malha
#surf(x,y)  superficies

x=1:.1:10;
y=x;
[X,Y]=meshgrid(x,y)
Z=X.^2+Y.^2;
surf(X,Y,Z)

## EX 1

# Define a função
f = @(x) 0.6 .* x.^5 - 5 .* x.^3 + 9 .* x + 2;

# Primeiro intervalo: -4 a 4
x1 = -4:0.1:4;
y1 = f(x1);

# Segundo intervalo: -2.7 a 2.7
x2 = -2.7:0.1:2.7;
y2 = f(x2);

# Gráficos
figure

subplot(1,2,1)
plot(x1, y1, 'b', 'LineWidth', 2)
title('f(x) no intervalo [-4, 4]')
xlabel('x')
ylabel('f(x)')
grid on

subplot(1,2,2)
plot(x2, y2, 'r', 'LineWidth', 2)
title('f(x) no intervalo [-2.7, 2.7]')
xlabel('x')
ylabel('f(x)')
grid on

## EX 2

x = -10:0.1:10;
f = @(x) (x.^2 - x + 1) ./ (x.^2 + x + 1);
y = f(x);

figure
plot(x, y, 'b', 'LineWidth', 2)
title('Exercício 2: f(x) = (x^2 - x + 1)/(x^2 + x + 1)')
xlabel('x')
ylabel('f(x)')
grid on


## EX 3

f = @(x) (1.5 .* x) ./ (x - 4);

x1 = -10:0.1:3.7;
x2 = 4.3:0.1:10;

y1 = f(x1);
y2 = f(x2);

figure
plot(x1, y1, 'b', 'LineWidth', 2)
hold on
plot(x2, y2, 'r', 'LineWidth', 2)
title('Exercício 3: f(x) = (1.5x)/(x - 4)')
xlabel('x')
ylabel('f(x)')
legend('x < 4', 'x > 4')
grid on

## EX 4

f = @(x) (x.^2 - 5*x + 10) ./ (x.^2 - 2*x - 3);

x1 = -10:0.1:-1.7;    % antes da primeira descontinuidade (x = -1)
x2 = -0.3:0.1:2.7;    % entre as duas descontinuidades (x = -1 e x = 3)
x3 = 3.3:0.1:10;      % depois da segunda descontinuidade (x = 3)

y1 = f(x1);
y2 = f(x2);
y3 = f(x3);

figure
plot(x1, y1, 'b', x2, y2, 'g', x3, y3, 'r', 'LineWidth', 2)
ylim([-20, 20])
title('Exercício 4: f(x) = (x^2 - 5x + 10)/(x^2 - 2x - 3)')
xlabel('x')
ylabel('f(x)')
legend('x < -1', '-1 < x < 3', 'x > 3')
grid on


## EX 5

f = @(x) 3 .* x .* sin(x) - 2 .* x;
df = @(x) 3 .* sin(x) + 3 .* x .* cos(x) - 2;

x = -2*pi:0.1:2*pi;
y = f(x);
dy = df(x);

figure
plot(x, y, 'b', 'LineWidth', 2)
hold on
plot(x, dy, '--r', 'LineWidth', 2)
title('Exercício 5: f(x) = 3x·sin(x) - 2x e sua derivada')
xlabel('x')
ylabel('f(x) e f''(x)')
legend('f(x)', 'f''(x)')
grid on


## EX 6

x = -3:0.1:3;
y = -3:0.1:3;
[X, Y] = meshgrid(x, y);

Z = 1.8.^(-1.5 * sqrt(X.^2 + Y.^2)) .* sin(X) .* cos(0.5 * Y);

figure
surf(X, Y, Z)
title('Exercício 6: Gráfico 3D da função z(x,y)')
xlabel('x')
ylabel('y')
zlabel('z')


