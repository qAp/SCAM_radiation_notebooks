
import os

import jinja2

import metadata_aerosol



template_dir = os.path.join(os.path.dirname(__file__), 'templates')
package_loader = jinja2.PackageLoader('projectpage', 'templates')
jinja_env = jinja2.Environment(loader = package_loader)


def page_index():
    template_index = jinja_env.get_template('index.html')
    
    with open('index.html', mode = 'w', encoding = 'utf-8') as file:
        file.write(template_index.render())


def tablerows_hrefs_2_panel(tables=None, hrefs=None):
    if not (tables and hrefs):
        return

    template_table =  jinja_env.get_template('table_data_model_SW_LW.html')
    template_hrefbutton = jinja_env.get_template('button_href.html')
    
    d = {}
    d['body'] = ' '.join(template_table.render(rows=table)
                         for table in tables)
    d['footer'] = ' '.join(\
        template_hrefbutton.render(href=href['href'], label=href['label'])
                                         for href in hrefs)
    return d

    
def html_aerosol_sw_effects():
    '''
    Returns HTML of Bootstrap panels summarising runs related
    to the effect of including aerosol in shortwave radiation models.
    '''
    template_panel = jinja_env.get_template('panel_body_footer.html')

    # panel: concurrent RTMs
    d_concurrent = metadata_aerosol.sw_concurrent()
    d_concurrent = tablerows_hrefs_2_panel(tables=[d_concurrent['rtms']],
                                               hrefs=d_concurrent['hrefs'])

    # panel: CLIRADs
    d_clirad_aeryes = metadata_aerosol.sw_clirad_aeryes()
    d_clirad_aerno = metadata_aerosol.sw_clirad_aerno()
    d_clirad = tablerows_hrefs_2_panel(tables=[d_clirad_aeryes['rtms'], \
                                               d_clirad_aerno['rtms']],
                                       hrefs=d_clirad_aeryes['hrefs'])

    # panel: RRTMGs
    d_rrtmg_aeryes = metadata_aerosol.sw_rrtmg_aeryes()
    d_rrtmg_aerno = metadata_aerosol.sw_rrtmg_aerno()
    d_rrtmg = tablerows_hrefs_2_panel(tables=[d_rrtmg_aeryes['rtms'], \
                                              d_rrtmg_aerno['rtms']],
                                      hrefs=d_rrtmg_aeryes['hrefs'])

    # render the HTML for each panel
    panels = [d_concurrent, d_clirad, d_rrtmg]
    html_panels = (template_panel.render(panel=panel) for panel in panels)

    html_aerosol_sw = '\n'.join(html_panels)
    
    return html_aerosol_sw


def page_aerosol():
    '''
    Generates string for aerosol.html
    '''
    template_affix = jinja_env.get_template('template_affix.html')

    name_section_1 = 'Shortwave effects'
    html_aerosol_sw = html_aerosol_sw_effects()
    
    html_aerosol = template_affix.render(content_1=html_aerosol_sw,
                                         name_section_1=name_section_1)
    
    with open('aerosol.html', mode = 'w', encoding = 'utf-8') as file:
        file.write(html_aerosol)

        

def keeps():
    template = jinja_env.get_template('table_data_modeal_SW_LW.html')
    print(template.render(rows = [{'reference': 'RTM',
                                   'model_name': 'CLIRAD',
                                   'aerosol_in_sw': 'Yes',
                                   'aerosol_in_lw': 'No'}]))    





if __name__ == '__main__':
    page_index()
    page_aerosol()

