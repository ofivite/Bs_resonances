# TODO: proper docstring for Functions, class implementation

import ROOT
from ROOT import RooFit as RF

def explore(data, model, fit_kwargs, signif_kwargs, id = 1, simple_pull = False, toys_pull = False,  plot_pll = False):
    """
    Explore the distribution with id by

    :param:
    :returns:
    """

    if id not in range(1,5):
        raise IOError('wrong id')
    # c = ROOT.TCanvas("c", "c", 800, 600)


    fit_data(data, model, **fit_kwargs)
    # plot_on_frame(roovar, data, model], '', left[sPlot_from], right[sPlot_from], nbins[sPlot_from], None, False, chi_dict)
    # CMS_tdrStyle_lumi.CMS_lumi( c_sPlot_1, 2, 0 ); c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); # c_sPlot_1.GetFrame().Draw();

    if len(signif_kwargs):
        w = prepare_workspace(data, model, **signif_kwargs)
        asympt_result = asympt_signif(w)
        asympt_result.Print()

################################################################################################################################

def fit_data(data, model, is_extended, is_sum_w2, fix_float, **kwargs):
    """
    Fit some data distribution.
    NB: the corresponding model parameters will be updated after executing

    :param:
    :returns: None
    """

    model.fitTo(data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
    model.fitTo(data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
    for param in fix_float:
        param.setConstant(1)
    model.fitTo(data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
    model.fitTo(data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))
    for param in fix_float:
        param.setConstant(0)
    model.fitTo(data, RF.Extended(is_extended), RF.SumW2Error(is_sum_w2))

################################################################################################################################

def prepare_workspace(data, model, roovar, poi, nuisances, **kwargs):
    w = ROOT.RooWorkspace("w", True)
    Import = getattr(ROOT.RooWorkspace, 'import') # special trick to make things not crush
    Import(w, model)
    mc = ROOT.RooStats.ModelConfig("ModelConfig", w)
    mc.SetPdf(w.pdf(model.GetName()))
    mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(poi)))
    # w.var("N_sig_X").setError(20.)
    mc.SetObservables(ROOT.RooArgSet(w.var(roovar)))
    mc.SetNuisanceParameters(ROOT.RooArgSet(*[w.var(nui) for nui in nuisances]))
    mc.SetSnapshot(ROOT.RooArgSet(w.var(poi)))
    Import(w, mc, 'ModelConfig')
    Import(w, data, 'data')
    return w

################################################################################################################################

def asympt_signif(w):
    """
    Function to calculate one-sided significance for a given in the workspace s+b model using RooStats.AsymptoticCalculator

    :param: w: workspace to open
    :returns: GetHypoTest() object for printing with Print()
    """

    data = w.obj("data")
    #
    sbModel = w.obj("ModelConfig")
    sbModel.SetName("S+B_model")
    poi = sbModel.GetParametersOfInterest().first()
    #
    bModel = sbModel.Clone()
    bModel.SetName("B_only_model")
    oldval = poi.getVal()
    poi.setVal(0)
    bModel.SetSnapshot(ROOT.RooArgSet(poi))
    poi.setVal(oldval)
    #
    ac = ROOT.RooStats.AsymptoticCalculator(data, sbModel, bModel)
    ac.SetOneSidedDiscovery(True)
    as_result = ac.GetHypoTest()
    return as_result
