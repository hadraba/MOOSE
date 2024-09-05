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

LIMIT_FOV_WORKFLOWS = {
    "clin_ct_liver_segments": {
        "model_to_crop_from": "clin_ct_fast_organs",
        "label_intensity_to_crop_from": 8
    },
    "clin_ct_aorta": {
        "model_to_crop_from": "clin_ct_cardiac",
        "label_intensity_to_crop_from": 6
    },
    "clin_ct_body_composition": {
        "model_to_crop_from": "clin_ct_vertebrae",
        "label_intensity_to_crop_from": 22
    }
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

This module is imported by other modules in the moosez package and the constants are used throughout the package to provide fixed values that are used repeatedly.
"""
