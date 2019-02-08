from RooSpace import *
from cuts import *
from math import sqrt


file_data = ROOT.TFile('new_2_with_more_B0_e3de87.root')
# file_data = ROOT.TFile('~/Study/Bs_resonances_ML/masses_tree_RF_0p9_both.root')
# file_data = ROOT.TFile('new_noKaon_fabs_76e92fd.root')
# file_data = ROOT.TFile('new_noKaon_9988200.root')
# file_data = ROOT.TFile('new.root')

w_Bs, f_Bs = get_workspace('workspace_' + mode + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + mode + '_phi.root', 'workspace')
w_delta_phi, f_delta_phi = get_workspace('workspace_' + mode + '_delta_gen_phi_dRmatched.root', 'workspace')


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

sigma_delta_1.setVal(w_delta_phi.var('sigma_delta_1').getVal());  sigma_delta_2.setVal(w_delta_phi.var('sigma_delta_2').getVal());
fr_delta.setVal(w_delta_phi.var('fr_delta').getVal()); # fr_Bs_1 = w_Bs.var('fr_Bs_1'); fr_Bs_2 = w_Bs.var('fr_Bs_2')
# mean_delta.setVal(w_delta_phi.var('mean_delta').getVal());


    ##   -----------------------------    ##
    ##      DATA: sPlot & Sidebands       ##
    ##   -----------------------------    ##

CMS_tdrStyle_lumi.extraText = "Preliminary"
# file_out_data = open('/home/yaourt/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/' + mode +'_data_evtN.txt', 'w')

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

fr = {'control': fr_X.getVal() if mode == 'X' else fr_psi.getVal(), 'Bs': fr_Bs.getVal()}
sigma_1 = {'control': sigma_X_1.getVal() if mode == 'X' else sigma_psi_1.getVal(), 'Bs': sigma_Bs_1.getVal()}
sigma_2 = {'control': sigma_X_2.getVal() if mode == 'X' else sigma_psi_2.getVal(), 'Bs': sigma_Bs_2.getVal()}
sigma_eff = sqrt( fr[sPlot_cut] * sigma_1[sPlot_cut]**2 + (1 - fr[sPlot_cut]) * sigma_2[sPlot_cut]**2) if sPlot_cut != 'phi' else 0.

window = 0.01 if sPlot_cut == 'phi' else 3*sigma_eff
wind_sideband_dist = 0.005 if sPlot_cut == 'phi' else 2*sigma_eff

# data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta), ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(BU_pt_Cjp, BU_eta_Cjp)),
# cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode]))
data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta),
                                                             ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(BU_pt_Cjp, BU_eta_Cjp, BU_reflmass_PP_Cjp)),
                                                             cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[mode]))
data_sig = data.reduce('TMath::Abs(' + var[sPlot_cut].GetName() + ' -' + str(mean[sPlot_cut].getVal()) + ')<' + str(window))
data_sideband = data.reduce('TMath::Abs(' + var[sPlot_cut].GetName() + ' - ' + str(mean[sPlot_cut].getVal()) + ')>' + str(window + wind_sideband_dist) + ' && TMath::Abs(' + var[sPlot_cut].GetName() + ' - ' + str(mean[sPlot_cut].getVal()) + ')<' + str(2.*window + wind_sideband_dist))

c = ROOT.TCanvas("c", "c", 1600, 800)
c.Divide(2, 1)

c.cd(1)
frame_1 = ROOT.RooPlot(" ", 'pipi reflection', BU_reflmass_PP_Cjp, 4.1, 5.4, 130);
data.plotOn(frame_1)
frame_1.Draw()

c.cd(2)
frame_2 = ROOT.RooPlot(" ", 'pipi reflection, ' + str(mode) + ' window', BU_reflmass_PP_Cjp, 4.1, 5.4, 130);
data_sig.plotOn(frame_2)
frame_2.Draw()

c.SaveAs('~/Study/Bs_resonances/pipi_refl_data_wide_' + str(mode) + '.pdf')
