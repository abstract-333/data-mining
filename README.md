# Data Mining Project

## Running on:
* Windows 11

* Python 3.11.4 or higher

## How to run

### Install from git:

#### Using GitFlic:

```shell
$ git clone https://gitflic.ru/project/abstract-333/data-mining.git

$ cd data-mining
```

### Create and activate virutal environment:

```shell
$ python -m venv .venv

$ .\.venv\Scripts\activate
```

### Install dependencies:

```shell
$ pip install -r requirements.txt
```

### Run App:

```shell
$ uvicorn src.app:app --reload
```

### Datasets:
##### Apriori:
Groceries purchase dataset used, around 9836 rows and 171 columns (features).


##### K-NN:
Mushroom dataset, around 54036 rows and 9 columns(features).


