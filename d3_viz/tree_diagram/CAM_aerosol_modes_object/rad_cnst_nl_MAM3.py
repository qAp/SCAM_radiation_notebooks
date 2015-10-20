import json


size = 2000

MAM3 = \
{'name': 'Modal aerosol model 3 (MAM3)', 'size': size,
 'children': [
    {'name': 'accum', 'size': size,
     'children': [
    {'name': 'number mixing', 'size': size,
     'children': [
    ]},
    {'name': 'mass mixing'}]},
    {'name': 'aitken', 'size': size},
    {'name': 'coarse', 'size': size}
    ]}


def saveas_file(name = 'noname.json'):
    global MAM3
    with open(name, mode = 'w') as file:
        json.dump(MAM3, file)



if __name__ == '__main__':
    saveas_file(name = 'rad_cnst_nl_MAM3.json')
    
