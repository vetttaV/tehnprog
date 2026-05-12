
/* родственные отношения */
parent(charlie, alice).
parent(diane, alice).
parent(charlie, bob).
parent(diane, bob).
parent(gregory, emily).
parent(harry, emily).
parent(gregory, fred).
parent(harry, fred).
parent(ian, diane).
parent(jack, diane).
parent(kevin, diane).
parent(ian, gregory).
parent(jack, gregory).
parent(kevin, gregory).
parent(michael, linda).
parent(norman, linda).
parent(michael, kevin).
parent(norman, kevin).
parent(oscar, fred).


child(X, Y) :- parent(Y,X).
grandchild(X, Y) :- parent(Z,X), parent(Y,Z).

woman(alice).
woman(diane).
woman(emily).
woman(linda).
man(bob).
man(charlie).
man(fred).
man(gregory).
man(harry).
man(ian).
man(jack).
man(kevin).
man(michael).
man(norman).
man(oscar).

grandmother(X,Y) :- grandchild(Y, X), woman(Y).
unkle(X,Y) :- parent(X,P), parent(P,D), parent(Y,D), man(Y), dif(Y,P).
sister(X,Y) :- parent(X,P), parent(Y,P),
               woman(X), woman(Y), dif(X,Y).

ancestor(X, Y) :- parent(X,Y).
ancestor(X, Y) :- parent(X,Z), ancestor(Z, Y).

/* членство в списке */
member(X, [X | _], yes).
member(_, [], no).
member(X, [_ | T], Answer) :- member(X, T, Answer).
has_kids_with_two_partners(X) :-
    parent(X, C1),
    parent(P1, C1),
    P1 \= X,

    parent(X, C2),
    parent(P2, C2),
    P2 \= X,

    P1 \= P2.

remove_third([], []).

remove_third([X], [X]).

remove_third([X, Y], [X, Y]).

remove_third([X, Y, _ | Tail], [X, Y | ResultTail]) :-
    remove_third(Tail, ResultTail).
even_length([]).

even_length([_, _ | Tail]) :-
    even_length(Tail).

is_prefix([], _).
is_prefix([H | SubTail], [H | ListTail]) :-
    is_prefix(SubTail, ListTail).


is_sublist(Sub, List) :-
    is_prefix(Sub, List).
is_sublist(Sub, [_ | Tail]) :-
    is_sublist(Sub, Tail).


join_lists([], L, L).
join_lists([H | T], L, [H | Res]) :-
    join_lists(T, L, Res).


flatten_one_level([], []).
flatten_one_level([HeadList | TailLists], Result) :-
    flatten_one_level(TailLists, TailResult),
    join_lists(HeadList, TailResult, Result).