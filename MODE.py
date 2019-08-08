import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode", help="mode to study: psi/X", type=str)
args = parser.parse_args()
if args.mode not in ['psi', 'X']:
    raise argparse.ArgumentTypeError('wrong naming, enter psi or X')

MODE = args.mode
RUN = 2
REGIONS_FROM = 'phi'; SPLOT_FROM = 'Bs'; SPLOT_TO = MODE
REFL_ON = False
REFL_LINE = '_refl' if REFL_ON else ''
CHI2_PVALUE_THRESHOLD = 0.05
# GET_MC_N_EVTS = False
# gStyle.SetTitleFontSize(.085)

if MODE == 'X' and REFL_ON:
    raise Exception('Can\'t use psi reflection model (default) in X mode: change REFL_ON or MODE')

if REFL_ON:
    raise Exception('The reflection option is not implemented and tested properly: \nVerify that the model_Bs is switched with REFL_ON flag and remove this exception')