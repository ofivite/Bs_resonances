from RooSpace import *
from cuts import *
from math import sqrt
import numpy as np


def fit_slice(data_slice):
    c = ROOT.TCanvas("c", "c", 800, 600)
    # mean_Bs.setConstant(1); mean_phi.setConstant(1); mean_control[mode].setConstant(1);
    N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)

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
    a1.setConstant(1); a2.setConstant(1); a3.setConstant(1);
    model_1D_Bs.fitTo(data_slice, RF.Extended(ROOT.kTRUE))
    a1.setConstant(0); a2.setConstant(0); a3.setConstant(0);
    # file_out_data.write(str(N_sig_Bs.getVal()) + ' ' + str(N_sig_Bs.getError()) + '\n')

    plot_on_frame(var_discr, data_slice, model_1D_Bs, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)

    CMS_tdrStyle_lumi.CMS_lumi( c, 2, 0 );
    c.Update(); c.RedrawAxis(); c.GetFrame().Draw();
    plot_on_frame(var_discr, data_slice, model_1D_Bs, 'Data: m(J/#psi#pi^{+}#pi^{-}#phi) projection', left_discr_data, right_discr_data, nbins_discr_data, plot_discr_param, False)

    c.SaveAs('~/Study/Bs_resonances/Slices/c_' + str(mode) + refl_line + '_' + str(round(left, 2)) + '_' + str(round(right, 2)) +'.pdf')


# --------------------------------------------------------- #

    sData_Bs_psi_side = ROOT.RooStats.SPlot(
        'sData_Bs_psi_side', 'sData_Bs_psi_side', data_slice, model_1D_Bs,
        ROOT.RooArgList(N_sig_Bs, N_bkgr_Bs) # N_B0_refl
    )
    data_side_weighted = ROOT.RooDataSet(data_slice.GetName(), data_slice.GetTitle(), data_slice, data_slice.get(), '1 > 0', N_sig_Bs.GetName() + '_sw') ; # cuts_Bs_data + '&&' + cuts_phi_data + '&&' + cuts_psi

    #
    c_sPlot = ROOT.TCanvas("c_sPlot", "c_sPlot", 800, 600)
    model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
    model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
    model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE))
    # file_out_data.write(str(N_control[mode].getVal()) + ' ' + str(N_control[mode].getError()) + '\n')
    # file_out_data.close()

    # model_control.fitTo(data_side_weighted, RF.Extended(ROOT.kTRUE), RF.SumW2Error(ROOT.kTRUE))
    plot_on_frame(var_control, data_side_weighted, model_control, 'Data: sPlot to m(K^{+}K^{-})', left_control_data, right_control_data, nbins_control_data, plot_control_param, False)
    CMS_tdrStyle_lumi.CMS_lumi( c_sPlot, 2, 0 );
    c_sPlot.Update(); c_sPlot.RedrawAxis(); c_sPlot.GetFrame().Draw();
    plot_on_frame(var_control, data_side_weighted, model_control, 'Data: sPlot to m(K^{+}K^{-})', left_control_data, right_control_data, nbins_control_data, plot_control_param, False)

    c_sPlot.SaveAs('~/Study/Bs_resonances/Slices/c_sPlot_' + str(mode) + refl_line + '_' + str(round(left, 2)) + '_' + str(round(right, 2)) +'.pdf')

    return (N_sig_Bs.getVal(), N_sig_Bs.getError(), N_control[mode].getVal(), N_control[mode].getError())


file_data = ROOT.TFile('new_noKaon_fabs_with_pt&eta_979cfd3.root')

window = 0.01
var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)

data = (ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp, mu_max_pt, mu_min_pt, mu_max_eta, mu_min_eta), ROOT.RooArgSet(K_max_pt, K_min_pt, K_max_eta, K_min_eta, pi_max_pt, pi_min_pt, pi_max_eta, pi_min_eta)), ROOT.RooArgSet(BU_pt_Cjp, BU_eta_Cjp)),
cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data  + ' && ' + cuts_pipi[mode]))


cuts = [(0.99, 1.), (1., 1.01), (1.03, 1.04), (1.04, 1.05)]
data_slices = [data.reduce('PHI_mass_Cjp > ' + str(cut[0]) + '&& PHI_mass_Cjp <' + str(cut[1])) for cut in cuts]
events_sideband = map(fit_slice, data_slices)
