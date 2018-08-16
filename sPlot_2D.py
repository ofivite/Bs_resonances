from RooSpace import *
from cuts import *
from math import sqrt


file_data = ROOT.TFile('new_noKaon_fabs_with_pt&eta_979cfd3.root')
# file_data = ROOT.TFile('new_noKaon_fabs_76e92fd.root')
# file_data = ROOT.TFile('new_noKaon_9988200.root')
# file_data = ROOT.TFile('new.root')

file_out_data = open('/home/yaourt/Study/Bs_resonances/' + sPlot_from_1 + '+' + sPlot_from_2 + '->' + sPlot_to + '/' + mode + '_data_evtN.txt', 'w')

w_Bs, f_Bs = get_workspace('workspace_' + mode + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + mode + '_phi.root', 'workspace')


sigma_Bs_1.setVal(w_Bs.var('sigma_Bs_1').getVal());  sigma_Bs_2.setVal(w_Bs.var('sigma_Bs_2').getVal());
# sigma_Bs_3.setVal(w_Bs.var('sigma_Bs_3').getVal());
# sigma_Bs.setVal(w_Bs.var('sigma_Bs').getVal());
# gamma_BW_Bs.setVal(w_Bs.var('gamma_BW_Bs').getVal());
fr_Bs.setVal(w_Bs.var('fr_Bs').getVal()); # fr_Bs_1 = w_Bs.var('fr_Bs_1'); fr_Bs_2 = w_Bs.var('fr_Bs_2')
mean_Bs.setVal(w_Bs.var('mean_Bs').getVal());

sigmaCB_phi_1.setVal(w_phi.var('sigmaCB_phi_1').getVal()); alpha_phi_1.setVal(w_phi.var('alpha_phi_1').getVal()); n_phi_1.setVal(w_phi.var('n_phi_1').getVal())
# sigmaCB_phi_2.setVal(w_phi.var('sigmaCB_phi_2').getVal()); alpha_phi_2.setVal(w_phi.var('alpha_phi_2').getVal()); n_phi_2.setVal(w_phi.var('n_phi_2').getVal())
# fr_phi.setVal(w_phi.var('fr_phi').getVal());
gamma_BW_phi.setVal(w_phi.var('gamma_BW_phi').getVal());
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



    ##   -----------------------------    ##
    ##      DATA: sPlot & Sidebands       ##
    ##   -----------------------------    ##

CMS_tdrStyle_lumi.extraText = "Preliminary"
# file_out_data = open('/home/yaourt/Study/Bs_resonances/' + sPlot_from + '->' + sPlot_to + '/' + mode +'_data_evtN.txt', 'w')

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

fr = {'X': fr_X.getVal(), 'psi': fr_psi.getVal()}
sigma_1 = {'X': sigma_X_1.getVal(), 'psi':sigma_psi_1.getVal()}
sigma_2 = {'X': sigma_X_2.getVal(), 'psi':sigma_psi_2.getVal()}
sigma_eff = sqrt( fr[mode] * sigma_1[mode]**2 + (1 - fr[mode]) * sigma_2[mode]**2)

# window = 3 * sigma_eff
# wind_sideband_dist = 2 * sigma_eff
window = 0.01
wind_sideband_dist = 0.005

data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta), ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(BU_pt_Cjp, BU_eta_Cjp)),
cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode]))


##        -------------        ##
##           2D SPLOT          ##
##        -------------        ##

c_sPlot = ROOT.TCanvas("c_sPlot", "c_sPlot", 2100, 1100)
c_sPlot.Divide(3,2)
c_sPlot.cd(1)

mean_control[mode].setConstant(1); mean_Bs.setConstant(1); mean_phi.setConstant(1)
N_ss_2D.setConstant(1); N_sb_2D.setConstant(1);

model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))
model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))

a1_bb_1.setConstant(1); a2_bb_1.setConstant(1); a3_bb_1.setConstant(1); a4_bb_1.setConstant(1);
a1_bb_2.setConstant(1); a2_bb_2.setConstant(1); a3_bb_2.setConstant(1); a4_bb_2.setConstant(1);
a1_bs.setConstant(1); a2_bs.setConstant(1); a3_bs.setConstant(1); a4_bs.setConstant(1);
a1_sb.setConstant(1); a2_sb.setConstant(1); a3_sb.setConstant(1); a4_sb.setConstant(1);
N_ss_2D.setConstant(0); N_sb_2D.setConstant(0)
# mean_control[mode].setConstant(0); mean_Bs.setConstant(0); mean_phi.setConstant(0)
# mean_control[mode].setRange(mean_control[mode].getVal() - 0.001, mean_control[mode].getVal() + 0.001,); mean_Bs.setRange(mean_Bs.getVal() - 0.001, mean_Bs.getVal() + 0.001); mean_phi.setRange(mean_phi.getVal() - 0.001, mean_phi.getVal() + 0.001)

