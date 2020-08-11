# Correcting band gaps and band-edge positions of oxide perovskites using DFT and  machine learning

We use DFT and machine learning techniques to correct band gaps and band-edge positions of semiconductors, using a representative subset of ABO3 perovskite oxides as example. Relying on results of HSE06 hybrid functional calculations as target values of band gaps, we find a systematic band gap correction of ~1.5 eV for this class of materials, where ~1 eV comes from downward shifting the valence band and ~0.5 eV from uplifting the conduction band. 

## How to cite

Correspondence and requests for materials should be addressed to Dr. Anderson Janotti (janotti@udel.edu), Dr. Bharat Medasani (mbkumar@gmail.com, bmedasan@pppl.gov), or Dr. Sanguthevar Rajasekaran (sanguthevar.rajasekaran@uconn.edu).

### Prerequisites

All the structures and data analysis were carried out using -[Pymatgen](https://pymatgen.org/index.html).

All the machine learning model manipulation were carried out using -[Scikit-Learn Toolbox](https://scikit-learn.org/stable/getting_started.html)


### Data and Models loading

All the data is stored in .json format

  Example to load binary_oxide_entries.json
```
import json
with open("data/vasprunxml.json", "r") as f:
     data = json.load(f)
```
All the data including material atomic features and structural properties are in .pkl and .csv format respectively. The data are loaded in model.ipynb for model training and testing purposes. 

```
data_ele_feature = pd.read_pickle("material_atomic_feature.pkl")
data = pd.read_csv("model_input.csv")
```

model.ipynb includes prediction model training (linear ridge regressor (LRR), kernel ridge regressor (KRR), and the gradient boosted decision tree (GBDT)), feature importance ranking etc. People may refer to the code and intermediate results in model.ipynb for details. 

## Related paper
Correcting band gaps and band-edge positions of oxide perovskites using DFT and machine learning

Wei Li, Zigeng Wang, Xia Xiao, Zhiqiang Zhang, Anderson Janotti, Rajasekaran Sanguthevar & Bharat Medasani

Department of Materials Science and Engineering, University of Delaware 
Computer Science and Engineering Department, University of Connecticut
Department of Physics and Astronomy, University of Delaware
Delaware Energy Institute, University of Delaware
Princeton Plasma Physics Laboratory, Princeton

## Contributing
Please feel free to contact any of the authors for clarifications and possible collaboration

Wei Li (verali@udel.edu)
Zigeng Wang (zigeng.wang@uconn.edu)
Xia Xiao (xia.xiao@uconn.edu)
Zhiqiang Zhang (zhangzq@udel.edu)
Anderson Janotti (janotti@udel.edu)
Rajasekaran Sanguthevar (sanguthevar.rajasekaran@uconn.edu)
Bharat Medasani (mbkumar@gmail.com, bmedasan@pppl.gov)
