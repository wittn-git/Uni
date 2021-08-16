multiples(X, 1, [X]) :- X>0.
multiples(X, N, [H|R]) :- X>0, N>0, K is N-1, multipleOf(X, N, H), multiples(X, K, R).

multipleOf(X, 1, X).
multipleOf(X, N, RES) :- (N > 0), (M is N-1), multipleOf(X, M, Y), (RES is Y+X).