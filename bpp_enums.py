from enum import Enum

class RTYenum(Enum):
    rpNO = -1
    rpX = 0
    rpY = 1
    rpXY = 2
    rpCIR = 3
    rpAL = 5

class CKAenum(Enum):
    azrNO = 0
    azrABS = 1
    azrINC = 2
    azrRELATIVE = 3

class RMDenum(Enum):
    rmdAuto = -1
    rmdComplete = 1
    rmdPartial = 2
    rmdQuote = 3

class BoolEnum(Enum):
    YES = 1
    NO = 0

class S32DIRenum(Enum):
    drX = 0
    drY = 1

class S32TYPenum(Enum):
    sysCorr = 0
    sysHole = 1
    sysSpace = 2
    sysOffset = 3

class CUT_GTYPenum(Enum):
    cutXY = 2
    cutXA = 3
    cutYA = 4
    cutLA = 5

class SHTenum(Enum):
    spByPost = 99
    spByPos = 0
    spByDist = 1

class SCenum(Enum):
    scOFF = 0
    sc1 = 1
    sc2 = 2

class DIRenum(Enum):
    dirCW = 1
    dirCCW = 2

class POCTYPenum(Enum):
    ptZIG = 0
    ptZZ = 1
    ptIN = 2
    pyOUT = 3
    ptFSH = 4

class WAITTYPenum(Enum):
    stNT = 0
    stTR = 1
    stOR = 2
    stCMAN = 4
    stCAUT = 5

class WAITMRenum(Enum):
    mrrNO = 0
    mrrX = 1
    mrrY = 2
    mrrXY = 3

class GEOTEXTPSTenum(Enum):
    txtExt = 0
    txtInt = 1

class CTenum(Enum):
    cmfNO = 0
    cmfLIN = 1
    cmfCIR = 2

if __name__=='__main__':
    for enum in list(CTenum):
        print(enum)
    for enum in list(GEOTEXTPSTenum):
        print(enum)
    for enum in list(WAITMRenum):
        print(enum)
    for enum in list(WAITTYPenum):
        print(enum)
    for enum in list(POCTYPenum):
        print(enum)
    for enum in list(DIRenum):
        print(enum)
    for enum in list(SCenum):
        print(enum)
    for enum in list(RTYenum):
        print(enum)
    for enum in list(CKAenum):
        print(enum)
    for enum in list(RMDenum):
        print(enum)    
    for enum in list(BoolEnum):
        print(enum)
    for enum in list(S32DIRenum):
        print(enum)   
    for enum in list(S32TYPenum):
        print(enum)
    for enum in list(CUT_GTYPenum):
        print(enum)
    for enum in list(SHTenum):
        print(enum)
