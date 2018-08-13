from RooSpace import *
from cuts import *
import numpy as np
import glob, os, os.path


filelist = glob.glob('Slices/*_' + mode + '*.pdf')
for f in filelist:
    os.remove(f)

w_Bs, f_Bs = get_workspace('workspace_' + mode + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + mode + '_phi.root', 'workspace')

sigma_Bs_1.setVal(w_Bs.var('sigma_Bs_1').getVal());  sigma_Bs_2.setVal(w_Bs.var('sigma_Bs_2').getVal()); # sigma_Bs_3 = w_Bs.var('sigma_Bs_3')
fr_Bs.setVal(w_Bs.var('fr_Bs').getVal()); # fr_Bs_1 = w_Bs.var('fr_Bs_1'); fr_Bs_2 = w_Bs.var('fr_Bs_2')
mean_Bs.setVal(w_Bs.var('mean_Bs').getVal());

sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); # sigma_Bs_3.setConstant(1);
fr_Bs.setConstant(1); # fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);

sigmaCB_phi_1.setVal(w_phi.var('sigmaCB_phi_1').getVal()); alpha_phi_1.setVal(w_phi.var('alpha_phi_1').getVal()); n_phi_1.setVal(w_phi.var('n_phi_1').getVal())
sigmaCB_phi_2.setVal(w_phi.var('sigmaCB_phi_2').getVal()); alpha_phi_2.setVal(w_phi.var('alpha_phi_2').getVal()); n_phi_2.setVal(w_phi.var('n_phi_2').getVal())

fr_phi.setVal(w_phi.var('fr_phi').getVal()); mean_phi.setVal(w_phi.var('mean_phi').getVal());

sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1); fr_phi.setConstant(1)
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
mean_phi.setConstant(1)

sigma_psi_1.setVal(w_psi.var('sigma_psi_1').getVal()); sigma_psi_2.setVal(w_psi.var('sigma_psi_2').getVal()); # sigma_psi_3 = w_control.var('sigma_psi_3')
fr_psi.setVal(w_psi.var('fr_psi').getVal()); #fr_psi_1 = w_control.var('fr_psi_1'); fr_psi_2 = w_control.var('fr_psi_2')
mean_psi.setVal(w_psi.var('mean_psi').getVal());

sigma_X_1.setVal(w_X.var('sigma_X_1').getVal()); sigma_X_2.setVal(w_X.var('sigma_X_2').getVal()); #sigma_X_3.setVal(w_X.var('sigma_X_3').getVal())
fr_X.setVal(w_X.var('fr_X').getVal()); # fr_X_1.setVal(w_X.var('fr_X_1').getVal()); fr_X_2.setVal(w_X.var('fr_X_2').getVal())
mean_X.setVal(w_X.var('mean_X').getVal());

sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); # sigma_psi_3.setConstant(1);
fr_psi.setConstant(1); # fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)
sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); #sigma_X_3.setConstant(1);
fr_X.setConstant(1); # fr_X_1.setConstant(1); fr_X_2.setConstant(1)

N_B0_refl = w_Bs.var('N_B0_refl'); N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
N_bkgr_Bs.setMax(100000.); N_bkgr_phi.setMax(100000.); N_bkgr_control.setMax(100000.);


###-----###  Systematics variation here

bkgr_phi = ROOT.RooBernstein('bkgr_phi', '', PHI_mass_Cjp, ROOT.RooArgList(a1_phi, a2_phi, a3_phi))
bkgr_control = ROOT.RooBernstein('bkgr_control', '', var_control, ROOT.RooArgList(a1, a2))
bkgr_Bs = ROOT.RooBernstein('bkgr_Bs', '', var_discr, ROOT.RooArgList(a1, a2, a3))

model_X = ROOT.RooAddPdf('model_X', 'model_X', ROOT.RooArgList(signal_X, bkgr_control), ROOT.RooArgList(N_sig_X, N_bkgr_control))
model_psi = ROOT.RooAddPdf('model_psi', 'model_psi', ROOT.RooArgList(signal_psi, bkgr_control), ROOT.RooArgList(N_sig_psi, N_bkgr_control))
model_1D_phi = ROOT.RooAddPdf('model_1D_phi', 'model_1D_phi', ROOT.RooArgList(signal_phi, bkgr_phi), ROOT.RooArgList(N_sig_phi, N_bkgr_phi))
model_1D_Bs = ROOT.RooAddPdf('model_1D_Bs', 'model_1D_Bs', ROOT.RooArgList(signal_Bs, bkgr_Bs, B0_refl), ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs, N_B0_refl))

###-----###


control_models = {'X': model_X, 'psi': model_psi}
model_control = control_models[mode]
N_control = {'X': N_sig_X, 'psi': N_sig_psi}
mean_control = {'X': mean_X, 'psi': mean_psi}

var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)


