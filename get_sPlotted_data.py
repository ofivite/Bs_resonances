from RooSpace import *
from cuts import *
from math import sqrt

needMC = 1

file_data = ROOT.TFile('psi_smatch_v2_fc33ffd.root') if needMC else ROOT.TFile('new_2_with_more_B0_e3de87.root')

w_Bs, f_Bs = get_workspace('workspace_' + mode + '_Bs.root', 'workspace')


sigma_Bs_1.setVal(w_Bs.var('sigma_Bs_1').getVal());  sigma_Bs_2.setVal(w_Bs.var('sigma_Bs_2').getVal());
# sigma_Bs_3.setVal(w_Bs.var('sigma_Bs_3').getVal());
# sigma_Bs.setVal(w_Bs.var('sigma_Bs').getVal());
# gamma_BW_Bs.setVal(w_Bs.var('gamma_BW_Bs').getVal());
fr_Bs.setVal(w_Bs.var('fr_Bs').getVal());
# fr_Bs_1.setVal(w_Bs.var('fr_Bs_1').getVal()); fr_Bs_2.setVal(w_Bs.var('fr_Bs_2').getVal());
mean_Bs.setVal(w_Bs.var('mean_Bs').getVal());


sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1);
sigma_Bs.setConstant(1); gamma_BW_Bs.setConstant(1);
fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);

N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

    ##   -----------------------------    ##
    ##      DATA: sPlot & Sidebands       ##
    ##   -----------------------------    ##

CMS_tdrStyle_lumi.extraText = "Preliminary"

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

fr = {'control': fr_X.getVal() if mode == 'X' else fr_psi.getVal(), 'Bs': fr_Bs.getVal()}
sigma_1 = {'control': sigma_X_1.getVal() if mode == 'X' else sigma_psi_1.getVal(), 'Bs': sigma_Bs_1.getVal()}
sigma_2 = {'control': sigma_X_2.getVal() if mode == 'X' else sigma_psi_2.getVal(), 'Bs': sigma_Bs_2.getVal()}
sigma_eff = sqrt( fr[sPlot_cut] * sigma_1[sPlot_cut]**2 + (1 - fr[sPlot_cut]) * sigma_2[sPlot_cut]**2) if sPlot_cut != 'phi' else 0.

window = 0.01 if sPlot_cut == 'phi' else 3*sigma_eff
wind_sideband_dist = 0.005 if sPlot_cut == 'phi' else 2*sigma_eff


data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(
        ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_1_pt, mu_2_pt, mu_1_eta, mu_2_eta, BU_eta_Cjp),
        ROOT.RooArgSet( ROOT.RooArgSet(K1_pt, K2_pt, K1_eta, K2_eta, PI1_pt, PI2_pt, PI1_eta, PI2_eta, BU_pt_Cjp),
                        ROOT.RooArgSet(BU_pvdistsignif2_Cjp, BU_pvcos2_Cjp, BU_vtxprob_Cjp, JP_pt, JP_eta, JPSI_pvdistsignif2_Cmumu, JPSI_pvcos2_Cmumu, JPSI_vtxprob_Cmumu, JPSI_mass_Cmumu))
        ),

# data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp,
#         mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta), ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)),
        ROOT.RooArgSet(dR_mup, dR_mum, dR_pip, dR_pim, dR_Kp, dR_Km) ) if needMC else ROOT.RooArgSet()
        )
data = data.reduce(cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[mode] + ' && ' + cut_phi_window)


# ---------------------#
# #  SR/SdR division  ##
# ---------------------#

print('\n\n' + 30*'#' + '\n\n\n         Data psi(2S): Bs mass now         \n\n\n' + 30*'#' + '\n\n')

data_sig = data.reduce('TMath::Abs(' + var[sPlot_cut].GetName() + ' -' + str(mean[sPlot_cut].getVal()) + ')<' + str(window))
if needMC: data_sig = data_sig.reduce(cuts_match_dR)

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
