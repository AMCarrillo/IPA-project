#from _typeshed import NoneType
from ipapy import UNICODE_TO_IPA
from tkinter import *
import tkinter.font as fnt
import pygame

class IPA:
  def __init__(self, symbol, description):
    self.symbol = symbol
    self.description = description

  def phoneme_features(self):
    consonant = ""
    sonorant = ""
    syllabic = ""
    continuant = ""
    nasal = ""
    voice = ""
    labial = ""
    round = ""

    #MAYOR CLASS FEATURES
    if "consonant" in self.description:
      consonant = "[+ consonant]"
    elif "vowel" in self.description:
      consonant = "[- consonant]"
    if "plosive" in self.description or "fricative" in self.description or "affricate" in self.description or "trill" in self.description or "flap" in self.description:
      sonorant = "[- sonorant]"
    else:
      sonorant = "[+ sonorant]"
    if "vowel" in self.description or UNICODE_TO_IPA[u"\u014B"] == self.symbol:#check
      syllabic = "[+ syllabic]"
    else:
      syllabic = "[- syllabic]"
    #MANNER OF ARTICULATION
    if "nasal" in self.description or "plosive" in self.description:
      continuant = "[- continuant]"
    else:
      continuant = "[+ continuant]"
    if "nasal" in self.description:
      nasal = "[+ nasal]"
    else:
      nasal = "[- nasal]"
    if "vowel" in self.description or "voiced" in self.description:
      voice = "[+ voice]"
    else:
      voice = "[- voice]"
    #PLACE FEATURES
    if "labi" in self.description or "vowel" in self.description or UNICODE_TO_IPA[u"\u006A"] == self.symbol:
      labial = "[LABIAL]"
      if UNICODE_TO_IPA[u"\u028B"] == self.symbol or "rounded" in self.description:#check
        round = "   [+ round]"
      else:
        round = "   [- round]"
    
    features = consonant + "\n" + sonorant + "\n" + syllabic + "\n" + continuant  + "\n" + nasal + "\n" + voice + "\n" + labial + "\n" + round

    return features
      

A1 = IPA(UNICODE_TO_IPA[u"\u0061"], "front open unrounded vowel")#a
A2 = IPA(UNICODE_TO_IPA[u"\u00E6"], "front near-open unrounded vowel")#æ
A3 = IPA(UNICODE_TO_IPA[u"\u0250"], "central near-open unrounded vowel")#ɐ
A4 = IPA(UNICODE_TO_IPA[u"\u0251"], "back open unrounded vowel")#ɑ

B1 = IPA(UNICODE_TO_IPA[u"\u0062"], "bilabial consonant plosive voiced")#b
B2 = IPA(UNICODE_TO_IPA[u"\u03B2"], "bilabial consonant non-sibilant-fricative voiced")#β
B3 = IPA(UNICODE_TO_IPA[u"\u0253"], "bilabial consonant implosive voiced")#ɓ
B4 = IPA(UNICODE_TO_IPA[u"\u0299"], "bilabial consonant trill voiced")#ʙ

C1 = IPA(UNICODE_TO_IPA[u"\u0063"], "consonant palatal plosive voiceless")#c
C2 = IPA(UNICODE_TO_IPA[u"\u00E7"], "consonant non-sibilant-fricative palatal voiceless")#ç
C3 = IPA(UNICODE_TO_IPA[u"\u0255"], "alveolo-palatal consonant sibilant-fricative voiceless")#ɕ

D1 = IPA(UNICODE_TO_IPA[u"\u0064"], "alveolar consonant plosive voiced")#d
D2 = IPA(UNICODE_TO_IPA[u"\u00F0"], "consonant dental non-sibilant-fricative voiced")#ð
D3 = IPA(UNICODE_TO_IPA[u"\u02A4"], "consonant palato-alveolar sibilant-affricate voiced")#d͡ʒ
D4 = IPA(UNICODE_TO_IPA[u"\u0256"], "consonant plosive retroflex voiced")#ɖ
D5 = IPA(UNICODE_TO_IPA[u"\u0257"], "alveolar consonant implosive voiced")#ɗ

E1 = IPA(UNICODE_TO_IPA[u"\u0065"], "close-mid front unrounded vowel")#e
E2 = IPA(UNICODE_TO_IPA[u"\u0259"], "central mid unrounded vowel")#ə
E3 = IPA(UNICODE_TO_IPA[u"\u025A"], "central mid rhotacized unrounded vowel")#ɚ
E4 = IPA(UNICODE_TO_IPA[u"\u0275"], "central close-mid rounded vowel")#ɵ
E5 = IPA(UNICODE_TO_IPA[u"\u0258"], "central close-mid unrounded vowel")#ɘ
E6 = IPA(UNICODE_TO_IPA[u"\u025E"], "central open-mid rounded vowel")#ɞ

