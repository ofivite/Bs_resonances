from RooSpace import *
from cuts import *
from math import sqrt

files_MC = {'X': 'BsToXPhi_step3_6c21fba.root', 'psi':'BsToPsiPhi_step3_4a91161.root'}
# files_MC = {'X': 'BsToXPhi_matched_all_1892449.root', 'psi':'BsToPsiPhi_matched_all_1519f1b.root'}
# files_MC = {'X': 'SimpleFileMC_b715x_0_14000.root', 'psi':'SimpleFileMC_b715psi_0_14000.root'}
file_MC = ROOT.TFile(files_MC[mode])

# file_data = ROOT.TFile('new.root')
# file_data = ROOT.TFile('new_noKaon_9988200.root')
file_data = ROOT.TFile('new_noKaon_fabs_76e92fd.root')



# c = ROOT.TCanvas("c", "c", 1700, 650)
# c.Divide(3,1)

var_discr.setMin(left_discr_MC); var_discr.setMax(right_discr_MC)
PHI_mass_Cjp.setMin(left_phi_MC); PHI_mass_Cjp.setMax(right_phi_MC)
var_control.setMin(left_control_MC); var_control.setMax(right_control_MC)

data_MC = (ROOT.RooDataSet('data_MC', '', file_MC.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(MoID_mu1, MoID_mu2, MoID_pi1, MoID_pi2, MoID_K1, MoID_K2)), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)),
                   cuts_Bs_MC + '&&' + cuts_phi_MC + '&&' + cuts_control_MC + ' && ' + cuts_pipi[mode] + '&&' + cuts_match_ID[mode] + '&&' + cuts_match_dR))

##        ---------------       ##
##           FIT OF MC          ##
##        ---------------       ##

CMS_tdrStyle_lumi.extraText       = "Simulation Preliminary"
CMS_tdrStyle_lumi.setTDRStyle()
print '\n\n' + 30*'#' + '\n\n\n         MC psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n'

# n_phi.setVal(0.8); n_phi.setConstant(1)
N_bkgr_Bs.setVal(100); # N_bkgr_Bs.setMax(200);
# N_bkgr_phi.setVal(100); #N_bkgr_phi.setMax(1000);
# N_bkgr_control.setVal(100); #N_bkgr_control.setMax(1000);
model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
mean_Bs.setVal(5.366);
mean_Bs.setMin(mean_Bs.getVal() - 0.005); mean_Bs.setMax(mean_Bs.getVal() + 0.005)
sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); fr_Bs.setConstant(1);
model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# mean_Bs.setConstant(1)
# model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))

mean_phi.setVal(1.0195); #mean_phi.setConstant(1)
# N_bkgr_phi.setVal(0); # N_bkgr_phi.setConstant(1)
# gamma_BW_phi.setVal(0.0042); gamma_BW_phi.setConstant(1)
model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1); fr_phi.setConstant(1)
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# mean_phi.setConstant(1)
# model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# mean_phi.setConstant(0)
# model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))

model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1), fr_psi.setConstant(1)
sigma_X_1.setConstant(1); sigma_X_2.setConstant(1), fr_X.setConstant(1)
model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))


#
c_MC_1 = ROOT.TCanvas("c_MC_1", "c_MC_1", 800, 600)
plot_on_frame(var_discr, data_MC, model_1D_Bs, 'MC: m(J/#psi#pi^{+}#pi^{#font[122]{\55}}#phi)', left_discr_MC, right_discr_MC, nbins_discr_MC, plot_discr_param, True)
CMS_tdrStyle_lumi.CMS_lumi( c_MC_1, 0, 0 );
c_MC_1.Update(); c_MC_1.RedrawAxis(); c_MC_1.GetFrame().Draw();
c_MC_1.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_MC_Bs.pdf')

#
c_MC_2 = ROOT.TCanvas("c_MC_2", "c_MC_2", 800, 600)
plot_on_frame(PHI_mass_Cjp, data_MC, model_1D_phi, 'MC: m(K^{+}K^{#font[122]{\55}})', left_phi_MC, right_phi_MC, nbins_phi_MC, plot_phi_param, True)
CMS_tdrStyle_lumi.CMS_lumi( c_MC_2, 0, 0 );
c_MC_2.Update(); c_MC_2.RedrawAxis(); c_MC_2.GetFrame().Draw();
c_MC_2.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_MC_phi.pdf')

