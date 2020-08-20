class BPPdescription:
    def __init(self, text = ""):
        self.text = text

    def to_bpp_code(self):
        s = self.text.split("\n")
        string ='[DESCRIPTION]\n' 
        for item in s:
            string =string +'|' + item +'\n'
        return string


if __name__=='__main__':
    d=BPPdescription()
    d.text='A\nB\nC\nD\nE'
    print(d.to_bpp_code())
