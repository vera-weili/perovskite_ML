import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import math
import os

np.random.seed(1)

def get_material():
    dirpath = os.getcwd()
    material = os.path.basename(dirpath)
    print(material)
    return [material]


def get_nbands_nele():
    input_file = open("vasprun.xml", "r")

    nbands = 0
    nelect = 0
    for line in input_file:
        if 'name="NBANDS"' in line:
            nbands = int(line.split()[-1][:-4])
        if 'name="NELECT"' in line:
            nelect = int(float(line.split()[-1][:-4]))
            break

    input_file.close()
    return nbands, nelect


def get_eigenvalue():
    input_file = open("vasprun.xml", "r")
    eigen_values = []

    tag = False
    start_tag = '<eigenvalues>'

    for line in input_file:
        if line.strip() == start_tag:
            tag = True
        elif tag:
            if line.strip() == "</eigenvalues>":
                tag = False
                break
            data_list = line.split()
            if data_list[0] == '<r>':
                data_list = [float(element) for element in data_list[1:-1]]
                eigen_values.append(data_list)

    # print(eigen_values)
    input_file.close()
    return eigen_values


def get_vbm_cbm():
    eigenvalues = get_eigenvalue()
    nbands, nele = get_nbands_nele()

    num_kpoint = int(len(eigenvalues)/nbands)
    vbm_position = -math.inf
    cbm_position = math.inf
    vbm_kpoint = 0
    cbm_kpoint = 0

    for kpoint in range(0, num_kpoint):
        eigenvalue_vbm = eigenvalues[kpoint*nbands + nele//2 - 1][0]
        if vbm_position < eigenvalue_vbm:
            vbm_position = eigenvalue_vbm
            vbm_kpoint = kpoint + 1

    for kpoint in range(0, num_kpoint):
        eigenvalue_cbm = eigenvalues[kpoint*nbands + nele//2][0]
        if cbm_position > eigenvalue_cbm:
            cbm_position = eigenvalue_cbm
            cbm_kpoint = kpoint + 1
    print('VBM position:', vbm_position, 'CBM position:', cbm_position, "VBM Kpoints index:", vbm_kpoint, "CBM Kpoints index:", cbm_kpoint)
    return [vbm_position, cbm_position, vbm_kpoint, cbm_kpoint]


def main():
    list_result = get_material() + get_vbm_cbm()
    df = pd.DataFrame()
    row = pd.Series(list_result)
    df = df.append([row])
    export_result = df.to_csv("../results.csv", mode="a", header=False)

if __name__=="__main__":
    main()