c_MC_3 = ROOT.TCanvas("c_MC_3", "c_MC_3", 800, 600)
plot_on_frame(var_control, data_MC, model_control, 'MC: m(J/#psi#pi^{+}#pi^{#font[122]{\55}})', left_control_MC, right_control_MC, nbins_control_MC, plot_control_param[mode], True)
CMS_tdrStyle_lumi.CMS_lumi( c_MC_3, 0, 0 );
c_MC_3.Update(); c_MC_3.RedrawAxis(); c_MC_3.GetFrame().Draw();
c_MC_3.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_MC_' + str(mode) + '.pdf')

mean_Bs.setMin(mean_Bs.getVal() - 0.005); mean_Bs.setMax(mean_Bs.getVal() + 0.005)
sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); fr_Bs.setConstant(1);
# a1.setVal(0.2); a2.setVal(0.2); a3.setVal(0.2); a4.setVal(0.2)
# a1_phi.setVal(0.2); a2_phi.setVal(0.2); a3_phi.setVal(0.2); a4_phi.setVal(0.2)
# N_sig_2D.setVal(100.); N_sig_2D.setMax(200.)
# N_bb_2D.setVal(30000.); N_sb_2D.setVal(400.); N_bs_2D.setVal(450.); N_ss_2D.setVal(2700.);
# N_bb_2D.setMin(5000.); N_sb_2D.setMin(10000.); N_bs_2D.setMin(0.); N_ss_2D.setMin(1000.);
# N_bb_2D.setMax(30000.); N_sb_2D.setMax(30000.); N_bs_2D.setMax(1000.); N_ss_2D.setMax(4000.);
# N_ss_2D.setConstant(1); N_bs_2D.setConstant(1); N_sb_2D.setConstant(1); N_bb_2D.setConstant(1);
# sigma_phi_1.setConstant(1); sigma_phi_2.setConstant(1); fr_phi.setConstant(1);
# mean_phi.setConstant(1); sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1);
# mean_phi.setMin(mean_phi.getVal() - 0.0005); mean_phi.setMax(mean_phi.getVal() + 0.0005)
sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1); fr_phi.setConstant(1)
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);

# mean_phi.setConstant(1);
sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1), fr_psi.setConstant(1)
sigma_X_1.setConstant(1); sigma_X_2.setConstant(1), fr_X.setConstant(1)
# gamma_BW_X.setConstant(1); sigma_X.setConstant(1)


##   -----------------------------    ##
##      DATA: sPlot & Sidebands       ##
##   -----------------------------    ##

CMS_tdrStyle_lumi.extraText       = "Preliminary"


