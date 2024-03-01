clc
clear all
close all
t=0:0.01:1
f1=4
f2=3
x1=sin(2*pi*f1*t)
x2=sin(2*pi*f2*t)
c=x1+x2
plot(c)
d=x1*x2
plot(d)
e=x1/x2
plot(e)