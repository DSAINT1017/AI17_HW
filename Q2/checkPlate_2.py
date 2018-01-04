
legalPos = [                                                [-4,8],
                                                        [-4,7],[-3,7],
                                                    [-4,6],[-3,6],[-2,6],
                                                [-4,5],[-3,5],[-2,5],[-1,5],
                  [-8,4],[-7,4],[-6,4],[-5,4],[-4,4],[-3,4],[-2,4],[-1,4],[0,4],[1,4],[2,4],[3,4],[4,4],
                     [-7,3],[-6,3],[-5,3],[-4,3],[-3,3],[-2,3],[-1,3],[0,3],[1,3],[2,3],[3,3],[4,3],
                        [-6,2],[-5,2],[-4,2],[-3,2],[-2,2],[-1,2],[0,2],[1,2],[2,2],[3,2],[4,2],
                           [-5,1],[-4,1],[-3,1],[-2,1],[-1,1],[0,1],[1,1],[2,1],[3,1],[4,1],
                               [-4,0],[-3,0],[-2,0],[-1,0],[0,0],[1,0],[2,0],[3,0],[4,0],
                            [-4,-1],[-3,-1],[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],
                        [-4,-2],[-3,-2],[-2,-2],[-1,-2],[0,-2],[1,-2],[2,-2],[3,-2],[4,-2],[5,-2],[6,-2],
                    [-4,-3],[-3,-3],[-2,-3],[-1,-3],[0,-3],[1,-3],[2,-3],[3,-3],[4,-3],[5,-3],[6,-3],[7,-3],
                [-4,-4],[-3,-4],[-2,-4],[-1,-4],[0,-4],[1,-4],[2,-4],[3,-4],[4,-4],[5,-4],[6,-4],[7,-4],[8,-4],
                                                [1,-5],[2,-5],[3,-5],[4,-5],
                                                    [2,-6],[3,-6],[4,-6],
                                                        [3,-7],[4,-7],
                                                            [4,-8]
            ]


# start position
agentStartPos = [
                    [0,-4],  [1,-4], [2,-4], [3,-4], [4,-4],
                    [1,-5],  [2,-5], [3,-5], [4,-5],
                    [2,-6],  [3,-6], [4,-6],
                    [3,-7],  [4,-7],
                    [4,-8]
                ]

# final position 1
agentFinalPos = [
                    [-8,4],[-7,4],[-6,4],[-5,4],[-4,4],
                    [-7,3],[-6,3],[-5,3],[-4,3],
                    [-6,2],[-5,2],[-4,2],
                    [-5,1],[-4,1],
                    [-4,0],
                ]


# available movement
actionMoves = [[1,-1], [0,1], [0,-1], [-1,1], [1,0], [-1,0]]

# available hop
actionHops = [[2,-2], [0,2], [0,-2], [-2,2], [2,0], [-2,0]]

class Check():

    def __init__(self, pos, initPos, name):
        self.pos = pos
        self.initPos = initPos
        self.name = name
        self.moveable = False
        self.ended = False

    def getPosition(self) :
        return self.pos

    def move(self, pos) :
        self.pos = pos

    def isMoveable(self) :
        return self.moveable

    def setMoveable(self, flag) :
        self.moveable = flag

    def setEnded(self):
        self.ended = True

    def isEnded(self):
        return self.ended

    def __str__(self) :
        return '%s at %s' % ( self.name, str( self.pos ) )

    def printout(self) :
        return "%s Move From %s to %s." % ( self.name, str( self.initPos ), str( self.pos ) )





