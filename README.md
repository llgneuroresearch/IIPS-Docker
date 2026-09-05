# IIPS-Docker
Docker for IVH-ICH-PHE Segmentation

[![Build Status](https://github.com/llgneuroresearch/IIPS-Docker/actions/workflows/docker.yml/badge.svg)](https://hub.docker.com/r/avnirlab/iips/tags)
![GitHub Release](https://img.shields.io/github/v/release/llgneuroresearch/IIPS-Docker)
[![Documentation](https://img.shields.io/badge/Documentation-blue)](https://avnir-models-documentation.readthedocs.io/models/iips.html)

Docker container for IVH-ICH-PHE Segmentation based on nnU-Net, a self-configuring method for medical image segmentation.

The Dockerfile sets up an environment for running NNUNETV2 with PyTorch and CUDA support. It includes the necessary dependencies and configurations for NNUNETV2.

## Instructions

> [!NOTE]  
> Before using the following command lines. Docker and nvidia-container-toolkit must be installed. (`sudo apt install -y docker.io nvidia-container-toolkit` or `sudo apt install -y docker.io nvidia-docker2`)
> **A CUDA-enabled NVIDIA GPU is strongly recommended**. Also see the [nnU-Net hardware requirements](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/installation_instructions.md?utm_source=chatgpt.com#hardware-requirements-for-inference). CPU inference is not tested and may not work properly.
> If using on a Mac with Apple silicon (arm64), the code must be adapted to be used with Rosetta emulation. Make sure that "Use Rosetta for x86/amd64 emulation on Apple Silicon" is enabled in Docker Desktop settings (Settings → General). 
> ```
> docker pull --platform linux/amd64 avnirlab/iips
> docker run --platform linux/amd64 ... avnirlab/iips
> ```

### Building the Docker Image Manually

To build the Docker image, run the following command in the directory containing the Dockerfile:

```
docker build -t iips:latest .
```

### Pulling the Docker Image from DockerHub

To pull the Docker image, run the following command:

```
docker pull avnirlab/iips:<tag>
```

1. Every time main branch is updated, the CICD builds the Dockerfile and pushes the image to Dockerhub with latest tag, i.e. `avnirlab/iips:latest`

2. Every time a new tag is created, the CICD builds the Dockerfile and pushes the image to Dockerhub with tag name e.g.: `avnirlab/iips:1.0.0`.

### Run inference

After building or pulling the Docker image, you can run inference on your nifti images.

> [!IMPORTANT]  
> If you want to run the inference using CUDA, please use NVIDIA driver 560 or higher and CUDA 12.6 or higher.

- Input

The input consists into a directory containing all your CT scans in Nifti format. Nifti files do not require a specific filename.

```
/project_root
├── input_data/               <-- Your source directory
│   ├── scan_001.nii.gz       (Filenames can be anything)
│   ├── patient_abc.nii       (Uncompressed Nifti works too)
│   ├── trauma_case_v2.nii.gz
│   └── 001_stroke_case.nii
```

- Output

Create an output folder where the ICH, IVH, and PHE segmentation masks will be saved.

- Command line

To run the inference on GPU, run the following command:

```
docker run -ti -v PATH_TO_INPUT:/input -v PATH_TO_OUTPUT:/output -u 0:$(id -g) --gpus all --rm --shm-size 2g avnirlab/iips:latest -device cuda
```

To run the inference on CPU, run the following command:

```
docker run -ti -v PATH_TO_INPUT:/input -v PATH_TO_OUTPUT:/output -u 0:$(id -g) --rm --shm-size 2g avnirlab/iips:latest -device cpu
```

If you're running inference on CPU, you can speed things up by predicting with only a single fold (0–4) using the -f option (e.g., `-f 0`) and/or by using the `--disable_tta` option. These options will theoretically produce slightly less accurate segmentation masks (though we have not thoroughly evaluated the impact on our end).
```
docker run -ti -v PATH_TO_INPUT:/input -v PATH_TO_OUTPUT:/output -u 0:$(id -g) --rm --shm-size 2g avnirlab/iips:latest -device cpu -f 0 --disable_tta
```

PATH_TO_INPUT and PATH_TO_OUTPUT must be absolute paths. See this [issue](https://github.com/llgneuroresearch/IIPS-Docker/issues/2#issuecomment-5499476356) regarding CPU inference.

## Citation

If you use this tool, please cite:

> Wu AN, Portafaix A, Pilon D, et al. Multiclass Segmentation of Intracerebral Hemorrhage, Intraventricular Hemorrhage, and Perihematomal Edema: Public CT Dataset and Benchmark Model. Radiology Advances. 2026;umag036. https://doi.org/10.1093/radadv/umag036

See [CITATION.cff](CITATION.cff) for machine-readable citation metadata.

## Funding 

The development of this tool was supported by the Foundation of the Radiological Society of North America - Seed Grant (RSD2122) and Radiology Research Grant (doi.org/10.69777/299979) from the Fonds de Recherche du Québec en Santé and Fondation de l'Association des Radiologistes du Québec, research funding from the Quebec Bio-Imaging Network (35450), internal funding from the "Support professoral du Departement de radiologie, radio-oncologie et medecine nucleaire" de l'Université de Montréal/Bayer and start-up grants from the Radiology Department Centre Hospitalier de l'Université de Montréal (CHUM) and CHUM Research Center (CRCHUM).

Laurent Létourneau-Guillon is supported by a Clinical Research Scholarship–Junior 1 Salary Award (doi.org/10.69777/311203) from the Fonds de Recherche du Québec en Santé and Fondation de l'Association des Radiologistes du Québec.

The development of the model was enabled in part by support provided by Calcul Québec (calculquebec.ca) and the Digital Research Alliance of Canada (alliancecan.ca).
