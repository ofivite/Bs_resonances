import ROOT
from ROOT import RooFit as RF, gStyle
import math
from RooSpace import *

# gStyle.SetTitleFontSize(.085)

left_discr =  5.3669 - 0.21; right_discr = 5.3669 + 0.21; nbins_discr = 42
left_psi = 3.686 - 0.03; right_psi = 3.686 + 0.03; nbins_psi = 60
left_X = 3.872 - 0.08; right_X = 3.872 + 0.08; nbins_X = 32

file_data = ROOT.TFile('new.root')
file_MC_psi = ROOT.TFile('SimpleFileMC_b715psi_0_14000.root')
# file_MC_X = ROOT.TFile('SimpleFileMC_b715x_0_14000.root')
file_MC_X = ROOT.TFile('BsToXPhi_matched_1892449.root')

cuts = 'TMath::Abs(PHI_mass_Cjp - 1.02)<0.01 && BU_mass_Cjp > ' + str(left_discr) + '&& BU_mass_Cjp < ' + str(right_discr) # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_dR = '1 > 0'
# cuts_dR = 'dR_mu1 < 0.003 && dR_mu2 < 0.003 && dR_pi1 < 0.01 && dR_pi2 < 0.05 && dR_K1 < 0.05 && dR_K2 < 0.05'
cuts_psi = 'X_mass_Cjp >' + str(left_psi) + ' && X_mass_Cjp < ' + str(right_psi)  + ' && PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'
cuts_X = 'X_mass_Cjp >' + str(left_X) + ' && X_mass_Cjp < ' + str(right_X)  + ' && PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78'

def plot_discr(title, data):
    frame_discr = ROOT.RooPlot(" ", title, var_discr, left_discr, right_discr, nbins_discr);
    data.plotOn(frame_discr)
    model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_discr_param)
    frame_discr.getAttText().SetTextSize(0.053)
    model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
    model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_1.getValV()));
    model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_2.getValV()));
    # model_discr.plotOn(frame_discr, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs.getValV(), mean_Bs.getValV() + 10 * sigma_Bs.getValV()));
    frame_discr.Draw()

def plot_control(title, data):
    frame_control = ROOT.RooPlot(" ", title, var_control, left_X, right_X, nbins_X);
    data.plotOn(frame_control)
    model_X.paramOn(frame_control,RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_X_param)
    frame_control.getAttText().SetTextSize(0.053)
    model_X.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
    model_X.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    # model_X.plotOn(frame_control, RF.Components("sig_X_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model_X.plotOn(frame_control, RF.Components("sig_X_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    model_X.plotOn(frame_control, RF.Components("signal_X"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    frame_control.Draw()


c = ROOT.TCanvas("c", "c", 1700, 650)
c.Divide(2,2)

####################################################
#_-_-_-_-_-_-      INCLUSIVE DATA      _-_-_-_-_-_-#
####################################################

var_discr.setMin(left_discr); var_discr.setMax(right_discr)
data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts)
# model_discr.fitTo(data)
# model_discr.fitTo(data)

# # c.cd(1)
# frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) inclusive', var_discr, left_discr, right_discr, nbins_discr);
# data.plotOn(frame_discr)
# model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.96, 0.9), RF.Parameters(plot_discr_param))
# # frame_discr.getAttText().SetTextSize(0.053)
# model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
# model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
# # model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 3 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 3 * sigma_Bs_1.getValV()));
# # model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 3 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 3 * sigma_Bs_2.getValV()));
# model_discr.plotOn(frame_discr, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs.getValV(), mean_Bs.getValV() + 10 * sigma_Bs.getValV()));
#
# frame_discr.Draw()

