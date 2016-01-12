


def sw_concurrent():
    rtms = [{'reference': 'RTM', 'model_name': 'RRTMG',
             'aerosol_in_sw': 'yes', 'aerosol_in_lw': 'no'},
            {'reference': 'RTM1', 'model_name': 'RRTMG',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'},
            {'reference': 'RTM2', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'yes', 'aerosol_in_lw': 'no'},
            {'reference': 'RTM3', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_RRTMG_RRTMG_SW_RRTMGaer_RRTMG.ipynb',
              'label': 'RTM - RTM1'},
             {'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_-_LW_RRTMG_SW_RRTMGaer_-_LW_CLIRAD_CLIRAD_SW_CLIRADaer_CLIRAD.ipynb',
              'label': 'RTM2 - RTM3'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def sw_clirad_aeryes():
    rtms = [{'reference': 'RTMyes', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'yes', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_CLIRAD_SW_CLIRAD_vs_LW_CLIRAD_SW_CLIRADaer.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def sw_clirad_aerno():
    rtms = [{'reference': 'RTMno', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_CLIRAD_SW_CLIRAD_vs_LW_CLIRAD_SW_CLIRADaer.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def sw_rrtmg_aeryes():
    rtms = [{'reference': 'RTMyes', 'model_name': 'RRTMG',
             'aerosol_in_sw': 'yes', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_RRTMG_SW_RRTMG_vs_LW_RRTMG_SW_RRTMGaer.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def sw_rrtmg_aerno():
    rtms = [{'reference': 'RTMno', 'model_name': 'RRTMG',
              'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_RRTMG_SW_RRTMG_vs_LW_RRTMG_SW_RRTMGaer.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}


####

def lw_concurrent():
    rtms = [{'reference': 'RTM', 'model_name': 'RRTMG',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'yes'},
            {'reference': 'RTM1', 'model_name': 'RRTMG',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'},
            {'reference': 'RTM2', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'yes'},
            {'reference': 'RTM3', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_RRTMGaer_RRTMG_SW_RRTMG_RRTMG.ipynb',
              'label': 'RTM - RTM1'},
             {'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_-_LW_RRTMGaer_SW_RRTMG_-_LW_CLIRADaer_CLIRAD_SW_CLIRAD_CLIRAD.ipynb',
              'label': 'RTM2 - RTM3'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def lw_clirad_aeryes():
    rtms = [{'reference': 'RTMyes', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'yes'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_CLIRAD_SW_CLIRAD_vs_LW_CLIRADaer_SW_CLIRAD.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def lw_clirad_aerno():
    rtms = [{'reference': 'RTMno', 'model_name': 'CLIRAD',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_CLIRAD_SW_CLIRAD_vs_LW_CLIRADaer_SW_CLIRAD.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def lw_rrtmg_aeryes():
    rtms = [{'reference': 'RTMyes', 'model_name': 'RRTMG',
             'aerosol_in_sw': 'no', 'aerosol_in_lw': 'yes'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_RRTMG_SW_RRTMG_vs_LW_RRTMGaer_SW_RRTMG.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}


def lw_rrtmg_aerno():
    rtms = [{'reference': 'RTMno', 'model_name': 'RRTMG',
              'aerosol_in_sw': 'no', 'aerosol_in_lw': 'no'}]
    hrefs = [{'href': 'http://nbviewer.ipython.org/github/qAp/SCAM_radiation_notebooks/blob/master/arm95_LW_RRTMG_SW_RRTMG_vs_LW_RRTMGaer_SW_RRTMG.ipynb',
              'label': 'RTMyes - RTMno'}]
    return {'rtms': rtms, 'hrefs': hrefs}
