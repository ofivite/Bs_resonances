from RooSpace import *
from cuts import *
from math import sqrt


file_data = ROOT.TFile('new_noKaon_fabs_with_pt&eta_979cfd3.root')
# file_data = ROOT.TFile('new_noKaon_fabs_76e92fd.root')
# file_data = ROOT.TFile('new_noKaon_9988200.root')
# file_data = ROOT.TFile('new.root')

w_Bs, f_Bs = get_workspace('workspace_' + mode + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + mode + '_phi.root', 'workspace')


sigma_Bs_1.setVal(w_Bs.var('sigma_Bs_1').getVal());  sigma_Bs_2.setVal(w_Bs.var('sigma_Bs_2').getVal());
# sigma_Bs_3.setVal(w_Bs.var('sigma_Bs_3').getVal());
# sigma_Bs.setVal(w_Bs.var('sigma_Bs').getVal());
# gamma_BW_Bs.setVal(w_Bs.var('gamma_BW_Bs').getVal());
fr_Bs.setVal(w_Bs.var('fr_Bs').getVal());
# fr_Bs_1.setVal(w_Bs.var('fr_Bs_1').getVal()); fr_Bs_2.setVal(w_Bs.var('fr_Bs_2').getVal());
mean_Bs.setVal(w_Bs.var('mean_Bs').getVal());

sigmaCB_phi_1.setVal(w_phi.var('sigmaCB_phi_1').getVal()); alpha_phi_1.setVal(w_phi.var('alpha_phi_1').getVal()); n_phi_1.setVal(w_phi.var('n_phi_1').getVal())
sigmaCB_phi_2.setVal(w_phi.var('sigmaCB_phi_2').getVal()); alpha_phi_2.setVal(w_phi.var('alpha_phi_2').getVal()); n_phi_2.setVal(w_phi.var('n_phi_2').getVal())
fr_phi.setVal(w_phi.var('fr_phi').getVal());
# gamma_BW_phi.setVal(w_phi.var('gamma_BW_phi').getVal());
# sigma_gauss_phi.setVal(w_phi.var('sigma_gauss_phi').getVal());
# sigma_phi.setVal(w_phi.var('sigma_phi').getVal());
# mean_zero_phi.setVal(w_phi.var('mean_zero_phi').getVal());
mean_phi.setVal(w_phi.var('mean_phi').getVal());

sigma_psi_1.setVal(w_psi.var('sigma_psi_1').getVal()); sigma_psi_2.setVal(w_psi.var('sigma_psi_2').getVal());
# sigma_psi_3.setVal(w_psi.var('sigma_psi_3').getVal());
# sigma_psi.setVal(w_psi.var('sigma_psi').getVal());
# gamma_BW_psi.setVal(w_psi.var('gamma_BW_psi').getVal());
fr_psi.setVal(w_psi.var('fr_psi').getVal()); # fr_psi_1.setVal(w_psi.var('fr_psi_1').getVal()); fr_psi_2.setVal(w_psi.var('fr_psi_2').getVal());
mean_psi.setVal(w_psi.var('mean_psi').getVal());

sigma_X_1.setVal(w_X.var('sigma_X_1').getVal()); sigma_X_2.setVal(w_X.var('sigma_X_2').getVal());
# sigma_X_3.setVal(w_X.var('sigma_X_3').getVal());
# sigma_X.setVal(w_X.var('sigma_X').getVal());
# gamma_BW_X.setVal(w_X.var('gamma_BW_X').getVal());
fr_X.setVal(w_X.var('fr_X').getVal()); # fr_X_1.setVal(w_X.var('fr_X_1').getVal()); fr_X_2.setVal(w_X.var('fr_X_2').getVal());
mean_X.setVal(w_X.var('mean_X').getVal());


sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1);
sigma_Bs.setConstant(1); gamma_BW_Bs.setConstant(1);
fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);

sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1);
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
gamma_BW_phi.setConstant(1); sigma_gauss_phi.setConstant(1); sigma_phi.setConstant(1)
fr_phi.setConstant(1); mean_zero_phi.setConstant(1)

sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); sigma_psi_3.setConstant(1);
sigma_psi.setConstant(1); gamma_BW_psi.setConstant(1)
fr_psi.setConstant(1);  fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)

sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); sigma_X_3.setConstant(1);
sigma_X.setConstant(1); gamma_BW_X.setConstant(1)
fr_X.setConstant(1); fr_X_1.setConstant(1); fr_X_2.setConstant(1)

