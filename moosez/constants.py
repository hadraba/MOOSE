#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains the constants that are used in the moosez.

.. moduleauthor:: Lalith Kumar Shiyam Sundar <lalith.shiyamsundar@meduniwien.ac.at>
.. versionadded:: 3.0.0
"""

import os

from moosez import file_utilities

project_root = file_utilities.get_virtual_env_root()

NNUNET_RESULTS_FOLDER = os.path.join(project_root, 'models', 'nnunet_trained_models')
MOOSEZ_MODEL_FOLDER = os.path.join(NNUNET_RESULTS_FOLDER, 'nnUNet', '3d_fullres')
ALLOWED_MODALITIES = ['CT', 'PT', 'MR']
TEMP_FOLDER = 'temp'

# COLOR CODES
ANSI_ORANGE = '\033[38;5;208m'
ANSI_GREEN = '\033[38;5;40m'
ANSI_VIOLET = '\033[38;5;141m'
ANSI_RED = '\033[38;5;196m'
ANSI_RESET = '\033[0m'

# SUPPORTED TRACERS (limited patch)

TRACER_FDG = 'FDG'

# FOLDER NAMES

SEGMENTATIONS_FOLDER = 'segmentations'
STATS_FOLDER = 'stats'

# PREPROCESSING PARAMETERS

MATRIX_THRESHOLD = 200 * 200 * 600
Z_AXIS_THRESHOLD = 200
MARGIN_PADDING = 20
INTERPOLATION = 'bspline'
CHUNK_THRESHOLD = 100

# POSTPROCESSING PARAMETERS

TUMOR_LABEL = 12

# FILE NAMES

RESAMPLED_IMAGE_FILE_NAME = 'resampled_image_0000.nii.gz'
RESAMPLED_MASK_FILE_NAME = 'resampled_mask.nii.gz'
CHUNK_FILENAMES = ["chunk01_0000.nii.gz", "chunk02_0000.nii.gz", "chunk03_0000.nii.gz"]
CHUNK_PREFIX = 'chunk'

# DISPLAY PARAMETERS

MIP_ROTATION_STEP = 40
DISPLAY_VOXEL_SPACING = (3, 3, 3)
FRAME_DURATION = 0.4

# CROPPING WORKFLOWS

LIMIT_FOV_WORKFLOWS ={
    "clin_ct_liver_segments":{
        "model_to_crop_from": "clin_ct_fast_organs",
        "label_intensity_to_crop_from": 8
    },
    "clin_ct_aorta":{
        "model_to_crop_from": "clin_ct_cardiac",
        "label_intensity_to_crop_from": 6
    },
    "clin_ct_body_composition":{
        "model_to_crop_from": "clin_ct_vertebrae",
        "label_intensity_to_crop_from": 22
    }
}

# ORGAN INDICES

ORGAN_INDICES = {
    "clin_ct_organs": {
        1: "adrenal_gland_left",
        2: "adrenal_gland_right",
        3: "bladder",
        4: "brain",
        5: "gallbladder",
        6: "kidney_left",
        7: "kidney_right",
        8: "liver",
        9: "lung_lower_lobe_left",
        10: "lung_lower_lobe_right",
        11: "lung_middle_lobe_right",
        12: "lung_upper_lobe_left",
        13: "lung_upper_lobe_right",
        14: "pancreas",
        15: "spleen",
        16: "stomach",
        17: "thyroid_left",
        18: "thyroid_right",
        19: "trachea"
    },
    "clin_ct_lungs": {
        1: "lung_upper_lobe_left",
        2: "lung_lower_lobe_left",
        3: "lung_upper_lobe_right",
        4: "lung_middle_lobe_right",
        5: "lung_lower_lobe_right"
    },
    "clin_ct_body": {
        1: "Legs",
        2: "Body",
        3: "Head",
        4: "Arms"
    },
    "clin_pt_fdg_tumor": {
        1: "tumor"
    },
    "preclin_mr_all": {
        1: "Brain",
        2: "Liver",
        3: "Intestines",
        4: "Pancreas",
        5: "Thyroid",
        6: "Spleen",
        7: "Bladder",
        8: "OuterKidney",
        9: "InnerKidney",
        10: "HeartInside",
        11: "HeartOutside",
        12: "WAT Subcutaneous",
        13: "WAT Visceral",
        14: "BAT",
        15: "Muscle TF",
        16: "Muscle TB",
        17: "Muscle BB",
        18: "Muscle BF",
        19: "Aorta",
        20: "Lung",
        21: "Stomach",
    },
    "clin_ct_ribs": {
        1: "rib_left_1",
        2: "rib_left_2",
        3: "rib_left_3",
        4: "rib_left_4",
        5: "rib_left_5",
        6: "rib_left_6",
        7: "rib_left_7",
        8: "rib_left_8",
        9: "rib_left_9",
        10: "rib_left_10",
        11: "rib_left_11",
        12: "rib_left_12",
        13: "rib_left_13",
        14: "rib_right_1",
        15: "rib_right_2",
        16: "rib_right_3",
        17: "rib_right_4",
        18: "rib_right_5",
        19: "rib_right_6",
        20: "rib_right_7",
        21: "rib_right_8",
        22: "rib_right_9",
        23: "rib_right_10",
        24: "rib_right_11",
        25: "rib_right_12",
        26: "rib_right_13",
        27: "sternum"
    },
    "clin_ct_muscles": {
        1: "autochthon_left",
        2: "autochthon_right",
        3: "gluteus_maximus_left",
        4: "gluteus_maximus_right",
        5: "gluteus_medius_left",
        6: "gluteus_medius_right",
        7: "gluteus_minimus_left",
        8: "gluteus_minimus_right",
        9: "iliopsoas_left",
        10: "iliopsoas_right"
    },
    "clin_ct_peripheral_bones": {
        1: "carpal_left",
        2: "carpal_right",
        3: "clavicle_left",
        4: "clavicle_right",
        5: "femur_left",
        6: "femur_right",
        7: "fibula_left",
        8: "fibula_right",
        9: "fingers_left",
        10: "fingers_right",
        11: "humerus_left",
        12: "humerus_right",
        13: "metacarpal_left",
        14: "metacarpal_right",
        15: "metatarsal_left",
        16: "metatarsal_right",
        17: "patella_left",
        18: "patella_right",
        19: "radius_left",
        20: "radius_right",
        21: "scapula_left",
        22: "scapula_right",
        23: "skull",
        24: "tarsal_left",
        25: "tarsal_right",
        26: "tibia_left",
        27: "tibia_right",
        28: "toes_left",
        29: "toes_right",
        30: "ulna_left",
        31: "ulna_right"
    },
    "clin_ct_fat": {
        1: "spinal_chord",
        2: "skeletal_muscle",
        3: "subcutaneous_fat",
        4: "visceral_fat",
        5: "thoracic_fat",
        6: "eyes",
        7: "testicles",
        8: "prostate"
    },
    "clin_ct_vertebrae": {
        1: "vertebra_C1",
        2: "vertebra_C2",
        3: "vertebra_C3",
        4: "vertebra_C4",
        5: "vertebra_C5",
        6: "vertebra_C6",
        7: "vertebra_C7",
        8: "vertebra_T1",
        9: "vertebra_T2",
        10: "vertebra_T3",
        11: "vertebra_T4",
        12: "vertebra_T5",
        13: "vertebra_T6",
        14: "vertebra_T7",
        15: "vertebra_T8",
        16: "vertebra_T9",
        17: "vertebra_T10",
        18: "vertebra_T11",
        19: "vertebra_T12",
        20: "vertebra_L1",
        21: "vertebra_L2",
        22: "vertebra_L3",
        23: "vertebra_L4",
        24: "vertebra_L5",
        25: "vertebra_L6",
        26: "hip_left",
        27: "hip_right",
        28: "sacrum"
    },
    "clin_ct_cardiac": {
        1: "heart_myocardium",
        2: "heart_atrium_left",
        3: "heart_atrium_right",
        4: "heart_ventricle_left",
        5: "heart_ventricle_right",
        6: "aorta",
        7: "iliac_artery_left",
        8: "iliac_artery_right",
        9: "iliac_vena_left",
        10: "iliac_vena_right",
        11: "inferior_vena_cava",
        12: "portal_splenic_vein",
        13: "pulmonary_artery"
    },
    "clin_ct_digestive": {
        1: "esophagus",
        2: "trachea",
        3: "small_bowel",
        4: "duodenum",
        5: "colon",
        6: "urinary_bladder",
        7: "face"
    },
    "preclin_ct_legs": {
        1: "right_leg_muscle",
        2: "left_leg_muscle"
    },
    "clin_ct_all_bones_v1": {
        1: "carpal",
        2: "clavicle",
        3: "femur",
        4: "fibula",
        5: "humerus",
        6: "metacarpal",
        7: "metatarsal",
        8: "patella",
        9: "pelvis",
        10: "fingers",
        11: "radius",
        12: "ribcage",
        13: "scapula",
        14: "skull",
        15: "spine",
        16: "sternum",
        17: "tarsal",
        18: "tibia",
        19: "toes",
        20: "ulna"
    },
    "clin_ct_PUMA": {
        0: "background",
        1: "Spleen",
        2: "Kidneys",
        3: "Gallbladder",
        4: "Liver",
        5: "Stomach",
        6: "Pancreas",
        7: "Adrenal_glands",
        8: "Lungs",
        9: "Heart_myocardium",
        10: "Heart_atrium_left",
        11: "Heart_ventricle_left",
        12: "Heart_atrium_right",
        13: "Heart_ventricle_right",
        14: "Pulmonary_artery",
        15: "Aorta",
        16: "Inferior_vena_cava",
        17: "Esophagus",
        18: "Trachea",
        19: "Digestive",
        20: "Brain",
        21: "Skeleton",
        22: "Muscles",
        23: "Bladder"
    },
    "clin_pt_fdg_brain_v1": {
        0: "background",
        1: "R-Hippocampus",
        2: "L-Hippocampus",
        3: "R-Amygdala",
        4: "L-Amygdala",
        5: "R-Anterior-temporal-lobe-medial-part",
        6: "L-Anterior-temporal-lobe-medial-part",
        7: "R-Anterior-temporal-lobe-lateral-part",
        8: "L-Anterior-temporal-lobe-lateral-part",
        9: "R-Parahippocampal-and-ambient-gyri",
        10: "L-Parahippocampal-and-ambient-gyri",
        11: "R-Superior-temporal-gyrus-posterior-part",
        12: "L-Superior-temporal-gyrus-posterior-part",
        13: "R-Middle and inferior temporal gyrus",
        14: "L-Middle and inferior temporal gyrus",
        15: "R-Fusiform gyrus",
        16: "L-Fusiform gyrus",
        17: "R-Cerebellum",
        18: "L-Cerebellum",
        19: "Brainstem",
        20: "L-Insula",
        21: "R-Insula",
        22: "L-Lateral remainder of occipital lobe",
        23: "R-Lateral remainder of occipital lobe",
        24: "L-Cingulate gyrus gyrus cinguli anterior part",
        25: "R-Cingulate gyrus gyrus cinguli anterior part",
        26: "L-Cingulate gyrus gyrus cinguli posterior part",
        27: "R-Cingulate gyrus gyrus cinguli posterior part",
        28: "L-Middle frontal gyrus",
        29: "R-Middle frontal gyrus",
        30: "L-Posterior temporal lobe",
        31: "R-Posterior temporal lobe",
        32: "L-Inferiolateral remainder of parietal lobe",
        33: "R-Inferiolateral remainder of parietal lobe",
        34: "L-Caudate nucleus",
        35: "R-Caudate nucleus",
        36: "L-Nucleus accumbens",
        37: "R-Nucleus accumbens",
        38: "L-Putamen",
        39: "R-Putamen",
        40: "L-Thalamus",
        41: "R-Thalamus",
        42: "L-Pallidum",
        43: "R-Pallidum",
        44: "Corpus callosum",
        45: "R-Lateral ventricle excluding temporal horn",
        46: "L-Lateral ventricle excluding temporal horn",
        47: "R-Lateral ventricle, temporal horn",
        48: "L-Lateral ventricle, temporal horn",
        49: "Third ventricle",
        50: "L-Precentral gyrus",
        51: "R-Precentral gyrus",
        52: "L-Straight gyrus",
        53: "R-Straight gyrus",
        54: "L-Anterior orbital gyrus",
        55: "R-Anterior orbital gyrus",
        56: "L-Inferior frontal gyrus",
        57: "R-Inferior frontal gyrus",
        58: "L-Superior frontal gyrus",
        59: "R-Superior frontal gyrus",
        60: "L-Postcentral gyrus",
        61: "R-Postcentral gyrus",
        62: "L-Superior parietal gyrus",
        63: "R-Superior parietal gyrus",
        64: "L-Lingual gyrus",
        65: "R-Lingual gyrus",
        66: "L-Cuneus",
        67: "R-Cuneus",
        68: "L-Medial orbital gyrus",
        69: "R-Medial orbital gyrus",
        70: "L-Lateral orbital gyrus",
        71: "R-Lateral orbital gyrus",
        72: "L-Posterior orbital gyrus",
        73: "R-Posterior orbital gyrus",
        74: "L-Substantia nigra",
        75: "R-Substantia nigra",
        76: "L-Subgenual frontal cortex",
        77: "R-Subgenual frontal cortex",
        78: "L-Subcallosal area",
        79: "R-Subcallosal area",
        80: "L-Pre-subgenual frontal cortex",
        81: "R-Pre-subgenual frontal cortex",
        82: "L-Superior temporal gyrus anterior part",
        83: "R-Superior temporal gyrus anterior part"
    },
    "clin_ct_ALPACA":{
        1: "heart_ventricle_left",
        2: "heart_ventricle_right",
        3: "pulmonary_artery",
        4: "iliac_artery_left",
        5: "iliac_artery_right",
        6: "aorta"
    },
    "clin_ct_PUMA4": {
        0: "background",
        1: "Spleen",
        2: "Kidneys",
        3: "Gallbladder",
        4: "Liver",
        5: "Stomach",
        6: "Pancreas",
        7: "Adrenal Glands",
        8: "Lungs",
        9: "Heart",
        10: "Vessels",
        11: "Esophagus",
        12: "Trachea",
        13: "Digestive",
        14: "Brain",
        15: "Skeleton",
        16: "Muscles",
        17: "Bladder",
        18: "Filler"
    },
    "clin_fast_organs":{
        1: "adrenal_gland_left",
        2: "adrenal_gland_right",
        3: "bladder",
        4: "brain",
        5: "gallbladder",
        6: "kidney_left",
        7: "kidney_right",
        8: "liver",
        9: "lung_lower_lobe_left",
        10: "lung_lower_lobe_right",
        11: "lung_middle_lobe_right",
        12: "lung_upper_lobe_left",
        13: "lung_upper_lobe_right",
        14: "pancreas",
        15: "spleen",
        16: "stomach",
        17: "thyroid_left",
        18: "thyroid_right",
        19: "trachea"
    },
    "clin_ct_liver_segments":{
        1: "segment_I",
        2: "segment_II",
        3: "segment_III",
        4: "segment_IV",
        5: "segment_V",
        6: "segment_VI",
        7: "segment_VII",
        8: "segment_VIII"
    },
    "clin_ct_aorta":{
        1: "zone_0",
        2: "innominate",
        3: "zone_1",
        4: "left_common_carotid",
        5: "zone_2",
        6: "left_subclavian_artery",
        7: "zone_3",
        8: "zone_4",
        9: "zone_5",
        10: "zone_6",
        11: "celiac_artery",
        12: "zone_7",
        13: "sma",
        14: "zone_8",
        15: "right_renal_artery",
        16: "left_renal_artery",
        17: "zone_9",
        18: "right_common_iliac_artery",
        19: "left_common_iliac_artery",
        20: "right_internal_iliac_artery",
        21: "left_internal_iliac_artery",
        22: "right_external_iliac_artery",
        23: "left_external_iliac_artery"
    }
    # More index-to-name dictionaries for other models...
}
"""

