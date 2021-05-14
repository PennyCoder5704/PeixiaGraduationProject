import  cv2
import nibabel
import numpy as np
from skimage import data,segmentation,measure,morphology,color


# def threshold_image(image):
#     # binarization image
#     ret, thresh = cv2.threshold(image, 170, 255, cv2.THRESH_BINARY)
#     return thresh

def connected_component(image):
    # label the input 3D image
    label, num = measure.label(image, background=0, connectivity=2, return_num=True)
    if num < 1:
        return image

    # get corresponding region
    region = measure.regionprops(label)
    # Get the area of each area and sort it
    num_list = [i for i in range(1, num + 1)]
    area_list = [region[i - 1].area for i in num_list]
    num_list_sorted = sorted(num_list, key=lambda x: area_list[x - 1])[::-1]
    # Remove the connected domain with small area
    if len(num_list_sorted) > 6:
        # for i in range(3, len(num_list_sorted)):
        for i in num_list_sorted[6:]:
            # label[label==i] = 0
            label[region[i - 1].slice][region[i - 1].image] = 0
        num_list_sorted = num_list_sorted[:6]
    return label


def connected_component_2(image):
    # label the input 3D image
    label, num = measure.label(image, background=0, connectivity=2, return_num=True)
    if num < 1:
        return image

    # get corresponding region
    region = measure.regionprops(label)
    # Get the area of each area and sort it
    num_list = [i for i in range(1, num + 1)]
    area_list = [region[i - 1].area for i in num_list]
    num_list_sorted = sorted(num_list, key=lambda x: area_list[x - 1])[::-1]
    # Remove the connected domain with small area
    if len(num_list_sorted) > 5:
        # for i in range(3, len(num_list_sorted)):
        for i in num_list_sorted[5:]:
            # label[label==i] = 0
            label[region[i - 1].slice][region[i - 1].image] = 0
        num_list_sorted = num_list_sorted[:5]
    return label


def connected_component_111(image):
    # label the input 3D image
    label, num = measure.label(image, background=0, connectivity=2, return_num=True)
    if num < 1:
        return image

    # get corresponding region
    region = measure.regionprops(label)
    # Get the area of each area and sort it
    num_list = [i for i in range(1, num + 1)]
    area_list = [region[i - 1].area for i in num_list]
    num_list_sorted = sorted(num_list, key=lambda x: area_list[x - 1])[::-1]
    # Remove the connected domain with small area
    if len(num_list_sorted) > 1:
        # for i in range(3, len(num_list_sorted)):
        for i in num_list_sorted[1:]:
            # label[label==i] = 0
            label[region[i - 1].slice][region[i - 1].image] = 0
        num_list_sorted = num_list_sorted[:1]
    return label

nib_img = nibabel.load('D:/philips_learning/1Steve_TJ/Brain_MRI-AI/2020.1.4_2D_WUHAN_glioma/inferts/LI_ZAO_PING.nii.gz')
img = nib_img.get_fdata()

label = connected_component(img)
label_2 = connected_component_2(img)

label_111 = connected_component_111(img)
#
out_img = nibabel.Nifti1Image(label.astype(np.uint8), nib_img.affine)
out_img.to_filename('D:/philips_learning/1Steve_TJ/Brain_MRI-AI/2020.1.4_2D_WUHAN_glioma/connected_component/LI_ZAO_PING_1.nii.gz')
#
out_img_2 = nibabel.Nifti1Image(label_2.astype(np.uint8), nib_img.affine)
out_img_2.to_filename('D:/philips_learning/1Steve_TJ/Brain_MRI-AI/2020.1.4_2D_WUHAN_glioma/connected_component/LI_ZAO_PING_2.nii.gz')
#
out1 = label - label_2
out2 = label_111

real_out = out1 +   out2
real_out = nibabel.Nifti1Image(real_out.astype(np.uint8), nib_img.affine)

real_out.to_filename('D:/philips_learning/1Steve_TJ/Brain_MRI-AI/2020.1.4_2D_WUHAN_glioma/connected_component/LI_ZAO_PING.nii.gz')