#
# ##########################################################
# #_-_-_-_-_-_-          PSI(2S) DATA          _-_-_-_-_-_-#
# ##########################################################
#
# print '\n\n' + 30*'#' + '\n\n\n           psi(2S) now\n\n', cuts
# print cuts_psi
# print cuts_X, '\n\n\n' + 30*'#' + '\n\n'
#
# data_psi = data.reduce(cuts_psi)
# # data_psi = ROOT.RooDataSet('data', '', file_MC_psi.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts_dR + '&&' + cuts + '&&' + cuts_psi)
#
# # # phi 10 Diag
# # sigma_Bs.setVal(0.006234); gamma_BW_Bs.setVal(0.007085)
# # sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1)
#
# # phi 10 MW
# sigma_Bs.setVal(0.006120); gamma_BW_Bs.setVal(0.007315)
# sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1)
#
# # # phi 5 Diag
# # sigma_Bs.setVal(0.006237); gamma_BW_Bs.setVal(0.006857); # N_B0_refl.setVal(10.);
# # sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1); # N_B0_refl.setConstant(1);
#
# # # phi 5 MW
# # sigma_Bs.setVal(0.006232); gamma_BW_Bs.setVal(0.006851)
# # sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1)
#
#
#
# model_discr.fitTo(data_psi)
# # model_discr.fitTo(data_psi)
# # model_discr.fitTo(data_psi)
#
# c.cd(1)
# frame_discr = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S) region', var_discr, left_discr, right_discr, nbins_discr);
# data_psi.plotOn(frame_discr)
# model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.96, 0.9), RF.Parameters(plot_discr_param))
# frame_discr.getAttText().SetTextSize(0.053)
# model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5), RF.Name('model'))
# model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4), RF.Name('bkgr_Bs') );
# # model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 3 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 3 * sigma_Bs_1.getValV()));
# # model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 3 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 3 * sigma_Bs_2.getValV()));
# model_discr.plotOn(frame_discr, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs.getValV(), mean_Bs.getValV() + 10 * sigma_Bs.getValV()), RF.Name('signal_Bs'));
# model_discr.plotOn(frame_discr, RF.Components("B0_refl"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-5), RF.LineWidth(4), RF.Normalization(10.0), RF.Name('B0_refl'));
#
# frame_discr.Draw()
#
# leg = ROOT.TLegend(0.15,0.7,0.43,0.85)
# leg.SetHeader("")
# leg.AddEntry(frame_discr.findObject('model'),"Total Fit","l")
# leg.AddEntry(frame_discr.findObject('signal_Bs'),"B_{s} signal","l")
# leg.AddEntry(frame_discr.findObject('bkgr_Bs'),"Background","l")
# leg.AddEntry(frame_discr.findObject('B0_refl'),"10x B^{0} reflection","l")
#
# # leg.AddEntry("f1","Function abs(#frac{sin(x)}{x})","l")
# # leg.AddEntry("gr","Graph with error bars","lep")
# leg.Draw()
#
# ##############
# # _-_-_-_-_-_-#
# ############
# #
# # sData_psi = ROOT.RooStats.SPlot(
# #     'sData_psi', 'sData_psi', data_psi, model_discr,
# #     ROOT.RooArgList(N_sig_discr, N_bkgr_discr)
# # )
# # print '\n\n' + 30*'#' + '\n\n\n           psi sPlot now\n\n\n' + 30*'#' + '\n\n'
# #
# #
# # c.cd(2)
# # var_control.setMin(left_psi); var_control.setMax(right_psi)
# # data_psi_weighted = ROOT.RooDataSet(data_psi.GetName(),data_psi.GetTitle(),data_psi, data_psi.get(), cuts_dR + '&&' + cuts + '&&' + cuts_psi, "N_sig_discr_sw") ;
# #
# # # # phi 10 Diag
# # # sigma_psi.setVal(0.002804); gamma_BW_psi.setVal(0.003435)
# # # sigma_psi.setConstant(1);  gamma_BW_psi.setConstant(1)
# #
# # # # phi 10 MW
# # # sigma_psi.setVal(0.002639); gamma_BW_psi.setVal(0.003858)
# # # sigma_psi.setConstant(1);  gamma_BW_psi.setConstant(1)
# #
# # # phi 5 Diag
# # sigma_psi.setVal(0.00268746); gamma_BW_psi.setVal(0.003658)
# # sigma_psi.setConstant(1);  gamma_BW_psi.setConstant(1)
# #
# # # # phi 5 MW
# # # sigma_psi.setVal(0.00268746); gamma_BW_psi.setVal(0.00372264)
# # # sigma_psi.setConstant(1);  gamma_BW_psi.setConstant(1)
# #
# # r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE)) #
# # # r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE)) # , RF.Range("psi")
# # # r_psi = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE)) # , RF.Range("psi")
# #
# #
# # frame_control = ROOT.RooPlot(" ", "sPlot for #psi(2S) region", var_control, left_psi, right_psi, nbins_psi);
# # # frame_control = var_control.frame(RF.Title('sPlot for #psi(2S) region'), RF.Bins(nbins_psi))
# # data_psi_weighted.plotOn(frame_control, ROOT.RooLinkedList())
# # model_psi.paramOn(frame_control, RF.Layout(0.55, 0.96, 0.9), RF.Parameters(plot_psi_param))
# # frame_control.getAttText().SetTextSize(0.053)
# # model_psi.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
# # model_psi.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
# # # model_psi.plotOn(frame_control, RF.Components("sig_psi_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_psi.getValV() - 5 * sigma_psi_1.getValV(), mean_psi.getValV() + 5 * sigma_psi_1.getValV()));
# # # model_psi.plotOn(frame_control, RF.Components("sig_psi_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_psi.getValV() - 5 * sigma_psi_2.getValV(), mean_psi.getValV() + 5 * sigma_psi_2.getValV()));
# # model_psi.plotOn(frame_control, RF.Components("signal_psi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
# #
# # frame_control.Draw()
#
# c.cd(2)
# frame_discr = ROOT.RooPlot(" ", 'B^{0}#rightarrow#psi(2S)K* KDE shape', var_discr, left_discr, right_discr, nbins_discr);
# B0_refl.plotOn(frame_discr, RF.LineStyle(ROOT.kSolid), RF.LineColor(ROOT.kGreen-5), RF.LineWidth(4))
# frame_discr.Draw()