# fr = {'X': fr_X.getVal(), 'psi':fr_psi.getVal()}
# sigma_1 = {'X': sigma_X_1.getVal(), 'psi':sigma_psi_1.getVal()}
# sigma_2 = {'X': sigma_X_2.getVal(), 'psi':sigma_psi_2.getVal()}
# sigma_eff = sqrt( fr[mode] * sigma_1[mode]**2 + (1 - fr[mode]) * sigma_2[mode]**2)
# window = 3 * sigma_eff
# wind_sideband_dist = 2 * sigma_eff
#
# var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data)
# PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data)
# var_control.setMin(left_control_data); var_control.setMax(right_control_data)
# data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode])
#
#
# c_inclus = ROOT.TCanvas("c_inclus", "c_inclus", 800, 600)
# #
# # bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2, a3, a4))
# model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_control), ROOT.RooArgList(N_sig_X, N_bkgr_control))
# model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(signal_psi, bkgr_control), ROOT.RooArgList(N_sig_psi, N_bkgr_control))
# control_models = {'X': model_X, 'psi': model_psi}
# model_control = control_models[mode]
#
# mean_X.setConstant(1); mean_psi.setConstant(1)
# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# mean_X.setConstant(0); mean_psi.setConstant(0)
# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
#
# # model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# # model_control.fitTo(data, RF.Extended(ROOT.kTRUE))
# plot_on_frame(var_control, data, model_control, 'Data: m(J/#psi#pi^{+}#pi^{-}) projection', left_control_data, right_control_data, nbins_control_data, plot_control_param[mode], False)
# CMS_tdrStyle_lumi.CMS_lumi( c_inclus, 2, 0 );
# c_inclus.Update(); c_inclus.RedrawAxis(); c_inclus.GetFrame().Draw();
# c_inclus.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_inclus.pdf')
#
#
# #
# # c_sPlot = ROOT.TCanvas("c_sPlot", "c_sPlot", 1700, 850)
# # c_sPlot.Divide(2,2)
# print '\n\n' + 30*'#' + '\n\n\n         Data psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n'
#
# means = {'X': mean_X.getVal(), 'psi':mean_psi.getVal()}
# data_sig = data.reduce('TMath::Abs(X_mass_Cjp -' + str(means[mode]) + ')<' + str(window))
# data_sideband = data.reduce('TMath::Abs(X_mass_Cjp - ' + str(means[mode]) + ')>' + str(window + wind_sideband_dist) + ' && TMath::Abs(X_mass_Cjp - ' + str(means[mode]) + ')<' + str(1.5*window + wind_sideband_dist))
#
# N_bkgr_Bs.setVal(10000); N_bkgr_Bs.setMax(50000);
# N_bkgr_phi.setVal(10000); N_bkgr_phi.setMax(50000);
# N_bkgr_control.setVal(1000); N_bkgr_control.setMax(50000);
#
# # c_wo_refl = ROOT.TCanvas("c_wo_refl", "c_wo_refl", 1700, 850)
# #
# # model_1D_Bs.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# # model_1D_Bs.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# # model_1D_Bs.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# # plot_on_frame(var_discr, data_sig, model_1D_Bs, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)
# #
# # c_sPlot.cd(1)
# # model_discr.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# # model_discr.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# # model_discr.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# # plot_on_frame(var_discr, data_sig, model_discr, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)
# #
# # ##########
# # sData_Bs_psi_sig = ROOT.RooStats.SPlot(
# #     'sData_Bs_psi_sig', 'sData_Bs_psi_sig', data_sig, model_discr,
# #     ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs, N_B0_refl)
# # )
# # data_sig_weighted = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', "N_sig_Bs_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# # ##########
#
#
# c_sPlot_1 = ROOT.TCanvas("c_sPlot_1", "c_sPlot_1", 800, 600)
# model_1D_Bs.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# # model_1D_Bs.fitTo(data_sig, RF.Extended(ROOT.kTRUE))
# plot_on_frame(var_discr, data_sig, model_1D_Bs, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)
# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_1, 2, 0 );
# c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); c_sPlot_1.GetFrame().Draw();
# c_sPlot_1.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_sPlot_1.pdf')
#
# ##########
# sData_Bs_psi_sig = ROOT.RooStats.SPlot(
#     'sData_Bs_psi_sig', 'sData_Bs_psi_sig', data_sig, model_1D_Bs,
#     ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs)
# )
# data_sig_weighted = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', "N_sig_Bs_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# ##########
#
# #
# c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600)
# model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# # model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# # model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# mean_phi.setConstant(0)
# model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# # model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# # model_1D_phi.fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# plot_on_frame(PHI_mass_Cjp, data_sig_weighted, model_1D_phi, 'Data: sPlot to m(K^{+}K^{-})', left_phi_data, right_phi_data, nbins_phi_data, plot_phi_param, False)
# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_2, 2, 0 );
# c_sPlot_2.Update(); c_sPlot_2.RedrawAxis(); c_sPlot_2.GetFrame().Draw();
# c_sPlot_2.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_sPlot_2.pdf')
#
# #
# c_sPlot_3 = ROOT.TCanvas("c_sPlot_3", "c_sPlot_3", 800, 600)
# mean_Bs.setConstant(1); mean_phi.setConstant(1)
# model_1D_Bs.fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
# model_1D_Bs.fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
# # model_1D_Bs.fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
# plot_on_frame(var_discr, data_sideband, model_1D_Bs, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)
# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_3, 2, 0 );
# c_sPlot_3.Update(); c_sPlot_3.RedrawAxis(); c_sPlot_3.GetFrame().Draw();
# c_sPlot_3.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_sPlot_3.pdf')
#
# ##########
# sData_Bs_psi_side = ROOT.RooStats.SPlot(
#     'sData_Bs_psi_side', 'sData_Bs_psi_side', data_sideband, model_1D_Bs,
#     ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs)
# )
# data_side_weighted = ROOT.RooDataSet(data_sideband.GetName(), data_sideband.GetTitle(), data_sideband, data_sideband.get(), '1 > 0', "N_sig_Bs_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# ##########
#
# #
# c_sPlot_4 = ROOT.TCanvas("c_sPlot_4", "c_sPlot_4", 800, 600)
# model_1D_phi.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# model_1D_phi.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# model_1D_phi.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# # model_1D_phi.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
# plot_on_frame(PHI_mass_Cjp, data_side_weighted, model_1D_phi, 'Data: sPlot to m(K^{+}K^{-})', left_phi_data, right_phi_data, nbins_phi_data, plot_phi_param, False)
# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_4, 2, 0 );
# c_sPlot_4.Update(); c_sPlot_4.RedrawAxis(); c_sPlot_4.GetFrame().Draw();
# c_sPlot_4.SaveAs('~/Study/Bs_resonances/Bs_' + str(mode) + 'phi_plots/c_sPlot_4.pdf')





