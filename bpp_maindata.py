class BPPmaindata:
    def __init__(self):
        self.lpx = 800.0
        self.lpy = 500.0
        self.lpz = 30.0
        self.orlst = "1"
        self.simmetry = 1
        self.tlchk = 0
        self.tooling = ""
        self.custstr = '$B$KBsExportToNcRvA.XncExtraPanelData$V""'
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
        
    def to_bpp_code(self):
        string = 'PAN=LPX|{:4.3f}||4|\n'.format(self.lpx) +\
                 'PAN=LPY|{:4.3f}||4|\n'.format(self.lpy) +\
                 'PAN=LPZ|{:3.3f}||4|\n'.format(self.lpz) +\
                 'PAN=ORLST|"{}"||3|\n'.format(self.orlst) +\
                 'PAN=SIMMETRY|{:d}||1|\n'.format(self.simmetry) +\
                 'PAN=TLCHK|{:d}||1|\n'.format(self.tlchk) +\
                 'PAN=TOOLING|"{}"||3|\n'.format(self.tooling) +\
                 'PAN=CUSTSTR|{}||3|\n'.format(self.custstr) +\
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

if __name__=='__main__':
    m=BPPmaindata()
    m.orlst="1,2,3,4"
    print(m.to_bpp_code())