EE1 = IPA(UNICODE_TO_IPA[u"\u025B"], "front open-mid unrounded vowel")#ɛ
EE2 = IPA(UNICODE_TO_IPA[u"\u025C"], "central open-mid unrounded vowel")#ɜ
EE3 = IPA(UNICODE_TO_IPA[u"\u025D"], "central open-mid rhotacized unrounded vowel")#ɝ

G1 = IPA(UNICODE_TO_IPA[u"\u0260"], "consonant implosive velar voiced")#ɠ
G2 = IPA(UNICODE_TO_IPA[u"\u0262"], "consonant plosive uvular voiced")#ɢ
G3 = IPA(UNICODE_TO_IPA[u"\u0261"], "consonant plosive velar voiced")#ɡ

H1 = IPA(UNICODE_TO_IPA[u"\u0127"], "consonant non-sibilant-fricative pharyngeal voiceless")#ħ
H2 = IPA(UNICODE_TO_IPA[u"\u0266"], "consonant glottal non-sibilant-fricative voiced")#ɦ
H3 = IPA(UNICODE_TO_IPA[u"\u0265"], "approximant consonant labio-palatal voiced")#ɥ
H4 = IPA(UNICODE_TO_IPA[u"\u0267"], "consonant palato-alveolo-velar sibilant-fricative voiceless")#ɧ
H5 = IPA(UNICODE_TO_IPA[u"\u029C"], "consonant pharyngeal trill voiceless")#ʜ

I1 = IPA(UNICODE_TO_IPA[u"\u026A"], "near-close near-front unrounded vowel")#ɪ
I2 = IPA(UNICODE_TO_IPA[u"\u0268"], "central close unrounded vowel")#ɨ

J1 = IPA(UNICODE_TO_IPA[u"\u006A"], "approximant consonant palatal voiced")#j
J2 = IPA(UNICODE_TO_IPA[u"\u029D"], "consonant non-sibilant-fricative palatal voiced")#ʝ
J3 = IPA(UNICODE_TO_IPA[u"\u025F"], "consonant palatal plosive voiced")#ɟ
J4 = IPA(UNICODE_TO_IPA[u"\u0284"], "consonant implosive palatal voiced")#ʄ

L1 = IPA(UNICODE_TO_IPA[u"\u026B"], "alveolar consonant lateral-approximant velarized voiced")#ɫ #ipapy does not recognize the correct symbol!
L2 = IPA(UNICODE_TO_IPA[u"\u026D"], "consonant lateral-approximant retroflex voiced")#ɭ
L3 = IPA(UNICODE_TO_IPA[u"\u026C"], "alveolar consonant lateral-fricative voiceless")#ɬ
L4 = IPA(UNICODE_TO_IPA[u"\u029F"], "consonant lateral-approximant velar voiced")#ʟ
L5 = IPA(UNICODE_TO_IPA[u"\u026E"], "alveolar consonant lateral-fricative voiced")#ɮ

M1 = IPA(UNICODE_TO_IPA[u"\u0271"], "consonant labio-dental nasal voiced")#ɱ

N1 = IPA(UNICODE_TO_IPA[u"\u014B"], "consonant nasal velar voiced")#ŋ
N2 = IPA(UNICODE_TO_IPA[u"\u0272"], "consonant nasal palatal voiced")#ɲ
N3 = IPA(UNICODE_TO_IPA[u"\u0273"], "consonant nasal retroflex voiced")#ɳ
N4 = IPA(UNICODE_TO_IPA[u"\u0274"], "consonant nasal uvular voiced")#ɴ

O1 = IPA(UNICODE_TO_IPA[u"\u006F"], "back close-mid rounded vowel")#o
O2 = IPA(UNICODE_TO_IPA[u"\u0254"], "back open-mid rounded vowel")#ɔ
O3 = IPA(UNICODE_TO_IPA[u"\u0153"], "front open-mid rounded vowel")#œ
O4 = IPA(UNICODE_TO_IPA[u"\u0252"], "back open rounded vowel")#ɒ
O5 = IPA(UNICODE_TO_IPA[u"\u0276"], "front open rounded vowel")#ɶ
O6 = IPA(UNICODE_TO_IPA[u"\u00F8"], "close-mid front rounded vowel")#ø

P1 = IPA(UNICODE_TO_IPA[u"\u0070"], "bilabial consonant plosive voiceless")#p
P2 = IPA(UNICODE_TO_IPA[u"\u0278"], "bilabial consonant non-sibilant-fricative voiceless")#ɸ