# c_X = ROOT.TCanvas("c_X", "c_X", 1700, 650)
# c_X.Divide(3,1)
# c_X.cd(1)
#
# sigma_Bs_eff = sqrt ( fr_Bs.getVal() * (sigma_Bs_1.getVal())**2 + (1 - fr_Bs.getVal()) * (sigma_Bs_2.getVal())**2 )
# data_niceX = data.reduce('TMath::Abs(PHI_mass_Cjp -' + str(mean_phi.getVal()) + ') < 0.01')
#
# mean_X.setConstant(1)
# model_control.fitTo(data_niceX, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_niceX, RF.Extended(ROOT.kTRUE))
# mean_X.setConstant(0)
# model_control.fitTo(data_niceX, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_niceX, RF.Extended(ROOT.kTRUE))
# plot_on_frame(var_control, data_niceX, model_control, 'Data: m(J/#psi#pi^{+}#pi^{-}) projection', left_control_data, right_control_data, nbins_control_data, plot_control_param[mode])
#
# c_X.cd(2)
#
# old_mean_X = mean_X.getVal()
# data_veryniceX = data.reduce('TMath::Abs(BU_mass_Cjp -' + str(mean_Bs.getVal()) + ')<' + str(3 * sigma_Bs_eff) + '&& TMath::Abs(PHI_mass_Cjp -' + str(mean_phi.getVal()) + ') < 0.01')
#
# mean_X.setConstant(1)
# model_control.fitTo(data_veryniceX, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_veryniceX, RF.Extended(ROOT.kTRUE))
# mean_X.setConstant(0)
# model_control.fitTo(data_veryniceX, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_veryniceX, RF.Extended(ROOT.kTRUE))
# plot_on_frame(var_control, data_veryniceX, model_control, 'Data: m(J/#psi#pi^{+}#pi^{-}) projection', left_control_data, right_control_data, nbins_control_data, plot_control_param[mode])
#
# print '\n\n' + 30*'#' + '\n\n\n         Significance now         \n\n\n' + 30*'#' + '\n\n'
#
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_control)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf("model_X"))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var("N_sig_X")))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var("X_mass_Cjp")))
# mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1"), w.var("a2"), w.var("N_bkgr_control"), w.var("mean_X")))
# mc.SetSnapshot(ROOT.RooArgSet(w.var("N_sig_X")))
# Import(w, mc)
#
# sbModel = w.obj("ModelConfig")
# sbModel.SetName("S+B_model")
# poi = sbModel.GetParametersOfInterest().first()
# bModel = sbModel.Clone()
# bModel.SetName("B_only_model")
# oldval = poi.getVal()
# poi.setVal(0)
# bModel.SetSnapshot(ROOT.RooArgSet(poi))
# poi.setVal(oldval)
# ac = ROOT.RooStats.AsymptoticCalculator(data_veryniceX, sbModel, bModel)
# ac.SetOneSidedDiscovery(True)
# asResult = ac.GetHypoTest()
# asResult.Print()
#