This module contains the constants that are used in the moosez.

Constants are values that are fixed and do not change during the execution of a program. They are used to store values that are used repeatedly throughout the program, such as file paths, folder names, and display parameters.

This module contains the following constants:

- `NNUNET_RESULTS_FOLDER`: A constant that stores the path to the folder that contains the trained models for the nnUNet algorithm.
- `MOOSEZ_MODEL_FOLDER`: A constant that stores the path to the folder that contains the 3D full resolution model for the moosez algorithm.
- `ALLOWED_MODALITIES`: A constant that stores a list of allowed modalities for the moosez algorithm.
- `TEMP_FOLDER`: A constant that stores the name of the temporary folder used by the moosez algorithm.
- `ANSI_ORANGE`: A constant that stores the ANSI color code for orange.
- `ANSI_GREEN`: A constant that stores the ANSI color code for green.
- `ANSI_VIOLET`: A constant that stores the ANSI color code for violet.
- `ANSI_RESET`: A constant that stores the ANSI color code for resetting the color.
- `TRACER_FDG`: A constant that stores the name of the tracer used by the moosez algorithm.
- `SEGMENTATIONS_FOLDER`: A constant that stores the name of the folder that contains the segmentations generated by the moosez algorithm.
- `STATS_FOLDER`: A constant that stores the name of the folder that contains the statistics generated by the moosez algorithm.
- `MATRIX_THRESHOLD`: A constant that stores the matrix threshold used by the moosez algorithm.
- `Z_AXIS_THRESHOLD`: A constant that stores the z-axis threshold used by the moosez algorithm.
- `MARGIN_PADDING`: A constant that stores the margin padding used by the moosez algorithm.
- `INTERPOLATION`: A constant that stores the interpolation method used by the moosez algorithm.
- `CHUNK_THRESHOLD`: A constant that stores the chunk threshold used by the moosez algorithm.
- `TUMOR_LABEL`: A constant that stores the label used for tumors by the moosez algorithm.
- `RESAMPLED_IMAGE_FILE_NAME`: A constant that stores the name of the resampled image file used by the moosez algorithm.
- `RESAMPLED_MASK_FILE_NAME`: A constant that stores the name of the resampled mask file used by the moosez algorithm.
- `CHUNK_FILENAMES`: A constant that stores the names of the chunk files used by the moosez algorithm.
- `CHUNK_PREFIX`: A constant that stores the prefix used for chunk files by the moosez algorithm.
- `MIP_ROTATION_STEP`: A constant that stores the MIP rotation step used by the moosez algorithm.
- `DISPLAY_VOXEL_SPACING`: A constant that stores the display voxel spacing used by the moosez algorithm.
- `FRAME_DURATION`: A constant that stores the frame duration used by the moosez algorithm.
- `ORGAN_INDICES`: A constant that stores a dictionary of index-to-name mappings for various organs used by the moosez algorithm.

This module is imported by other modules in the moosez package and the constants are used throughout the package to provide fixed values that are used repeatedly.
"""
