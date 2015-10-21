import json

size = 2000

modes = \
{'name': 'modes', 'size': size,
 'children': [
    {'name': 'nmodes', 'size': size},
    {'name': 'names', 'size': size,
     'children': [
        {'name': 'mode 1', 'size': size},
        {'name': 'mode 2', 'size': size},
        {'name': '...', 'size': size}
        ]
     },
    {'name': 'types', 'size': size,
     'children': [
        {'name': 'mode 1', 'size': size},
        {'name': 'mode 2', 'size': size},
        {'name': '...', 'size': size}
        ]
     },
    {'name': 'comps', 'size': size,
     'children': [
        {'name': 'mode 1', size: 'size',
         'children': [
            {'name': 'nspec', 'size': size},
            {'name': 'source_num_a', 'size': size},
            {'name': 'camname_num_a', 'size': size},
            {'name': 'idx_num_a', 'size': size},
            {'name': 'source_num_c', 'size': size},
            {'name': 'camname_num_c', 'size': size},
            {'name': 'idx_num_c', 'size': size},
            {'name': 'source_mmr_a', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]
             },
            {'name': 'camname_mmr_a', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'idx_mmr_a', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'source_mmr_c', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'camname_mmr_c', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'idx_mmr_c', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'type', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'props', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]},
            {'name': 'idx_props', 'size': size,
             'children': [
                {'name': 'species 1', 'size': size},
                {'name': 'species 2', 'size': size},
                {'name': '...', 'size': size}
                ]}
            ]
         },
        {'name': 'mode 2', size: 'size'},
        {'name': '...', size: 'size'}]}
    ]
 }






if __name__ == '__main__':
    with open('modes_object.json', mode = 'w') as file:
        json.dump(modes, file)
