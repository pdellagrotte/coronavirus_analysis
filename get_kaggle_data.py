import kaggle
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Download Coronovirus-Dataset from Kaggle, save to project/data directory
def get_data():
    kaggle.api.authenticate() # keys stored in ~/.kaggle directory - see Kaggle docs
    kaggle.api.dataset_download_files('kimjihoo/coronavirusdataset',
                                      path=ROOT_DIR + "/data", unzip=True)

get_data()