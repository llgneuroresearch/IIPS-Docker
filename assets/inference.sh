#! /bin/sh

# This script is used to run inference on a trained model.

python3 /assets/avnir_iips_banner.py

nnUNetv2_install_pretrained_model_from_zip /assets/nnUNetv2_pretrained_model.zip
python3 /assets/preprocess.py --input_folder /input --output_folder /preprocessed

for file in /preprocessed/*; do
    if [ "${file##*_}" != "0000.nii.gz" ]; then
        mv "$file" "${file%.nii.gz}_0000.nii.gz"
    fi
done

nnUNetv2_predict -i /preprocessed -o /output/results -d 003 -c 3d_fullres $@
