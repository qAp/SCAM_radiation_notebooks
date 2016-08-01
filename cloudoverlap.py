import os

import data_cloudoverlap as data



def getHTML_panel_coupled(site='ARM95', tmpl_panel=None,
                          tmpl_table=None, tmpl_link=None):

    rows = [{'reference': 'RTM',
             'model_name': 'RRTMG',
             'sw_overlap_scheme': 'McICA',
             'lw_overlap_scheme': 'McICA'},
            {'reference': 'RTM1',
             'model_name': 'RRTMG',
             'sw_overlap_scheme': 'MaxRand',
             'lw_overlap_scheme': 'MaxRand'}]
    table = tmpl_table.render(rows=rows)

    href = data.NBS[site]['coupled']
    label = 'RTM1 - RTM'
    link = tmpl_link.render(href=href, label=label)

    panel = {}
    panel['body'] = table
    panel['footer'] = link
    html = tmpl_panel.render(panel=panel)
    return html



def getHTML_panel_independent(site='ARM95', tmpl_panel=None,
                              tmpl_table=None, tmpl_link=None):

    rows = [{'reference': 'RTM_MCICA',
             'model_name': 'RRTMG',
             'sw_overlap_scheme': 'McICA',
             'lw_overlap_scheme': 'McICA'}]
    table_mcica = tmpl_table.render(rows=rows)

    rows = [{'reference': 'RTM_MaxRand',
             'model_name': 'RRTMG',
             'sw_overlap_scheme': 'MaxRand',
             'lw_overlap_scheme': 'MaxRand'}]
    table_maxrand = tmpl_table.render(rows=rows)

    href = data.NBS[site]['independent']
    label = 'RTM_MaxRand - RTM_McICA'
    link = tmpl_link.render(href=href, label=label)
    
    panel = {}
    panel['body'] = '\n'.join([table_mcica, table_maxrand])
    panel['footer'] = link
    html = tmpl_panel.render(panel=panel)
    return html



def getHTML_affix(tmpl_affix=None, tmpl_panel=None,
                  tmpl_table=None, tmpl_link=None):
    page_title = 'Cloud Overlapping'
    page_info = '''The maximum-random cloud overlapping scheme used in CLIRAD is incoperated into RRTMG and the result is compared with the McICA scheme.  Each table represents a single execution of RRTMG executable.  Entries in the same table are concurrent runs of RRTMG which share the same input from CAM.  The first entry in the table is the one that sends radiation feedback to CAM at each model time-step.'''
    website_name = 'SCAM radiation notebooks'

    sites = data.SITES

    contents = []
    for site in sites:
        panels = [getHTML_panel_coupled(site=site,
                                        tmpl_panel=tmpl_panel,
                                        tmpl_table=tmpl_table,
                                        tmpl_link=tmpl_link),
                  getHTML_panel_independent(site=site,
                                            tmpl_panel=tmpl_panel,
                                            tmpl_table=tmpl_table,
                                            tmpl_link=tmpl_link)]
        content = '\n'.join(panels)
        contents.append(content)

    html = tmpl_affix.render(page_title=page_title,
                             page_info=page_info,
                             website_name=website_name,
                             name_section_1=sites[0],
                             content_1=contents[0],
                             name_section_2=sites[1],
                             content_2=contents[1],
                             name_section_3=sites[2],
                             content_3=contents[2])
    return html
        



