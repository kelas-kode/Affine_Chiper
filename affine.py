import os

logo="""
  ╱▔▔▔▔▔▔▔╲
 /         \   ÷Cryptograpy Affine Chiper÷
▕┃. ┊┃.╰╮   |
▕╰━╭╮╰━╯ ╰┈╮▏      Author : Tegar Sabila
▕▂╮┗┛ ╭┳┳┳╯▕
 ▕┳┳┳┳┳┫╰┃▂╱       Github : kelas-kode
 ▕╋╋╋╋┫🚬💨╯
 ▕┻┻┻┻┻╯▕
 ▕▂▂▂▂▂▂╱

  [>Menu<]

1)Encrypt
2)Decrypt
"""
class AffineChiper(object):
   mati=128
   kunci=(7, 3, 55)
   def __init__(self):
      pass
   def enkripsiChar(self, karakter):
      c1, c2, cI = self.kunci
      return chr((c1 * ord(karakter) + c2) % self.mati)

   def enkripsi(self, string):
      return "".join(map(self.enkripsiChar, string))

   def dekripsiChar(self, karakter):
      c1, c2, cI = self.kunci
      return chr(cI * (ord(karakter) - c2) % self.mati)

   def dekripsi(self, string):
      return "".join(map(self.dekripsiChar, string))
chiper=AffineChiper()
def enk():
    enkrip=input("Enter char to encrypt: ")
    print("Encrypt:",chiper.enkripsi(enkrip))
def dek():
    dekrip=input("Enter char to decrypt: ")
    print("Decrypt:",chiper.dekripsi(dekrip))

if __name__=="__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    pilih=input('Choose => ')
    if pilih == "1":
        enk()
    elif pilih == "2":
        dek()
    else:
        print('nothing')