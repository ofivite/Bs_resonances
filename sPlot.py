import ROOT
from ROOT import RooFit as RF
import math
from RooSpace import *

left_psi = 3.686 - 0.03; right_psi = 3.686 + 0.03; nbins_psi = 60
left_X = 3.872 - 0.07; right_X = 3.872 + 0.07; nbins_X = 35
# var_control.setRange("psi", left_psi, right_psi)
# var_control.setRange("X", left_X, right_X)

file_data = ROOT.TFile('new.root')
cuts = 'TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15' #PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78 &&

c = ROOT.TCanvas("c", "c", 1700, 650)
c.Divide(3,2)

###############
#_-_-_-_-_-_-#
#############

data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts)
model_discr.fitTo(data)
model_discr.fitTo(data)

c.cd(1)
frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) inclusive', var_discr, left_discr, right_discr, nbins_discr);
data.plotOn(frame_discr)
model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.87, 0.6))
model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 4 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 4 * sigma_Bs_1.getValV()));

frame_discr.Draw()

################
##_-_-_-_-_-_-#
##############
print '\n\n#################################\n\n\n           psi(2S) now\n\n\n#################################\n\n'

data_psi = data.reduce('X_mass_Cjp >' + str(left_psi) + ' && X_mass_Cjp < ' + str(right_psi))
model_discr.fitTo(data_psi)
model_discr.fitTo(data_psi)
model_discr.fitTo(data_psi)

c.cd(2)
frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S) region', var_discr, left_discr, right_discr, nbins_discr);
data_psi.plotOn(frame_discr)
model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.87, 0.6))
model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 4 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 4 * sigma_Bs_1.getValV()));

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
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save()) #
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save()) # , RF.Range("psi")
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save()) # , RF.Range("psi")


frame_control = ROOT.RooPlot(" ", "sPlot for #psi(2S) region", var_control, left_psi, right_psi, nbins_psi);
# frame_control = var_control.frame(RF.Title('sPlot for #psi(2S) region'), RF.Bins(nbins_psi))
data_psi_weighted.plotOn(frame_control, ROOT.RooLinkedList())
model_psi.paramOn(frame_control, RF.Layout(0.55, 0.87, 0.6))
model_psi.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_psi.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_psi.plotOn(frame_control, RF.Components("sig_psi_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_psi.getValV() - 4 * sigma_psi_1.getValV(), mean_psi.getValV() + 4 * sigma_psi_1.getValV()));
model_psi.plotOn(frame_control, RF.Components("sig_psi_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_psi.getValV() - 4 * sigma_psi_2.getValV(), mean_psi.getValV() + 4 * sigma_psi_2.getValV()));
# model_psi.plotOn(frame_control) # , RF.NormRange("psi"), RF.Range("psi")
frame_control.Draw()

###############################################################################################################################
print '\n\n#################################\n\n\n           X now\n\n\n#################################\n\n'

data_X = data.reduce('X_mass_Cjp >' + str(left_X) + ' && X_mass_Cjp < ' + str(right_X))
model_discr.fitTo(data_X)
model_discr.fitTo(data_X)
model_discr.fitTo(data_X)

c.cd(5)
frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) from X(3872) region', var_discr, left_discr, right_discr, nbins_discr);
data_X.plotOn(frame_discr)
model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.87, 0.6))
model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 4 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 4 * sigma_Bs_1.getValV()));

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

data_X_weighted = ROOT.RooDataSet(data_X.GetName(),data_X.GetTitle(),data_X, data_X.get(), 'X_mass_Cjp >' + str(left_X) + ' && X_mass_Cjp < ' + str(right_X), "N_sig_discr_sw") ;
r_X = model_X.fitTo(data_X_weighted, RF.Save())
r_X = model_X.fitTo(data_X_weighted, RF.Save())
r_X = model_X.fitTo(data_X_weighted, RF.Save())

# frame_control = ROOT.RooPlot('frame_control', 'sPlot for X(3872) region', var_control, left_X, right_X, nbins_X)
frame_control = ROOT.RooPlot(" ", "sPlot for X(3872) region", var_control, left_X, right_X, nbins_X);
data_X_weighted.plotOn(frame_control)
model_X.paramOn(frame_control, RF.Layout(0.55, 0.87, 0.6))
model_X.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_X.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_X.plotOn(frame_control, RF.Components("signal_X"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_X.getValV() - 4 * sigma_X.getValV(), mean_X.getValV() + 4 * sigma_X.getValV()));

# model_X.plotOn(frame_control) # , RF.NormRange("X"), RF.Range("X")
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
# frame_control_X = var_control.frame(RF.Title('sPlot for X(3872) region'), RF.Bins(nbins))
#
# print '\n\n#################################\n\n\n           X now\n\n\n#################################\n\n'
# model_X.fitTo(data_X_weighted)
# model_X.fitTo(data_X_weighted)
# data_X_weighted.plotOn(frame_control_X)
# model_X.paramOn(frame_control_X)
# model_X.plotOn(frame_control_X)
# frame_control_X.Draw()

c.SaveAs('sPlot.png')
