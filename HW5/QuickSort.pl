% Author:    Ali Alimohammadi
%   Date:    Dec 26th, 2020.

% QuickSort for empty inputs.
quicksort([],[]).
% QuickSort for non-empty inputs.
quicksort([H|T],Sorted) :-
    % QuickSort Partition function (to pick a pivot element).
    partition(H,T,Less,Greater),
    % Sort the left sub-array using recursive call of QuickSort.
    quicksort(Less,SortedLess),
    % Sort the right sub-array using recursive call of QuickSort.
    quicksort(Greater,SortedGreater),
    % Merge the two sorted sub-arrays.
    append(SortedLess,[H|SortedGreater],Sorted).

% Partition for empty inputs.
partition(_,[],[],[]).
% Partition for non-empty inputs.
% Case that the element is Less than/Equal to pivot element.
partition(P,[H|T],[H|Less],Greater) :-
    H =< P,
    partition(P,T,Less,Greater).
% Case that the element is Greater than pivot element.
partition(P,[H|T],Less,[H|Greater]) :-
    H > P,
    partition(P,T,Less,Greater).