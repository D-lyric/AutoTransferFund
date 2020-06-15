"""
This file contains all operations about building small model using PyTorch

Created by Kunhong Yu
Date: 2020/05/19
"""
import torch as t
from torch.nn import functional as F

class LeNet(t.nn.Module):
    """Define LeNet model"""
    def __init__(self, num_classes = 26, length = 4):
        """
        Args :
            --num_classes: how many outputs classes, default is 26
            --length: how many characters in one image, default is 4
        """
        super(LeNet, self).__init__()

        self.layer1 = t.nn.Sequential(
            t.nn.Conv2d(in_channels = 1, out_channels = 64, kernel_size = 5, stride = 1, padding = 2),
            t.nn.BatchNorm2d(64),
            t.nn.ReLU(inplace = True),
        )

        self.layer2 = t.nn.Sequential(
            t.nn.Conv2d(in_channels = 64, out_channels = 128, kernel_size = 5, stride = 1, padding = 2),
            t.nn.BatchNorm2d(128),
            t.nn.ReLU(inplace = True),
        )

        self.layer3 = t.nn.Sequential(
            t.nn.Conv2d(in_channels = 128, out_channels = 256, kernel_size = 3, stride = 1, padding = 1),
            t.nn.BatchNorm2d(256),
            t.nn.ReLU(inplace = True),
            t.nn.Dropout(0.2),
        )

        self.layer4 = t.nn.Sequential(
            t.nn.Conv2d(in_channels = 256, out_channels = 512, kernel_size = 3, stride = 1, padding = 1),
            t.nn.BatchNorm2d(512),
            t.nn.ReLU(inplace = True),
            t.nn.Dropout(0.2),
        )

        self.fcs = []
        for k in range(length):
            fcs = t.nn.Sequential(
                t.nn.Linear(512, 100),
                t.nn.ReLU(inplace = True),
                t.nn.Linear(100, num_classes),
            )
            self.fcs.append(fcs)

        self.fcs = t.nn.ModuleList(self.fcs)

        self.length = length

    def forward(self, x):
        """
        Args :
            --x: input image tensor
        return :
            --outputs: Python list, each is output for one character
        """
        x1 = self.layer1(x)
        x1 = F.max_pool2d(x1, 2)

        x2 = self.layer2(x1)
        x2 = F.max_pool2d(x2, 2)

        x3 = self.layer3(x2)
        x3 = F.max_pool2d(x3, 2)

        x4 = self.layer4(x3)
        x4 = F.max_pool2d(x4, 2)

        #5. Global Average Pooling#
        x5 = F.adaptive_avg_pool2d(x4, (1, 1))
        #6. FCs#
        x6 = x5.view(x5.size(0), -1)

        outputs = []
        for k in range(self.length):
            output = self.fcs[k](x6)
            outputs.append(output)

        return outputs