N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)


###-----###  Systematics variation here

# bkgr_phi = ROOT.RooBernstein('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_phi, a2_phi, a3_phi))
# bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2, a3))
# bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2, a3))
#
# model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_control), ROOT.RooArgList(N_sig_X, N_bkgr_control))
# model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(signal_psi, bkgr_control), ROOT.RooArgList(N_sig_psi, N_bkgr_control))
# model_1D_phi = ROOT.RooAddPdf('model_1D_phi', 'model_1D_phi', ROOT.RooArgList(signal_phi, bkgr_phi), ROOT.RooArgList(N_sig_phi, N_bkgr_phi))
# model_1D_Bs = ROOT.RooAddPdf('model_1D_Bs', 'model_1D_Bs', ROOT.RooArgList(signal_Bs, bkgr_Bs, B0_refl), ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs, N_B0_refl))

# control_models = {'X': model_X, 'psi': model_psi}
# model_control = control_models[mode]
# N_control = {'X': N_sig_X, 'psi': N_sig_psi}
# mean_control = {'X': mean_X, 'psi': mean_psi}

###-----###


    ##   -----------------------------    ##
    ##      DATA: sPlot & Sidebands       ##
    ##   -----------------------------    ##

CMS_tdrStyle_lumi.extraText = "Preliminary"
file_out_data = open('/home/yaourt/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/' + mode +'_data_evtN.txt', 'w')

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

fr = {'control': fr_X.getVal() if mode == 'X' else fr_psi.getVal(), 'Bs': fr_Bs.getVal()}
sigma_1 = {'control': sigma_X_1.getVal() if mode == 'X' else sigma_psi_1.getVal(), 'Bs': sigma_Bs_1.getVal()}
sigma_2 = {'control': sigma_X_2.getVal() if mode == 'X' else sigma_psi_2.getVal(), 'Bs': sigma_Bs_2.getVal()}
sigma_eff = sqrt( fr[sPlot_cut] * sigma_1[sPlot_cut]**2 + (1 - fr[sPlot_cut]) * sigma_2[sPlot_cut]**2) if sPlot_cut != 'phi' else 0.

window = 0.01 if sPlot_cut == 'phi' else 3*sigma_eff
wind_sideband_dist = 0.005 if sPlot_cut == 'phi' else 2*sigma_eff

data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta), ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(BU_pt_Cjp, BU_eta_Cjp)),
cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode]))
# data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode])

#---------------#
##  Inclusive  ##
#---------------#

c_inclus = ROOT.TCanvas("c_inclus", "c_inclus", 800, 600)

mean[sPlot_cut].setConstant(1);
model[sPlot_cut].fitTo(data, RF.Extended(ROOT.kTRUE))
model[sPlot_cut].fitTo(data, RF.Extended(ROOT.kTRUE))
mean[sPlot_cut].setConstant(0);
model[sPlot_cut].fitTo(data, RF.Extended(ROOT.kTRUE))


plot_on_frame(var[sPlot_cut], data, model[sPlot_cut], '', left[sPlot_cut], right[sPlot_cut], nbins[sPlot_cut], None, False)
CMS_tdrStyle_lumi.CMS_lumi( c_inclus, 2, 0 );

#----------------#
##  Draw lines  ##
#----------------#

y_sdb_l = {'control': 950 if mode == 'X' else 1750}; y_sig = {'control': 1220 if mode == 'X' else 2400 }; y_sdb_r = {'control': 1290 if mode == 'X' else 2750 };
line_width = 4

line_ll_sdb = ROOT.TLine(mean[sPlot_cut].getVal() - 2.*window - wind_sideband_dist, 0, mean[sPlot_cut].getVal() - 2.*window - wind_sideband_dist, y_sdb_l['control'])
line_lr_sdb = ROOT.TLine(mean[sPlot_cut].getVal() - window - wind_sideband_dist, 0, mean[sPlot_cut].getVal() - window - wind_sideband_dist, y_sdb_l['control'])
line_rl_sdb = ROOT.TLine(mean[sPlot_cut].getVal() + 2.*window + wind_sideband_dist, 0, mean[sPlot_cut].getVal() + 2.*window + wind_sideband_dist, y_sdb_r['control'])
line_rr_sdb = ROOT.TLine(mean[sPlot_cut].getVal() + window + wind_sideband_dist, 0, mean[sPlot_cut].getVal() + window + wind_sideband_dist, y_sdb_r['control'])
line_l_sig = ROOT.TLine(mean[sPlot_cut].getVal() - window, 0, mean[sPlot_cut].getVal() - window, y_sig['control'])
line_r_sig = ROOT.TLine(mean[sPlot_cut].getVal() + window, 0, mean[sPlot_cut].getVal() + window, y_sig['control'])