def fit_slice(data_slice):
    c = ROOT.TCanvas("c", "c", 800, 600)

    # a1.setVal(0.04); a2.setVal(0.025); a3.setVal(0.015)

    a1_phi.setConstant(0); a2_phi.setConstant(0); a3_phi.setConstant(0);
    a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);


    left = np.zeros(1); right = np.zeros(1)
    data_slice.getRange(PHI_mass_Cjp, left, right)
    # model_control.fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
    # model_control.fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
    # a1.setConstant(1); a2.setConstant(1); a3.setConstant(1);
    # model_control.fitTo(data_sideband, RF.Extended(ROOT.kTRUE))
    # a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
    # file_out_data.write(str(N_control[mode].getVal()) + ' ' + str(N_control[mode].getError()) + '\n')
    #
    # plot_on_frame(var_control, data_sideband, model_control, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_control_data, right_control_data, nbins_control_data, plot_control_param, False)

    model_1D_Bs.fitTo(data_slice, RF.Extended(ROOT.kTRUE))
    model_1D_Bs.fitTo(data_slice, RF.Extended(ROOT.kTRUE))
    model_1D_Bs.fitTo(data_slice, RF.Extended(ROOT.kTRUE))
    a1.setConstant(1); a2.setConstant(1); a3.setConstant(1);
    model_1D_Bs.fitTo(data_slice, RF.Extended(ROOT.kTRUE))
    model_1D_Bs.fitTo(data_slice, RF.Extended(ROOT.kTRUE))
    a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
    # file_out_data.write(str(N_sig_Bs.getVal()) + ' ' + str(N_sig_Bs.getError()) + '\n')

    plot_on_frame(var_discr, data_slice, model_1D_Bs, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, None, False)

    CMS_tdrStyle_lumi.CMS_lumi( c, 2, 0 );
    c.Update(); c.RedrawAxis(); c.GetFrame().Draw();
    plot_on_frame(var_discr, data_slice, model_1D_Bs, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, None, False)

    c.SaveAs('~/Study/Bs_resonances/Slices/c_' + str(mode) + refl_line + '_' + str(round(left, 3)) + '_' + str(round(right, 3)) +'.pdf')


# --------------------------------------------------------- #

    sData_Bs_psi_side = ROOT.RooStats.SPlot(
        'sData_Bs_psi_side', 'sData_Bs_psi_side', data_slice, model_1D_Bs,
        ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs, N_B0_refl)
    )
    data_side_weighted = ROOT.RooDataSet(data_slice.GetName(), data_slice.GetTitle(), data_slice, data_slice.get(), '1 > 0', N_sig_Bs.GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi


    #
    c_sPlot = ROOT.TCanvas("c_sPlot", "c_sPlot", 800, 600)
    model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
    model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
    a1.setConstant(1); a2.setConstant(1); a3.setConstant(1);
    model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
    a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);

    plot_on_frame(var_control, data_side_weighted, model_control, 'Data: sPlot to m(K^{+}K^{-})', left_control_data, right_control_data, nbins_control_data, None, False)
    CMS_tdrStyle_lumi.CMS_lumi( c_sPlot, 2, 0 );
    c_sPlot.Update(); c_sPlot.RedrawAxis(); c_sPlot.GetFrame().Draw();
    plot_on_frame(var_control, data_side_weighted, model_control, 'Data: sPlot to m(K^{+}K^{-})', left_control_data, right_control_data, nbins_control_data, None, False)

    c_sPlot.SaveAs('~/Study/Bs_resonances/Slices/c_sPlot_' + str(mode) + refl_line + '_' + str(round(left, 3)) + '_' + str(round(right, 3)) +'.pdf')

    return [N_sig_Bs.getVal(), N_sig_Bs.getError(), N_control[mode].getVal(), N_control[mode].getError()]


window = 0.01
file_data = ROOT.TFile('new_noKaon_fabs_with_pt&eta_979cfd3.root')
data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta), ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(BU_pt_Cjp, BU_eta_Cjp)),
cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode]))


# cuts = [(0.99, 1.), (1., 1.01), (1.03, 1.0325), (1.0325, 1.035), (1.035, 1.0375), (1.0375, 1.04), (1.04, 1.0425), (1.0425, 1.045), (1.045, 1.0475), (1.0475, 1.05)]
cuts = [(0.99, 1.), (1., 1.01), (1.03, 1.035), (1.035, 1.04), (1.04, 1.045), (1.045, 1.05)]
data_slices = [data.reduce('PHI_mass_Cjp > ' + str(cut[0]) + '&& PHI_mass_Cjp <' + str(cut[1])) for cut in cuts]
events_sideband = map(fit_slice, data_slices)

splotted_slice_numbers = [item[2] for item in events_sideband]
splotted_slice_numbers_err = [item[3] for item in events_sideband]
cuts_Xcoord = [(cut_range[0] + cut_range[1]) / 2. for cut_range in cuts]
cuts_Xcoord_err = [(cut_range[1] - cut_range[0]) / 2. for cut_range in cuts]

gr = ROOT.TGraphErrors(len(splotted_slice_numbers), np.array(cuts_Xcoord), np.array(splotted_slice_numbers), np.array(cuts_Xcoord_err), np.array(splotted_slice_numbers_err))
c = ROOT.TCanvas()
gr.Draw('AP')
c.SaveAs('~/Study/Bs_resonances/Slices/nonresonant_in_bins_' + sPlot_from + '->' + sPlot_to + '_' + str(mode) + '.pdf')
