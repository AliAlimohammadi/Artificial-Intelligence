% Author:    Ali Alimohammadi
%   Date:    Dec 26th, 2020.

% Reverse function signature to call the corresponding functions.
reverse(List, RevList) :-
    reverse(List, RevList, []).

% Reverse for empty lists.
reverse([], L, L).

% Recursive call of reverse function to sub-lists
% that have been already reversed.
reverse([H|T], L, SoFar) :-
    reverse(T, L, [H|SoFar]).