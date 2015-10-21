import json


size = 20

MAM3 = \
{'name': 'Modal aerosol model 3 (MAM3)', 'size': size,
 'children': [
    {'name': 'coarse', 'size': size,
     'children': [
        {'name': 'number mixing', 'size': size,
         'children': [
            {'name': 'interstitial', 'size': size},
            {'name': 'cloud-bourne', 'size': size}
            ]
         },
        {'name': 'mass mixing', 'size': size,
         'children': [
            {'name': 'dust', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 'seasalt', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 'sulfate', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             }
            ]
         }
        ]
     },
    {'name': 'aitken', 'size': size,
     'children': [
        {'name': 'number mixing', 'size': size,
         'children': [
            {'name': 'interstitial', 'size': size},
            {'name': 'cloud-bourne', 'size': size}
            ]
         },
        {'name': 'mass mixing', 'size': size,
         'children': [
            {'name': 'sulfate', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 's-organic', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 'seasalt', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             }
            ]
         }
        ]
     },
    {'name': 'accum', 'size': size,
     'children': [
        {'name': 'number mixing', 'size': size,
         'children': [
            {'name': 'interstitial', 'size': size},
            {'name': 'cloud-bourne', 'size': size}
            ]
         },
        {'name': 'mass mixing', 'size': size,
         'children': [
            {'name': 'sulfate', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 'p-organic', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 's-organic', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 'black-c', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 'dust', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             },
            {'name': 'seasalt', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
                ]
             }
            ]
         }
        ]
     },
    {'name': 'MODE TYPE', 'size': size,
     'children': [
        {'name': 'number mixing', 'size': size,
         'children': [
            {'name': 'interstitial', 'size': size},
            {'name': 'cloud-bourne', 'size': size}
            ]
         },
        {'name': 'mass mxing', 'size': size,
         'children': [
            {'name': 'SPECIES', 'size': size,
             'children': [
                {'name': 'interstitial', 'size': size},
                {'name': 'cloud-bourne', 'size': size}
            ]
             }
            ]
         }
        ]
     }
    ]
 }


def saveas_file(name = 'noname.json'):
    global MAM3
    with open(name, mode = 'w') as file:
        json.dump(MAM3, file)



if __name__ == '__main__':
    saveas_file(name = 'rad_cnst_nl_MAM3.json')
    
