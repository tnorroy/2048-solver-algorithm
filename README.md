This code creates a square matrix of size 4 to simulate the game grid. The algorithm searches for the best move at each iteration using a recursive function of variable depth. 
A matrix of weights is used to influence the algorithm so that it plays in a manner similar to that of a human (i.e. it places the squares in the corners preferentially). 
The "profondeur" variable corresponds to the number of moves performed by the recursive function and the "repetition" variable corresponds to the number of times each move is repeated, to take into account the effects of randomness.