#
line_ll_sdb.SetLineWidth(line_width); line_lr_sdb.SetLineWidth(line_width); line_rl_sdb.SetLineWidth(line_width); line_rr_sdb.SetLineWidth(line_width);
line_l_sig.SetLineWidth(line_width); line_r_sig.SetLineWidth(line_width);
#
line_l_sig.SetLineColor(47); line_r_sig.SetLineColor(47)
line_ll_sdb.SetLineColor(ROOT.kBlue-8); line_lr_sdb.SetLineColor(ROOT.kBlue-8); line_rl_sdb.SetLineColor(ROOT.kBlue-8); line_rr_sdb.SetLineColor(ROOT.kBlue-8);
#
line_ll_sdb.Draw(); line_lr_sdb.Draw(); line_rl_sdb.Draw(); line_rr_sdb.Draw(); line_l_sig.Draw(); line_r_sig.Draw()

c_inclus.Update(); c_inclus.RedrawAxis(); # c_inclus.GetFrame().Draw();
c_inclus.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_inclus___' + str(mode) + refl_line + '.pdf')
###


# ---------------------#
# #  SR/SdR division  ##
# ---------------------#

print '\n\n' + 30*'#' + '\n\n\n         Data psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n'

data_sig = data.reduce('TMath::Abs(' + var[sPlot_cut].GetName() + ' -' + str(mean[sPlot_cut].getVal()) + ')<' + str(window))
data_sideband = data.reduce('TMath::Abs(' + var[sPlot_cut].GetName() + ' - ' + str(mean[sPlot_cut].getVal()) + ')>' + str(window + wind_sideband_dist) + ' && TMath::Abs(' + var[sPlot_cut].GetName() + ' - ' + str(mean[sPlot_cut].getVal()) + ')<' + str(2.*window + wind_sideband_dist))


if refl_ON and mode == 'psi':  N_B0_refl.setVal(200.); N_B0_refl.setConstant(0)
else:        N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

            #-------------#
            ##  sPlot I  ##
            #-------------#

c_sPlot_1 = ROOT.TCanvas("c_sPlot_1", "c_sPlot_1", 800, 600)

model[sPlot_from].fitTo(data_sig, RF.Extended(ROOT.kTRUE))
model[sPlot_from].fitTo(data_sig, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);

model[sPlot_from].fitTo(data_sig, RF.Extended(ROOT.kTRUE))
a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);

file_out_data.write(str(N[sPlot_from].getVal()) + ' ' + str(N[sPlot_from].getError()) + '\n')
plot_on_frame(var[sPlot_from], data_sig, model[sPlot_from], '', left[sPlot_from], right[sPlot_from], nbins[sPlot_from], None, False)

CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_1, 2, 0 ); c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); # c_sPlot_1.GetFrame().Draw();
c_sPlot_1.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_1_' + str(mode) + refl_line + '.pdf')

            #--------------#
            ##  sPlot II  ##
            #--------------#

sPlot_list = ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from], N_B0_refl) if sPlot_from == 'Bs' else ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from])
sData_Bs_psi_sig = ROOT.RooStats.SPlot('sData_Bs_psi_sig', 'sData_Bs_psi_sig', data_sig, model[sPlot_from], sPlot_list)
data_sig_weighted = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N[sPlot_from].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi

# data_sig_weighted_unbinned = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N_control[mode].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# data_sig_weighted = ROOT.RooDataHist(data_sig.GetName(), data_sig.GetTitle(), ROOT.RooArgSet(PHI_mass_Cjp), data_sig_weighted_unbinned)
##########

c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600)

model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
results_splot2 = model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE))
# results_splot2 = model[sPlot_to].fitTo(data_sig_weighted, RF.Save(), RF.Hesse(ROOT.kFALSE), RF.Extended(ROOT.kTRUE), RF.Minos(ROOT.kTRUE), RF.Minos(ROOT.RooArgSet(N_sig_phi)))

a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);


file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
plot_on_frame(var[sPlot_to], data_sig_weighted, model[sPlot_to], ' ', left[sPlot_to], right[sPlot_to], nbins[sPlot_to], None, False)

CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_2, 2, 0 ); c_sPlot_2.Update(); c_sPlot_2.RedrawAxis();
# c_sPlot_2.GetFrame().Draw();
c_sPlot_2.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_2_' + str(mode) + refl_line + '.pdf')


# #####---- NLL plots ----####
# ###
# #
# nll = model[sPlot_to].createNLL(data_sig_weighted)
# m = ROOT.RooMinuit(nll)
# m.setVerbose(ROOT.kTRUE)
# #
# # m.migrad()
# m.minos(ROOT.RooArgSet(N_sig_phi, mean_phi))
# N_sig_phi.Print()
#
#
# pll = nll.createProfile(ROOT.RooArgSet(N_sig_phi))
# N_sig_phi.setRange(N_sig_phi.getVal() - 100., N_sig_phi.getVal() + 100. )
# frame = N_sig_phi.frame()
#
# nll.plotOn(frame, RF.LineColor(ROOT.kBlue), RF.ShiftToZero())
# pll.plotOn(frame, RF.LineColor(ROOT.kRed))
#
# c = ROOT.TCanvas()
# frame.Draw()
# c.SaveAs('~/nll_pll.pdf')


#       X:  119.6 +/- (-11.45,12.11)  L(19.56 - 219.6)
# psi(2S):  2541 +/- (-53.86,54.52)  L(0 - 1e+05)
#
# m.migrad()
# m.hesse()
# N_sig_phi.Print()


# ###---- Significance ----####
#
# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, model_control)
# mc = ROOT.RooStats.ModelConfig("ModelConfig",w)
# mc.SetPdf(w.pdf(model_control.GetName()))
# mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(N_control[mode].GetName())))
# # w.var("N_sig_X").setError(20.)
# mc.SetObservables(ROOT.RooArgSet(w.var("X_mass_Cjp")))
# mc.SetNuisanceParameters(ROOT.RooArgSet(w.var("a1"), w.var("a2"), w.var("N_bkgr_control"), w.var(mean_control[mode].GetName())))
# mc.SetSnapshot(ROOT.RooArgSet(w.var(N_control[mode].GetName())))
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
# ac = ROOT.RooStats.AsymptoticCalculator(data_sig_weighted, sbModel, bModel)
# ac.SetOneSidedDiscovery(True)
# asResult = ac.GetHypoTest()
# asResult.Print()

            #---------------#
            ##  sPlot III  ##
            #---------------#

c_sPlot_3 = ROOT.TCanvas("c_sPlot_3", "c_sPlot_3", 800, 600)
mean_Bs.setConstant(1); mean_phi.setConstant(1); mean_control[mode].setConstant(1);
N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
model[sPlot_from].fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);

file_out_data.write(str(N[sPlot_from].getVal()) + ' ' + str(N[sPlot_from].getError()) + '\n')
plot_on_frame(var[sPlot_from], data_sideband, model[sPlot_from], '', left[sPlot_from], right[sPlot_from], nbins[sPlot_from], None, False)

CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_3, 2, 0 );
c_sPlot_3.Update(); c_sPlot_3.RedrawAxis(); # c_sPlot_3.GetFrame().Draw();
c_sPlot_3.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_3_' + str(mode) + refl_line + '.pdf')

            #--------------#
            ##  sPlot IV  ##
            #--------------#

sData_Bs_psi_side = ROOT.RooStats.SPlot(
    'sData_Bs_psi_side', 'sData_Bs_psi_side', data_sideband, model[sPlot_from],
    sPlot_list
)
data_side_weighted = ROOT.RooDataSet(data_sideband.GetName(), data_sideband.GetTitle(), data_sideband, data_sideband.get(), '1 > 0', N[sPlot_from].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi

#
c_sPlot_4 = ROOT.TCanvas("c_sPlot_4", "c_sPlot_4", 800, 600)
model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
model[sPlot_to].fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);

file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
file_out_data.close()

# model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
plot_on_frame(var[sPlot_to], data_side_weighted, model[sPlot_to], '', left[sPlot_to], right[sPlot_to], nbins[sPlot_to], None, False)
CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_4, 2, 0 );
c_sPlot_4.Update(); c_sPlot_4.RedrawAxis(); # c_sPlot_4.GetFrame().Draw();
c_sPlot_4.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_4_' + str(mode) + refl_line + '.pdf')
