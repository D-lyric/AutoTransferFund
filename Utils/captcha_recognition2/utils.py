"""
This file contains all operations about utilities for using functions using PyTorch

Created by Kunhong Yu
Date: 2020/05/19
"""
import os
import torch as t
from PIL import Image
import torchvision as tv

class Dataset(t.utils.data.Dataset):
    """
    Define data iterator
    """
    def __init__(self,
                 inverse_vocab = None,
                 transform = None,
                 verification = True,
                 extend_format = 'jpg',
                 folder = os.path.join('./data', 'test')):
        """
        Args :
            --inverse_vocab: inversed_vocabulary
            --transform: default is None
            --verification: True or False, True for calculating accuracy, False for only predicting
            --extend_format: default is 'jpg'
            --folder: verification images folder
        """
        super(Dataset, self).__init__()

        # files = os.listdir(folder)
        # files = list(filter(lambda x : x.endswith(extend_format), files))
        # self.files = [os.path.join(folder, file) for file in files]
        #传入指定路径：
        self.files = [folder]
        self.transform = transform
        self.inverse_vocab = inverse_vocab
        self.verification = verification

    def __getitem__(self, index):
    #def __getitem__(self, img_path):
        img_path = self.files[index]
        #1. get label#
        label = t.Tensor([0.])
        if self.verification:
            img_name = img_path.split(os.sep)[-1].split('.')[0]
            label = list(img_name)
            label = [self.inverse_vocab[l] for l in label]
            label = t.Tensor(label)

        #2. get image and convert to gray-scale image#
        img = Image.open(img_path).convert('RGB')
        img = self.transform(img)

        return img, label

    def __len__(self):
        return len(self.files)

def get_dataloader(inverse_vocab,
                   verification = True,
                   extend_format = 'jpg',
                   folder = os.path.join('./data', 'test')):

    """This function is used to get data loader
    Args :
        --inverse_vocab: inversed_vocabulary
        --verification: True or False, True for calculating accuracy, False for only predicting
        --extend_format: default is 'jpg'
        --folder: verification images folder
    return :
        --loader: DataLoader instance
    """
    #Data augmentation#
    transform = tv.transforms.Compose([
        tv.transforms.Grayscale(),
        tv.transforms.Resize((40, 40)),
        tv.transforms.ToTensor(),
    ])
    dataset = Dataset(inverse_vocab = inverse_vocab,
                      transform = transform,
                      verification = verification,
                      extend_format = extend_format,
                      folder = folder)
    loader = t.utils.data.DataLoader(dataset,
                                     shuffle = False,
                                     batch_size = 64,
                                     drop_last = False)

    return loader

def get_preds(outputs):
    """This function is used to get_predictions
    Args :
        --outputs: [a, b, c, d] outputs
    return :
        --preds: predictions labels
    """
    preds = []
    for kk, output in enumerate(outputs):
        pred = t.max(output, dim = 1, keepdim = True)[1]
        if kk == 0:
            preds = pred
        else:
            preds = t.cat((preds, pred), dim = 1)

    return preds