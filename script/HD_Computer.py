# -*- coding: utf-8 -*-

import numpy as np
import os
import SimpleITK as sitk


def nii_multiply(path_image, path_label):
    image_names = os.listdir(path_image)
    label_names = os.listdir(path_label)
    for image_name, label_name in zip(image_names, label_names):
        # print(image_name)
        # print(label_name)
        image_name_path = os.path.join(path_image, image_name)
        label_name_path = os.path.join(path_label, label_name)
        itk_image = sitk.ReadImage(image_name_path)
        itk_label = sitk.ReadImage(label_name_path)

        #computer HD for whole tumor
        image_arr_whole = sitk.GetArrayFromImage(itk_image)
        label_arr_whole = sitk.GetArrayFromImage(itk_label)

        labelPred_whole = sitk.GetImageFromArray(image_arr_whole, isVector=False)
        labelTrue_whole = sitk.GetImageFromArray(label_arr_whole, isVector=False)

        hausdorffcomputer = sitk.HausdorffDistanceImageFilter()
        hausdorffcomputer.Execute(labelTrue_whole > 0.5, labelPred_whole > 0.5)
        hd_whole = hausdorffcomputer.GetHausdorffDistance()
        HD_whole = '%.3f ' % (hd_whole)
        #print(HD_whole)

        #computer HD for enhance tumor
        image_arr_en = sitk.GetArrayFromImage(itk_image)
        label_arr_en = sitk.GetArrayFromImage(itk_label)
        image_arr_en[image_arr_en == 1] = 0
        image_arr_en[image_arr_en == 2] = 0
        image_arr_en[image_arr_en == 4] = 4

        labelPred_en = sitk.GetImageFromArray(image_arr_en, isVector=False)
        labelTrue_en = sitk.GetImageFromArray(label_arr_en, isVector=False)

        hausdorffcomputer = sitk.HausdorffDistanceImageFilter()
        hausdorffcomputer.Execute(labelTrue_en > 0.5, labelPred_en > 0.5)
        hd_en = hausdorffcomputer.GetHausdorffDistance()
        HD_en = '%.3f ' % (hd_en)

        #computer HD for tumor core
        image_arr_core = sitk.GetArrayFromImage(itk_image)
        label_arr_core = sitk.GetArrayFromImage(itk_label)
        image_arr_core[image_arr_core == 1] = 1
        image_arr_core[image_arr_core == 2] = 0
        image_arr_core[image_arr_core == 4] = 4

        labelPred_core = sitk.GetImageFromArray(image_arr_core, isVector=False)
        labelTrue_core = sitk.GetImageFromArray(label_arr_core, isVector=False)

        hausdorffcomputer = sitk.HausdorffDistanceImageFilter()
        hausdorffcomputer.Execute(labelTrue_core > 0.5, labelPred_core > 0.5)
        hd_core = hausdorffcomputer.GetHausdorffDistance()
        HD_core = '%.3f ' % (hd_core)
        #print(HD_core)

        print("***************************************")
        print("HD whole tumor score : ", HD_whole)
        print("HD enhance tumor score : ", HD_en)
        print("HD tumor core socre : ", HD_core)
        print("*********************************")


if __name__ == '__main__':
    nii_image = r'D:\1philips_learning\1Steve_TJ\Brain_MRI-AI\HD\Meningeoma_predict'
    nii_label = r'D:\1philips_learning\1Steve_TJ\Brain_MRI-AI\HD\Meningeoma_GT'
    nii_multiply(nii_image, nii_label)



