import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

stored_vecs = {}

class EmojiDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.tweets_frame = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.landmarks_frame)

    def __getitem__(self, index):
        if torch.is_tensor(index):
            index = index.tolist()

        sentence = self.tweets_frame.iloc[index, 0]
        words = np.array(sentence.split(" "))
        emoji = self.tweets_frame.iloc[index, 1]

        sample = {'words': words, 'emoji':emoji}
        if self.transform:
            sample = self.transform(sample)

        return sample
    
emoji_dataset = EmojiDataset(csv_file="py_dev.csv")


output_file = open("dataset.dev", "w+")
output_file.write("words,emoji\n")

for sample in emoji_dataset:
    np.set_printoptions(linewidth=np.inf, threshold=np.inf)
    output_file.write(str(sample['words']))
    output_file.write(",")
    output_file.write(str(sample['emoji']))
    output_file.write("\n")
