
p(s,sa).
p(sa,a).
gp(X,Y) :- p(X,Z) , p(Z,Y).
