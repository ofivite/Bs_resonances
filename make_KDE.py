import ROOT

dR_mu1 = ROOT.RooRealVar('dR_mu1', '', 0., 0.5)
dR_mu2 = ROOT.RooRealVar('dR_mu2', '', 0., 0.5)
dR_pi1 = ROOT.RooRealVar('dR_pi1', '', 0., 0.5)
dR_pi2 = ROOT.RooRealVar('dR_pi2', '', 0., 0.5)
dR_K1 = ROOT.RooRealVar('dR_K1', '', 0., 0.5)
dR_K2 = ROOT.RooRealVar('dR_K2', '', 0., 0.5)

var_discr = ROOT.RooRealVar('BU_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}#phi) [GeV]', 5.1, 5.6)
var_control = ROOT.RooRealVar('X_mass_Cjp', 'm(J/#psi#pi^{+}#pi^{-}) [GeV]', 3.4, 4.2)
PIPI_mass_Cjp = ROOT.RooRealVar('PIPI_mass_Cjp', 'PIPI_mass_Cjp', 0.2, 1.2)
PHI_mass_Cjp = ROOT.RooRealVar('PHI_mass_Cjp', 'PHI_mass_Cjp', 0., 2.)

left_discr =  5.3669 - 0.21; right_discr = 5.3669 + 0.21; nbins_discr = 60
left_psi = 3.686 - 0.03; right_psi = 3.686 + 0.03; nbins_psi = 60

cuts_dR = '1 > 0'
#cuts_dR = 'dR_mu1 < 0.003 && dR_mu2 < 0.003 && dR_pi1 < 0.01 && dR_pi2 < 0.05 && dR_K1 < 0.05 && dR_K2 < 0.05'
cuts = 'TMath::Abs(PHI_mass_Cjp - 1.02)<0.005 && BU_mass_Cjp > ' + str(left_discr) + '&& BU_mass_Cjp < ' + str(right_discr) + '&& PIPI_mass_Cjp > X_mass_Cjp - 3.0969 - 0.15'
cuts_psi = 'X_mass_Cjp >' + str(left_psi) + ' && X_mass_Cjp < ' + str(right_psi) # + ' && PIPI_mass_Cjp > 0.4 && PIPI_mass_Cjp < 0.6'

file_B0_refl = ROOT.TFile('~/Study/Bs_resonances/SimpleFileMC_b715x_0_14000_BdToPsiKstar_wo_phi_match_v6_488_496_1245c8f.root')
data_B0_refl = ( ROOT.RooDataSet('data_B0_refl', 'data_B0_refl', file_B0_refl.Get('mytree'),
                 ROOT.RooArgSet(ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp), ROOT.RooArgSet(dR_mu1, dR_mu2, dR_pi1, dR_pi2, dR_K1, dR_K2)),
                 cuts_dR + '&&' + cuts + '&&' + cuts_psi )
                )

B0_refl = ROOT.RooKeysPdf("B0_refl", "B0_refl", var_discr, data_B0_refl, ROOT.RooKeysPdf.MirrorBoth, 2)

w = ROOT.RooWorkspace("w", True)
Import = getattr(ROOT.RooWorkspace, 'import')
Import(w, B0_refl)
w.writeToFile('file_B0_refl_ws_after_cuts_dR0p05_5MeV_DC.root')
