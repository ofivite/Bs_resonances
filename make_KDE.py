from cuts import *
from RooSpace import *

wind = 0.014038941893838098
mean = 3.6862759784026586

# file_B0_refl = ROOT.TFile('~/Study/Bs_resonances/SimpleFileMC_b715x_0_14000_BdToPsiKstar_wo_phi_match_v6_488_496_1245c8f.root')
file_B0_refl = ROOT.TFile('~/Study/Bs_resonances/B0ToPsiKstar_step3_837be9c.root')

data_B0_refl = ( ROOT.RooDataSet('data_B0_refl', 'data_B0_refl', file_B0_refl.Get('mytree'),
                 ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)),
                 cuts_Bs_MC + '&&' + cuts_phi_MC + '&&' + cuts_control_MC + ' && ' + cuts_pipi[mode] + '&&' + cuts_match_dR + ' && ' + 'TMath::Abs(X_mass_Cjp -' + str(mean) + ')<' + str(wind))
                )
print data_B0_refl.sumEntries()
B0_refl = ROOT.RooKeysPdf("B0_refl", "B0_refl", var_discr, data_B0_refl, ROOT.RooKeysPdf.MirrorBoth, 2)

w = ROOT.RooWorkspace("w", True)
Import = getattr(ROOT.RooWorkspace, 'import')
Import(w, B0_refl)
w.writeToFile('~/Study/Bs_resonances/file_B0_refl_ws_data_cuts_dR0p05_SC.root')
