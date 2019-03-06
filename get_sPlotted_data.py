from RooSpace import *
from cuts import *
from math import sqrt

needMC = 0

file_data = ROOT.TFile('BsToPsiPhi_Smatch_v1_pair_dR_phi_genmass.root') if needMC else ROOT.TFile('new_2_with_more_B0_e3de87.root')

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

sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1);
sigma_Bs.setConstant(1); gamma_BW_Bs.setConstant(1);
fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);

sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1);
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
# gamma_BW_phi.setConstant(1); sigma_gauss_phi.setConstant(1); sigma_phi.setConstant(1)
fr_phi.setConstant(1); mean_zero_phi.setConstant(1)

sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); sigma_psi_3.setConstant(1);
sigma_psi.setConstant(1); gamma_BW_psi.setConstant(1)
fr_psi.setConstant(1);  fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)

sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); sigma_X_3.setConstant(1);
sigma_X.setConstant(1); gamma_BW_X.setConstant(1)
fr_X.setConstant(1); fr_X_1.setConstant(1); fr_X_2.setConstant(1)

sigma_delta_1.setConstant(1); sigma_delta_2.setConstant(1); fr_delta.setConstant(1);
mean_delta.setVal(0.); mean_delta.setConstant(1)

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

sig_delta_1 = ROOT.RooGaussian("sig_delta_1", "", PHI_mass_Cjp, mean_delta, sigma_delta_1)
sig_delta_2 = ROOT.RooGaussian("sig_delta_2", "", PHI_mass_Cjp, mean_delta, sigma_delta_2)
signal_delta = ROOT.RooAddPdf("signal_delta", "signal_delta", ROOT.RooArgList(sig_delta_1, sig_delta_2), ROOT.RooArgList(fr_delta))

signal_phi = ROOT.RooFFTConvPdf('resolxrelBW', '', PHI_mass_Cjp, relBW_phi, signal_delta)
model_1D_phi = ROOT.RooAddPdf('model_1D_phi', 'model_1D_phi', ROOT.RooArgList(signal_phi, bkgr_phi), ROOT.RooArgList(N_sig_phi, N_bkgr_phi))

model = {'Bs': model_1D_Bs, 'phi': model_1D_phi, 'control': model_control}
signal = {'Bs': signal_Bs, 'phi': signal_phi, 'control': signal_control}


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


data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(
        ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_1_pt, mu_2_pt, mu_1_eta, mu_2_eta, BU_eta_Cjp),
        ROOT.RooArgSet( ROOT.RooArgSet(K1_pt, K2_pt, K1_eta, K2_eta, PI1_pt, PI2_pt, PI1_eta, PI2_eta, BU_pt_Cjp),
                        ROOT.RooArgSet(BU_pvdistsignif2_Cjp, BU_pvcos2_Cjp, BU_vtxprob_Cjp, JP_pt, JP_eta, JPSI_pvdistsignif2_Cmumu, JPSI_pvcos2_Cmumu, JPSI_vtxprob_Cmumu, JPSI_mass_Cmumu))
        ),

# data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp,
#         mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta), ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)),
        ROOT.RooArgSet(ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2), ROOT.RooArgSet(dR_mu1_vv, dR_mu2_vv, dR_pi1_vv, dR_pi2_vv, dR_K1_vv, dR_K2_vv) ) if needMC else ROOT.RooArgSet()
        ),
        cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[mode] + ' && ' + cut_phi_window))

###
BU_pt_Cjp = ROOT.RooRealVar('BU_pt_Cjp', 'p_{T}(B_{s}^{0}) [GeV]', 0, 800)
BU_eta_Cjp = ROOT.RooRealVar('BU_eta_Cjp', '#eta(B_{s}^{0})', -2.5, 2.5)
BU_pvdistsignif2_Cjp = ROOT.RooRealVar('BU_pvdistsignif2_Cjp', 'DS_{2D}(B_{s}^{0})', 0., 2000.)
BU_pvcos2_Cjp = ROOT.RooRealVar('BU_pvcos2_Cjp', 'cos_{2D}(B_{s}^{0}, PV)', 0., 1.)
BU_vtxprob_Cjp = ROOT.RooRealVar('BU_vtxprob_Cjp', 'vtx prob(B_{s}^{0})', 0., 1.)

###
JP_pt = ROOT.RooRealVar('JP_pt', 'p_{T}(#mu#mu) [GeV]', 0, 800)
JP_eta = ROOT.RooRealVar('JP_eta', '#eta(#mu#mu)', -2.5, 2.5)
JPSI_pvdistsignif2_Cmumu = ROOT.RooRealVar('JPSI_pvdistsignif2_Cmumu', 'DS_{2D}(#mu#mu)', 0., 2000.)
JPSI_pvcos2_Cmumu = ROOT.RooRealVar('JPSI_pvcos2_Cmumu', 'cos_{2D}(#mu#mu, PV)', 0., 1.)
JPSI_vtxprob_Cmumu = ROOT.RooRealVar('JPSI_vtxprob_Cmumu', 'vtx prob(#mu#mu)', 0., 1.)
JPSI_mass_Cmumu = ROOT.RooRealVar('JPSI_mass_Cmumu', 'm(#mu#mu)', 2.8, 3.4)

