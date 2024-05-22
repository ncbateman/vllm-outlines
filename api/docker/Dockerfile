# Use the official Ubuntu image as a parent image
FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu20.04

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
ENV VLLM_NO_USAGE_STATS=1
ENV DO_NOT_TRACK=1

# Update package list and install software-properties-common
RUN apt-get update && \
    apt-get install -y software-properties-common git

# Add deadsnakes PPA and install Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-distutils python3.10-venv

# Install pip using Python 3.10
RUN python3.10 -m ensurepip && \
    python3.10 -m pip install --upgrade pip setuptools wheel

# NVIDIA Libraries for CUDA Support
RUN python3.10 -m pip install nvidia-cublas-cu12==12.1.3.1          # CUDA Basic Linear Algebra Subprograms library
RUN python3.10 -m pip install nvidia-cuda-cupti-cu12==12.1.105      # CUDA Profiling Tools Interface
RUN python3.10 -m pip install nvidia-cuda-nvrtc-cu12==12.1.105      # CUDA Runtime Compilation library
RUN python3.10 -m pip install nvidia-cuda-runtime-cu12==12.1.105    # CUDA Runtime library
RUN python3.10 -m pip install nvidia-cudnn-cu12==8.9.2.26           # NVIDIA CUDA Deep Neural Network library
RUN python3.10 -m pip install nvidia-cufft-cu12==11.0.2.54          # CUDA Fast Fourier Transform library
RUN python3.10 -m pip install nvidia-curand-cu12==10.3.2.106        # CUDA Random Number Generation library
RUN python3.10 -m pip install nvidia-cusolver-cu12==11.4.5.107      # CUDA Solver library for linear algebra
RUN python3.10 -m pip install nvidia-cusparse-cu12==12.1.0.106      # CUDA Sparse Matrix library
RUN python3.10 -m pip install nvidia-nccl-cu12==2.18.1              # NVIDIA Collective Communications Library
RUN python3.10 -m pip install nvidia-nvtx-cu12==12.1.105            # NVIDIA Tools Extension library

# General Utility Libraries
RUN python3.10 -m pip install filelock              # File locking mechanism that provides a simple API
RUN python3.10 -m pip install fsspec                # Filesystem specification interface
RUN python3.10 -m pip install jinja2                # Templating language for Python
RUN python3.10 -m pip install packaging             # Core utilities for Python packages
RUN python3.10 -m pip install pyyaml                # YAML parser and emitter for Python
RUN python3.10 -m pip install regex                 # Regular expression matching operations similar to those found in Perl
RUN python3.10 -m pip install tqdm                  # Fast, extensible progress bar for loops and CLI
RUN python3.10 -m pip install typing-extensions     # Backported and experimental type hints for Python

# Data Handling and Scientific Computing
RUN python3.10 -m pip install networkx              # Python library for studying graphs and networks
RUN python3.10 -m pip install numpy                 # Fundamental package for scientific computing with Python
RUN python3.10 -m pip install sympy                 # Python library for symbolic mathematics

# Machine Learning, AI Frameworks, and Utilities
RUN python3.10 -m pip install huggingface-hub       # Client library to download and publish models on the Hugging Face Hub
RUN python3.10 -m pip install safetensors           # Safe, efficient, and portable serialization format for tensors
RUN python3.10 -m pip install tokenizers            # Fast and customizable text tokenization library
RUN python3.10 -m pip install triton                # Programming language and compiler for neural network accelerators
RUN python3.10 -m pip install torch==2.1.2          # Tensors and Dynamic neural networks in Python with strong GPU acceleration
RUN python3.10 -m pip install accelerate            # PyTorch utility for easy mixed precision and distributed training in Pytorch
RUN python3.10 -m pip install optimum               # Performance optimization tools for transformers
RUN python3.10 -m pip install autoawq               # Quantization Library for AWQ models
RUN python3.10 -m pip install auto-gptq             # Quantization Library for GPTQ models
RUN python3.10 -m pip install outlines              # Guided generation library

# Web Development and APIs
RUN python3.10 -m pip install fastapi               # Modern, fast, web framework for building APIs
RUN python3.10 -m pip install uvicorn               # ASGI server implementation, using uvloop and httptools
RUN python3.10 -m pip install requests              # Elegant and simple HTTP library for Python, built for human beings
RUN python3.10 -m pip install redis                 # Asynchronous task queue/job queue based on distributed message passing  
RUN python3.10 -m pip install celery                # Asynchronous task queue/job queue based on distributed message passing   
RUN python3.10 -m pip install flask                 # Asynchronous task queue/job queue based on distributed message passing  
RUN python3.10 -m pip install flask_socketio        # Asynchronous task queue/job queue based on distributed message passing  
RUN python3.10 -m pip install transformers          # Guided generation library
RUN python3.10 -m pip install vllm
RUN python3.10 -m pip install flash-attn
RUN python3.10 -m pip install ray

# Set working directory
WORKDIR /app

RUN mkdir -p models

# Copy the necessary files from your host to the container
COPY src/ ./src/

# Command to run when the container starts
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
