

class Dosya():

    def __init__(self,dosya_ismi):
        #kelimeleri sade şekilde listeler

        with open(dosya_ismi,"r",encoding = "utf-8") as file:

            dosya_icerigi = file.read()
            kelimelerim=dosya_icerigi.split()
            self.sade_k=list()
            for i in kelimelerim:
                i = i.strip("\n")
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip(" ")
                i = i.strip(":")
                i = i.strip(";")
                i = i.strip("!")
                i = i.strip("?")
                self.sade_k.append(i)
            print()
            
    def butun_kelimeler(self):
        #listelenmiş kelimelerdeki tekrarı engeller
        self.kelimeler_kumesi =set()

        for i in self.sade_k:
            self.kelimeler_kumesi.add(i)
        #print("bütün_kelimeler")
        #for i in kelimeler_kümesi:
        #   print(i)
        #   print("////////////////////////////////")
    def kac_var(self):

        sayac=0
        for i in self.kelimeler_kumesi:
            for j in self.sade_k:
                if i==j:
                    sayac=sayac+1
            print(i)
            print("bu kelime şu kadar geçmiş",(sayac))
            print("*************************************")
            sayac=0




dosya = Dosya("HarryPoter.txt")
dosya.butun_kelimeler()
dosya.kac_var()