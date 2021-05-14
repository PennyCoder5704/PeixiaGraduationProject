import collections
import os
import SimpleITK as sitk
import numpy as np

work_path='D:/philips_learning/kidney_stone/NewData/data'

rowIndex1 = 1

for root,dirs,files in os.walk(work_path):
    for dir_name in dirs:
        main_path = os.path.join(work_path, dir_name)
        ori_name = os.path.join(main_path, 'image.nii.gz')
        # Mask1.nii is gray matter and Mask2.nii is write matter
        mask1_path = os.path.join(main_path, 'mask.nii.gz')

        # 获取Mask1和Mask2中所有的label值
        mask1 = sitk.ReadImage(mask1_path)
#        mask2 = sitk.ReadImage(mask2_path)
        mask1Array = sitk.GetArrayFromImage(mask1)
#        mask2Array = sitk.GetArrayFromImage(mask2)
        values1 = np.unique(mask1Array)
#        values2 = np.unique(mask2Array)

        featureVector = collections.OrderedDict()
        # featureVector['image'] = os.path.basename(ori_name) # Only save the filename of image
        featureVector['image'] = os.path.dirname(ori_name) + '/image.nii.gz' # Save the whole path of image
        # featureVector['mask'] = os.path.basename(mask1_path)
        tmp = mask1Array.copy()
        # print(tmp)
        # for v1 in values1:
        #     if v1 != 0:
                # tmp = mask1Array.copy()
        # 将Mask1中非0的label值都置为1
        tmp[tmp != 0] = 1
        # print(tmp)

        masktmp = sitk.GetImageFromArray(tmp)
        masktmp.CopyInformation(mask1)
        sitk.WriteImage(masktmp, os.path.join(main_path + '/mask_new.nii.gz'))
        mask1_new_path = os.path.join(main_path, 'mask_new.nii.gz')
        featureVector['mask'] = os.path.basename(mask1_new_path)
