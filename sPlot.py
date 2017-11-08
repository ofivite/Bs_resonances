import ROOT
from ROOT import RooFit as RF
import math
from RooSpace import *

left_discr =  5.3669 - 0.21; right_discr = 5.3669 + 0.21; nbins_discr = 60   # var_discr is defined accordingly to these values
left_psi = 3.686 - 0.03; right_psi = 3.686 + 0.03; nbins_psi = 60
left_X = 3.872 - 0.08; right_X = 3.872 + 0.08; nbins_X = 32

file_data = ROOT.TFile('new.root')
cuts = 'TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15 && BU_mass_Cjp > ' + str(left_discr) + '&& BU_mass_Cjp < ' + str(right_discr)
cuts_psi = 'X_mass_Cjp >' + str(left_psi) + ' && X_mass_Cjp < ' + str(right_psi) # + ' && PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'
cuts_X = 'X_mass_Cjp >' + str(left_X) + ' && X_mass_Cjp < ' + str(right_X) # + ' && PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78'

c = ROOT.TCanvas("c", "c", 1700, 650)
c.Divide(3,2)

####################################################
#_-_-_-_-_-_-      INCLUSIVE DATA      _-_-_-_-_-_-#
####################################################

var_discr.setMin(left_discr); var_discr.setMax(right_discr)
data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts)
model_discr.fitTo(data)
model_discr.fitTo(data)

c.cd(1)
frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) inclusive', var_discr, left_discr, right_discr, nbins_discr);
data.plotOn(frame_discr)
model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.87, 0.6))
model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 40 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 40 * sigma_Bs_1.getValV()));
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 40 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 40 * sigma_Bs_2.getValV()));

frame_discr.Draw()


##########################################################
#_-_-_-_-_-_-          PSI(2S) DATA          _-_-_-_-_-_-#
##########################################################

print '\n\n' + 30*'#' + '\n\n\n           psi(2S) now\n\n\n' + 30*'#' + '\n\n'

file_MC_psi = ROOT.TFile('SimpleFileMC_b715psi_0_14000.root')
data_psi = data.reduce(cuts_psi)
# data_psi = ROOT.RooDataSet('data', '', file_MC_psi.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts + '&& ' + cuts_psi)

sigma_Bs_1.setVal(0.01923);  sigma_Bs_2.setVal(0.007333)
sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1)
fr_Bs.setVal(0.2651); fr_Bs.setConstant(1)

model_discr.fitTo(data_psi)
model_discr.fitTo(data_psi)
model_discr.fitTo(data_psi)

c.cd(2)
frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S) region', var_discr, left_discr, right_discr, nbins_discr);
data_psi.plotOn(frame_discr)
model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.87, 0.6))
model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 40 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 40 * sigma_Bs_1.getValV()));
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 40 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 40 * sigma_Bs_2.getValV()));

frame_discr.Draw()

################
##_-_-_-_-_-_-#
##############

sData_psi = ROOT.RooStats.SPlot(
    'sData_psi', 'sData_psi', data_psi, model_discr,
    ROOT.RooArgList(N_sig_discr, N_bkgr_discr)
)

print '\n\n\n\n\n\n\n\n\n\n\n\n'
print "Yield of signal is " , N_sig_discr.getVal() , ".  From sWeights it is " , sData_psi.GetYieldFromSWeight("N_sig_discr")
print '\n\n\n\n\n\n\n\n\n\n\n\n'


c.cd(3)
var_control.setMin(left_psi); var_control.setMax(right_psi)
data_psi_weighted = ROOT.RooDataSet(data_psi.GetName(),data_psi.GetTitle(),data_psi, data_psi.get(), cuts + '&& ' + cuts_psi, "N_sig_discr_sw") ;

sigma_psi_1.setVal(0.00668);  sigma_psi_2.setVal(0.003120)
sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1)
fr_psi.setVal(0.371); fr_psi.setConstant(1)

r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE)) #
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE)) # , RF.Range("psi")
r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE)) # , RF.Range("psi")


