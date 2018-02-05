import ROOT
from ROOT import RooFit as RF, gStyle
import math
from RooSpace import *

# gStyle.SetTitleFontSize(.085)

left_discr_data =  5.3669 - 0.21; right_discr_data = 5.3669 + 0.21; nbins_discr_data = 42
left_discr_MC =  5.3669 - 0.06; right_discr_MC = 5.3669 + 0.06; nbins_discr_MC = 24

left_phi_data = 0.99; right_phi_data = 1.045; nbins_phi_data = 55
left_phi_MC = 1.0; right_phi_MC = 1.040; nbins_phi_MC = 40

left_psi = 3.686 - 0.03; right_psi = 3.686 + 0.03; nbins_psi = 60
left_X = 3.872 - 0.08; right_X = 3.872 + 0.08; nbins_X = 32

# var_discr.setRange('dicsr_range_MC', left_discr_MC, right_discr_MC)
# PHI_mass_Cjp.setRange('phi_range_MC', left_phi_MC, right_phi_MC)


file_data = ROOT.TFile('new.root')
file_MC_psi = ROOT.TFile('BsToPsiPhi_matched_all_1519f1b.root')
file_MC_X = ROOT.TFile('BsToXPhi_matched_all_1892449.root')
# file_MC_psi = ROOT.TFile('SimpleFileMC_b715psi_0_14000.root')
# file_MC_X = ROOT.TFile('SimpleFileMC_b715x_0_14000.root')


cuts_dR = '1 > 0'
# cuts_dR = 'dR_mu1 < 0.003 && dR_mu2 < 0.003 && dR_pi1 < 0.01 && dR_pi2 < 0.05 && dR_K1 < 0.05 && dR_K2 < 0.05'

cuts_Bs_data = 'BU_mass_Cjp > ' + str(left_discr_data) + ' && BU_mass_Cjp < ' + str(right_discr_data)   # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_Bs_MC = 'BU_mass_Cjp > ' + str(left_discr_MC) + ' && BU_mass_Cjp < ' + str(right_discr_MC)  # + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'

cuts_phi_data = 'PHI_mass_Cjp > ' + str(left_phi_data) + ' && PHI_mass_Cjp < ' + str(right_phi_data)
cuts_phi_MC = 'PHI_mass_Cjp > ' + str(left_phi_MC) + ' && PHI_mass_Cjp < ' + str(right_phi_MC)  # TMath::Abs(PHI_mass_Cjp - 1.02)<0.01 &&

cuts_psi = 'X_mass_Cjp >' + str(left_psi) + ' && X_mass_Cjp < ' + str(right_psi)  + ' && PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'
cuts_X = 'X_mass_Cjp >' + str(left_X) + ' && X_mass_Cjp < ' + str(right_X)  + ' && PIPI_mass_Cjp > 0.65 && PIPI_mass_Cjp < 0.78'

