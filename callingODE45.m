tRange = [0 4*pi];
y0 = 0;
[tSol,ySol] = ode45(@myTrigODE,tRange,y0);
tExact = linspace(0,4*pi,40);
yExact = 1 - cos(tExact);
plot(tSol,ySol, "--")
xlabel("time")
ylabel("y")
hold on
plot(tExact,yExact,"m:o");
hold off
legend("ode45","exact")

function dydt = myTrigODE(t,y)
    % Define dydt:
    dydt = sin(t);
end