R1 = IPA(UNICODE_TO_IPA[u"\u027E"], "alveolar consonant flap voiced")#ɾ
R2 = IPA(UNICODE_TO_IPA[u"\u0279"], "alveolar approximant consonant voiced")#ɹ
R3 = IPA(UNICODE_TO_IPA[u"\u0281"], "consonant non-sibilant-fricative uvular voiced")#ʁ
R4 = IPA(UNICODE_TO_IPA[u"\u0280"], "consonant trill uvular voiced")#ʀ
R5 = IPA(UNICODE_TO_IPA[u"\u027B"], "approximant consonant retroflex voiced")#ɻ
R6 = IPA(UNICODE_TO_IPA[u"\u027D"], "consonant flap retroflex voiced")#ɽ
R7 = IPA(UNICODE_TO_IPA[u"\u027A"], "alveolar consonant lateral-flap voiced")#ɺ

S1 = IPA(UNICODE_TO_IPA[u"\u0073"], "alveolar consonant sibilant-fricative voiceless")#s
S2 = IPA(UNICODE_TO_IPA[u"\u0283"], "consonant palato-alveolar sibilant-fricative voiceless")#ʃ
S3 = IPA(UNICODE_TO_IPA[u"\u0282"], "consonant retroflex sibilant-fricative voiceless")#ʂ

T1 = IPA(UNICODE_TO_IPA[u"\u0074"], "alveolar consonant plosive voiceless")#t
T2 = IPA(UNICODE_TO_IPA[u"\u03B8"], "consonant dental non-sibilant-fricative voiceless")#θ
T3 = IPA(UNICODE_TO_IPA[u"\u02A7"], "consonant palato-alveolar sibilant-affricate voiceless")#t͡ʃ
T4 = IPA(UNICODE_TO_IPA[u"\u02A6"], "alveolar consonant sibilant-affricate voiceless")#t͡s
T5 = IPA(UNICODE_TO_IPA[u"\u0288"], "consonant plosive retroflex voiceless")#ʈ

U1 = IPA(UNICODE_TO_IPA[u"\u0075"], "back close rounded vowel")#u
U2 = IPA(UNICODE_TO_IPA[u"\u028A"], "near-back near-close rounded vowel")#ʊ
U3 = IPA(UNICODE_TO_IPA[u"\u0289"], "central close rounded vowel")#ʉ

V1 = IPA(UNICODE_TO_IPA[u"\u0076"], "consonant labio-dental non-sibilant-fricative voiced")#v
V2 = IPA(UNICODE_TO_IPA[u"\u028C"], "back open-mid unrounded vowel")#ʌ
V3 = IPA(UNICODE_TO_IPA[u"\u028B"], "approximant consonant labio-dental voiced")#ʋ
V4 = IPA(UNICODE_TO_IPA[u"\u2C71"], "consonant flap labio-dental voiced")#ⱱ

W1 = IPA(UNICODE_TO_IPA[u"\u026F"], "back close unrounded vowel")#ɯ
W2 = IPA(UNICODE_TO_IPA[u"\u028D"], "approximant consonant labio-velar voiceless")#ʍ

X1 = IPA(UNICODE_TO_IPA[u"\u0078"], "consonant non-sibilant-fricative velar voiceless")#x
X2 = IPA(UNICODE_TO_IPA[u"\u03C7"], "consonant non-sibilant-fricative uvular voiceless")#χ

Y1 = IPA(UNICODE_TO_IPA[u"\u0263"], "consonant non-sibilant-fricative velar voiced")#ɣ
Y2 = IPA(UNICODE_TO_IPA[u"\u028E"], "consonant lateral-approximant palatal voiced")#ʎ
Y3 = IPA(UNICODE_TO_IPA[u"\u028F"], "near-close near-front rounded vowel")#ʏ
Y4 = IPA(UNICODE_TO_IPA[u"\u0264"], "back close-mid unrounded vowel")#ɤ

Z1 = IPA(UNICODE_TO_IPA[u"\u007A"], "alveolar consonant sibilant-fricative voiced")#z
Z2 = IPA(UNICODE_TO_IPA[u"\u0292"], "consonant palato-alveolar sibilant-fricative voiced")#ʒ
Z3 = IPA(UNICODE_TO_IPA[u"\u0290"], "consonant retroflex sibilant-fricative voiced")#ʐ
Z4 = IPA(UNICODE_TO_IPA[u"\u0291"], "alveolo-palatal consonant sibilant-fricative voiced")#ʑ

ZZ1 = IPA(UNICODE_TO_IPA[u"\u0294"], "consonant glottal plosive voiceless")#ʔ
ZZ2 = IPA(UNICODE_TO_IPA[u"\u0295"], "consonant non-sibilant-fricative pharyngeal voiced")#ʕ
ZZ3 = IPA(UNICODE_TO_IPA[u"\u02A1"], "consonant pharyngeal plosive voiceless")#ʡ
ZZ4 = IPA(UNICODE_TO_IPA[u"\u02A2"], "consonant pharyngeal trill voiced")#ʢ