def plot_discr(data, model, title, left, right, nbins):
    frame_discr = ROOT.RooPlot(" ", title, var_discr, left, right, nbins);
    data.plotOn(frame_discr)
    model.paramOn(frame_discr, RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_discr_param)
    frame_discr.getAttText().SetTextSize(0.053)
    model.plotOn(frame_discr, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5)) #, RF.NormRange("full"), RF.Range('full')
    model.plotOn(frame_discr, RF.Components("model_bb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-2), RF.LineWidth(4) );
    model.plotOn(frame_discr, RF.Components("model_bs_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kAzure+3), RF.LineWidth(4));
    model.plotOn(frame_discr, RF.Components("model_sb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame_discr, RF.Components("model_ss_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kOrange+7), RF.LineWidth(4) );

    # model.plotOn(frame_discr, RF.Components("sig_Bs_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_1.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_1.getValV()));
    # model.plotOn(frame_discr, RF.Components("sig_Bs_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs_2.getValV(), mean_Bs.getValV() + 10 * sigma_Bs_2.getValV()));
    # model.plotOn(frame_discr, RF.Components("signal_Bs"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4), RF.Range(mean_Bs.getValV() - 10 * sigma_Bs.getValV(), mean_Bs.getValV() + 10 * sigma_Bs.getValV()));
    frame_discr.Draw()

def plot_control(data, model, title, left, right, nbins):
    frame_control = ROOT.RooPlot(" ", title, var_control, left, right, nbins);
    data.plotOn(frame_control)
    model.paramOn(frame_control, RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_X_param)
    frame_control.getAttText().SetTextSize(0.053)
    model.plotOn(frame_control, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
    model.plotOn(frame_control, RF.Components("bkgr_control"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    # model_X.plotOn(frame_control, RF.Components("sig_X_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model_X.plotOn(frame_control, RF.Components("sig_X_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model.plotOn(frame_control, RF.Components("signal_X"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    frame_control.Draw()

def plot_phi(data, model, title, left, right, nbins):
    frame_phi = ROOT.RooPlot(" ", title, PHI_mass_Cjp, left, right, nbins);
    data.plotOn(frame_phi)
    model.paramOn(frame_phi, RF.Layout(0.55, 0.96, 0.9)) #, RF.Parameters(plot_X_param)
    frame_phi.getAttText().SetTextSize(0.053)
    model.plotOn(frame_phi, RF.LineColor(ROOT.kRed-6), RF.LineWidth(5))
    model.plotOn(frame_phi, RF.Components("model_bb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kGreen-2), RF.LineWidth(4) );
    model.plotOn(frame_phi, RF.Components("model_bs_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kAzure+3), RF.LineWidth(4) );
    model.plotOn(frame_phi, RF.Components("model_sb_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    model.plotOn(frame_phi, RF.Components("model_ss_2D"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kOrange+7), RF.LineWidth(4) );

    # model.plotOn(frame_phi, RF.Components("bkgr_phi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(ROOT.kBlue-8), RF.LineWidth(4) );
    # model_X.plotOn(frame_phi, RF.Components("sig_X_1"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model_X.plotOn(frame_phi, RF.Components("sig_X_2"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    # model.plotOn(frame_phi, RF.Components("signal_phi"), RF.LineStyle(ROOT.kDashed), RF.LineColor(47), RF.LineWidth(4));
    frame_phi.Draw()


c = ROOT.TCanvas("c", "c", 1700, 650)
c.Divide(2,2)

####################################################
#_-_-_-_-_-_-      INCLUSIVE DATA      _-_-_-_-_-_-#
####################################################
#
# model_discr.fitTo(data)
# model_discr.fitTo(data)
#
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


##########################################################
#_-_-_-_-_-_-          PSI(2S) DATA          _-_-_-_-_-_-#
# ##########################################################

var_discr.setMin(left_discr_MC); var_discr.setMax(right_discr_MC)
PHI_mass_Cjp.setMin(left_phi_MC); PHI_mass_Cjp.setMax(right_phi_MC)
data_psi_MC = ROOT.RooDataSet('data_psi_MC', '', file_MC_psi.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)), cuts_dR + '&&' + cuts_Bs_MC + '&&' + cuts_phi_MC+ '&&' + cuts_psi)


c.cd(1)
print '\n\n' + 30*'#' + '\n\n\n         MC psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n'


model_1D_Bs.fitTo(data_psi_MC)
# model_1D_Bs.fitTo(data_psi_MC)
model_1D_phi.fitTo(data_psi_MC)
# model_1D_phi.fitTo(data_psi_MC)

plot_discr(data_psi_MC, model_1D_Bs, 'MC: m(J/#psi#pi^{+}#pi^{-}#phi)', left_discr_MC, right_discr_MC, nbins_discr_MC)

c.cd(2)
plot_phi(data_psi_MC, model_1D_phi, 'MC: m(K^{+}K^{-})', left_phi_MC, right_phi_MC, nbins_phi_MC)

###############
#_-_-_-_-_-_-#
#############

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data)

data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts_Bs_data + '&&' + cuts_phi_data)
data_psi = data.reduce(cuts_psi)

c.cd(3)
print '\n\n' + 30*'#' + '\n\n\n         Data psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n'

sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); fr_Bs.setConstant(1);
mean_Bs.setMin(mean_Bs.getVal() - 0.001); mean_Bs.setMax(mean_Bs.getVal() + 0.001)
# a1.setVal(0.2); a2.setVal(0.2); a3.setVal(0.2); a4.setVal(0.2)
# a1_phi.setVal(0.2); a2_phi.setVal(0.2); a3_phi.setVal(0.2); a4_phi.setVal(0.2)
# N_sig_2D.setVal(100.); N_sig_2D.setMax(200.)
N_bb_2D.setVal(30000.); N_sb_2D.setVal(500.); N_bs_2D.setVal(500.); N_ss_2D.setVal(3000.);
# N_bb_2D.setMin(5000.); N_sb_2D.setMin(10000.); N_bs_2D.setMin(0.); N_ss_2D.setMin(1000.);
# N_bb_2D.setMax(30000.); N_sb_2D.setMax(30000.); N_bs_2D.setMax(1000.); N_ss_2D.setMax(4000.);
# N_ss_2D.setConstant(1); N_bs_2D.setConstant(1); N_sb_2D.setConstant(1); N_bb_2D.setConstant(1);
# sigma_phi_1.setConstant(1); sigma_phi_2.setConstant(1); fr_phi.setConstant(1);
# mean_phi.setConstant(1); sigma_phi.setConstant(1); alpha_phi.setConstant(1); n_phi.setConstant(1);
sigma_phi.setConstant(1); alpha_phi.setConstant(1); n_phi.setConstant(1); sigma_gauss_phi.setConstant(1); mean_phi.setConstant(1)
# mean_phi.setMin(mean_phi.getVal() - 0.0005); mean_phi.setMax(mean_phi.getVal() + 0.0005)

model_2D_data.fitTo(data_psi)
model_2D_data.fitTo(data_psi)
# model_2D.fitTo(data_psi, RF.Extended())
# model_discr.fitTo(data_X)
plot_discr(data_psi, model_2D_data, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S) region', left_discr_data, right_discr_data, nbins_discr_data)

c.cd(4)
plot_phi(data_psi, model_2D_data, 'Data: m(K^{+}K^{-}) from #psi(2S) region', left_phi_data, right_phi_data, nbins_phi_data)

w = ROOT.RooWorkspace("w", True)
Import = getattr(ROOT.RooWorkspace, 'import')
Import(w, model_2D_data)
w.writeToFile('model_2D_data_SC.root')

##############
#_-_-_-_-_-_-#
############

c_sPlot = ROOT.TCanvas("c_sPlot", "c_sPlot", 1700, 650)
c_sPlot.Divide(2,1)

c_sPlot.cd(1)
print '\n\n' + 30*'#' + '\n\n\n         MC X: X mass now         \n\n\n' + 30*'#' + '\n\n'

var_control.setMin(left_psi); var_control.setMax(right_psi)
model_psi.fitTo(data_psi_MC)
plot_control(data_psi_MC, model_psi, 'MC: m(J/#psi#pi^{+}#pi^{-}) projection', left_psi, right_psi, nbins_psi)

###############
#_-_-_-_-_-_-#
#############

c_sPlot.cd(2)
print '\n\n' + 30*'#' + '\n\n\n         Data X: splot now         \n\n\n' + 30*'#' + '\n\n'


file_model_2D = ROOT.TFile('~/Study/Bs_resonances/model_2D_data_SC.root')
w = file_model_2D.Get('w')

model_2D_data = w.pdf('model_2D_data')
model_2D_data.fitTo(data_psi)

ROOT.RooStats.SPlot(
    'sData_psi', 'sData_psi', data_psi, model_2D_data,
    ROOT.RooArgList(N_ss_2D, N_bb_2D, N_sb_2D, N_bs_2D)
)

data_psi_weighted = ROOT.RooDataSet(data_psi.GetName(), data_psi.GetTitle(), data_psi, data_psi.get(), '1 > 0', "N_ss_2D_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
sigma_psi.setConstant(1);  gamma_BW_psi.setConstant(1)
rrr_sig = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
plot_control(data_psi_weighted, model_psi, 'Data: sPlot for #psi(2S) region', left_psi, right_psi, nbins_psi)



################   PREVIOUS BELOW  ####################
### --------------------------------------------------

#
#
# print '\n\n' + 30*'#' + '\n\n\n           psi(2S) now\n\n', cuts
# print cuts_psi
# print cuts_phi
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

# c.cd(1)
# print '\n\n' + 30*'#' + '\n\n\n         MC X: Bs mass now         \n\n\n' + 30*'#' + '\n\n'
#
# data_X = data.reduce(cuts_X)
# data_X_MC = ROOT.RooDataSet('data', '', file_MC_X.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)), cuts_dR + '&&' + cuts + '&&' + cuts_X)
#
# # mean_phi.setConstant(1)
# model_2D.fitTo(data_X_MC, RF.Extended())
# # model_2D.fitTo(data_X_MC)
# # model_discr.fitTo(data_X)
# plot_discr('MC: m(J/#psi#pi^{+}#pi^{-}#phi)', data_X_MC, model_2D)
#
# c.cd(2)
# plot_phi('MC: m(K^{+}K^{-})', data_X_MC, model_2D)
#
# ###############
# #_-_-_-_-_-_-#
# #############
#
# c.cd(3)
# print '\n\n' + 30*'#' + '\n\n\n         Data X: Bs mass now         \n\n\n' + 30*'#' + '\n\n'
#
# sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); fr_Bs.setConstant(1);
# mean_Bs.setMin(5.367 - 0.01); mean_Bs.setMax(5.367 + 0.01)
# a1.setVal(0.01); a2.setVal(0.01); a3.setVal(0.01); a4.setVal(0.01)
# a1_phi.setVal(0.01); a2_phi.setVal(0.01); a3_phi.setVal(0.01); a4_phi.setVal(0.01)
# N_sig_2D.setVal(100.); N_sig_2D.setMax(200.)
# N_bkgr_2D.setVal(300000.)
#
# sigma_phi_1.setConstant(1); sigma_phi_2.setConstant(1); fr_phi.setConstant(1);# mean_phi.setConstant(1); # sigma_phi.setConstant(1); gamma_BW_phi.setConstant(1)
# model_2D.fitTo(data_X, RF.Extended())
# model_2D.fitTo(data_X, RF.Extended())
# # model_discr.fitTo(data_X)
# plot_discr('Data: m(J/#psi#pi^{+}#pi^{-}#phi) from X(3872) region', data_X, model_2D)
#
# c.cd(4)
# plot_phi('Data: m(K^{+}K^{-}) from X(3872) region', data_X, model_2D)

##############
#_-_-_-_-_-_-#
############
#
# c.cd(3)
# print '\n\n' + 30*'#' + '\n\n\n         MC X: X mass now         \n\n\n' + 30*'#' + '\n\n'
#
# var_control.setMin(left_X); var_control.setMax(right_X)
# model_X.fitTo(data_X_MC)
# plot_control('MC: m(J/#psi#pi^{+}#pi^{-}) projection', data_X_MC)
#
# ###############
# #_-_-_-_-_-_-#
# #############
#
# c.cd(4)
# print '\n\n' + 30*'#' + '\n\n\n         Data X: splot now         \n\n\n' + 30*'#' + '\n\n'
#
# ROOT.RooStats.SPlot(
#     'sData_X', 'sData_X', data_X, model_discr,
#     ROOT.RooArgList(N_sig_discr,N_bkgr_discr)
# )
#
# data_X_weighted = ROOT.RooDataSet(data_X.GetName(), data_X.GetTitle(), data_X, data_X.get(), cuts_dR + '&&' + cuts + '&&' + cuts_X, "N_sig_discr_sw") ;
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)
# rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# # rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# # rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kFALSE))
# plot_control('Data: sPlot for X(3872) region', data_X_weighted)

###############
#_-_-_-_-_-_-#
#############

##############################################################################################################################
# nll_sig  = rrr_sig.minNll()
# nll_null = rrr_null.minNll()
# P = ROOT.TMath.Prob(nll_null - nll_sig, 1) ## !!! Change delta of ndf appropriately
# S = ROOT.TMath.ErfcInverse(P) * math.sqrt(2)
# print 'P=', P, ' nll_sig=', nll_sig, ' nll_null=', nll_null, '\n', 'S=', S

# c.SaveAs('sPlot.png')
