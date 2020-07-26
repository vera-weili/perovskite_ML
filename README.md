# Correcting band gaps and band-edge positions of oxide perovskites using DFT and  machine learning

we use DFT and machine learning techniques to correct band gaps and band-edge positions of semiconductors, using a representative subset of ABO$_3$ perovskite oxides as example. Relying on results of HSE06 hybrid functional calculations as target values of band gaps, we find a systematic band gap correction of $\sim$1.5 eV for this class of materials, where $\sim$1 eV comes from downward shifting the valence band and $\sim$0.5 eV from uplifting the conduction band. The main chemical and structural factors determining the band gap correction are determined through the feature selection procedure. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

All the structures and data analysis were carried out using -Pymatgen.

All the deep learning model manipulation were carried out using

-Scikit-Learn Toolbox

```
Give examples
```

### Data and Models loading

A step by step series of examples that tell you how to get a development env running

Say what the step will be

All the data is stored in .json format

  Example to load binary_oxide_entries.json
```
import json
with open("data/binary_oxide_entries.json", "r") as f:
  data = json.load(f)
```
All the model and scalers are in .h5 and .pkl format respectively. They can be loaded using keras or pickle, or they can be loaded together using garnetdnn.util.load_model_and_scaler

Example to load garnet unmix model and scaler

```
from kears.models import load_model
import pickle
model = load_model("models/garnet/model_unmix.h5")
with open("models/garnet/scaler_unmix.pkl", "rb") as f:
  scaler = pickle.load(f)
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

