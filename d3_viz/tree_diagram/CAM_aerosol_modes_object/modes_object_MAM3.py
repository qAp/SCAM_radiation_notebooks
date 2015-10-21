import json

size = 2000

modes = \
{'name': 'modes (MAM3)', 'size': size,
 'children': [
    {'name': 'nmodes = 3', 'size': size},
    {'name': 'names', 'size': size,
     'children': [
        {'name': '1: mam3_mode1', 'size': size},
        {'name': '2: mam3_mode2', 'size': size},
        {'name': '3: mam3_mode3', 'size': size}
        ]
     },
    {'name': 'types', 'size': size,
     'children': [
        {'name': '1: accum', 'size': size},
        {'name': '2: aitken', 'size': size},
        {'name': '3: coarse', 'size': size}
        ]
     },
    {'name': 'comps', 'size': size,
     'children': [
        {'name': '1:', size: 'size',
         'children': [
            {'name': 'nspec = 6', 'size': size},
            {'name': 'source_num_a = A', 'size': size},
            {'name': 'camname_num_a = num_a1', 'size': size},
            {'name': 'idx_num_a', 'size': size},
            {'name': 'source_num_c = N', 'size': size},
            {'name': 'camname_num_c = num_c1', 'size': size},
            {'name': 'idx_num_c', 'size': size},
            {'name': 'source_mmr_a', 'size': size,
             'children': [
                {'name': '1: A', 'size': size},
                {'name': '2: A', 'size': size},
                {'name': '3: A', 'size': size},
                {'name': '4: A', 'size': size},
                {'name': '5: A', 'size': size},
                {'name': '6: A', 'size': size}
                ]},
            {'name': 'camname_mmr_a', 'size': size,
             'children': [
                {'name': '1: so4_a1', 'size': size},
                {'name': '2: pom_a1', 'size': size},
                {'name': '3: soa_a1', 'size': size},
                {'name': '4: bc_a1', 'size': size},
                {'name': '5: dst_a1', 'size': size},
                {'name': '6: ncl_a1', 'size': size}
                ]
             },
            {'name': 'idx_mmr_a', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'source_mmr_c', 'size': size,
             'children': [
                {'name': '1: N', 'size': size},
                {'name': '2: N', 'size': size},
                {'name': '3: N', 'size': size},
                {'name': '4: N', 'size': size},
                {'name': '5: N', 'size': size},
                {'name': '6: N', 'size': size}
                ]
             },
            {'name': 'camname_mmr_c', 'size': size,
             'children': [
                {'name': '1: so4_c1', 'size': size},
                {'name': '2: pom_c1', 'size': size},
                {'name': '3: soa_c1', 'size': size},
                {'name': '4: bc_c1', 'size': size},
                {'name': '5: dst_c1', 'size': size},
                {'name': '6: ncl_c1', 'size': size}
                ]
             },
            {'name': 'idx_mmr_c', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'type', 'size': size,
             'children': [
                {'name': '1: sulfate', 'size': size},
                {'name': '2: p-organic', 'size': size},
                {'name': '3: s-organic', 'size': size},
                {'name': '4: black-c', 'size': size},
                {'name': '5: dust', 'size': size},
                {'name': '6: seasalt', 'size': size}
                ]
             },
            {'name': 'props', 'size': size,
             'children': [
                {'name': '1: sulfate_rrtmg_c080918.nc', 'size': size},
                {'name': '2: ocpho_rrtmg_c101112.nc', 'size': size},
                {'name': '3: ocphi_rrtmg_c100508.nc', 'size': size},
                {'name': '4: bcpho_rrtmg_c100508.nc', 'size': size},
                {'name': '5: dust4_rrtmg_c090521.nc', 'size': size},
                {'name': '6: ssam_rrtmg_c100508.nc', 'size': size}
                ]
             },
            {'name': 'idx_props', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]}
            ]
         },
        {'name': '2:', size: 'size'},
        {'name': '3:', size: 'size'}]}
    ]
 }






if __name__ == '__main__':
    with open('modes_object_MAM3.json', mode = 'w') as file:
        json.dump(modes, file)