# ---------------------#
# #  SR/SdR division  ##
# ---------------------#

print('\n\n' + 30*'#' + '\n\n\n         Data psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n')

data_sig = data.reduce('TMath::Abs(' + var[sPlot_cut].GetName() + ' -' + str(mean[sPlot_cut].getVal()) + ')<' + str(window))
data_sideband = data.reduce('TMath::Abs(' + var[sPlot_cut].GetName() + ' - ' + str(mean[sPlot_cut].getVal()) + ')>' + str(window + wind_sideband_dist) + ' && TMath::Abs(' + var[sPlot_cut].GetName() + ' - ' + str(mean[sPlot_cut].getVal()) + ')<' + str(2.*window + wind_sideband_dist))
# data_sig = data_sig.reduce(cuts_match_dR)

if needMC: data_sig = data_sig.reduce(cuts_match_ID[mode] + '&&' + 'TMath::Min(dR_mu1, dR_mu1_vv) < 0.05 && TMath::Min(dR_mu2, dR_mu2_vv) < 0.05 && TMath::Min(dR_pi1, dR_pi1_vv) < 0.05' +
                                                '&& TMath::Min(dR_pi2, dR_pi2_vv) < 0.05 && TMath::Min(dR_K1, dR_K1_vv) < 0.05 && TMath::Min(dR_K2, dR_K2_vv) < 0.05')

if refl_ON and mode == 'psi':  N_B0_refl.setVal(9.); N_B0_refl.setConstant(0)
else:                          N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

            #-------------#
            ##  sPlot I  ##
            #-------------#

if needMC:
    data_sig.SaveAs('psi_MC_sPlot_sig.root')
else:
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
    # model[sPlot_from].fitTo(data_sig, RF.Extended(ROOT.kTRUE))
    # model[sPlot_from].fitTo(data_sig, RF.Extended(ROOT.kTRUE))

    plot_on_frame(var[sPlot_from], data_sig, model[sPlot_from], ' ', left[sPlot_from], right[sPlot_from], nbins[sPlot_from], None, False)

    CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_1, 2, 0 ); c_sPlot_1.Update(); c_sPlot_1.RedrawAxis();
    c_sPlot_1.GetFrame().Draw();


    sPlot_list = ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from], N_B0_refl) if sPlot_from == 'Bs' else ROOT.RooArgList(N[sPlot_from], N_bkgr[sPlot_from])
    sData_Bs_psi_sig = ROOT.RooStats.SPlot('sData_Bs_psi_sig', 'sData_Bs_psi_sig', data_sig, model[sPlot_from], sPlot_list)
    data_sig_weighted_s = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N[sPlot_from].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
    data_sig_weighted_b = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N_bkgr[sPlot_from].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi

    data_sig_weighted_s.SaveAs('psi_data_sPlot_sig.root')
    data_sig_weighted_b.SaveAs('psi_data_sPlot_bkgr.root')

#

# data_sig_weighted_unbinned = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N[sPlot_from].GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
# data_sig_weighted = ROOT.RooDataHist(data_sig.GetName(), data_sig.GetTitle(), ROOT.RooArgSet(PHI_mass_Cjp), data_sig_weighted_unbinned)
##########

# c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600)

# model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
# model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE)) # RF.SumW2Error(ROOT.kTRUE)
# model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE))
# a1.setConstant(1); a2.setConstant(1); a3.setConstant(1); a4.setConstant(1);
# a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1); a4_phi.setConstant(1);
# a1_ext.setConstant(1); a2_ext.setConstant(1); a3_ext.setConstant(1); a4_ext.setConstant(1);
# model[sPlot_to].fitTo(data_sig_weighted, RF.Extended(ROOT.kTRUE))
# a1.setConstant(0); a2.setConstant(0); a3.setConstant(0); a4.setConstant(0);
# a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0); a4_phi.setConstant(0);
# a1_ext.setConstant(0); a2_ext.setConstant(0); a3_ext.setConstant(0); a4_ext.setConstant(0);
#

# file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
# plot_on_frame(var[sPlot_to], data_sig_weighted, model[sPlot_to], ' ', left[sPlot_to], right[sPlot_to], nbins[sPlot_to], None, False)

# CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_2, 2, 0 ); c_sPlot_2.Update(); c_sPlot_2.RedrawAxis();
# c_sPlot_2.GetFrame().Draw();
# c_sPlot_2.SaveAs('~/Study/Bs_resonances/' + sPlot_from_text + '->' + sPlot_to_text + '/c_sPlot_2_' + str(mode) + refl_line + '.pdf')
