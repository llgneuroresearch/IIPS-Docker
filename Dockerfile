FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-devel

# Install NNUNETV2
RUN apt update && apt install -y git
RUN pip install nnunetv2==2.4.1 gdown
RUN pip install --upgrade git+https://github.com/FabianIsensee/hiddenlayer.git
RUN pip install blosc2 acvl_utils==0.2
RUN mkdir /input /output /assets

# Download pretrained model
ENV MODEL_URL=https://drive.google.com/file/d/1GMm7ypR3emUL20qE2uRzkthby_vuVqAb/view?usp=sharing
RUN gdown --fuzzy ${MODEL_URL} -O /assets/nnUNetv2_pretrained_model.zip

# Prepare folders for NNUNETV2
WORKDIR /output
ENV nnUNet_results=/assets
ENV nnUNet_raw=/assets
ENV nnUNet_preprocessed=/assets

COPY assets/inference.sh /assets

ENTRYPOINT [ "bash", "/assets/inference.sh" ]