import os
import shutil
from settings import ML_MODELS

for i, model in enumerate(ML_MODELS):
    print("Processing %d/%d\n" % (i + 1, len(ML_MODELS)))
    
    if not os.path.isdir("models/" + model["name"]):
        os.makedirs("models/" + model["name"])
    if "mono" in model["name"]:
        model_marker = "single_tones"
    if "poly" in model["name"]:
        model_marker = "combined_tones"
    if not os.path.isdir("data/raw/" + model["name"]):
        for s1 in os.listdir("data/" + model_marker):
            os.makedirs("data/raw/" + model["name"] + "/" + s1)
    for s1 in os.listdir("data/" + model_marker):
        for s2 in os.listdir("data/" + model_marker + "/" + s1):
            shutil.copy("data/" + model_marker + "/" + s1 + "/" + s2, "data/raw/" + model["name"] + "/" + s1 + "/" + s2)
