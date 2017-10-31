from ROOT import *
import glob 
from math import sqrt
 
ch = TChain("mytree");
MyFileNames12 = glob.glob('new.root')
#MyFileNames12 = glob.glob('../SimpleFile_Bs_to_Xphi_b711_preselection_test5_NoMultCandRemoval_0_14000.root')
for fName in MyFileNames12 :
    ch.Add(fName)

print "Adding chain done", ch.GetNtrees(), 'files '
print 'variables: ', [a.GetName() for a in ch.GetListOfLeaves()]

hXmas1 = TH1F('hXmas1', 'h', 125, 5.10,  5.60)  # M(Bs)       bin =  4 MeV 
hXmas2 = TH1F('hXmas2', 'h', 150, 3.8,  4.1)    # M(X)        bin =  2 MeV 
hXmas3 = TH1F('hXmas3', 'h', 20, 0.2,  0.8)     # M(pi+pi-)   bin = 20 MeV
hXmas4 = TH1F('hXmas4', 'h', 50, 0.950,  1.100) # M(K+K-)     bin =  3 MeV 

cc = TCanvas('cc', 'cc', 1000, 1000)
cc.Divide(2,2)
cc.cd(1)

BU1m = 4.2; 	BU1M = 4.4; 	BU1col = 2
BU2m = 4.4; 	BU2M = 4.6; 	BU2col = 4
BU3m = 4.5; 	BU3M = 4.6; 	BU3col = 6
BU4m = 4.6; 	BU4M = 4.7; 	BU4col = 1
BU5m = 4.8; 	BU5M = 4.9; 	BU5col = 6


cuts1 = 'PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78  && abs(X_mass_Cjp-3.872)<0.010 && abs(PHI_mass_Cjp - 1.02)<0.005 && abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.686)<110.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'
cuts2 = 'PIPI_mass_Cjp > 0.65  && PIPI_mass_Cjp < 0.78 && abs(PHI_mass_Cjp - 1.02)<0.005 && abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.872)<0.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'
cuts3 = 'abs(X_mass_Cjp-3.872)<0.010 && abs(PHI_mass_Cjp - 1.02)<0.005 && abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.872)<0.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'
cuts4 = 'PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78 && abs(X_mass_Cjp-3.872)<0.010 && abs(PHI_mass_Cjp - 1.02)<10.010 && abs(BU_mass_Cjp-5.367-X_mass_Cjp+3.872)<0.015 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.999 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 5 && K1_pt > .7 && K2_pt > .7 && PI1_pt > 0.6 && PI2_pt > 0.6'
 


#cuts1 = 'PIPI_mass_Cjp > 0.6 && PIPI_mass_Cjp < 0.78 &&  abs(PHI_mass_Cjp - 1.02)<0.007 && abs(BU_mass_Cjp-5.367)<0.030 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.99 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 3 && K1_pt > 0.7 && K2_pt > 0.7 && PI1_pt > 0.6 && PI2_pt > 0.6'
#cuts2 = 'PIPI_mass_Cjp > 0.6  && PIPI_mass_Cjp < 0.78 && abs(PHI_mass_Cjp - 1.02)<0.007 && abs(BU_mass_Cjp-5.367)<0.030 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.99 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 3 && K1_pt > 1.0 && K2_pt > 1.0 && PI1_pt > 0.6 && PI2_pt > 0.6'
#cuts3 = 'PIPI_mass_Cjp > 0.6  && PIPI_mass_Cjp < 0.78 && abs(PHI_mass_Cjp - 1.02)<0.007 && abs(BU_mass_Cjp-5.367)<0.020 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.99 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 7 && K1_pt > 1.0 && K2_pt > 1.0 && PI1_pt > 0.6 && PI2_pt > 0.6'
#cuts4 = 'PIPI_mass_Cjp > 0.6  && PIPI_mass_Cjp < 0.78 && abs(PHI_mass_Cjp - 1.02)<0.007 && abs(BU_mass_Cjp-5.367)<0.030 && BU_pt_Cjp > 15 && BU_pvcos2_Cjp > 0.99 && BU_vtxprob_Cjp > 0.10 && BU_pvdistsignif2_Cjp > 10 && K1_pt > 1.0 && K2_pt > 1.0 && PI1_pt > 0.6 && PI2_pt > 0.6'


#cuts1 = cuts0 + '&& BU_mass_Cjp > %f && BU_mass_Cjp < %f'%(BU2m, BU2M)
#cuts2 = cuts0 + '&& BU_mass_Cjp > %f && BU_mass_Cjp < %f'%(BU3m, BU3M)
#cuts3 = cuts00 + '&& BU_mass_Cjp > %f && BU_mass_Cjp < %f'%(BU2m, BU2M)
#cuts4 = cuts00 + '&& BU_mass_Cjp > %f && BU_mass_Cjp < %f'%(BU3m, BU3M)


hXmas1.SetLineColor(BU1col); 
ch.Draw('BU_mass_Cjp-X_mass_Cjp+3.872 >> hXmas1', cuts1)
#ch.Draw('BU_mass_Cjp-X_mass_Cjp+3.686 >> hXmas1', cuts1)
L11=TLine(5.382, 0, 5.382, 22)
L11.Draw("same")
L12=TLine(5.352, 0, 5.352, 22)
L12.Draw("same")

cc.cd(2)
hXmas2.SetLineColor(BU2col)
ch.Draw('X_mass_Cjp >> hXmas2', cuts2)
L21=TLine(3.882, 0, 3.882, 20.5)
L21.Draw("same")
L22=TLine(3.862, 0, 3.862, 20.5)
L22.Draw("same")

cc.cd(3)
hXmas3.SetLineColor(BU3col)
ch.Draw('PIPI_mass_Cjp >> hXmas3', cuts3)
L31=TLine(0.65, 0, 0.65, 35)
L31.Draw("same")
L32=TLine(0.78, 0, 0.78, 35)
L32.Draw("same")

cc.cd(4)
hXmas4.SetLineColor(BU4col)
ch.Draw('PHI_mass_Cjp >> hXmas4', cuts4)
L41=TLine(1.015, 0, 1.015, 42)
L41.Draw("same")
L42=TLine(1.025, 0, 1.025, 42)
L42.Draw("same")

cc.SaveAs('picX_test.r0.pdf')
 
ff=TFile("b715_test7_X.root", "recreate") 
hXmas1.Write()
hXmas2.Write()
hXmas3.Write()
hXmas4.Write()
cc.Write()
ff.Close()






'''

def mydraw(_cuts):
    h = TH1F('h', 'h', 200, 5.1, 5.5)
    cc = TCanvas('cc', 'cc', 800, 600)
    h.SetTitle(_cuts)
    ch.Draw('BU_mass_Cjp >> h', _cuts)
    cc.SaveAs('pica.gif')


mydraw('K1_pt > 0.8 && BU_pvcos2_Cjp > 0.98 && BU_pvdistsignif2_Cjp > 5')


'''

