#-------------------GUI-------------------

#root config
root = Tk()
root.title("IPA")
root.iconbitmap("IPA_img.ico")
root.resizable(False,False)

font = fnt.nametofont("TkDefaultFont")
font.configure(family = "Helvetica", size = 12)

#-------------frames-------------
main_frame = Frame(root)
main_frame.grid(row=0, column=0, sticky="nswe")
main_frame.config(bg='DeepSkyBlue4')

left_frame = Frame(main_frame, padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="nswe")
left_frame.config(bg='DeepSkyBlue4')

right_frame = Frame(main_frame, padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="nswe")
right_frame.config(bg='DeepSkyBlue4')

#Function to insert the information inside the textbox
def select(option):
  txt_bx.configure(state="normal")
  txt_bx.delete("1.0", END)#to delete the old info before displaying the new one
  txt_bx.insert(END, option)
  txt_bx.configure(state="disabled")#It doesn't allow the user to manually modify the textbox


pygame.mixer.init()#Initialize pygame

def audio(recording):
    pygame.mixer.music.load(recording)
    pygame.mixer.music.play(loops=0)#loops = 0 to repeat the music once

#-------textbox--------

txt_bx_label = Label(right_frame, text="Description:", fg="grey79", bg="DeepSkyBlue4")
txt_bx_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

txt_bx = Text(right_frame, wrap=WORD, selectbackground="grey49")#wrap breaks the section of a txt to fit into multiple sections of lines
txt_bx.grid(row=3, column=1, pady=5)
txt_bx.config(width=20, height=14, font = fnt.Font(size = 12))

scrollbar = Scrollbar(right_frame, orient="vertical", command=txt_bx.yview)
scrollbar.grid(row=3, column=2, pady=5, sticky="ns")
txt_bx.config(yscrollcommand=scrollbar.set)

#-----------BUTTONS-------------

A1_btn = Button(left_frame, text = "a", command=lambda:(audio("sounds/Pa.mp3"), select("/"+str(A1.symbol)+"/" + "\n\n" + A1.description +"\n\n"+ A1.phoneme_features())), width=2)
A1_btn.grid(row=1, column=1)

A2_btn = Button(left_frame, text = "æ", command =lambda:(audio("sounds/Pa.mp3"), select("/"+str(A2.symbol)+"/"+"\n\n"+ A2.description +"\n\n"+ A2.phoneme_features())), width=2)
A2_btn.grid(row=1, column=2)

