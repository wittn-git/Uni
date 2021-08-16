%colors

blau(vorkogel).
blau(sonnalm).
blau(arbiskogel).
blau(wiesenalm).
blau(plattenalm).
rot(isskogel).
schwarz(teufeltal).

%start and end

start(sonnalm).
start(teufeltal).

endetIn(sonnalm, vorkogel).
endetIn(sonnalm, arbiskogel).
endetIn(teufeltal, wiesenalm).
endetIn(arbiskogel, plattenalm).
endetIn(plattenalm, wiesenalm).
endetIn(vorkogel, isskogel).
endetIn(wiesenalm, tal).
endetIn(isskogel, tal).

% Anfrage b)    endetIn(X,wiesenalm).

%same startingpoint

gleicherStartpunkt(X,Y) :- endetIn(Z,X),endetIn(Z,Y). 
gleicherStartpunkt(X,Y) :- start(X),start(Y).

% accessibility

erreichbar(X,Y) :- endetIn(X,Y),endetIn(Y, tal).
erreichbar(X,Y) :- endetIn(X,Y),endetIn(Y,Z),erreichbar(Y,Z).
erreichbar(X,Y) :- endetIn(X,Z),erreichbar(Z,Y).

% possible last track

moeglicheSchlusspiste(X,S) :-endetIn(X,S), endetIn(S, tal).
moeglicheSchlusspiste(X,S) :-endetIn(X,Y), moeglicheSchlusspiste(Y,S).

% meeting tracks

treffPisten(X,Y,T) :- erreichbar(X,T), erreichbar(Y,T).

% for beginners

anfaengerGeeignet(X) :- blau(X), endetIn(X, tal).
anfaengerGeeignet(X) :- blau(X), endetIn(X, Y), anfaengerGeeignet(Y).

% pathOfLength

pathOfLength(cons(tal, nil), 0).
pathOfLength(cons(H1, cons(H2, XS)), s(L)) :- pathOfLength(cons(H2, XS), L), endetIn(H1, H2).

% tourOfLength

tourOfLength(cons(tal, nil), 0).
tourOfLength(cons(tal, cons(H1, XS)), L) :- start(H1), tourHelper(cons(H1, XS), L).

tourHelper(cons(H1, cons(H2, XS)), s(L)) :- endetIn(H1,H2), tourOfLength(cons(H2, XS), L); endetIn(H1,H2), tourHelper(cons(H2, XS), L).

% partTour

partTour(P,T) :- tourOfLength(P, _), tourOfLength(T, _), partTourHelperBeginning(P, T).

partTourHelperBeginning(cons(H, XS), cons(H, YS)) :- partTourHelperEnding(cons(H, XS), cons(H, YS)).
partTourHelperBeginning(cons(H1, XS), cons(_, YS)) :- partTourHelperBeginning(cons(H1, XS), YS).

partTourHelperEnding(cons(tal, nil), _).
partTourHelperEnding(cons(H, XS), cons(H, YS)) :- partTourHelperEnding(XS, YS).

% convert

convert([H], cons(H, nil)).
convert([H|XS], cons(H, YS)) :- convert(XS,YS).

% enumerateTours

enumerateTours(T) :- convert(T, X), enumerateTours(X, 0).
enumerateTours(T, L) :- tourOfLength(T, L), enumerateTours(T, s(L)).

% tourRedBlack

tourRotSchwarz(T,R,S) :- 

tourRotSchwarz(cons(H, nil), R, suc(0)) :- schwarz(H).
tourRotSchwarz(cons(H, nil), suc(0), S) :- rot(H).
tourRotSchwarz(cons(H, nil), R, S).

tourRotSchwarz(cons(H, XS), R, S) :- schwarz(H), tourRotSchwarz(XS, R, suc(S)).
tourRotSchwarz(cons(H, XS), R, S) :- rot(H), tourRotSchwarz(XS, suc(R), S).
tourRotSchwarz(cons(H, XS), R, S) :- tourRotSchwarz(XS, R, S).