model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))
model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))

file_out_data.write(str(N_ss_2D.getVal()) + ' ' + str(N_ss_2D.getError()) + '\n')
file_out_data.write(str(N_sb_2D.getVal()) + ' ' + str(N_sb_2D.getError()) + '\n')
file_out_data.write(str(N_bs_2D.getVal()) + ' ' + str(N_bs_2D.getError()) + '\n')

# # N_ss_2D.setConstant(1);
#
# # a1_bb_1.setConstant(0); a2_bb_1.setConstant(0); a3_bb_1.setConstant(0); a4_bb_1.setConstant(0);
# # a1_bb_2.setConstant(0); a2_bb_2.setConstant(0); a3_bb_2.setConstant(0); a4_bb_2.setConstant(0);
# # a1_bs.setConstant(0); a2_bs.setConstant(0); a3_bs.setConstant(0); a4_bs.setConstant(0);
# # a1_sb.setConstant(0); a2_sb.setConstant(0); a3_sb.setConstant(0); a4_sb.setConstant(0);
#
# model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))
# model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))
# mean_control[mode].setConstant(0); mean_Bs.setConstant(0); mean_phi.setConstant(0)

# N_sb_2D.setConstant(1); N_bs_2D.setConstant(1);
# model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))
#
# N_bb_2D.setConstant(1)
# model_2D_data.fitTo(data, RF.Extended(ROOT.kTRUE))

plot_on_frame(var_to_plot[sPlot_from_1], data, model_2D_data, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S) region', left_from[sPlot_from_1], right_from[sPlot_from_1], nbins_from[sPlot_from_1], plot_param_from[sPlot_from_1], False)

c_sPlot.cd(2)
plot_on_frame(var_to_plot[sPlot_from_2], data, model_2D_data, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) from #psi(2S) region', left_from[sPlot_from_2], right_from[sPlot_from_2], nbins_from[sPlot_from_2], plot_param_from[sPlot_from_2], False)



ROOT.RooStats.SPlot(
    'sData_psi', 'sData_psi', data, model_2D_data,
    ROOT.RooArgList(N_ss_2D, N_bb_2D, N_sb_2D, N_bs_2D)
)

#
data_weighted_ss = ROOT.RooDataSet(data.GetName(), data.GetTitle(), data, data.get(), '1 > 0', "N_ss_2D_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
data_weighted_sb = ROOT.RooDataSet(data.GetName(), data.GetTitle(), data, data.get(), '1 > 0', "N_sb_2D_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi
data_weighted_bs = ROOT.RooDataSet(data.GetName(), data.GetTitle(), data, data.get(), '1 > 0', "N_bs_2D_sw") ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi

model[sPlot_to].fitTo(data_weighted_ss, RF.Extended(ROOT.kTRUE))
model[sPlot_to].fitTo(data_weighted_ss, RF.Extended(ROOT.kTRUE))
model[sPlot_to].fitTo(data_weighted_ss, RF.Extended(ROOT.kTRUE))
a1.setConstant(1); a2.setConstant(1); a3.setConstant(1);
a1_phi.setConstant(1); a2_phi.setConstant(1); a3_phi.setConstant(1);

model[sPlot_to].fitTo(data_weighted_ss, RF.Extended(ROOT.kTRUE))
a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0);


c_sPlot.cd(4)
file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
plot_on_frame(var_to_plot[sPlot_to], data_weighted_ss, model[sPlot_to], 'SS', left_from[sPlot_to], right_from[sPlot_to], nbins_from[sPlot_to], plot_param_from[sPlot_to], False)

c_sPlot.cd(5)
model[sPlot_to].fitTo(data_weighted_sb, RF.Extended(ROOT.kTRUE))
file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
plot_on_frame(var_to_plot[sPlot_to], data_weighted_sb, model[sPlot_to], 'SB', left_from[sPlot_to], right_from[sPlot_to], nbins_from[sPlot_to], plot_param_from[sPlot_to], False)

c_sPlot.cd(6)
model[sPlot_to].fitTo(data_weighted_bs, RF.Extended(ROOT.kTRUE))
file_out_data.write(str(N[sPlot_to].getVal()) + ' ' + str(N[sPlot_to].getError()) + '\n')
plot_on_frame(var_to_plot[sPlot_to], data_weighted_bs, model[sPlot_to], 'BS', left_from[sPlot_to], right_from[sPlot_to], nbins_from[sPlot_to], plot_param_from[sPlot_to], False)

file_out_data.close()
c_sPlot.SaveAs('~/Study/Bs_resonances/' + sPlot_from_1 + '+' + sPlot_from_2 + '->' + sPlot_to + '/' + mode + '_2D.pdf')
