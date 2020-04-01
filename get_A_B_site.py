from pymatgen.core.periodic_table import Element
import pandas as pd
import json
import numpy as np


element_dic = {}
for element in Element:
    symbol = element.name
    element_dic[symbol] = {}
    for element_property in ['Name','Atomic mass', 'Atomic no', 'Atomic orbitals', 'Atomic radius',
                             #'Atomic radius calculated',
                             #'Coefficient of linear thermal expansion','Density of solid', 'Electrical resistivity','Melting point',
                             # 'Oxidation states',
                             'Common oxidation states',
                             'X'
                             # 'Shannon radii',
                             #'Thermal conductivity','Youngs modulus'
                             # 'Van der waals radius'
                            ]:
        if element_property in element.data:
            element_dic[symbol][element_property] = element.data[element_property]
        else:
            print(element_property, 'not in ', symbol)

data = pd.read_csv('results_cubic.csv',header=None, names=['A','B','O','material', 'vbm_pbe', 'cbm_pbe', 'vbm_k_pbe', 'cbm_k_pbe','vbm_hse', 'cbm_hse', 'gap_diff', 'vb_diff', 'cb_diff'])


df_A_site=pd.DataFrame(columns=['Name','Atomic mass', 'Atomic no', 'Atomic orbitals', 'Atomic radius',
                                'Common oxidation states',
                                # 'Oxidation states',
                                'X'
                                # 'Shannon radii',
                                #'Van der waals radius',
                                ])

for A_site in data['A']:
    A_site_feature_dic={}
    A_site_feature=element_dic[A_site]
    row = pd.Series(A_site_feature)
    df_A_site = df_A_site.append([row])

df_A_site


df_A_site = pd.concat([df_A_site, df_A_site['Atomic orbitals'].apply(pd.Series)], axis = 1).drop('Atomic orbitals', axis = 1)

# df_A_site['Coefficient of linear thermal expansion'] = df_A_site['Coefficient of linear thermal expansion'].str.replace(r'x10<sup>-6</sup>K<sup>-1</sup>', '')
df_A_site['Common oxidation states'] = df_A_site['Common oxidation states'].str[0]
# df_A_site['Density of solid'] = df_A_site['Density of solid'].str.replace(r'kg m<sup>-3</sup>', '')
# df_A_site['Electrical resistivity'] = df_A_site['Electrical resistivity'].str.replace(r'10<sup>-8</sup> &Omega; m', '')
# df_A_site['Electrical resistivity'] = df_A_site['Electrical resistivity'].str.replace(r'about', '')
# df_A_site['Melting point'] = df_A_site['Melting point'].str.replace(r'K', '')
# df_A_site['Thermal conductivity'] = df_A_site['Thermal conductivity'].str.replace(r'W m<sup>-1</sup> K<sup>-1</sup>', '')
# df_A_site['Youngs modulus'] = df_A_site['Youngs modulus'].str.replace(r'GPa', '')
df_A_site = df_A_site.drop(columns=[
                                    # 'Name',
                                    # '1s','2s','2p'
                                    # '4d','4p','4s',
                                    # '4f','5s', '5d', '5p', '6s', '6p'
                                    ])
df_A_site=df_A_site.fillna(0)
df_A_site=df_A_site.replace(['no data', 'no data '], 0)
df_A_site=df_A_site.replace(['(white P) 317.3 '], '317.3')

df_site_list = df_A_site.values.tolist()

outshell_orb_1 = []
outshell_orb_2 = []
for i in range(len(df_site_list)):
    row = df_site_list[i]
    outshell_orb = []
    for j in range(len(row)-1, 0, -1):
        if row[j] != 0:
            outshell_orb.append(row[j])

    outshell_orb_1.append(outshell_orb[0])
    outshell_orb_2.append(outshell_orb[1])

idx_1 = 6
idx_2 = 7

df_A_site.insert(loc=idx_1, column = 'outshell_orb_1', value=outshell_orb_1)
df_A_site.insert(loc=idx_2, column = 'outshell_orb_2', value=outshell_orb_2)
# df_A_site['outshell_orb_1'] = outshell_orb_1
# df_A_site['outshell_orb_2'] = outshell_orb_2


print(df_A_site.columns)
export_result = df_A_site.to_csv("A_site.csv", header=False)
