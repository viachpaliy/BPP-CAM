class Rout:
    def __init__(self):
        self.rout_id ="P" + str(id(self))
        self.side = 0
        self.crn = "1"
        self.z = 0.0
        self.dp = 10.0
        self.iso = ""
        self.opt = "YES"
        self.dia = 18.0
        self.rty = "rpNO"
        self.xrc = 0
        self.yrc = 0
        self.dx = 32.0
        self.dy = 32.0
        self.r = 50
        self.a = 0.0
        self.da = 45
        self.rdl = "YES"
        self.nrp = 0
        self.az = 0
        self.ar = 0
        self.zs = 0
        self.ze = 0
        self.cka = "azrNO"
        self.thr = "NO"
        self.rv = "NO"
        self.ckt = "NO"
        self.arp = 0
        self.lrp = 0
        self.er = "YES"
        self.cow = "NO"
        self.ovm = 0
        self.a21 = 0
        self.tos = "NO"
        self.vtr = 0
        self.dvr = 0
        self.otr = 0
        self.svr = 0
        self.cof = "NO"
        self.dof = 0
        self.gip = "YES"
        self.lsv = 0
        self.s21 = -1
        self.azs = 0
        self.dsp = 0
        self.rsp = 0
        self.ios = 0
        self.wsp = 0
        self.tnm = ""
        self.ttp = 103
        self.tcl = 1
        self.crc = 2
        self.tin = 1
        self.ain = 45
        self.cin = "NO"
        self.gin = 0
        self.tbi = "NO"
        self.tli = 0
        self.tqi = 0
        self.tou = 1
        self.aou = 45
        self.cou = "NO"
        self.gou = 0
        self.tbo = "NO"
        self.tlo = 0
        self.tqo = 0
        self.din = 0
        self.dou = 0
        self.sds = 0
        self.prp = 0
        self.bdr = "NO"
        self.spi = ""
        self.sc = "NO"
        self.swi = "NO"
        self.blw = "NO"
        self.prs = "NO"
        self.bfc = "NO"
        self.shp = 0
        self.swp = "NO"
        self.csp = 0
        self.udt = "NO"
        self.tdt = ""
        self.ddt = 5
        self.sdt = 0
        self.idt = 20
        self.fdt = 80
        self.rdt = 60
        self.ea21 = "NO"
        self.cen = ""
        self.agg = ""
        self.lay = "ROUT"
        self.eecs = 0
        self.pdin = 1
        self.pdu = 1
        self.pcin = 0
        self.pcu = 0
        self.pmol = 0
        self.aux = 0
        self.crr = "NO"
        self.nebs = "NO"
        self.etb = "NO"
        self.fxd = "NO"
        self.fxda = 0
        self.kdt = "NO"
        self.eml = "NO"
        self.etg = "NO"
        self.rtas = "NO"
        self.rdin = "NO"
        self.sdsf = 0
        self.incstp = "NO"
        self.etgt = 0.1
        self.ajt = "NO"
        self.ion = "NO"
        self.lubmnz = "NO"
        self.sht = "spByPost"
        self.shd = 0

    def to_cix(self):
        string='BEGIN MACRO\n\tNAME=ROUT\n\tPARAM,NAME=ID,VALUE="{}"\n'.format(self.rout_id) +\
               '\tPARAM,NAME=SIDE,VALUE={}\n'.format(self.side) +\
               '\tPARAM,NAME=CRN,VALUE="{}"\n'.format(self.crn) +\
               '\tPARAM,NAME=Z,VALUE={}\n'.format(self.z) +\
               '\tPARAM,NAME=DP,VALUE={}\n'.format(self.dp) +\
               '\tPARAM,NAME=ISO,VALUE="{}"\n'.format(self.iso) +\
               '\tPARAM,NAME=OPT,VALUE={}\n'.format(self.opt) +\
               '\tPARAM,NAME=DIA,VALUE={}\n'.format(self.dia) +\
               '\tPARAM,NAME=RTY,VALUE={}\n'.format(self.rty) +\
               '\tPARAM,NAME=XRC,VALUE={}\n'.format(self.xrc) +\
               '\tPARAM,NAME=YRC,VALUE={}\n'.format(self.yrc) +\
               '\tPARAM,NAME=DX,VALUE={}\n'.format(self.dx) +\
               '\tPARAM,NAME=DY,VALUE={}\n'.format(self.dy) +\
               '\tPARAM,NAME=R,VALUE={}\n'.format(self.r) +\
               '\tPARAM,NAME=A,VALUE={}\n'.format(self.a) +\
               '\tPARAM,NAME=DA,VALUE={}\n'.format(self.da) +\
               '\tPARAM,NAME=RDL,VALUE={}\n'.format(self.rdl) +\
               '\tPARAM,NAME=NRP,VALUE={}\n'.format(self.nrp) +\
               '\tPARAM,NAME=AZ,VALUE={}\n'.format(self.az) +\
               '\tPARAM,NAME=AR,VALUE={}\n'.format(self.ar) +\
               '\tPARAM,NAME=ZS,VALUE={}\n'.format(self.zs) +\
               '\tPARAM,NAME=ZE,VALUE={}\n'.format(self.ze) +\
               '\tPARAM,NAME=CKA,VALUE={}\n'.format(self.cka) +\
               '\tPARAM,NAME=THR,VALUE={}\n'.format(self.thr) +\
               '\tPARAM,NAME=RV,VALUE={}\n'.format(self.rv) +\
               '\tPARAM,NAME=CKT,VALUE={}\n'.format(self.ckt) +\
               '\tPARAM,NAME=ARP,VALUE={}\n'.format(self.arp) +\
               '\tPARAM,NAME=LRP,VALUE={}\n'.format(self.lrp) +\
               '\tPARAM,NAME=ER,VALUE={}\n'.format(self.er) +\
               '\tPARAM,NAME=COW,VALUE={}\n'.format(self.cow) +\
               '\tPARAM,NAME=OVM,VALUE={}\n'.format(self.ovm) +\
               '\tPARAM,NAME=A21,VALUE={}\n'.format(self.a21) +\
               '\tPARAM,NAME=TOS,VALUE={}\n'.format(self.tos) +\
               '\tPARAM,NAME=VTR,VALUE={}\n'.format(self.vtr) +\
               '\tPARAM,NAME=DVR,VALUE={}\n'.format(self.dvr) +\
               '\tPARAM,NAME=OTR,VALUE={}\n'.format(self.otr) +\
               '\tPARAM,NAME=SVR,VALUE={}\n'.format(self.svr) +\
               '\tPARAM,NAME=COF,VALUE={}\n'.format(self.cof) +\
               '\tPARAM,NAME=DOF,VALUE={}\n'.format(self.dof) +\
               '\tPARAM,NAME=GIP,VALUE={}\n'.format(self.gip) +\
               '\tPARAM,NAME=LSV,VALUE={}\n'.format(self.lsv) +\
               '\tPARAM,NAME=S21,VALUE={}\n'.format(self.s21) +\
               '\tPARAM,NAME=AZS,VALUE={}\n'.format(self.azs) +\
               '\tPARAM,NAME=DSP,VALUE={}\n'.format(self.dsp) +\
               '\tPARAM,NAME=RSP,VALUE={}\n'.format(self.rsp) +\
               '\tPARAM,NAME=IOS,VALUE={}\n'.format(self.ios) +\
               '\tPARAM,NAME=WSP,VALUE={}\n'.format(self.wsp) +\
               '\tPARAM,NAME=TNM,VALUE="{}"\n'.format(self.tnm) +\
               '\tPARAM,NAME=TTP,VALUE={}\n'.format(self.ttp) +\
               '\tPARAM,NAME=TCL,VALUE={}\n'.format(self.tcl) +\
               '\tPARAM,NAME=CRC,VALUE={}\n'.format(self.crc) +\
               '\tPARAM,NAME=TIN,VALUE={}\n'.format(self.tin) +\
               '\tPARAM,NAME=AIN,VALUE={}\n'.format(self.ain) +\
               '\tPARAM,NAME=CIN,VALUE={}\n'.format(self.cin) +\
               '\tPARAM,NAME=GIN,VALUE={}\n'.format(self.gin) +\
               '\tPARAM,NAME=TBI,VALUE={}\n'.format(self.tbi) +\
               '\tPARAM,NAME=TLI,VALUE={}\n'.format(self.tli) +\
               '\tPARAM,NAME=TQI,VALUE={}\n'.format(self.tqi) +\
               '\tPARAM,NAME=TOU,VALUE={}\n'.format(self.tou) +\
               '\tPARAM,NAME=AOU,VALUE={}\n'.format(self.aou) +\
               '\tPARAM,NAME=COU,VALUE={}\n'.format(self.cou) +\
               '\tPARAM,NAME=GOU,VALUE={}\n'.format(self.gou) +\
               '\tPARAM,NAME=TBO,VALUE={}\n'.format(self.tbo) +\
               '\tPARAM,NAME=TLO,VALUE={}\n'.format(self.tlo) +\
               '\tPARAM,NAME=TQO,VALUE={}\n'.format(self.tqo) +\
               '\tPARAM,NAME=DIN,VALUE={}\n'.format(self.din) +\
               '\tPARAM,NAME=DOU,VALUE={}\n'.format(self.dou) +\
               '\tPARAM,NAME=SDS,VALUE={}\n'.format(self.sds) +\
               '\tPARAM,NAME=PRP,VALUE={}\n'.format(self.prp) +\
               '\tPARAM,NAME=BDR,VALUE={}\n'.format(self.bdr) +\
               '\tPARAM,NAME=SPI,VALUE="{}"\n'.format(self.spi) +\
               '\tPARAM,NAME=SC,VALUE={}\n'.format(self.sc) +\
               '\tPARAM,NAME=SWI,VALUE={}\n'.format(self.swi) +\
               '\tPARAM,NAME=BLW,VALUE={}\n'.format(self.blw) +\
               '\tPARAM,NAME=PRS,VALUE={}\n'.format(self.prs) +\
               '\tPARAM,NAME=BFC,VALUE={}\n'.format(self.bfc) +\
               '\tPARAM,NAME=SHP,VALUE={}\n'.format(self.shp) +\
               '\tPARAM,NAME=SWP,VALUE={}\n'.format(self.swp) +\
               '\tPARAM,NAME=CSP,VALUE={}\n'.format(self.csp) +\
               '\tPARAM,NAME=UDT,VALUE={}\n'.format(self.udt) +\
               '\tPARAM,NAME=TDT,VALUE="{}"\n'.format(self.tdt) +\
               '\tPARAM,NAME=DDT,VALUE={}\n'.format(self.ddt) +\
               '\tPARAM,NAME=SDT,VALUE={}\n'.format(self.sdt) +\
               '\tPARAM,NAME=IDT,VALUE={}\n'.format(self.idt) +\
               '\tPARAM,NAME=FDT,VALUE={}\n'.format(self.fdt) +\
               '\tPARAM,NAME=RDT,VALUE={}\n'.format(self.rdt) +\
               '\tPARAM,NAME=EA21,VALUE={}\n'.format(self.ea21) +\
               '\tPARAM,NAME=CEN,VALUE="{}"\n'.format(self.cen) +\
               '\tPARAM,NAME=AGG,VALUE="{}"\n'.format(self.agg) +\
               '\tPARAM,NAME=LAY,VALUE="{}"\n'.format(self.lay) +\
               '\tPARAM,NAME=EECS,VALUE={}\n'.format(self.eecs) +\
               '\tPARAM,NAME=PDIN,VALUE={}\n'.format(self.pdin) +\
               '\tPARAM,NAME=PDU,VALUE={}\n'.format(self.pdu) +\
               '\tPARAM,NAME=PCIN,VALUE={}\n'.format(self.pcin) +\
               '\tPARAM,NAME=PCU,VALUE={}\n'.format(self.pcu) +\
               '\tPARAM,NAME=PMOL,VALUE={}\n'.format(self.pmol) +\
               '\tPARAM,NAME=AUX,VALUE={}\n'.format(self.aux) +\
               '\tPARAM,NAME=CRR,VALUE={}\n'.format(self.crr) +\
               '\tPARAM,NAME=NEBS,VALUE={}\n'.format(self.nebs) +\
               '\tPARAM,NAME=ETB,VALUE={}\n'.format(self.etb) +\
               '\tPARAM,NAME=FXD,VALUE={}\n'.format(self.fxd) +\
               '\tPARAM,NAME=FXDA,VALUE={}\n'.format(self.fxda) +\
               '\tPARAM,NAME=KDT,VALUE={}\n'.format(self.kdt) +\
               '\tPARAM,NAME=EML,VALUE={}\n'.format(self.eml) +\
               '\tPARAM,NAME=ETG,VALUE={}\n'.format(self.etg) +\
               '\tPARAM,NAME=RTAS,VALUE={}\n'.format(self.rtas) +\
               '\tPARAM,NAME=RDIN,VALUE={}\n'.format(self.rdin) +\
               '\tPARAM,NAME=SDSF,VALUE={}\n'.format(self.sdsf) +\
               '\tPARAM,NAME=INCSTP,VALUE={}\n'.format(self.incstp) +\
               '\tPARAM,NAME=ETGT,VALUE={}\n'.format(self.etgt) +\
               '\tPARAM,NAME=AJT,VALUE={}\n'.format(self.ajt) +\
               '\tPARAM,NAME=ION,VALUE={}\n'.format(self.ion) +\
               '\tPARAM,NAME=LUBMNZ,VALUE={}\n'.format(self.lubmnz) +\
               '\tPARAM,NAME=SHT,VALUE={}\n'.format(self.sht) +\
               '\tPARAM,NAME=SHD,VALUE={}\n'.format(self.shd) +\
               'END MACRO\n'

        return string

    def to_bpp_code150(self):
        return '@ ROUT, "", "", {114}, "", 0 : {0},{1},"{2}",{3},{4},{5},{6},{7},{8},{9},\
{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},\
{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},\
{30},{31},{32},{33},{34},{35},{36},{37},{38},{39},\
{40},{41},{42},{43},{44},{45},"{46}",{47},{48},{49},\
{50},{51},{52},{53},{54},{55},{56},{57},{58},{59},\
{60},{61},{62},{63},{64},{65},{66},{67},{68},"{69}",\
{70},{71},{72},{73},{74},{75},{76},{77},{78},"{79}",\
{80},{81},{82},{83},{84},{85},"{86}","{87}","{88}",{89},\
{90},{91},{92},{93},{94},{95},{96},{97},{98},{99},\
{100},{101},{102},{103},{104},{105},{106},{107},{108},{109},\
{110},{111},{112},{113}'.format(self.rout_id,self.side,self.crn,self.z,self.dp,self.opt,self.dia,self.rty,self.xrc,self.yrc,\
                                               self.dx,self.dy,self.r,self.a,self.da,self.rdl,self.nrp,self.az,self.ar,self.zs,\
                                               self.ze,self.cka,self.thr,self.rv,self.ckt,self.arp,self.lrp,self.er,self.cow,self.ovm,\
                                               self.a21,self.tos,self.vtr,self.dvr,self.otr,self.svr,self.cof,self.dof,self.gip,self.lsv,\
                                               self.s21,self.azs,self.dsp,self.rsp,self.ios,self.wsp,self.tnm,self.ttp,self.tcl,self.crc,\
                                               self.tin,self.ain,self.cin,self.gin,self.tbi,self.tli,self.tqi,self.tou,self.aou,self.cou,\
                                               self.gou,self.tbo,self.tlo,self.tqo,self.din,self.dou,self.sds,self.prp,self.bdr,self.spi,\
                                               self.sc,self.swi,self.blw,self.prs,self.bfc,self.shp,self.swp,self.csp,self.udt,self.tdt,\
                                               self.ddt,self.sdt,self.idt,self.fdt,self.rdt,self.ea21,self.cen,self.agg,self.lay,self.eecs,\
                                               self.pdin,self.pdu,self.pcin,self.pcu,self.pmol,self.aux,self.crr,self.nebs,self.etb,self.fxd,\
                                               self.fxda,self.kdt,self.eml,self.etg,self.rtas,self.rdin,self.sdsf,self.incstp,self.etgt,self.ajt,\
                                               self.ion,self.lubmnz,self.sht,self.shd,str(id(self)))
    

if __name__=='__main__':
    r =Rout()
    print(r.to_bpp_code150())
    
