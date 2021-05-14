import numpy as np
import os
import SimpleITK as sitk


def sensitivity(seg, ground):
    # compute false negative rate
    num = np.sum(np.multiply(ground, seg))
    denom = np.sum(ground)
    if denom == 0:
        return 1
    else:
        return  num/denom


def specificity(seg, ground):
    # compute false positive rate
    num = np.sum(np.multiply(ground==0, seg==0))
    denom = np.sum(ground==0)
    if denom == 0:
        return 1
    else:
        return num/denom


def sensitivity_whole (seg,ground):
    return sensitivity(seg>0,ground>0)


def sensitivity_en (seg,ground):
    return sensitivity(seg==4,ground==4)


def sensitivity_core (seg,ground):
    seg_=np.copy(seg)
    ground_=np.copy(ground)
    seg_[seg_==2]=0
    ground_[ground_==2]=0
    return sensitivity(seg_>0,ground_>0)


def specificity_whole (seg,ground):
    return specificity(seg>0,ground>0)


def specificity_en (seg,ground):
    return specificity(seg==4,ground==4)


def specificity_core (seg,ground):
    seg_=np.copy(seg)
    ground_=np.copy(ground)
    seg_[seg_==2]=0
    ground_[ground_==2]=0
    return specificity(seg_>0,ground_>0)


def nii_multiply(path_image, path_label):
    image_names = os.listdir(path_image)
    label_names = os.listdir(path_label)
    for image_name, label_name in zip(image_names, label_names):
        # print(image_name)
        # print(label_name)
        image_name_path = os.path.join(path_image, image_name)
        label_name_path = os.path.join(path_label, label_name)
        itk_seg = sitk.ReadImage(image_name_path)
        itk_ground = sitk.ReadImage(label_name_path)

        arr_seg = sitk.GetArrayFromImage(itk_seg)
        arr_ground = sitk.GetArrayFromImage(itk_ground)

        # compute the infer metrics
        Sensitivity_whole = sensitivity_whole(arr_seg, arr_ground)
        Sensitivity_en = sensitivity_en(arr_seg, arr_ground)
        Sensitivity_core = sensitivity_core(arr_seg, arr_ground)

        Specificity_whole = specificity_whole(arr_seg, arr_ground)
        Specificity_en = specificity_en(arr_seg, arr_ground)
        Specificity_core = specificity_core(arr_seg, arr_ground)

        print("**********************************************")
        print("Sensitivity complete tumor score : {:0.4f}".format(Sensitivity_whole))
        print("Sensitivity core tumor score (tt sauf vert): {:0.4f}".format(Sensitivity_core))
        print("Sensitivity enhancing tumor score (jaune):{:0.4f} ".format(Sensitivity_en))
        print("***********************************************")
        print("Specificity complete tumor score : {:0.4f}".format(Specificity_whole))
        print("Specificity core tumor score (tt sauf vert): {:0.4f}".format(Specificity_core))
        print("Specificity enhancing tumor score (jaune):{:0.4f} ".format(Specificity_en))
        print("***********************************************")


if __name__ == '__main__':
    nii_seg = r'D:\1philips_learning\1Steve_TJ\Brain_MRI-AI\HD\BrainMets_predict'
    nii_ground = r'D:\1philips_learning\1Steve_TJ\Brain_MRI-AI\HD\BrainMets_GT'
    nii_multiply(nii_seg, nii_ground)
