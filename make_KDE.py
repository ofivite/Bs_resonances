from cuts import *
from RooSpace import *

file_B0_refl = ROOT.TFile('~/Study/Bs_resonances/SimpleFileMC_b715x_0_14000_BdToPsiKstar_wo_phi_match_v6_488_496_1245c8f.root')
data_B0_refl = ( ROOT.RooDataSet('data_B0_refl', 'data_B0_refl', file_B0_refl.Get('mytree'),
                 ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)),
                 cuts_dR + '&&' + cuts_psi_data + '&&' + cuts_Bs_data + '&&' + cuts_phi_data )
                )

B0_refl = ROOT.RooKeysPdf("B0_refl", "B0_refl", var_discr, data_B0_refl, ROOT.RooKeysPdf.MirrorBoth, 2)

w = ROOT.RooWorkspace("w", True)
Import = getattr(ROOT.RooWorkspace, 'import')
Import(w, B0_refl)
w.writeToFile('~/Study/Bs_resonances/file_B0_refl_ws_data_cuts_dR0p05_SC.root')
