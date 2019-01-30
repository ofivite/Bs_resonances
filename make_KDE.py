from cuts import *
from RooSpace import *


CMS_tdrStyle_lumi.extraText       = "Simulation Preliminary"
CMS_tdrStyle_lumi.setTDRStyle()

wind = 0.015300207788743353
wind_sideband_dist = 0.010200138525828902
mean = 3.6862420523971746

# file_B0_refl = ROOT.TFile('~/Study/Bs_resonances/SimpleFileMC_b715x_0_14000_BdToPsiKstar_wo_phi_match_v6_488_496_1245c8f.root')
file_B0_refl = ROOT.TFile('~/Study/Bs_resonances/B0ToPsiKstar_REFL_dR0p05_a1c59b9.root')

data_B0_refl = ( ROOT.RooDataSet('data_B0_refl', 'data_B0_refl', file_B0_refl.Get('mytree'),
                 ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp),
                   cuts_Bs_MC + '&&' + cuts_phi_MC + '&&' + cuts_control_MC + ' && ' + cuts_pipi[mode])
)

print (data_B0_refl.sumEntries())

var_discr.setMin(5.32); var_discr.setMax(5.42); var_discr.setBins(40)
# PHI_mass_Cjp.setMin(left_phi_MC); PHI_mass_Cjp.setMax(right_phi_MC); PHI_mass_Cjp.setBins(nbins_phi_MC)

###
var_KDE = var_discr
###

B0_refl_SR = ROOT.RooKeysPdf("B0_refl_SR", "B^{0} to #psi(2S)K^{*}(892)^{0} reflection", var_KDE, data_B0_refl.reduce('TMath::Abs(X_mass_Cjp -' + str(mean) + ')<' + str(wind)), ROOT.RooKeysPdf.MirrorBoth, 1.)
B0_refl_SdR = ROOT.RooKeysPdf("B0_refl_SdR", "B0_refl_SdR", var_KDE, data_B0_refl.reduce('TMath::Abs(X_mass_Cjp - ' + str(mean) + ')>' + str(wind + wind_sideband_dist) + ' && TMath::Abs(X_mass_Cjp - ' + str(mean) + ')<' + str(2.*wind + wind_sideband_dist)), ROOT.RooKeysPdf.MirrorBoth, 2)

# w = ROOT.RooWorkspace("w", True)
# Import = getattr(ROOT.RooWorkspace, 'import')
# Import(w, B0_refl_SR)
# Import(w, B0_refl_SdR)
# w.writeToFile('~/Study/Bs_resonances/file_B0_refl_dR0p05_from_a1c59b9_rho1.root')

c_refl = ROOT.TCanvas("c_refl", "c_refl", 800, 600)
plot_on_frame(var_KDE, data_B0_refl.reduce('TMath::Abs(X_mass_Cjp -' + str(mean) + ')<' + str(wind)), B0_refl_SR, 'MC: m(J/#psi#pi^{+}#pi^{#font[122]{\55}}#phi)', var_KDE.getMin(), var_KDE.getMax(), var_KDE.getBins(), plot_phi_param, True)
CMS_tdrStyle_lumi.CMS_lumi( c_refl, 0, 0 );
c_refl.Update(); c_refl.RedrawAxis(); c_refl.GetFrame().Draw();

# c_refl.SaveAs('~/Study/Bs_resonances/B0_psi_Kstar_refl_KDE_rho1.pdf')
