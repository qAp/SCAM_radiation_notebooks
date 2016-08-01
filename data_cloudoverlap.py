import os




URL_BASE = os.path.join('http://nbviewer.jupyter.org/github',
                        'qAp',
                        'SCAM_radiation_notebooks/blob/master')

SITES = ['ARM95', 'MPACE', 'TWPICE']

NBS = {}
for site in SITES:
    site_low = site.lower()
    name_coupled = '{}_rrtmgMcICA_vs_rrtmgMaxRand.ipynb'.format(site_low)
    name_indie = ('{}_LW_rrtmgMcICA_rrtmgMaxRand'
                  '_SW_rrtmgMcICA_rrtmgMaxRand.ipynb').format(site_low)
    NBS[site] = {'coupled': os.path.join(URL_BASE,
                                         site_low,
                                         'study__cloud_overlapping',
                                         name_coupled),
                 'independent': os.path.join(URL_BASE,
                                             site_low,
                                             'study__cloud_overlapping',
                                             name_indie)}
    
    