A3_btn = Button(left_frame, text = "ɐ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(A3.symbol)+"/"+"\n\n"+ A3.description +"\n\n"+ A3.phoneme_features())), width=2)
A3_btn.grid(row=1, column=3)
A4_btn = Button(left_frame, text = "ɑ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(A4.symbol)+"/"+"\n\n"+ A4.description +"\n\n"+ A4.phoneme_features())), width=2)
A4_btn.grid(row=1, column=4)

B1_btn = Button(left_frame, text = "b", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(B1.symbol)+"/"+"\n\n"+ B1.description +"\n\n"+  B1.phoneme_features())), width=2)
B1_btn.grid(row=1, column=5)
B2_btn = Button(left_frame, text = "β", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(B2.symbol)+"/"+"\n\n"+ B2.description +"\n\n"+ B2.phoneme_features())), width=2)
B2_btn.grid(row=1, column=6)
B3_btn = Button(left_frame, text = "ɓ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(B3.symbol)+"/"+"\n\n"+ B3.description +"\n\n"+ B3.phoneme_features())), width=2)
B3_btn.grid(row=1, column=7)
B4_btn = Button(left_frame, text = "ʙ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(B4.symbol)+"/"+"\n\n"+ B4.description +"\n\n"+ B4.phoneme_features())), width=2)
B4_btn.grid(row=1, column=8)

C1_btn = Button(left_frame, text = "c", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(C1.symbol)+"/"+"\n\n"+ C1.description +"\n\n"+ C1.phoneme_features())), width=2)
C1_btn.grid(row=1, column=9)
C2_btn = Button(left_frame, text = "ç", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(C2.symbol)+"/"+"\n\n"+ C2.description +"\n\n"+ C2.phoneme_features())), width=2)
C2_btn.grid(row=1, column=10)
C3_btn = Button(left_frame, text = "ɕ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(C3.symbol)+"/"+"\n\n"+ C3.description +"\n\n"+ C3.phoneme_features())), width=2)
C3_btn.grid(row=1, column=11)

D1_btn = Button(left_frame, text = "d", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(D1.symbol)+"/"+"\n\n"+ D1.description +"\n\n"+ D1.phoneme_features())), width=2)
D1_btn.grid(row=1, column=12)
D2_btn = Button(left_frame, text = "ð", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(D2.symbol)+"/"+"\n\n"+ D2.description +"\n\n"+ D2.phoneme_features())), width=2)
D2_btn.grid(row=2, column=1)
D3_btn = Button(left_frame, text = "d͡ʒ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(D3.symbol)+"/"+"\n\n"+ D3.description +"\n\n"+ D3.phoneme_features())), width=2)
D3_btn.grid(row=2, column=2)
D4_btn = Button(left_frame, text = "ɖ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(D4.symbol)+"/"+"\n\n"+ D4.description +"\n\n"+ D4.phoneme_features())), width=2)
D4_btn.grid(row=2, column=3)
D5_btn = Button(left_frame, text = "ɗ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(D5.symbol)+"/"+"\n\n"+ D5.description +"\n\n"+ D5.phoneme_features())), width=2)
D5_btn.grid(row=2, column=4)

E1_btn = Button(left_frame, text = "e", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(E1.symbol)+"/"+"\n\n"+ E1.description +"\n\n"+ E1.phoneme_features())), width=2)
E1_btn.grid(row=2, column=5)
E2_btn = Button(left_frame, text = "ə", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(E2.symbol)+"/"+"\n\n"+ E2.description +"\n\n"+ E2.phoneme_features())), width=2)
E2_btn.grid(row=2, column=6)
E3_btn = Button(left_frame, text = "ɚ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(E3.symbol)+"/"+"\n\n"+ E3.description +"\n\n"+ E3.phoneme_features())), width=2)
E3_btn.grid(row=2, column=7)
E4_btn = Button(left_frame, text = "ɵ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(E4.symbol)+"/"+"\n\n"+ E4.description +"\n\n"+ E4.phoneme_features())), width=2)
E4_btn.grid(row=2, column=8)
E5_btn = Button(left_frame, text = "ɘ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(E5.symbol)+"/"+"\n\n"+ E5.description +"\n\n"+ E5.phoneme_features())), width=2)
E5_btn.grid(row=2, column=9)
E6_btn = Button(left_frame, text = "ɞ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(E6.symbol)+"/"+"\n\n"+ E6.description +"\n\n"+ E6.phoneme_features())), width=2)
E6_btn.grid(row=2, column=10)

EE1_btn = Button(left_frame, text = "ɛ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(EE1.symbol)+"/"+"\n\n"+ EE1.description +"\n\n"+ EE1.phoneme_features())), width=2)
EE1_btn.grid(row=2, column=11)
EE2_btn = Button(left_frame, text = "ɜ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(EE2.symbol)+"/"+"\n\n"+ EE2.description +"\n\n"+ EE2.phoneme_features())), width=2)
EE2_btn.grid(row=2, column=12)
EE3_btn = Button(left_frame, text = "ɝ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(EE3.symbol)+"/"+"\n\n"+ EE3.description +"\n\n"+ EE3.phoneme_features())), width=2)
EE3_btn.grid(row=3, column=1)

G1_btn = Button(left_frame, text = "ɠ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(G1.symbol)+"/"+"\n\n"+ G1.description +"\n\n"+ G1.phoneme_features())), width=2)
G1_btn.grid(row=3, column=2)
G2_btn = Button(left_frame, text = "ɢ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(G2.symbol)+"/"+"\n\n"+ G2.description +"\n\n"+ G2.phoneme_features())), width=2)
G2_btn.grid(row=3, column=3)
G3_btn = Button(left_frame, text = "ɡ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(G3.symbol)+"/"+"\n\n"+ G3.description +"\n\n"+ G3.phoneme_features())), width=2)
G3_btn.grid(row=3, column=4)

H1_btn = Button(left_frame, text = "ħ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(H1.symbol)+"/"+"\n\n"+ H1.description +"\n\n"+ H1.phoneme_features())), width=2)
H1_btn.grid(row=3, column=5)
H2_btn = Button(left_frame, text = "ɦ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(H2.symbol)+"/"+"\n\n"+ H2.description +"\n\n"+ H2.phoneme_features())), width=2)
H2_btn.grid(row=3, column=6)
H3_btn = Button(left_frame, text = "ɥ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(H3.symbol)+"/"+"\n\n"+ H3.description +"\n\n"+ H3.phoneme_features())), width=2)
H3_btn.grid(row=3, column=7)
H4_btn = Button(left_frame, text = "ɧ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(H4.symbol)+"/"+"\n\n"+ H4.description +"\n\n"+ H4.phoneme_features())), width=2)
H4_btn.grid(row=3, column=8)
H5_btn = Button(left_frame, text = "ʜ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(H5.symbol)+"/"+"\n\n"+ H5.description +"\n\n"+ H5.phoneme_features())), width=2)
H5_btn.grid(row=3, column=9)

I1_btn = Button(left_frame, text = "ɪ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(I1.symbol)+"/"+"\n\n"+ I1.description +"\n\n"+ I1.phoneme_features())), width=2)
I1_btn.grid(row=3, column=10)
I2_btn = Button(left_frame, text = "ɨ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(I2.symbol)+"/"+"\n\n"+ I2.description +"\n\n"+ I2.phoneme_features())), width=2)
I2_btn.grid(row=3, column=11)

J1_btn = Button(left_frame, text = "j", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(J1.symbol)+"/"+"\n\n"+ J1.description +"\n\n"+ J1.phoneme_features())), width=2)
J1_btn.grid(row=3, column=12)
J2_btn = Button(left_frame, text = "ʝ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(J2.symbol)+"/"+"\n\n"+ J2.description +"\n\n"+ J2.phoneme_features())), width=2)
J2_btn.grid(row=4, column=1)
J3_btn = Button(left_frame, text = "ɟ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(J3.symbol)+"/"+"\n\n"+ J3.description +"\n\n"+ J3.phoneme_features())), width=2)
J3_btn.grid(row=4, column=2)
J4_btn = Button(left_frame, text = "ʄ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(J4.symbol)+"/"+"\n\n"+ J4.description +"\n\n"+ J4.phoneme_features())), width=2)
J4_btn.grid(row=4, column=3)

L1_btn = Button(left_frame, text = "ɫ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(L1.symbol)+"/"+"\n\n"+ L1.description +"\n\n"+ L1.phoneme_features())), width=2)
L1_btn.grid(row=4, column=4)
L2_btn = Button(left_frame, text = "ɭ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(L2.symbol)+"/"+"\n\n"+ L2.description +"\n\n"+ L2.phoneme_features())), width=2)
L2_btn.grid(row=4, column=5)
L3_btn = Button(left_frame, text = "ɬ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(L3.symbol)+"/"+"\n\n"+ L3.description +"\n\n"+ L3.phoneme_features())), width=2)
L3_btn.grid(row=4, column=6)
L4_btn = Button(left_frame, text = "ʟ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(L4.symbol)+"/"+"\n\n"+ L4.description +"\n\n"+ L4.phoneme_features())), width=2)
L4_btn.grid(row=4, column=7)
L5_btn = Button(left_frame, text = "ɮ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(L5.symbol)+"/"+"\n\n"+ L5.description +"\n\n"+ L5.phoneme_features())), width=2)
L5_btn.grid(row=4, column=8)

M1_btn = Button(left_frame, text = "ɱ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(M1.symbol)+"/"+"\n\n"+ M1.description +"\n\n"+ M1.phoneme_features())), width=2)
M1_btn.grid(row=4, column=9)

N1_btn = Button(left_frame, text = "ŋ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(N1.symbol)+"/"+"\n\n"+ N1.description +"\n\n"+ N1.phoneme_features())), width=2)
N1_btn.grid(row=4, column=10)
N2_btn = Button(left_frame, text = "ɲ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(N2.symbol)+"/"+"\n\n"+ N2.description +"\n\n"+ N2.phoneme_features())), width=2)
N2_btn.grid(row=4, column=11)
N3_btn = Button(left_frame, text = "ɳ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(N3.symbol)+"/"+"\n\n"+ N3.description +"\n\n"+ N3.phoneme_features())), width=2)
N3_btn.grid(row=4, column=12)
N4_btn = Button(left_frame, text = "ɴ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(N4.symbol)+"/"+"\n\n"+ N4.description +"\n\n"+ N4.phoneme_features())), width=2)
N4_btn.grid(row=5, column=1)

O1_btn = Button(left_frame, text = "o", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(O1.symbol)+"/"+"\n\n"+ O1.description +"\n\n"+ O1.phoneme_features())), width=2)
O1_btn.grid(row=5, column=2)
O2_btn = Button(left_frame, text = "ɔ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(O2.symbol)+"/"+"\n\n"+ O2.description +"\n\n"+ O2.phoneme_features())), width=2)
O2_btn.grid(row=5, column=3)
O3_btn = Button(left_frame, text = "œ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(O3.symbol)+"/"+"\n\n"+ O3.description +"\n\n"+ O3.phoneme_features())), width=2)
O3_btn.grid(row=5, column=4)
O4_btn = Button(left_frame, text = "ɒ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(O4.symbol)+"/"+"\n\n"+ O4.description +"\n\n"+ O4.phoneme_features())), width=2)
O4_btn.grid(row=5, column=5)
O5_btn = Button(left_frame, text = "ɶ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(O5.symbol)+"/"+"\n\n"+ O5.description +"\n\n"+ O5.phoneme_features())), width=2)
O5_btn.grid(row=5, column=6)
O6_btn = Button(left_frame, text = "ø", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(O6.symbol)+"/"+"\n\n"+ O6.description +"\n\n"+ O6.phoneme_features())), width=2)
O6_btn.grid(row=5, column=7)

P1_btn = Button(left_frame, text = "p", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(P1.symbol)+"/"+"\n\n"+ P1.description +"\n\n"+ P1.phoneme_features())), width=2)
P1_btn.grid(row=5, column=8)
P2_btn = Button(left_frame, text = "ɸ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(P2.symbol)+"/"+"\n\n"+ P2.description +"\n\n"+ P2.phoneme_features())), width=2)
P2_btn.grid(row=5, column=9)

R1_btn = Button(left_frame, text = "ɾ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(R1.symbol)+"/"+"\n\n"+ R1.description +"\n\n"+ R1.phoneme_features())), width=2)
R1_btn.grid(row=5, column=10)
R2_btn = Button(left_frame, text = "ɹ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(R2.symbol)+"/"+"\n\n"+ R2.description +"\n\n"+ R2.phoneme_features())), width=2)
R2_btn.grid(row=5, column=11)
R3_btn = Button(left_frame, text = "ʁ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(R3.symbol)+"/"+"\n\n"+ R3.description +"\n\n"+ R3.phoneme_features())), width=2)
R3_btn.grid(row=5, column=12)
R4_btn = Button(left_frame, text = "ʀ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(R4.symbol)+"/"+"\n\n"+ R4.description +"\n\n"+ R4.phoneme_features())), width=2)
R4_btn.grid(row=6, column=1)
R5_btn = Button(left_frame, text = "ɻ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(R5.symbol)+"/"+"\n\n"+ R5.description +"\n\n"+ R5.phoneme_features())), width=2)
R5_btn.grid(row=6, column=2)
R6_btn = Button(left_frame, text = "ɽ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(R6.symbol)+"/"+"\n\n"+ R6.description +"\n\n"+ R6.phoneme_features())), width=2)
R6_btn.grid(row=6, column=3)
R7_btn = Button(left_frame, text = "ɺ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(R7.symbol)+"/"+"\n\n"+ R7.description +"\n\n"+ R7.phoneme_features())), width=2)
R7_btn.grid(row=6, column=4)

S1_btn = Button(left_frame, text = "s", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(S1.symbol)+"/"+"\n\n"+ S1.description +"\n\n"+ S1.phoneme_features())), width=2)
S1_btn.grid(row=6, column=5)
S2_btn = Button(left_frame, text = "ʃ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(S2.symbol)+"/"+"\n\n"+ S2.description +"\n\n"+ S2.phoneme_features())), width=2)
S2_btn.grid(row=6, column=6)
S3_btn = Button(left_frame, text = "ʂ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(S3.symbol)+"/"+"\n\n"+ S3.description +"\n\n"+ S3.phoneme_features())), width=2)
S3_btn.grid(row=6, column=7)

T1_btn = Button(left_frame, text = "t", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(T1.symbol)+"/"+"\n\n"+ T1.description +"\n\n"+ T1.phoneme_features())), width=2)
T1_btn.grid(row=6, column=8)
T2_btn = Button(left_frame, text = "θ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(T2.symbol)+"/"+"\n\n"+ T2.description +"\n\n"+ T2.phoneme_features())), width=2)
T2_btn.grid(row=6, column=9)
T3_btn = Button(left_frame, text = "t͡ʃ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(T3.symbol)+"/"+"\n\n"+ T3.description +"\n\n"+ T3.phoneme_features())), width=2)
T3_btn.grid(row=6, column=10)
T4_btn = Button(left_frame, text = "t͡s", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(T4.symbol)+"/"+"\n\n"+ T4.description +"\n\n"+ T4.phoneme_features())), width=2)
T4_btn.grid(row=6, column=11)
T5_btn = Button(left_frame, text = "ʈ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(T5.symbol)+"/"+"\n\n"+ T5.description +"\n\n"+ T5.phoneme_features())), width=2)
T5_btn.grid(row=6, column=12)

U1_btn = Button(left_frame, text = "u", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(U1.symbol)+"/"+"\n\n"+ U1.description +"\n\n"+ U1.phoneme_features())), width=2)
U1_btn.grid(row=7, column=1)
U2_btn = Button(left_frame, text = "ʊ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(U2.symbol)+"/"+"\n\n"+ U2.description +"\n\n"+ U2.phoneme_features())), width=2)
U2_btn.grid(row=7, column=2)
U3_btn = Button(left_frame, text = "ʉ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(U3.symbol)+"/"+"\n\n"+ U3.description +"\n\n"+ U3.phoneme_features())), width=2)
U3_btn.grid(row=7, column=3)

V1_btn = Button(left_frame, text = "v", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(V1.symbol)+"/"+"\n\n"+ V1.description +"\n\n"+ V1.phoneme_features())), width=2)
V1_btn.grid(row=7, column=4)
V2_btn = Button(left_frame, text = "ʌ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(V2.symbol)+"/"+"\n\n"+ V2.description +"\n\n"+ V2.phoneme_features())), width=2)
V2_btn.grid(row=7, column=5)
V3_btn = Button(left_frame, text = "ʋ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(V3.symbol)+"/"+"\n\n"+ V3.description +"\n\n"+ V3.phoneme_features())), width=2)
V3_btn.grid(row=7, column=6)
V4_btn = Button(left_frame, text = "ⱱ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(V4.symbol)+"/"+"\n\n"+ V4.description +"\n\n"+ V4.phoneme_features())), width=2)
V4_btn.grid(row=7, column=7)

W1_btn = Button(left_frame, text = "ɯ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(W1.symbol)+"/"+"\n\n"+ W1.description +"\n\n"+ W1.phoneme_features())), width=2)
W1_btn.grid(row=7, column=8)
W2_btn = Button(left_frame, text = "ʍ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(W2.symbol)+"/"+"\n\n"+ W2.description +"\n\n"+ W2.phoneme_features())), width=2)
W2_btn.grid(row=7, column=9)

X1_btn = Button(left_frame, text = "x", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(X1.symbol)+"/"+"\n\n"+ X1.description +"\n\n"+ X1.phoneme_features())), width=2)
X1_btn.grid(row=7, column=10)
X2_btn = Button(left_frame, text = "χ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(X2.symbol)+"/"+"\n\n"+ X2.description +"\n\n"+ X2.phoneme_features())), width=2)
X2_btn.grid(row=7, column=11)

Y1_btn = Button(left_frame, text = "ɣ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Y1.symbol)+"/"+"\n\n"+ Y1.description +"\n\n"+ Y1.phoneme_features())), width=2)
Y1_btn.grid(row=7, column=12)
Y2_btn = Button(left_frame, text = "ʎ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Y2.symbol)+"/"+"\n\n"+ Y2.description +"\n\n"+ Y2.phoneme_features())), width=2)
Y2_btn.grid(row=8, column=1)
Y3_btn = Button(left_frame, text = "ʏ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Y3.symbol)+"/"+"\n\n"+ Y3.description +"\n\n"+ Y3.phoneme_features())), width=2)
Y3_btn.grid(row=8, column=2)
Y4_btn = Button(left_frame, text = "ɤ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Y4.symbol)+"/"+"\n\n"+ Y4.description +"\n\n"+ Y4.phoneme_features())), width=2)
Y4_btn.grid(row=8, column=3)

Z1_btn = Button(left_frame, text = "z", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Z1.symbol)+"/"+"\n\n"+ Z1.description +"\n\n"+ Z1.phoneme_features())), width=2)
Z1_btn.grid(row=8, column=4)
Z2_btn = Button(left_frame, text = "ʒ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Z2.symbol)+"/"+"\n\n"+ Z2.description +"\n\n"+ Z2.phoneme_features())), width=2)
Z2_btn.grid(row=8, column=5)
Z3_btn = Button(left_frame, text = "ʐ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Z3.symbol)+"/"+"\n\n"+ Z3.description +"\n\n"+ Z3.phoneme_features())), width=2)
Z3_btn.grid(row=8, column=6)
Z4_btn = Button(left_frame, text = "ʑ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(Z4.symbol)+"/"+"\n\n"+ Z4.description +"\n\n"+ Z4.phoneme_features())), width=2)
Z4_btn.grid(row=8, column=7)
ZZ1_btn = Button(left_frame, text = "ʔ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(ZZ1.symbol)+"/"+"\n\n"+ ZZ1.description +"\n\n"+ ZZ1.phoneme_features())), width=2)
ZZ1_btn.grid(row=8, column=8)
ZZ2_btn = Button(left_frame, text = "ʕ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(ZZ2.symbol)+"/"+"\n\n"+ ZZ2.description +"\n\n"+ ZZ2.phoneme_features())), width=2)
ZZ2_btn.grid(row=8, column=9)
ZZ3_btn = Button(left_frame, text = "ʡ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(ZZ3.symbol)+"/"+"\n\n"+ ZZ3.description +"\n\n"+ ZZ3.phoneme_features())), width=2)
ZZ3_btn.grid(row=8, column=10)
ZZ4_btn = Button(left_frame, text = "ʢ", command = lambda:(audio("sounds/Pa.mp3"), select("/"+str(ZZ4.symbol)+"/"+"\n\n"+ ZZ4.description +"\n\n"+ ZZ4.phoneme_features())), width=2)
ZZ4_btn.grid(row=8, column=11)


root.mainloop()

