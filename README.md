# Correcting band gaps and band-edge positions of oxide perovskites using DFT and  machine learning

we use DFT and machine learning techniques to correct band gaps and band-edge positions of semiconductors, using a representative subset of ABO3 perovskite oxides as example. Relying on results of HSE06 hybrid functional calculations as target values of band gaps, we find a systematic band gap correction of ~1.5 eV for this class of materials, where ~1 eV comes from downward shifting the valence band and ~0.5 eV from uplifting the conduction band. 

## How to cite

Correspondence and requests for materials should be addressed to Dr. Anderson Janotti or Dr. Bharat Medasani  (janotti@udel.edu, mbkumar@gmail.com, bmedasan@pppl.gov)

### Prerequisites

All the structures and data analysis were carried out using -[Pymatgen](https://pymatgen.org/index.html).

All the machine learning model manipulation were carried out using -[Scikit-Learn Toolbox](https://scikit-learn.org/stable/getting_started.html)


### Data and Models loading

A step by step series of examples that tell you how to get a development env running

Say what the step will be

All the data is stored in .json format

  Example to load binary_oxide_entries.json
```
import json
with open("data/vasprunxml.json", "r") as f:
     data = json.load(f)
```
All the data including material atomic features and perovskites properties are in .pkl and .csv format respectively. The data are loaded in model.ipynb for model training and testing purposes. 

```
data_ele_feature = pd.read_pickle("material_atomic_feature.pkl")
data = pd.read_csv("model_input.csv")
```

model.ipynb includes prediction model training (linear ridge regressor (LRR), kernel ridge regressor (KRR), and the gradient boosted decision tree (GBDT)), feature importance ranking etc. People may refer to the code and intermediate results in model.ipynb for details. 

## Contributing

Please feel free to contact us for further collaborations. 