# c_X.cd(3)
#
# data_not_niceX = data.reduce('TMath::Abs(BU_mass_Cjp -' + str(mean_Bs.getVal()) + ')>' + str(3 * sigma_Bs_eff) + '&& TMath::Abs(PHI_mass_Cjp -' + str(mean_phi.getVal()) + ') < 0.01')
# mean_X.setVal(old_mean_X); mean_X.setConstant(1)
# model_control.fitTo(data_not_niceX, RF.Extended(ROOT.kTRUE))
# model_control.fitTo(data_not_niceX, RF.Extended(ROOT.kTRUE))
# mean_X.setConstant(0)
# model_control.fitTo(data_not_niceX, RF.Extended(ROOT.kTRUE))
# plot_on_frame(var_control, data_not_niceX, model_control, 'Data: m(J/#psi#pi^{+}#pi^{-}) projection', left_control_data, right_control_data, nbins_control_data, plot_control_param[mode])
#

# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_control)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf("model_X"))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var("N_sig_X")))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var("X_mass_Cjp")))
# mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1"), w.var("a2"), w.var("N_bkgr_control"), w.var("mean_X")))
# mc.SetSnapshot(ROOT.RooArgSet(w.var("N_sig_X")))
# Import(w, mc)
#
# sbModel = w.obj("ModelConfig")
# sbModel.SetName("S+B_model")
# poi = sbModel.GetParametersOfInterest().first()
# bModel = sbModel.Clone()
# bModel.SetName("B_only_model")
# oldval = poi.getVal()
# poi.setVal(0)
# bModel.SetSnapshot(ROOT.RooArgSet(poi))
# poi.setVal(oldval)
# # ac = ROOT.RooStats.AsymptoticCalculator(data_veryniceX, sbModel, bModel)
# # ac.SetOneSidedDiscovery(True)
# # asResult = ac.GetHypoTest()
# # asResult.Print()
#
#
# masses = []
# p0values = []
# p0valuesExpected = []
#
# stepsize = (right_control_data - left_control_data)/20
# masslist = [left_control_data + i*stepsize for i in range(20 + 1)]
# for mass in masslist:
#     w.var("mean_X").setVal(mass)
#     ac = ROOT.RooStats.AsymptoticCalculator(data_veryniceX, sbModel, bModel)
#     ac.SetOneSidedDiscovery(True)
#     ac.SetPrintLevel(-1)
#     asymCalcResult = ac.GetHypoTest()
#     masses.append(mass)
#     p0values.append(asymCalcResult.NullPValue())
#     expectedP0 = ROOT.RooStats.AsymptoticCalculator.GetExpectedPValues(asymCalcResult.NullPValue(),  asymCalcResult.AlternatePValue(), 0, False)
#     p0valuesExpected.append(expectedP0)
#
# import numpy as np
# c = ROOT.TCanvas()
# graph1 = ROOT.TGraph(len(masses),np.asarray(masses),np.asarray(p0values))
# graph2 = ROOT.TGraph(len(masses),np.asarray(masses),np.asarray(p0valuesExpected))
# graph1.SetMarkerStyle(20)
# graph1.Draw("APC")
# graph2.SetLineStyle(2)
# graph2.Draw("C")
#
# graph1.GetXaxis().SetTitle("X(3872) mass")
# graph1.GetYaxis().SetTitle("p0 value")
# graph1.SetTitle("Significance vs Mass")
# graph1.SetMinimum(graph2.GetMinimum())
# graph1.SetLineColor(4)
# graph2.SetLineColor(2)
# ROOT.gPad.SetLogy(True)
# c.Draw()














##        -------------        ##
##           2D SPLOT          ##
##        -------------        ##

