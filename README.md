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

Open your terminal and run the following commands to clone the GitHub repository:
```sh
git clone https://github.com/LucijaZuzic/sopila-transcriptor.git
cd sopila-transcriptor
```

*Note: You must have Python 3.5 and conda and pip on your system*

*Note: The requirements - vc=14.1=h21ff451_3 and - vs2015_runtime=15.5.2=3 had to be loosened to - vc=14.1 and - vs2015_runtime*

1. conda env create -f sopila_env.yml --name sopila_env
Different env for using visualization/make_sheets.py due to python v    *   **ersion incompatibility
2. conda env create -f make_sheets_env.yml --name make_sheets_env
3. conda activate sopila_env
4. pip install -r requirements.txt

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

*Note: You must install FFmpeg and include it in the PATH varaible for your operating system.*

*Note: If there are broken files run the following command to fix them: `ffmpeg -f s16le -ar 44100 -ac 1 -i "path\to\files\m3v2\m3v2.wav" "path\to\files\m3v2\m3v2_fixed.wav"`*

*Note: You must set the number of CPU cores available and the number of GPUs available in the secrets.json file.*

# Appendix

This repository is part of a larger project for the automatic transcription of sopila (a traditional Croatian instrument) music.

## Scientific Papers

*   The scientific papers describe the:
    *   ***Sopele*** **music dataset:** [https://doi.org/10.1016/j.dib.2019.104840](https://doi.org/10.1016/j.dib.2019.104840)
    *   **Automatic music transcription for traditional woodwind instruments sopele:** [https://doi.org/10.1016/j.patrec.2019.09.024](https://doi.org/10.1016/j.patrec.2019.09.024)

## Repository Index

*   The repositories include the:
    *   **Web Interface Code:** [https://github.com/LucijaZuzic/sopila_transcriptor_web](https://github.com/LucijaZuzic/sopila_transcriptor_web)
    *   **Android Application:** [https://github.com/LucijaZuzic/SopilaTranscriptor](https://github.com/LucijaZuzic/SopilaTranscriptor)
        *   **Forked from:** [https://github.com/askoki/SopilaTranscriptor](https://github.com/askoki/SopilaTranscriptor)
    *   **Django Backend Server:** [https://github.com/LucijaZuzic/django-sopila](https://github.com/LucijaZuzic/django-sopila)
        *   **Forked from:** [https://github.com/askoki/django-sopila](https://github.com/askoki/django-sopila)
    *   **Machine Learning Model Training:** [https://github.com/LucijaZuzic/sopila-transcriptor](https://github.com/LucijaZuzic/sopila-transcriptor)
        *   **Forked from:** [https://github.com/askoki/sopila-transcriptor](https://github.com/askoki/sopila-transcriptor)

## Machine Learning

The models use `scikit-learn` and default parameters, unless stated otherwise.

*   The transcription is done with the following possible setups:
    *   **Music Type:**
        *   **Polyphonic (Poly):** two instruments (both small and great sopila) - **used in deployment**
        *   **Monophonic (Mono):** a single instrument (small or great sopila)
    *   **Architecture:**
        *   the Random Forest (RF) model - **used in deployment**
        *   a Convolutional Neural Network (CNN)
    *   **Discrete Fourier Transform (DFT):**
        *   with the DFT - **used in deployment**
        *   without the DFT

*   The model parameters were obtained in hyperparameter tuning:
    *   **Poly RF DFT (used in deployment):**
        *   **n_estimators:** 900
        *   **criterion:** Gini
        *   **min_samples_split:** 2
        *   **max_samples_leaf:** 1
        *   **max_features:** auto**
        *   **max_depth:** 80
        *   **bootstrap:** false
    *   **Poly RF:**
        *   **n_estimators:** 1000
        *   **criterion:** Gini
        *   **min_samples_split:** 6
        *   **max_samples_leaf:** 1
        *   **max_features:** auto**
        *   **max_depth:** 60
        *   **bootstrap:** false
    *   **Mono RF DFT:**
        *   **n_estimators:** 1000
        *   **criterion:** entropy
        *   **min_samples_split:** 2
        *   **max_samples_leaf:** 1
        *   **max_features:** auto**
        *   **max_depth:** 60
        *   **bootstrap:** false
    *   **Mono RF:**
        *   **n_estimators:** 900
        *   **criterion:** Gini
        *   **min_samples_split:** 2
        *   **max_samples_leaf:** 1
        *   **max_features:** auto**
        *   **max_depth:** 80
        *   **bootstrap:** false

# Supplementary Links

*   The supplementary links define the:
    *   **Web Interface Access:**
        *   [https://sopilatranscriptorweb.firebaseapp.com/](https://sopilatranscriptorweb.firebaseapp.com/)
    *   **Application Installation Android Package Kit (APK):**
        *   [https://drive.google.com/file/d/1pdoee_afd3XuugroIi6P6vlkh9txp2-h/view?usp=drive_link](https://drive.google.com/file/d/1pdoee_afd3XuugroIi6P6vlkh9txp2-h/view?usp=drive_link)
    *   **Trained Machine Learning Models:**
        *   **Poly RF DFT (used in deployment):** [https://drive.google.com/file/d/1HIAFEaunJomerYyrKrfPycj9OpVPSkuP/view?usp=drive_link](https://drive.google.com/file/d/1HIAFEaunJomerYyrKrfPycj9OpVPSkuP/view?usp=drive_link)
        *   **Poly RF:** [https://drive.google.com/file/d/11_mbaqlTAu3-1QkXD8GqYuaBDI1J5DEP/view?usp=drive_link](https://drive.google.com/file/d/11_mbaqlTAu3-1QkXD8GqYuaBDI1J5DEP/view?usp=drive_link)
        *   **Mono RF DFT:** [https://drive.google.com/file/d/1_fHYT2Ykz4xWumwj4j0yT-wxdwABUEQ9/view?usp=drive_link](https://drive.google.com/file/d/1_fHYT2Ykz4xWumwj4j0yT-wxdwABUEQ9/view?usp=drive_link)
        *   **Mono RF:** [https://drive.google.com/file/d/1UhBfw_QOduRCRDoJjlifEHBBNoOirqUL/view?usp=drive_link](https://drive.google.com/file/d/1UhBfw_QOduRCRDoJjlifEHBBNoOirqUL/view?usp=drive_link)