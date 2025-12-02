#1. Create a Prolog knowledge base representing family relationships (e.g., parent, child, sibling).
# 2. Write queries to determine relationships like ancestors and siblings.

#parent(odin, thor).
#parent(odin, loki).
#sibling(X, Y) :- parent(Z, X), parent(Z, Y).
#child(X, Y) :- parent(Y, X).

#?- child(X, odin).