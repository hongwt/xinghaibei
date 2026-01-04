import torch.utils.data as data

from PIL import Image
from torchvision import transforms

myDataset = data.Dataset()
print(myDataset)

img = Image.open('images/ability_racial_avatar.jpg')

toTensor = transforms.ToTensor()
img_tensor = toTensor(img)
print(img_tensor.size())  # 输出: torch.Size([3, H, W])，其中 H 和 W 分别是图像的高度和宽度

transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
normalized_img_tensor = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])(img_tensor)
print(normalized_img_tensor.size())  # 输出: torch.Size([3, H, W