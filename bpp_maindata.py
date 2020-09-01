class BPPmaindata:
    def __init__(self):
        self.lpx = 800.0
        self.lpy = 500.0
        self.lpz = 30.0
        self.orlst = "1"
        self.simmetry = 1
        self.tlchk = 0
        self.tooling = ""
        self.custstr = ""
        self.fcn = 1.0
        self.xcut = 0.0
        self.ycut = 0.0
        self.jigth = 0.0
        self.ckop = 0
        self.unique = 0
        self.material = 'wood'
        self.putlst = ""
        self.oppwkrs = 0
        self.uniclamp = 0
        self.chkcoll = 0
        self.wtpiani = 0
        self.colltool = 0
        self.calcedth = 0
        self.enablelabel = 0
        self.lockwaste = 0
        self.loadedgeopt = 0
        self.itltype = 0
        self.runpav = 0
        self.flipend = 0
        self.enablemachlinks = 0
        self.enablepursuits = 0
        self.enablefastvertborings = 0
        self.fastvertboringvalue = 0.0
        
    def to_bpp_code150(self):
        string = 'PAN=LPX|{:4.3f}||4|\n'.format(self.lpx) +\
                 'PAN=LPY|{:4.3f}||4|\n'.format(self.lpy) +\
                 'PAN=LPZ|{:3.3f}||4|\n'.format(self.lpz) +\
                 'PAN=ORLST|"{}"||3|\n'.format(self.orlst) +\
                 'PAN=SIMMETRY|{:d}||1|\n'.format(self.simmetry) +\
                 'PAN=TLCHK|{:d}||1|\n'.format(self.tlchk) +\
                 'PAN=TOOLING|"{}"||3|\n'.format(self.tooling) +\
                 'PAN=CUSTSTR|$B$KBsExportToNcRvA.XncExtraPanelData$V"{}"||3|\n'.format(self.custstr) +\
                 'PAN=FCN|{:2.6f}||2|\n'.format(self.fcn) +\
                 'PAN=XCUT|{}||4|\n'.format(self.xcut) +\
                 'PAN=YCUT|{}||4|\n'.format(self.ycut) +\
                 'PAN=JIGTH|{}||4|\n'.format(self.jigth) +\
                 'PAN=CKOP|{:d}||1|\n'.format(self.ckop) +\
                 'PAN=UNIQUE|{:d}||1|\n'.format(self.unique) +\
                 'PAN=MATERIAL|"{}"||3|\n'.format(self.material) +\
                 'PAN=PUTLST|"{}"||3|\n'.format(self.putlst) +\
                 'PAN=OPPWKRS|{:d}||1|\n'.format(self.oppwkrs) +\
                 'PAN=UNICLAMP|{:d}||1|\n'.format(self.uniclamp) +\
                 'PAN=CHKCOLL|{:d}||1|\n'.format(self.chkcoll) +\
                 'PAN=WTPIANI|{:d}||1|\n'.format(self.wtpiani) +\
                 'PAN=COLLTOOL|{:d}||1|\n'.format(self.colltool) +\
                 'PAN=CALCEDTH|{:d}||1|\n'.format(self.calcedth) +\
                 'PAN=ENABLELABEL|{:d}||1|\n'.format(self.enablelabel) +\
                 'PAN=LOCKWASTE|{:d}||1|\n'.format(self.lockwaste) +\
                 'PAN=LOADEDGEOPT|{:d}||1|\n'.format(self.loadedgeopt) +\
                 'PAN=ITLTYPE|{:d}||1|\n'.format(self.itltype) +\
                 'PAN=RUNPAV|{:d}||1|\n'.format(self.runpav) +\
                 'PAN=FLIPEND|{:d}||1|\n'.format(self.flipend) +\
                 'PAN=ENABLEMACHLINKS|{:d}||1|\n'.format(self.enablemachlinks) +\
                 'PAN=ENABLEPURSUITS|{:d}||1|\n'.format(self.enablepursuits) +\
                 'PAN=ENABLEFASTVERTBORINGS|{:d}||1|\n'.format(self.enablefastvertborings) +\
                 'PAN=FASTVERTBORINGSVALUE|{}||4|\n'.format(self.fastvertboringvalue)

        return string

    def to_bpp_code130(self):
        string = 'PAN=LPX|{:4.3f}||4|\n'.format(self.lpx) +\
                 'PAN=LPY|{:4.3f}||4|\n'.format(self.lpy) +\
                 'PAN=LPZ|{:3.3f}||4|\n'.format(self.lpz) +\
                 'PAN=ORLST|"{}"||0|\n'.format(self.orlst) +\
                 'PAN=SIMMETRY|{:d}||0|\n'.format(self.simmetry) +\
                 'PAN=TLCHK|{:d}||0|\n'.format(self.tlchk) +\
                 'PAN=TOOLING|"{}"||0|\n'.format(self.tooling) +\
                 'PAN=CUSTSTR|"{}"||0|\n'.format(self.custstr) +\
                 'PAN=FCN|{:2.6f}||0|\n'.format(self.fcn) +\
                 'PAN=XCUT|{}||4|\n'.format(self.xcut) +\
                 'PAN=YCUT|{}||4|\n'.format(self.ycut) +\
                 'PAN=JIGTH|{}||4|\n'.format(self.jigth) +\
                 'PAN=CKOP|{:d}||0|\n'.format(self.ckop) +\
                 'PAN=UNIQUE|{:d}||0|\n'.format(self.unique) +\
                 'PAN=MATERIAL|"{}"||0|\n'.format(self.material) +\
                 'PAN=PUTLST|"{}"||0|\n'.format(self.putlst) +\
                 'PAN=OPPWKRS|{:d}||0|\n'.format(self.oppwkrs) +\
                 'PAN=UNICLAMP|{:d}||0|\n'.format(self.uniclamp) +\
                 'PAN=CHKCOLL|{:d}||0|\n'.format(self.chkcoll) +\
                 'PAN=WTPIANI|{:d}||0|\n'.format(self.wtpiani) +\
                 'PAN=COLLTOOL|{:d}||0|\n'.format(self.colltool) +\
                 'PAN=CALCEDTH|{:d}||0|\n'.format(self.calcedth) +\
                 'PAN=ENABLELABEL|{:d}||0|\n'.format(self.enablelabel)
        return string

    def to_vb_script(self):
        string = 'Dim LPX: LPX = {:4.3f}\n'.format(self.lpx) +\
                 'Dim LPY: LPY = {:4.3f}\n'.format(self.lpy) +\
                 'Dim LPZ: LPZ = {:3.3f}\n'.format(self.lpz) +\
                 'Dim ORLST: ORLST = "{}"\n'.format(self.orlst) +\
                 'Dim SIMMETRY: SIMMETRY = {:d}\n'.format(self.simmetry) +\
                 'Dim TLCHK: TLCHK = {:d}\n'.format(self.tlchk) +\
                 'Dim TOOLING: TOOLING = "{}"\n'.format(self.tooling) +\
                 'Dim CUSTSTR: CUSTSTR = "{}"\n'.format(self.custstr) +\
                 'Dim FCN: FCN = {:2.6f}\n'.format(self.fcn) +\
                 'Dim XCUT: XCUT = {}\n'.format(self.xcut) +\
                 'Dim YCUT: YCUT = {}\n'.format(self.ycut) +\
                 'Dim JIGTH: JIGTH = {}\n'.format(self.jigth) +\
                 'Dim CKOP: CKOP = {:d}\n'.format(self.ckop) +\
                 'Dim UNIQUE: UNIQUE = {:d}\n'.format(self.unique) +\
                 'Dim MATERIAL: MATERIAL = "{}"\n'.format(self.material) +\
                 'Dim PUTLST: PUTLST = "{}"\n'.format(self.putlst) +\
                 'Dim OPPWKRS: OPPWKRS = {:d}\n'.format(self.oppwkrs) +\
                 'Dim UNICLAMP: UNICLAMP = {:d}\n'.format(self.uniclamp) +\
                 'Dim CHKCOLL: CHKCOLL = {:d}\n'.format(self.chkcoll) +\
                 'Dim WTPIANI: WTPIANI = {:d}\n'.format(self.wtpiani) +\
                 'Dim COLLTOOL: COLLTOOL = {:d}\n'.format(self.colltool) +\
                 'Dim CALCEDTH: CALCEDTH = {:d}\n'.format(self.calcedth) +\
                 'Dim ENABLELABEL: ENABLELABEL = {:d}\n'.format(self.enablelabel)
        return string

    def to_cid(self):
        string ='BEGIN MAINDATA\n  LX={:4.3f}\n'.format(self.lpx) +\
                '  LY={:4.3f}\n'.format(self.lpy) +\
                '  LZ={:3.3f}\n'.format(self.lpz) +\
                '  OX= 0.00\n  OY= 0.00\n  OZ= 0.00\n' +\
                '\tBEGIN TECH\n    CAT=0\n        END TECH\nEND MAINDATA \n'
        return string

    def to_cix(self):
        string = 'BEGIN MAINDATA\n\tLPX={:4.3f}\n'.format(self.lpx) +\
                 '\tLPY={:4.3f}\n'.format(self.lpy) +\
                 '\tLPZ={:3.3f}\n'.format(self.lpz) +\
                 '\tORLST="{}"\n'.format(self.orlst) +\
                 '\tSIMMETRY={:d}\n'.format(self.simmetry) +\
                 '\tTLCHK={:d}\n'.format(self.tlchk) +\
                 '\tTOOLING="{}"\n'.format(self.tooling) +\
                 '\tCUSTSTR="$B$KBsExportToNcRvA.XncExtraPanelData$V""{}"\n'.format(self.custstr) +\
                 '\tFCN={:2.6f}\n'.format(self.fcn) +\
                 '\tXCUT={}\n'.format(self.xcut) +\
                 '\tYCUT={}\n'.format(self.ycut) +\
                 '\tJIGTH={}\n'.format(self.jigth) +\
                 '\tCKOP={:d}\n'.format(self.ckop) +\
                 '\tUNIQUE={:d}\n'.format(self.unique) +\
                 '\tMATERIAL="{}"\n'.format(self.material) +\
                 '\tPUTLST="{}"\n'.format(self.putlst) +\
                 '\tOPPWKRS={:d}\n'.format(self.oppwkrs) +\
                 '\tUNICLAMP={:d}\n'.format(self.uniclamp) +\
                 '\tCHKCOLL={:d}\n'.format(self.chkcoll) +\
                 '\tWTPIANI={:d}\n'.format(self.wtpiani) +\
                 '\tCOLLTOOL={:d}\n'.format(self.colltool) +\
                 '\tCALCEDTH={:d}\n'.format(self.calcedth) +\
                 '\tENABLELABEL={:d}\n'.format(self.enablelabel) +\
                 '\tLOCKWASTE={:d}\n'.format(self.lockwaste) +\
                 '\tLOADEDGEOPT={:d}\n'.format(self.loadedgeopt) +\
                 '\tITLTYPE={:d}\n'.format(self.itltype) +\
                 '\tRUNPAV={:d}\n'.format(self.runpav) +\
                 '\tFLIPEND={:d}\n'.format(self.flipend) +\
                 '\tENABLEMACHLINKS={:d}\n'.format(self.enablemachlinks) +\
                 '\tENABLEPURSUITS={:d}\n'.format(self.enablepursuits) +\
                 '\tENABLEFASTVERTBORINGS={:d}\n'.format(self.enablefastvertborings) +\
                 '\tFASTVERTBORINGSVALUE={}\n'.format(self.fastvertboringvalue) +\
                 'END MAINDATA\n'

        return string


if __name__=='__main__':
    m=BPPmaindata()
    m.orlst="1,2,3,4"
    print(m.to_bpp_code150())
    print(m.to_bpp_code130())
    print(m.to_vb_script())
    print(m.to_cid())
    print(m.to_cix())
