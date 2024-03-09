% Define parent-child relationships
parent(john, mary).
parent(john, jim).
parent(jane, mary).
parent(jane, jim).
parent(mary, anne).
parent(mary, patrick).
parent(jim, kate).


% Define grandparent-grandchild relationships
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).


% Define sibling relationships
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.


% Define cousin relationships (children of siblings)
cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W), X \= Y.


% Define aunt/uncle-niece/nephew relationships
aunt(X, Y) :- parent(Z, Y), sibling(X, Z), female(X).
uncle(X, Y) :- parent(Z, Y), sibling(X, Z), male(X).


% Define spouse relationships
married(john, jane).
married(jane, john).


% Define gender of individuals
male(john).
male(jim).
male(patrick).
male(Z) :- \+ female(Z).


female(jane).
female(mary).
female(anne).
female(kate).
female(Z) :- \+ male(Z).
