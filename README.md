sopila-transcriptor
==============================

Automated music processing of traditional Croatian instrument - sopila

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── real_pieces    <- Data for transciption of real music pieces.
    │   ├── combined_tones <- Data for combined two instruments.
    │   ├── single_tones   <- Data for a single instrument.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │   └── sheets         <- Generated PDF music sheet predictions
    │   └── statistics     <- Accuracy, precision, recall and F1 score for training, validation and test data.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    |   |   ├── make_alternate_data.py
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   ├── create_processed_data              <- Creates processed data for all models
    │   │   ├── create_processed_data_mono         <- Creates processed data for mono models
    │   │   ├── create_processed_data_cnn          <- Creates processed data for cnn models
    │   │   ├── create_processed_data_rf_poly_only <- Creates processed data for the rf poly model
    │   │   ├── create_processed_data_other_rf     <- Creates processed data for other rf models
    │   │   ├── create_processed_data_other_poly   <- Creates processed data for other poly models
    │   │   └── alternate_data_create.py <- Creates processed real music recording for model prediction
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    |   |   ├── rf         <- Random forest train and predict scripts
    │   │   └── cnn        <- Convolutional Neural Network train and predict scripts
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── make_sheets.py
    │
    ├── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
    └── settings.py        <- Project specific settings
    └── corrupted.py       <- Check for corrupted .wav files in the data
    └── new_divide.py      <- Run before processing data to copy the raw data for each model


--------
Environment instructions:

*Note: You must have Python 3.5 and conda and pip on your system*

*Note: The requirements - vc=14.1=h21ff451_3 and - vs2015_runtime=15.5.2=3 had to be loosened to - vc=14.1 and - vs2015_runtime*

1. conda env create -f sopila_env.yml --name sopila_env
Different env for using visualization/make_sheets.py due to python version incompatibility
2. conda env create -f make_sheets_env.yml --name make_sheets_env
3. conda activate sopila_env
4. pip install -r requirements.txt

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

*Note: You must install FFmpeg and include it in the PATH varaible for your operating system.*

*Note: If there are broken files run the following command to fix them: `ffmpeg -f s16le -ar 44100 -ac 1 -i "path\to\files\m3v2\m3v2.wav" "path\to\files\m3v2\m3v2_fixed.wav"`*

*Note: You must set the number of CPU cores available and the number of GPUs available in the secrets.json file.*
