import os
import numpy as np
import nibabel as nib
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Normalize NIfTI images by clipping values.")
    parser.add_argument("--input_folder", type=str, required=True, help="Path to the input folder containing NIfTI images.")
    parser.add_argument("--output_folder", type=str, required=True, help="Path to the output folder to save normalized images.")
    parser.add_argument("--min_val", type=float, default=-10, help="Minimum value for clipping.")
    parser.add_argument("--max_val", type=float, default=140, help="Maximum value for clipping.")
    return parser.parse_args()

def normalize_nii_images(input_folder, output_folder, min_val=-10, max_val=140):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".nii.gz"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # Load NIfTI image
            nii_image = nib.load(input_path)
            img_data = nii_image.get_fdata()
            
            # Clip values to the specified range
            img_data = np.clip(img_data, min_val, max_val)
            
            # Save processed image
            new_nii = nib.Nifti1Image(img_data, affine=nii_image.affine, header=nii_image.header)
            nib.save(new_nii, output_path)
            
            print(f"Processed: {filename}")

if __name__ == "__main__":
    args = parse_args()
    # Use command line arguments or set default values
    if args.input_folder and args.output_folder:
        input_folder = args.input_folder
        output_folder = args.output_folder
    else:
        # Default values if not provided via command line
        input_folder = "imagesTs"  # Change this to your actual input folder
        output_folder = "imagesTs"  # Change this to your actual output folder
        
    normalize_nii_images(input_folder, output_folder)