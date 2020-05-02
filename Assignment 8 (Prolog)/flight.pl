f1([1900,2100],[Delhi,Mumbai]).
f2([1900,2100],[Chennai,Rajasthan]).
f3([1900,2100],[Mumbai,Bangalore]).
f4([1900,2100],[Assam,Pune]).

on(Item,[Item|Rest]).  

on(Item,[DisregardHead|Tail]) :- on(Item,Tail).