####################################################
#_-_-_-_-_-_-          X DATA          _-_-_-_-_-_-#
####################################################

c.cd(1)
print '\n\n' + 30*'#' + '\n\n\n         MC X: Bs mass now\n\n\n' + 30*'#' + '\n\n'
data_X = data.reduce(cuts_X)
# data_X = ROOT.RooDataSet('data', '', file_MC_X.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts + '&& ' + cuts_X)
data_X_MC = ROOT.RooDataSet('data', '', file_MC_X.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)), cuts_dR + '&&' + cuts + '&&' + cuts_X)

# # phi 10 DC
# sigma_Bs.setVal(0.00521); gamma_BW_Bs.setVal(0.00996)
# sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1)

# # phi 10 SC
# sigma_Bs.setVal(0.00566); gamma_BW_Bs.setVal(0.00867)
# sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1)

# # phi 5 DC
# sigma_Bs.setVal(0.0052); gamma_BW_Bs.setVal(0.00971)
# sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1)

# # phi 5 SC
# sigma_Bs.setVal(0.0057); gamma_BW_Bs.setVal(0.00829)
# sigma_Bs.setConstant(1);  gamma_BW_Bs.setConstant(1)

#### MC MATCHED ####
###
##
# # phi 5 SC
# sigma_Bs_1.setVal(0.01848); sigma_Bs_2.setVal(0.00739); fr_Bs.setVal(0.235);
# sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); fr_Bs.setConstant(1);

# # phi 10 SC
# sigma_Bs_1.setVal(0.01876); sigma_Bs_2.setVal(0.007472); fr_Bs.setVal(0.237);
# sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); fr_Bs.setConstant(1);

model_discr.fitTo(data_X_MC)
# model_discr.fitTo(data_X)
# model_discr.fitTo(data_X)
plot_discr('MC: m(J/#psi#pi^{+}#pi^{-}#phi) from X(3872) region', data_X_MC)

c.cd(2)
print '\n\n' + 30*'#' + '\n\n\n           Data X: Bs mass now\n\n\n' + 30*'#' + '\n\n'

# frame_discr = ROOT.RooPlot(" ", 'MC: m(J/#psi#pi^{+}#pi^{-}#phi) from X(3872) region', var_discr, left_discr, right_discr, nbins_discr);
# data_X.plotOn(frame_discr)
# model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_discr_param)
# frame_discr.getAttText().SetTextSize(0.053)
# model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
# model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
# model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_1.getValV()));
# model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_2.getValV()));
# # model_discr.plotOn(frame_discr, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs.getValV(), mean_Bs.getValV() + 10 * sigma_Bs.getValV()));
#
# frame_discr.Draw()

