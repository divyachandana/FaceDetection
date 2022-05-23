from pathlib import Path
import random
from tqdm import tqdm
def autosplit():
    weights = (.9,.1)
    path_dir = './training/tello/dataset'
    path_save = './training/tello'
    path = Path(path_dir)
    files = list(path.rglob('*.jpeg'))
    n = len(files)
    indices = random.choices([0,1], weights=weights, k=n)
    txt = ['train.txt', 'test.txt']

    for i, img in tqdm(zip(indices, files), total=n):
        with open(path / txt[i],'a') as f:
            f.write(str(img) + '\n')

autosplit()

