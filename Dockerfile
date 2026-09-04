FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-devel

# Install NNUNETV2
RUN apt update && apt install -y git
RUN pip install nnunetv2==2.8.1 gdown
RUN pip install --upgrade git+https://github.com/FabianIsensee/hiddenlayer.git
RUN mkdir /input /output /assets

# Download pretrained model
ENV MODEL_URL=https://drive.google.com/file/d/1SvGhxReZe3SbaGfiOrmvjmoVqMxibyW0/view?usp=sharing
RUN gdown ${MODEL_URL} -O /assets/nnUNetv2_pretrained_model.zip

# Prepare folders for NNUNETV2
WORKDIR /output
ENV nnUNet_results=/assets
ENV nnUNet_raw=/assets
ENV nnUNet_preprocessed=/assets

COPY assets/inference.sh /assets
COPY assets/preprocess.py /assets
COPY assets/avnir_iips_banner.py /assets

ENTRYPOINT [ "bash", "/assets/inference.sh" ]