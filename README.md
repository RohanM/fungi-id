# Fungi Identifier

Website to identify Australian fungi, backed by a deep learning model trained on photos from iNaturalist.


## Getting Started

Install pipenv:

```
pip install pipenv
```

Install dependencies:

```
pipenv install
```

Build assets:

```
pipenv run assets-dev
# or
pipenv run assets-prod
```

Run the development server:

```
pipenv run server
```

Run tests:

```
pipenv run test
# or
pipenv run test-watch
```


## Fetching images and training the model

This repository comes with a pre-trained model. If you wish to design and train a new model,
notebooks are provided as a starting point.

The data export from iNaturalist is provided in this repository in a CSV file. It refers to
images, which can be fetched using the `notebooks/fetch_images.ipynb` notebook.

Once the images are retrieved, the model can be trained using the `notebooks/train.ipynb`
notebook.


## Dataset

Dataset of Australian fungi exported from https://inaturalist.org.

Image licences as specified in data table (most are CC-BY, CC-BY-NC or CC-BY-NC-SA).


## Licence

Copyright Rohan Mitchell, released under GPL v3 licence.