# c_sPlot = ROOT.TCanvas("c_sPlot", "c_sPlot", 1700, 650)
# c_sPlot.Divide(2,2)
# c_sPlot.cd(1)
#
# model_2D_data.fitTo(data_psi, RF.Extended(ROOT.kTRUE))
# model_2D_data.fitTo(data_psi, RF.Extended(ROOT.kTRUE))
# # model_2D.fitTo(data_psi, , RF.Extended(ROOT.kTRUE))
#
# plot_on_frame(var_discr, data_psi, model_2D_data, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S) region', left_discr_data, right_discr_data, nbins_discr_data)
#
# c_sPlot.cd(2)
# plot_on_frame(PHI_mass_Cjp, data_psi, model_2D_data, 'Data: m(K^{+}K^{-}) from #psi(2S) region', left_phi_data, right_phi_data, nbins_phi_data)
#
# # w = ROOT.RooWorkspace("w", True)
# # Import = getattr(ROOT.RooWorkspace, 'import')
# # Import(w, model_2D_data)
# # w.writeToFile('~/Study/Bs_resonances/model_2D_data_SC.root')
#
#
# # c_sPlot = ROOT.TCanvas("c_sPlot", "c_sPlot", 1700, 650)
# # c_sPlot.Divide(2,1)
#
# #############
#
# print '\n\n' + 30*'#' + '\n\n\n         Data psi(2S): splot now         \n\n\n' + 30*'#' + '\n\n'
#
# # file_model_2D = ROOT.TFile('~/Study/Bs_resonances/model_2D_data_SC.root')
# # w = file_model_2D.Get('w')
# # model_2D_data = w.pdf('model_2D_data')
# # model_2D_data.fitTo(data_psi, RF.Extended(ROOT.kTRUE))
#
# ROOT.RooStats.SPlot(
#     'sData_psi', 'sData_psi', data_psi, model_2D_data,
#     ROOT.RooArgList(N_ss_2D, N_bb_2D, N_sb_2D)
# )
#
# # c_sPlot.cd(1)
# # print '\n\n' + 30*'#' + '\n\n\n         MC psi(2S): psi(2S) mass now         \n\n\n' + 30*'#' + '\n\n'
# # model_psi.fitTo(data_psi_MC, RF.Extended(ROOT.kTRUE))
# # plot_on_frame(var_control, data_psi_MC, model_psi, 'MC: m(J/#psi#pi^{+}#pi^{-}) projection', left_psi, right_psi, nbins_psi)
#
#
# c_sPlot.cd(3)
# data_psi_weighted = ROOT.RooDataSet(data_psi.GetName(), data_psi.GetTitle(), data_psi, data_psi.get(), '1 > 0', "N_ss_2D_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# # sigma_psi.setConstant(1);  gamma_BW_psi.setConstant(1)
# # sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1), fr_psi.setConstant(1)
# rrr_sig = model_psi.fitTo(data_psi_weighted, RF.Save(), RF.SumW2Error(ROOT.kTRUE), RF.Extended(ROOT.kTRUE))
# # rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kTRUE), RF.Extended(ROOT.kTRUE))
# # rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kTRUE), RF.Extended(ROOT.kTRUE))
# plot_on_frame(var_control, data_psi_weighted, model_psi, 'Data: sPlot for #psi(2S) region', left_psi_data, right_psi_data, nbins_psi_data)


###############################################
#_-_-_-_-_-_-          X          _-_-_-_-_-_-#
###############################################

# c.cd(1)
# print '\n\n' + 30*'#' + '\n\n\n         MC X: Bs mass now         \n\n\n' + 30*'#' + '\n\n'
#
# data_X = data.reduce(cuts_X)
# data_X_MC = ROOT.RooDataSet('data', '', file_MC_X.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)), cuts_dR + '&&' + cuts + '&&' + cuts_X)
#
# # mean_phi.setConstant(1)
# model_2D.fitTo(data_X_MC, RF.Extended(ROOT.kTRUE))
# # model_2D.fitTo(data_X_MC, RF.Extended(ROOT.kTRUE))
# # model_discr.fitTo(data_X, RF.Extended(ROOT.kTRUE))
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
# model_2D.fitTo(data_X, RF.Extended(ROOT.kTRUE))
# model_2D.fitTo(data_X, RF.Extended(ROOT.kTRUE))
# # model_discr.fitTo(data_X, RF.Extended(ROOT.kTRUE))
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
# model_X.fitTo(data_X_MC, RF.Extended(ROOT.kTRUE))
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
# data_X_weighted = ROOT.RooDataSet(data_X.GetName(), data_X.GetTitle(), data_X, data_X.get(), cuts + '&&' + cuts_X, "N_sig_discr_sw") ;
# sigma_X.setConstant(1);  gamma_BW_X.setConstant(1)
# rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kTRUE), RF.Extended(ROOT.kTRUE))
# # rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kTRUE), RF.Extended(ROOT.kTRUE))
# # rrr_sig = model_X.fitTo(data_X_weighted, RF.Save(), RF.SumW2Error(ROOT.kTRUE), RF.Extended(ROOT.kTRUE))
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