# phi 10 SC
# sigma_Bs_1.setVal(0.01876); sigma_Bs_2.setVal(0.007472); fr_Bs.setVal(0.237);
sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); fr_Bs.setConstant(1);
model_discr.fitTo(data_X)
model_discr.fitTo(data_X)
model_discr.fitTo(data_X)
plot_discr('Data: m(J/#psi#pi^{+}#pi^{-}#phi) from X(3872) region', data_X)
# frame_discr = ROOT.RooPlot(" ", 'MC: m(J/#psi#pi^{+}#pi^{-}#phi) from X(3872) region', var_discr, left_discr, right_discr, nbins_discr);
# data_X.plotOn(frame_discr)
# model_discr.paramOn(frame_discr, RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_discr_param)
# frame_discr.getAttText().SetTextSize(0.053)
# model_discr.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
# model_discr.plotOn(frame_discr, RF.Components("bkgr_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
# model_discr.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_1.getValV()));
# model_discr.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_2.getValV()));
# # model_discr.plotOn(frame_discr, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs.getValV(), mean_Bs.getValV() + 10 * sigma_Bs.getValV()));
#
# frame_discr.Draw()
###############
#_-_-_-_-_-_-#
#############

c.cd(3)
print '\n\n' + 30*'#' + '\n\n\n          MC X: X mass now\n\n\n' + 30*'#' + '\n\n'

ROOT.RooStats.SPlot(
    'sData_X', 'sData_X', data_X, model_discr,
    ROOT.RooArgList(N_sig_discr,N_bkgr_discr)
)

# c.cd(5)
#
var_control.setMin(left_X); var_control.setMax(right_X)
data_X_weighted = ROOT.RooDataSet(data_X.GetName(), data_X.GetTitle(), data_X, data_X.get(), cuts_dR + '&&' + cuts + '&&' + cuts_X, "N_sig_discr_sw") ;

# # phi 10 SC
# sigma_X.setVal(0.004265); gamma_BW_X.setVal(0.004021)
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)

# # phi 10 DC
# sigma_X.setVal(0.004039); gamma_BW_X.setVal(0.0048)
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)

# # phi 5 DC
# sigma_X.setVal(0.0039819); gamma_BW_X.setVal(0.0049330)
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)

# # phi 5 SC
# sigma_X.setVal(0.0043164); gamma_BW_X.setVal(0.0038798)
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)

#### MC MATCHED ####
###
##
# # phi 5 SC
# sigma_X.setVal(0.0048223); gamma_BW_X.setVal(0.002608)
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)

# # phi 10 SC
# sigma_X.setVal(0.0048267); gamma_BW_X.setVal(0.0026608)
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)


# N_sig_X.setVal(0)
# N_sig_X.setConstant(1)
#
# rrr_null = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# rrr_null = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# rrr_null = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))

# frame_control = ROOT.RooPlot(" ", 'm(J/#psi#pi^{+}#pi^{-}#phi) bkgr only', var_control, left_X, right_X, nbins_X);
# data_X_weighted.plotOn(frame_control)
# model_X.paramOn(frame_control, RF.Layout(0.6, 0.87, 0.6))
# model_X.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
#
# frame_control.Draw()

################
##_-_-_-_-_-_-#
##############
# N_sig_X.setVal(50)
# N_bkgr_control.setVal(5)
# N_sig_X.setConstant(0)

model_X.fitTo(data_X_MC)
plot_control('MC: m(J/#psi#pi^{+}#pi^{-}) projection for X(3872) region', data_X_MC)

c.cd(4)
print '\n\n' + 30*'#' + '\n\n\n           Data X: splot now\n\n\n' + 30*'#' + '\n\n'
sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)
rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
plot_control('Data: sPlot for X(3872) region', data_X_weighted)


#
# # frame_control = ROOT.RooPlot('frame_control', 'sPlot for X(3872) region', var_control, left_X, right_X, nbins_X)
# frame_control = ROOT.RooPlot(" ", "sPlot for X(3872) region", var_control, left_X, right_X, nbins_X);
# data_X_weighted.plotOn(frame_control)
# model_X.paramOn(frame_control,RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_X_param)
# frame_control.getAttText().SetTextSize(0.053)
# model_X.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
# model_X.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
# # model_X.plotOn(frame_control, RF.Components("sig_X_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
# # model_X.plotOn(frame_control, RF.Components("sig_X_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
# model_X.plotOn(frame_control, RF.Components("signal_X"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
#
# frame_control.Draw()

#
# ##############################################################################################################################
# nll_sig  = rrr_sig.minNll()
# nll_null = rrr_null.minNll()
# P = ROOT.TMath.Prob(nll_null - nll_sig, 1) ## !!! Change delta of ndf appropriately
# S = ROOT.TMath.ErfcInverse(P) * math.sqrt(2)
# print 'P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S

c.SaveAs('sPlot.png')
