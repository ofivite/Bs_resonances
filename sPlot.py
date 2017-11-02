import ROOT
from ROOT import RooFit as RF
import math
from RooSpace import *

left_psi = 3.686 - 0.03; right_psi = 3.686 + 0.03; nbins_psi = 60
left_X = 3.872 - 0.07; right_X = 3.872 + 0.07; nbins_X = 35
var_control.setRange("psi", left_psi, right_psi)
var_control.setRange("X", left_X, right_X)

file_data = ROOT.TFile('new.root')
cuts = 'TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15' #PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78 &&

c = ROOT.TCanvas("c", "c", 1700, 650)
c.Divide(3,2)

###############
#_-_-_-_-_-_-#
#############

data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts)
# model_discr.fitTo(data)
# model_discr.fitTo(data)
#
# c.cd(1)
# frame_discr = var_discr.frame(RF.Title('m(J/#psi#pi^{+}#pi^{-}#phi) inclusive'))
# data.plotOn(frame_discr)
# model_discr.paramOn(frame_discr)
# model_discr.plotOn(frame_discr)
# frame_discr.Draw()

################
##_-_-_-_-_-_-#
##############
print '\n\n#################################\n\n\n           psi(2S) now\n\n\n#################################\n\n'

data_psi = data.reduce('X_mass_Cjp >' + str(left_psi) + ' && X_mass_Cjp < ' + str(right_psi))
model_discr.fitTo(data_psi)
model_discr.fitTo(data_psi)
model_discr.fitTo(data_psi)

c.cd(2)
frame_discr = var_discr.frame(RF.Title('m(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S)'))
data_psi.plotOn(frame_discr)
model_discr.paramOn(frame_discr)
model_discr.plotOn(frame_discr)
frame_discr.Draw()

# ----- Compute sWeights
sData_psi = ROOT.RooStats.SPlot(
    'sData_psi', 'sData_psi', data_psi, model_discr,
    ROOT.RooArgList(N_sig_discr, N_bkgr_discr)
)

print '\n\n\n\n\n\n\n\n\n\n\n\n'
print "Yield of signal is " , N_sig_discr.getVal() , ".  From sWeights it is " , sData_psi.GetYieldFromSWeight("N_sig_discr")
print '\n\n\n\n\n\n\n\n\n\n\n\n'

################
##_-_-_-_-_-_-#
##############

c.cd(3)
var_control.setMin(left_psi); var_control.setMax(right_psi)
data_psi_weighted = ROOT.RooDataSet(data_psi.GetName(),data_psi.GetTitle(),data_psi, data_psi.get(),'X_mass_Cjp >' + str(left_psi) + ' && X_mass_Cjp < ' + str(right_psi), "N_sig_discr_sw") ;
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.Range("psi")) #
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.Range("psi")) # , RF.Range("psi")
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.Range("psi")) # , RF.Range("psi")

frame_control = var_control.frame(RF.Title('sPlot for #psi(2S))'), RF.Bins(nbins_psi), RF.Range('psi'))
data_psi_weighted.plotOn(frame_control)
model_psi.paramOn(frame_control)
model_psi.plotOn(frame_control, RF.NormRange("psi"), RF.Range("psi"))
frame_control.Draw()

###############################################################################################################################
print '\n\n#################################\n\n\n           X now\n\n\n#################################\n\n'

data_X = data.reduce('X_mass_Cjp >' + str(left_X) + ' && X_mass_Cjp < ' + str(right_X))
model_discr.fitTo(data_X)
model_discr.fitTo(data_X)
model_discr.fitTo(data_X)

c.cd(5)
frame_discr = var_discr.frame(RF.Title('m(J/#psi#pi^{+}#pi^{-}#phi) from X(3872)'))
data_X.plotOn(frame_discr)
model_discr.paramOn(frame_discr)
model_discr.plotOn(frame_discr)
frame_discr.Draw()

# ----- Compute sWeights
ROOT.RooStats.SPlot(
    'sData_X', 'sData_X', data_X, model_discr,
    ROOT.RooArgList(N_sig_discr,N_bkgr_discr)
)

################
##_-_-_-_-_-_-#
##############

c.cd(6)

var_control.setMin(left_X); var_control.setMax(right_X)

data_X_weighted = ROOT.RooDataSet(data_X.GetName(),data_X.GetTitle(),data_X, data_X.get(),'', "N_sig_discr_sw") ;
r_X = model_X.fitTo(data_X_weighted, RF.Save(), RF.Range("X"))
r_X = model_X.fitTo(data_X_weighted, RF.Save(), RF.Range("X"))
r_X = model_X.fitTo(data_X_weighted, RF.Save(), RF.Range("X"))

# frame_control = ROOT.RooPlot('frame_control', 'sPlot for X(3872)', var_control, left_X, right_X, nbins_X)
frame_control = var_control.frame(RF.Title('sPlot for X(3872)'), RF.Bins(nbins_X), RF.Range('X'))
data_X_weighted.plotOn(frame_control)
model_X.paramOn(frame_control)
model_X.plotOn(frame_control, RF.NormRange("X"), RF.Range("X"))
frame_control.Draw()


################################################################################################################################

################
##_-_-_-_-_-_-#
##############
#
# data_X = data.reduce('X_mass_Cjp > 3.872 - 0.15 && X_mass_Cjp < 3.872 + 0.15')
# model_discr.fitTo(data_X)
# model_discr.fitTo(data_X)
#
# c.cd(5)
# frame_discr_X = var_discr.frame(RF.Title('m(J/#psi#pi^{+}#pi^{-}#phi from X(3872)'))
# data_X.plotOn(frame_discr_X)
# model_discr.paramOn(frame_discr_X)
# model_discr.plotOn(frame_discr_X)
# frame_discr_X.Draw()
#
# # Compute sWeights
# ROOT.RooStats.SPlot(
#     'sData_X', 'sData_X', data_X, model_discr,
#     ROOT.RooArgList(N_sig_discr,N_bkgr_discr)
# )
#
# data_X_weighted = ROOT.RooDataSet(data_X.GetName(),data_X.GetTitle(),data_X, data_X.get(),'X_mass_Cjp > 3.872 - 0.15 && X_mass_Cjp < 3.872 + 0.15', "N_sig_discr_sw") ;
# # data_bkgr_weighted = ROOT.RooDataSet(data.GetName(),data.GetTitle(),data, data.get(),'',"N_bkgr_discr_sw") ;
#
# c.cd(6)
# left = 3.872 - 0.15; right = 3.872 - 0.15; nbins = 60
# var_control.setRange(left, right)
# frame_control_X = var_control.frame(RF.Title('sPlot for X(3872)'), RF.Bins(nbins))
#
# print '\n\n#################################\n\n\n           X now\n\n\n#################################\n\n'
# model_X.fitTo(data_X_weighted)
# model_X.fitTo(data_X_weighted)
# data_X_weighted.plotOn(frame_control_X)
# model_X.paramOn(frame_control_X)
# model_X.plotOn(frame_control_X)
# frame_control_X.Draw()

c.SaveAs('sPlot.png')
