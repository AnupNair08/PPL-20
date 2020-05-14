city(toronto,50,60).
city(london,75,80).
city(madrid,75,45).
city(barcelona,40,30).
city(malaga,50,30).
city(valencia,40,20).
city(paris,56,60).
city(toulouse,40,30).


/*toronto to madrid*/
flight(united,toronto,madrid,950,540).
flight(iberia,toronto,madrid,800,480).
flight(aircanada,toronto,madrid,900,480).
/*toronto to london*/
flight(aircanada,toronto,london,500,360).
flight(united,toronto,london,650,420).
/*madrid to barcelona*/
flight(aircanada,madrid,barcelona,100,60).
flight(iberia,madrid,barcelona,120,65).

/*madrid to valencia*/
flight(iberia,madrid,valencia,40,50).
/*madrid to malaga*/
flight(iberia,madrid,malaga,50,60).

/*paris to toulouse*/
flight(united,paris,toulouse,35,120).
flight(iberia,london,barcelona,220,240).
flight(iberia,valencia,barcelona,110,75).
flight(iberia,valencia,malaga,80,120).

chkflight(X,Y,Z,P,D) :- flight(Y,X,Z,P,D),
                        write('\nAirline '),
                        write(Y),
                        write(' exists from '),
                        write(X),
                        write(' to '),
                        write(Z),
                        write(' with a price of $'),
                        write(P),
                        write(' and a duration of '),
                        write(D),
                        write(' min') ; 
                        flight(Y,Z,X,P,D),
                        write('\nAirline '),
                        write(Y),
                        write(' exists from '),
                        write(Z),
                        write(' to '),
                        write(X),
                        write(' with a price of $'),
                        write(P),
                        write(' and a duration of '),
                        write(D),
                        write(' min') .



/*Gets all the cities in the database*/
airport(X) :- city(X,Y,Z),
                write('\nAirport tax is $'),
                write(Y),
                write('\nMinimum security delay is '),
                write(Z),
                write(' min\n').


/*Displays whether X and Y are directly connected or not. If yes displays the name of one of the direct flights*/
direct(X,Y) :- (
    flight(Z,X,Y,_,_),
    write('\nDirect flight is '),
    write(Z), 
    write('\n') ; 
    flight(Z,Y,X,_,_),
    write('\nDirect flight is '),
    write(Z), 
    write('\n')
).

/*Query that checks if there is a  direct flight from X to Y named Z and also lists all directly connected cities and airlines*/
df(X,Y,Z) :- flight(Z,X,Y,_,_).

/*Query that checks for flights that are classified as cheap */
cheapflight(X,Y):-
    flight(Z,X,Y,P,_) , <(P,400),
    write('Flight with price less than $400 is : '),
    write(Z),
    write(' with price $'),
    write(P).

/*Query that checks if it is possible to go between two cities in two flights*/
twoflight(X,Y) :- direct(X,Z) , direct(Z,Y).

/*Query to check if there is a preferable flight between X,Y */
prefer(X,Y) :- (
    flight(Z,X,Y,P,_) , (<(P,400) ; ==(Z,'aircanada')),
    write('\nPreferable flight found is : '),
    write(Z)
).

/*Query to check if there are united and aircanada flights between X and Y*/
check(X,Y):-(
    write('\nCities which have both united and aircanada flights are :'),
    flight(Z,X,Y,_,_) , (==(Z,'united')) ,  (flight(W,X,Y,_,_) , ==(W,'aircanada'))
).