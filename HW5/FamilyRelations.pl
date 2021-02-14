% Author:    Ali Alimohammadi
%   Date:    Dec 26th, 2020.

%  Facts and Rules of the program and their meaning are as follows:
%      father(X,Y) means X is Y’s father.
%      mother(X,Y) means X is Y’s mother.
%      female(X) means X is a female.
%      male(X) means X is a male.
%      husband(X,Y) means X is Y’s husband
%      parent(X,Y) means X is Y’s parent.
%      grandfather(X,Y) means X is Y’s grandfather.
%      grandparent(X,Y) means X is Y’s grandparent.
%      children(X,Y) means X is Y’s child.
%      son(X,Y) means X is Y’s son.
%      daughter(X,Y) means X is Y’s daughter.
%      sibling(X,Y) means X and Y are siblings.
%      h-mother-in-law(X,Y) means X is Y’s husband’s mother.
%      h-father-in-law(X,Y) means X is Y’s husband’s father.
%      w-mother-in-law(X,Y) means X is Y’s wife’s mother.
%      w-father-in-law(X,Y) means X is Y’s wife’s father.

% Knowledge Base:
father(vin,aby).
father(ral,nic).
father(chris,vin).
father(vin,sky).
mother(gina,vin).
mother(nic,aby).
mother(ala,nic).
mother(nic,sky).
female(aby).
female(nic).
female(ala).
female(gina).
female(sky).
male(ral).
male(vin).
male(chris).

% Relations:
parent(X,Y) :- father(X,Y);mother(X,Y).
grandparent(X,Y) :- parent(X,M),parent(M,Y).
children(X,Y) :- parent(Y,X).
husband(X,Y) :- male(X),female(Y),children(M,X),children(M,Y).
sibling(X,Y) :- mother(M,X),mother(M,Y),father(F,X),father(F,Y),X=Y.
grandfather(X,Y) :- father(X,K),father(K,Y).
grandfather(X,Y) :- father(X,K),mother(K,Y).
grandmother(X,Y) :- mother(X,K),mother(K,Y).
grandmother(X,Y) :- mother(X,K),father(K,Y).
h-mother-in-law(X,Y) :- mother(X,K),male(K),husband(K,Y).
w-mother-in-law(X,Y) :- mother(X,K),female(K),husband(Y,K).
h-father-in-law(X,Y) :- father(X,K),male(K),husband(K,Y).
w-father-in-law(X,Y) :- father(X,K),female(K),husband(Y,K).
son(X,Y) :- children(X,Y),male(X).
daughter(X,Y) :- children(X,Y),female(X).


