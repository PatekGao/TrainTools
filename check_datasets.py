import os

img_path = '/home/stevegao/datasets/images/train/'
label_path = '/home/stevegao/datasets/labels/train/'

img_list = os.listdir(img_path)
label_list = os.listdir(label_path)

for img in img_list:
    if img.split('.')[0] + '.txt' not in label_list:
        print(img + ' is redundancy.')

for label in label_list:
    if label.split('.')[0] + '.jpg' not in img_list:
        print(label + ' is redundancy.')
