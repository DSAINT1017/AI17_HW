import os 
import json

# chess position
legalPos = [                                                [13, 1],
                                                        [12, 2],[14, 2],
                                                    [11, 3],[13, 3],[15, 3],
                                                [10, 4],[12, 4],[14, 4],[16, 4],
            [ 1, 5],[ 3, 5],[ 5, 5],[ 7, 5],[ 9, 5],[11, 5],[13, 5],[15, 5],[17, 5],[19, 5],[21, 5],[23, 5],[25, 5],
                [ 2, 6],[ 4, 6],[ 6, 6],[ 8, 6],[10, 6],[12, 6],[14, 6],[16, 6],[18, 6],[20, 6],[22, 6],[24, 6],  
                    [ 3, 7],[ 5, 7],[ 7, 7],[ 9, 7],[11, 7],[13, 7],[15, 7],[17, 7],[19, 7],[21, 7],[23, 7],          
                        [ 4, 8],[ 6, 8],[ 8, 8],[10, 8],[12, 8],[14, 8],[16, 8],[18, 8],[20, 8],[22, 8],                  
                            [ 5, 9],[ 7, 9],[ 9, 9],[11, 9],[13, 9],[15, 9],[17, 9],[19, 9],[21, 9],                          
                        [ 4,10],[ 6,10],[ 8,10],[10,10],[12,10],[14,10],[16,10],[18,10],[20,10],[22,10],                  
                    [ 3,11],[ 5,11],[ 7,11],[ 9,11],[11,11],[13,11],[15,11],[17,11],[19,11],[21,11],[23,11],          
                [ 2,12],[ 4,12],[ 6,12],[ 8,12],[10,12],[12,12],[14,12],[16,12],[18,12],[20,12],[22,12],[24,12],  
            [ 1,13],[ 3,13],[ 5,13],[ 7,13],[ 9,13],[11,13],[13,13],[15,13],[17,13],[19,13],[21,13],[23,13],[25,13],
                                                [10,14],[12,14],[14,14],[16,14],
                                                    [11,15],[13,15],[15,15],
                                                        [12,16],[14,16],
															[13,17]
			]



# start position
agentStartPos = [ [9,13], [11,13], [13,13], [15,13], [17,13], \
				[10,14], [12,14], [14,14], [16,14], [11,15], [13,15], [15,15], [12,16], [14,16], [13,17]]

# final position
agentFinalPos = [ [13, 1], [12, 2], [14, 2], [11, 3], [13, 3], [15, 3], [10, 4], [12, 4], [14, 4], [16, 4], \
				[ 9, 5],[11, 5],[13, 5],[15, 5],[17, 5]]

# print agentStartPos, len( agentStartPos )
# print agentFinalPos, len( agentFinalPos )
                

# available movement
actionMoves = [[1,1], [1,-1], [-1,1], [-1,-1], [2,0], [-2,0]];

# available hop
actionHops = [[2,2], [2,-2], [-2,2], [-2,-2], [4,0], [-4,0]];


xscale=30;
yscale=40;
radius=15;

def add( x, y ) :
	return [ x[0]+y[0], x[1]+y[1] ]

def minus( x, y ) :
	return [ x[0]-y[0], x[1]-y[1] ]

def getForwordMoveSpace( checker ) :
	spaces = list()
	for i in [1, 3, 4, 5] :
		spaces.append( add( checker, actionMoves[i] ) )
		spaces.append( add( checker, actionHops[i] ) )
	return spaces

def getAllMoveSpace( checker ) :
	spaces = list()
	assert len( actionMoves ) == len( actionHops )
	for i in range( len( actionMoves ) ) :
		spaces.append( add( checker, actionMoves[i] ) )
		spaces.append( add( checker, actionHops[i] ) )
	return spaces


if __name__ == '__main__':
	print( getAllMoveSpace( [13, 13] ) )














