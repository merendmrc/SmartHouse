class House():
    def __init__(self,ad) -> None:
        self.ad = ad

def s(x):
    kelime = ""
    for i in x:
        kelime = kelime+str(i.ad())
