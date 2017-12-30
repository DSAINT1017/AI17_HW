from checkPlate import legalPos
from checkPlate import Check

# start position
Checkers = []
agentStartPos = [
                    [9,13], [11,13], [13,13], [15,13], [17,13],
                    [10,14], [12,14], [14,14], [16,14],
                    [11,15], [13,15], [15,15],
                    [12,16], [14,16],
                    [13,17]
                ]

# final position
agentFinalPos = [
                    [13, 1],
                    [12, 2], [14, 2],
                    [11, 3], [13, 3], [15, 3],
                    [10, 4], [12, 4], [14, 4], [16, 4],
                    [9, 5],[11, 5],[13, 5],[15, 5],[17, 5]
                ]

# available movement
actionMoves = [[1,1], [1,-1], [-1,1], [-1,-1], [2,0], [-2,0]]

# available hop
actionHops = [[2,2], [2,-2], [-2,2], [-2,-2], [4,0], [-4,0]]

for pos in agentStartPos :
    Checkers.append( Check( pos ) )
# for check in Checkers :
    # print( check, check.isMoveable() )

# xscale=30;
# yscale=40;
# radius=15;

def add( x, y ) :
    return [ x[0]+y[0], x[1]+y[1] ]

# def minus( x, y ) :
#     return [ x[0]-y[0], x[1]-y[1] ]

def getForwordMoveSpace( checker, hasCheck ) :
    space = list()
    for i in [1, 3, 4, 5] :
        try :
            posMove = add( checker, actionMoves[i] )
            if not hasCheck[ legalPos.index( posMove ) ] :
                space.append( posMove )
            else :
                posHop = add( checker, actionHops[i] )
                if not hasCheck[ legalPos.index(posHop) ] :
                    space.append( add( checker, actionHops[i] ) )
                else :
                    pass
        except :
            pass
    return space

# def getAllMoveSpace( checker ) :
#     spaces = list()
#     assert len( actionMoves ) == len( actionHops )
#     for i in range( len( actionMoves ) ) :
#         spaces.append( add( checker, actionMoves[i] ) )
#         spaces.append( add( checker, actionHops[i] ) )
#     return spaces

def nowPositions( checkerPositions ) :
    hasCheck = [False] * len( legalPos )
    if all( pos in legalPos for pos in checkerPositions ) :
        for check in checkerPositions :
            hasCheck[ legalPos.index( check ) ] = True

    return hasCheck

# def getMoveableCheck( checkPositions ) :
#     moveableChecks = []
#     for check in checkPositions :
#         if moveable( check ) :
#             pass
#     return moveableChecks

def moveable( check, hasCheck ) :
    space = getForwordMoveSpace( check )
    print( space )
    for item in space :
        try :
            if not hasCheck[ legalPos.index( item )] :
                print( item )
        except Exception as e :
            pass
    return True

if __name__ == '__main__':
    testCheck = [16, 14]
    hasCheck = nowPositions( agentStartPos )
    print( getForwordMoveSpace( testCheck, hasCheck ) )
    # print( moveable( testCheck, hasCheck ) )
    # print( legalPos.index( [13,18] ) )














