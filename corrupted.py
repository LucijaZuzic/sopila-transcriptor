import os
import wave
from settings import ML_MODELS

for i, model in enumerate(ML_MODELS):
    notbroken = 0
    path = "C:\\Users\\Lucija\\Downloads\\sopila-transcriptor-master\\sopila-transcriptor-master\\data\\raw\\" + model["name"]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.wav'):
                full_path = os.path.join(root, file)
                try:
                    with wave.open(full_path, 'r') as f:
                        notbroken += 1
                        pass
                except:
                    print(f"BROKEN FILE FOUND: {full_path}")
    print(model["name"], notbroken)