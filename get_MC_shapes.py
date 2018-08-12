from RooSpace import *
from cuts import *

files_MC = {'X': 'BsToXPhi_Smatch_v1_min_e233994.root', 'psi':'BsToPsiPhi_Smatch_v1_min_with_pt&eta_8e25fe7.root'}
# files_MC = {'X': 'BsToXPhi_Smatch_v1_min_e233994.root', 'psi':'BsToPsiPhi_Smatch_v1_min_e4a2edf.root'}
# files_MC = {'X': 'BsToXPhi_step3_6c21fba.root', 'psi':'BsToPsiPhi_step3_4a91161.root'}
# files_MC = {'X': 'BsToXPhi_matched_all_1892449.root', 'psi':'BsToPsiPhi_matched_all_1519f1b.root'}
# files_MC = {'X': 'SimpleFileMC_b715x_0_14000.root', 'psi':'SimpleFileMC_b715psi_0_14000.root'}
file_MC = ROOT.TFile(files_MC[mode])

if get_MC_N_evts: file_out_MC = open('/home/yaourt/Study/Bs_resonances/MC_'  + mode + '_fit_results/' + mode + '_MC_evtN_' + sPlot_from + '->' + sPlot_to + '.txt', 'w')

N_control = {'X': N_sig_X, 'psi': N_sig_psi}
mean_control = {'X': mean_X, 'psi': mean_psi}

var_discr.setMin(left_discr_MC); var_discr.setMax(right_discr_MC); #var_discr.setBins(50)
PHI_mass_Cjp.setMin(left_phi_MC); PHI_mass_Cjp.setMax(right_phi_MC); #PHI_mass_Cjp.setBins(50)
var_control.setMin(left_control_MC); var_control.setMax(right_control_MC); #var_control.setBins(50)

data_MC = (ROOT.RooDataSet('data_MC', '', file_MC.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp),
ROOT.RooArgSet(MoID_mu1, MoID_mu2, MoID_pi1, MoID_pi2, MoID_K1, MoID_K2)), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta),
ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2, BU_pt_Cjp, BU_eta_Cjp))),
                   cuts_Bs_MC + '&&' + cuts_phi_MC + '&&' + cuts_control_MC + ' && ' + cuts_pipi[mode]))

data_MC_matched = data_MC.reduce(cuts_match_ID[mode] + '&&' + cuts_match_dR)

##        ---------------       ##
##           FIT OF MC          ##
##        ---------------       ##

CMS_tdrStyle_lumi.extraText       = "Simulation Preliminary"
CMS_tdrStyle_lumi.setTDRStyle()
print '\n\n' + 30*'#' + '\n\n\n         MC psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n'

###-----###

N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

model_1D_Bs.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))
model_1D_Bs.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))

mean_Bs.setMin(mean_Bs.getVal() - 0.005); mean_Bs.setMax(mean_Bs.getVal() + 0.005)
a1.setConstant(1); a2.setConstant(1);
model_1D_Bs.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))

a1.setConstant(0); a2.setConstant(0);
if get_MC_N_evts:
    sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1); fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);
    model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
    model_1D_Bs.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
    file_out_MC.write(str(N_sig_Bs.getVal()) + ' ' + str(N_sig_Bs.getError()) + '\n')

f_out = ROOT.TFile('workspace_' + mode + '_Bs.root', 'recreate')
save_in_workspace(f_out, pdf = [model_1D_Bs])  # signal_Bs
f_out.Close()

###-----###

mean_phi.setVal(1.0195);
model_1D_phi.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))
model_1D_phi.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))
a1_phi.setConstant(1); a2_phi.setConstant(1);
model_1D_phi.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))
a1_phi.setConstant(0); a2_phi.setConstant(0);

if get_MC_N_evts:
    
    sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1); fr_phi.setConstant(1)
    sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
    gamma_BW_phi.setConstant(1);

    model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
    model_1D_phi.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
    file_out_MC.write(str(N_sig_phi.getVal()) + ' ' + str(N_sig_phi.getError()) + '\n')

f_out = ROOT.TFile('workspace_' + mode + '_phi.root', 'recreate')
save_in_workspace(f_out, pdf = [model_1D_phi])   # signal_phi
f_out.Close()

###-----###

model_control.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))
model_control.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1)
model_control.fitTo(data_MC_matched, RF.Extended(ROOT.kTRUE))
a1.setConstant(0); a2.setConstant(0)

f_out = ROOT.TFile('workspace_' + mode + '_control.root', 'recreate')
save_in_workspace(f_out, pdf = [model_control])  #   signal_X
f_out.Close()

if get_MC_N_evts:
    sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); sigma_psi_3.setConstant(1); fr_psi.setConstant(1); fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)
    sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); sigma_X_3.setConstant(1); fr_X.setConstant(1); fr_X_1.setConstant(1); fr_X_2.setConstant(1)

    model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
    model_control.fitTo(data_MC, RF.Extended(ROOT.kTRUE))
    file_out_MC.write(str(N_control[mode].getVal()) + ' ' + str(N_control[mode].getError()))

if get_MC_N_evts: file_out_MC.close()


# ###-----###
#
# c_MC_1 = ROOT.TCanvas("c_MC_1", "c_MC_1", 800, 600)
# plot_on_frame(var_discr, data_MC, model_1D_Bs, 'MC: m(J/#psi#pi^{+}#pi^{#font[122]{\55}}#phi)', left_discr_MC, right_discr_MC, nbins_discr_MC, plot_discr_param, True)
# CMS_tdrStyle_lumi.CMS_lumi( c_MC_1, 0, 0 );
# c_MC_1.Update(); c_MC_1.RedrawAxis(); c_MC_1.GetFrame().Draw();
# # c_MC_1.SaveAs('~/Study/Bs_resonances/MC_'  + mode + '_fit_results/c_MC_Bs___' + str(mode) + '.pdf')
#
# #
# c_MC_2 = ROOT.TCanvas("c_MC_2", "c_MC_2", 800, 600)
# plot_on_frame(PHI_mass_Cjp, data_MC, model_1D_phi, 'MC: m(K^{+}K^{#font[122]{\55}})', left_phi_MC, right_phi_MC, nbins_phi_MC, plot_phi_param, True)
# CMS_tdrStyle_lumi.CMS_lumi( c_MC_2, 0, 0 );
# c_MC_2.Update(); c_MC_2.RedrawAxis(); c_MC_2.GetFrame().Draw();
# # c_MC_2.SaveAs('~/Study/Bs_resonances/MC_'  + mode + '_fit_results/c_MC_phi___' + str(mode) + '.pdf')
#
# #
# c_MC_3 = ROOT.TCanvas("c_MC_3", "c_MC_3", 800, 600)
# plot_on_frame(var_control, data_MC, model_control, 'MC: m(J/#psi#pi^{+}#pi^{#font[122]{\55}})', left_control_MC, right_control_MC, nbins_control_MC, plot_control_param[mode], True)
# CMS_tdrStyle_lumi.CMS_lumi( c_MC_3, 0, 0 );
# c_MC_3.Update(); c_MC_3.RedrawAxis(); c_MC_3.GetFrame().Draw();
# # c_MC_3.SaveAs('~/Study/Bs_resonances/MC_'  + mode + '_fit_results/c_MC_' + str(mode) + '.pdf')
#
