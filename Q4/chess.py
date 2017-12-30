from checkPlate import *
from random import randint
import time

Checkers = []

for pos in agentStartPos :
    Checkers.append( Check( pos ) )

def nowPositions( checkerPositions ) :
    hasCheck = [False] * len( legalPos )
    if all( pos in legalPos for pos in checkerPositions ) :
        for check in checkerPositions :
            hasCheck[ legalPos.index( check ) ] = True
    # print( hasCheck )
    return hasCheck

hasCheck = nowPositions( agentStartPos )

def add( x, y ) :
    return [ x[0]+y[0], x[1]+y[1] ]

def minus( x, y ) :
    return [ x[0]-y[0], x[1]-y[1] ]

def moveWay( x, y ):
    # print( x, y )
    return ( ( x[0] * y[0] ) >= 0 and ( x[1] * y[1] ) >= 0 )


def getMoveSpace( checker ) :
    space = list()
    for i in range( len( actionMoves ) ) :
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


def setMoveable() :
    for checker in Checkers :
        if getMoveSpace( checker.pos ) :
            checker.setMoveable( True )
        else :
            checker.setMoveable( False )


def selectChecker() :
    tmp = []
    [ tmp.append( checker ) for checker in Checkers if checker.isMoveable() ]
    return tmp[ randint( 0, len(tmp)-1 )]


def moveChecker( checker ) :
    for i in range( len(agentFinalPos) ) :
        if not hasCheck[ legalPos.index( agentFinalPos[i] ) ] and not checker.isEnded():
            print( agentFinalPos[i] )
            print( 'Before', checker, '\n' )

            moveCheck = []
            vectorFinal = minus( agentFinalPos[i], checker.pos )
            for item in getMoveSpace( checker.pos ) :
                vectorMove = minus( item, checker.pos )
                if moveWay( vectorMove, vectorFinal ) :
                    moveCheck.append( item )

            hasCheck[ legalPos.index( checker.pos ) ] = False
            if not moveCheck :
                return
            checker.move( moveCheck[0] )
            setMoveable()
            hasCheck[ legalPos.index( checker.pos ) ] = True
            print( 'After', checker )
            print( '-----------------------------------------' )

            if checker.pos == agentFinalPos[i] :
                checker.setEnded()
            return


def checkersIsFinished() :
    for checker in Checkers :
        if not checker.isEnded() :
            return False
    return True


def testChecker() :
    for item in Checkers :
        print( item )


if __name__ == '__main__':

    # testCheck = [12, 16]
    # print( getMoveSpace( testCheck, hasCheck ) )
    setMoveable()
    with open( 'status.txt', 'w+', encoding='UTF-8' ) as f :
        f.writelines( str( hasCheck ) + '\n' )
        while not checkersIsFinished() :
            moveChecker( selectChecker() )
            time.sleep( 0.2 )

        f.writelines( '--------------------------------\n' )
        f.writelines( str( hasCheck ) + '\n' )


    print("")
    testChecker()














