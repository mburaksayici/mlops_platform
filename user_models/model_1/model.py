#from torchvision.models import resnet50, ResNet50_Weights
from __future__ import annotations

import os
import sys

import numpy as np
import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision.models import vgg16
from torchvision.models import VGG16_Weights


class Model:
    def __init__(self):
        ...

    def load(self, model_url=None):
        weights = VGG16_Weights.DEFAULT
        model = vgg16(weights=weights)
        model.eval()
        self.model = model

    def preprocess(self, image_url):
        img = Image.open(image_url).convert('RGB')
        preprocess = weights.transforms()
        img_batch = preprocess(img)
        img_batch = torch.unsqueeze(img_batch, 0)
        img_batch = torch.tensor(img_batch).float()

        return img_batch

    def predict(self, img_batch):
        return self.model.predict(img_batch)

    def postprocess(prediction):
        return prediction