frame_control = ROOT.RooPlot(" ", "sPlot for #psi(2S) region", var_control, left_psi, right_psi, nbins_psi);
# frame_control = var_control.frame(RF.Title('sPlot for #psi(2S) region'), RF.Bins(nbins_psi))
data_psi_weighted.plotOn(frame_control, ROOT.RooLinkedList())
model_psi.paramOn(frame_control, RF.Layout(0.55, 0.87, 0.6))
model_psi.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_psi.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_psi.plotOn(frame_control, RF.Components("sig_psi_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_psi.getValV() - 40 * sigma_psi_1.getValV(), mean_psi.getValV() + 40 * sigma_psi_1.getValV()));
model_psi.plotOn(frame_control, RF.Components("sig_psi_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_psi.getValV() - 40 * sigma_psi_2.getValV(), mean_psi.getValV() + 40 * sigma_psi_2.getValV()));
# model_psi.plotOn(frame_control) # , RF.NormRange("psi"), RF.Range("psi")
frame_control.Draw()


####################################################
#_-_-_-_-_-_-          X DATA          _-_-_-_-_-_-#
####################################################

print '\n\n' + 30*'#' + '\n\n\n           X now\n\n\n' + 30*'#' + '\n\n'

file_MC_X = ROOT.TFile('SimpleFileMC_b715x_0_14000.root')
data_X = data.reduce(cuts_X)
# data_X = ROOT.RooDataSet('data', '', file_MC_X.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts + '&& ' + cuts_X)

sigma_Bs_1.setConstant(0); sigma_Bs_2.setConstant(0)
sigma_Bs_1.setVal(0.008227);  sigma_Bs_2.setVal(0.0332)
sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1)
fr_Bs.setConstant(0); fr_Bs.setVal(0.8057); fr_Bs.setConstant(1)

model_discr.fitTo(data_X)
model_discr.fitTo(data_X)
model_discr.fitTo(data_X)

c.cd(5)
frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) from X(3872) region', var_discr, left_discr, right_discr, nbins_discr);
data_X.plotOn(frame_discr)
model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.87, 0.6))
model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 40 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 40 * sigma_Bs_1.getValV()));
model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 40 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 40 * sigma_Bs_2.getValV()));

frame_discr.Draw()

################
##_-_-_-_-_-_-#
##############

ROOT.RooStats.SPlot(
    'sData_X', 'sData_X', data_X, model_discr,
    ROOT.RooArgList(N_sig_discr,N_bkgr_discr)
)

c.cd(4)
var_control.setMin(left_X); var_control.setMax(right_X)
data_X_weighted = ROOT.RooDataSet(data_X.GetName(),data_X.GetTitle(),data_X, data_X.get(), cuts + '&& ' + cuts_X, "N_sig_discr_sw") ;

sigma_X_1.setVal(0.005049);  sigma_X_2.setVal(0.01456)
sigma_X_1.setConstant(1); sigma_X_2.setConstant(1)
fr_X.setVal(0.775); fr_X.setConstant(1)

N_sig_X.setVal(0)
N_sig_X.setConstant(1)
# sigma_X.setConstant(1)

rrr_null = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
rrr_null = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
rrr_null = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))

frame_control = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) bkgr only', var_control, left_X, right_X, nbins_X);
data_X_weighted.plotOn(frame_control)
model_X.paramOn(frame_control, RF.Layout(0.55, 0.87, 0.6))
model_X.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_X.plotOn(frame_control, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
# model_X.plotOn(frame_control, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 40 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 40 * sigma_Bs_1.getValV()));

frame_control.Draw()

################
##_-_-_-_-_-_-#
##############

c.cd(6)

N_sig_X.setConstant(0)
N_sig_X.setVal(50)

rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))

# frame_control = ROOT.RooPlot('frame_control', 'sPlot for X(3872) region', var_control, left_X, right_X, nbins_X)
frame_control = ROOT.RooPlot(" ", "sPlot for X(3872) region", var_control, left_X, right_X, nbins_X);
data_X_weighted.plotOn(frame_control)
model_X.paramOn(frame_control, RF.Layout(0.55, 0.87, 0.6))
model_X.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
model_X.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
model_X.plotOn(frame_control, RF.Components("sig_X_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_X.getValV() - 40 * sigma_X_1.getValV(), mean_X.getValV() + 40 * sigma_X_1.getValV()));
model_X.plotOn(frame_control, RF.Components("sig_X_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_X.getValV() - 40 * sigma_X_2.getValV(), mean_X.getValV() + 40 * sigma_X_2.getValV()));

# model_X.plotOn(frame_control) # , RF.NormRange("X"), RF.Range("X")
frame_control.Draw()


###############################################################################################################################
nll_sig  = rrr_sig.minNll()
nll_null = rrr_null.minNll()
P = ROOT.TMath.Prob(nll_null - nll_sig, 2)## !!! Change delta of ndf appropriately
S = ROOT.TMath.ErfcInverse(P) * math.sqrt(2)
print 'P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S

c.SaveAs('sPlot.png')
