# Calcul les intervales pour un nombre de FFT

BRP = 10
pilot = 9
guard_Droit = 27
guard_Gauche = 28

Nfft= int(input("NFFT (puissance de 2) : "))

if Nfft != 64 and Nfft != 128 and Nfft != 256 and Nfft != 512 and Nfft != 1024:
	print("NFFT donné n'est pas un puissance de 2 ! Les valeurs possibles sont  64 / 128 / 256 / 512 / 1024")
	Nfft= int(input("NFFT (puissance de 2) : "))

taillePrefixe=int(input("Taille préfixe cyclique : "))

SampleParFrame = Nfft - pilot - guard_Droit - guard_Gauche
print("Sample par Frame : ",SampleParFrame)

nombreEchanBRP = (SampleParFrame//10) * 8
print("nombreEchanBRP : ",nombreEchanBRP)
IntervalBase = SampleParFrame//10
print("Interval de base : ",IntervalBase)
intervalExtrem = (SampleParFrame - nombreEchanBRP)/2
print("Interval de chaque coté : ",intervalExtrem)
#Select Row
print("selectRow = {",1,":",int(intervalExtrem)," ",int(intervalExtrem+1),":",int(intervalExtrem+IntervalBase)," ",int(intervalExtrem+IntervalBase+1),":",int(intervalExtrem+2*IntervalBase)," ",int(intervalExtrem+2*IntervalBase+1),":",int(intervalExtrem+3*IntervalBase)," ",int(intervalExtrem+3*IntervalBase+1),":",int(intervalExtrem+4*IntervalBase)," ",int(intervalExtrem+4*IntervalBase+1),":",int(intervalExtrem+5*IntervalBase)," ",int(intervalExtrem+5*IntervalBase+1),":",int(intervalExtrem+6*IntervalBase)," ",int(intervalExtrem+6*IntervalBase+1),":",int(intervalExtrem+7*IntervalBase)," ",int(intervalExtrem+7*IntervalBase+1),":",int(intervalExtrem+8*IntervalBase)," ",int(intervalExtrem+8*IntervalBase+1),":",int(2*intervalExtrem+8*IntervalBase),"}")
print("prefixeCyclique = [",Nfft-taillePrefixe+1,":",Nfft," ",1,":",Nfft,"]")
print("removePrefixeCyclique = [",taillePrefixe+1,":",Nfft+taillePrefixe,"]")
print("removeZeroPading = [",guard_Gauche+1,":",int(Nfft/2)," ",int((Nfft/2)+2),":",Nfft-guard_Droit,"]")
print("removePilot = {[",1,":",int(intervalExtrem)," ",int(intervalExtrem+2),":",int(intervalExtrem+IntervalBase+1)," ",int(intervalExtrem+IntervalBase+3),":",int(intervalExtrem+(2*IntervalBase)+2)," ",int(intervalExtrem+(2*IntervalBase)+4),":",int(intervalExtrem+(3*IntervalBase)+3)," ",int(intervalExtrem+(3*IntervalBase)+5),":",int(intervalExtrem+(5*IntervalBase)+4)," ",int(intervalExtrem+(5*IntervalBase)+6),":",int(intervalExtrem+(6*IntervalBase)+5)," ",int(intervalExtrem+(6*IntervalBase)+7),":",int(intervalExtrem+(7*IntervalBase)+6)," ",int(intervalExtrem+(7*IntervalBase)+8),":",int(intervalExtrem+(8*IntervalBase)+7)," ",int(intervalExtrem+(8*IntervalBase)+9),":",int((2*intervalExtrem)+(8*IntervalBase)+8),"],[",int(intervalExtrem+1)," ",int(intervalExtrem+IntervalBase+2)," ",int(intervalExtrem+(2*IntervalBase)+3)," ",int(intervalExtrem+(3*IntervalBase)+4)," ",int(intervalExtrem+(5*IntervalBase)+5)," ",int(intervalExtrem+(6*IntervalBase)+6)," ",int(intervalExtrem+(7*IntervalBase)+7)," ",int(intervalExtrem+(8*IntervalBase)+8),"]}",)