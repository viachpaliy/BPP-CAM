class BPP_Header:

    def __init__(self, prg_type = 'BPP', ver = 150):
        self.prg_type = prg_type
        self.ver = ver

    def to_bpp_code(self):
        return '[HEADER]\nTYPE={0}\nVER={1}\n'.format(self.prg_type,int(self.ver))

    def to_cix(self):
        return 'BEGIN ID CID3\n	REL= 5.0\nEND ID\n'

    def to_cid(self):
        return 'BEGIN ID CID3\n' +"'" + '"untitled"\n  REL= 3.0\n  AXIS=x+,y-,z-\nEND ID\n'

if __name__=='__main__':
    h = BPP_Header()
    print(h.to_bpp_code())
    print(h.to_cix())
    print(h.to_cid())
