# coding:utf-8
import SimpleITK as sitk
import cv2

def dcmtopng(filename,outpath,data):
    ds = sitk.ReadImage(filename)
    print('ds',ds)
    img_array = sitk.GetArrayFromImage(ds)
    print('img_array',img_array)
    for img_item in img_array:
        print('img_item',img_item)
        # cv2.imwrite("%s/%s.png" % (outpath,data.split('.')[0]), img_item)
        pass