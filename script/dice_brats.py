import numpy as np
import SimpleITK as sitk
import os


def dice_coefficient(y_true, y_pred):
    y_true = y_true
    y_pred = y_pred
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = np.sum(y_true_f * y_pred_f)
    return (2. * intersection + 1) / (np.sum(y_true_f) + np.sum(y_pred_f) + 1)


def DSC_whole(orig_label, pred):
    #computes dice for the whole tumor
    return dice_coefficient(orig_label > 0, pred > 0)


def DSC_en(orig_label, pred):
    #computes dice for enhancing region
    return dice_coefficient(orig_label == 4, pred == 4)


def DSC_core(orig_label, pred):
    #computes dice for core region
    seg_ = np.copy(pred)
    ground_ = np.copy(orig_label)
    seg_[seg_==2] = 0
    ground_[ground_==2] = 0
    return dice_coefficient(ground_ > 0, seg_ > 0)


path_gt = "D:/1philips_learning/1Steve_TJ/Brain_MRI-AI/27thFeb2021_Dice/meningeoma/GT"
path_pre = "D:/1philips_learning/1Steve_TJ/Brain_MRI-AI/27thFeb2021_Dice/meningeoma/inferTs"
#txt_path = "D:/philips_learning/1Steve_TJ/Brain_MRI-AI/3DUNet_BraTS_Multi/diceResults"

# dice_txt = open(txt_path + "dice.txt", "w+")
# dice_txt.truncate()

filelist = os.listdir(path_gt)

for file in filelist:
    gt = sitk.ReadImage(os.path.join(path_gt, file))
    gt_array = sitk.GetArrayFromImage(gt)

    #num = file.split(".nii.gz")[0].split("glioma")[-1]
    #new_name = "glioma" + num + ".nii.gz"
    num = file.split(".nii.gz")[0].split("glioma")[-1]
    new_name = num + ".nii.gz"

    pre = sitk.ReadImage(os.path.join(path_pre, new_name))
    pre_array = sitk.GetArrayFromImage(pre)

    Dice_complete = DSC_whole(gt_array, pre_array)
    Dice_enhancing = DSC_en(gt_array, pre_array)
    Dice_core = DSC_core(gt, pre_array)

    print("************************************************************")
    print("Dice complete tumor score : {:0.4f}".format(Dice_complete))
    print("Dice core tumor score (tt sauf vert): {:0.4f}".format(Dice_core))
    print("Dice enhancing tumor score (jaune):{:0.4f} ".format(Dice_enhancing))
    print("**********************************************")

