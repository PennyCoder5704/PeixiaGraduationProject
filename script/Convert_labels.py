import numpy as np
import SimpleITK as sitk
import os


def convert_labels_back_to_BraTS(seg: np.ndarray):
    new_seg = np.zeros_like(seg)
    new_seg[seg == 1] = 2
    new_seg[seg == 2] = 1
    new_seg[seg == 3] = 4
    return new_seg


path_pre = "D:/1philips_learning/1Steve_TJ/Brain_MRI-AI/2020.1.4_2D_WUHAN_glioma/7thFeb2021_WUHAN_Glioma/inferTs/"
path_convert = "D:/1philips_learning/1Steve_TJ/Brain_MRI-AI/2020.1.4_2D_WUHAN_glioma/7thFeb2021_WUHAN_Glioma/LabelConvert/"

filelist = os.listdir(path_pre)
print(sorted(filelist))

for file in filelist:
    pre = sitk.ReadImage(os.path.join(path_pre, file))
    pre_array = sitk.GetArrayFromImage(pre)

    num = file.split(".nii.gz")[0].split("Brats18")[-1]
    #new_name = "convert" + num + ".nii.gz"
    new_name = num + ".nii.gz"
#    print(new_name)

    convert_label = convert_labels_back_to_BraTS(pre_array)
    convert = sitk.GetImageFromArray(convert_label)
    convert.CopyInformation(pre)
    convert_image = sitk.WriteImage(convert, os.path.join(path_convert, new_name))


