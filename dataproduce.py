import os
from readdcm import dcmtopng
from PIL import Image

pationts_sir = r'E:\project\Unet&center\B_task\data\data'
pationts = os.listdir(pationts_sir)
print('pationts',pationts)
count1 = 0
count2 = 0
for pationt in pationts:
    dirs = os.listdir(os.path.join(pationts_sir, pationt))
    print('dirs', dirs)
    for dir in dirs:
        datasets = os.listdir(os.path.join(os.path.join(pationts_sir, pationt), dir))
        print('datasets', datasets)
        for data in datasets:
            filepath = os.path.join(os.path.join(os.path.join(pationts_sir, pationt), dir), data)
            print('filepath', filepath)
            if data.split('.')[1] == 'dcm':
                print('data', data)
                dcmtopng(filepath, r'E:\project\Unetdata\data', str(count1) + '.png')
                count1 += 1
            elif data.split('.')[1] == 'png':
                image = Image.open(filepath)
                # image.save(os.path.join(r'E:\project\Unetdata\label',str(count2)+'.png'))
                count2 += 1
