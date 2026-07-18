# 🚗 AI Track: Computer Vision Workspace
Welcome to the Computer Vision Hub! This repository contains the foundational workspace scripts designed to take you from classical image manipulation to deep learning architectures used by industry leaders like Tesla.

---

## 🛠️ Step 1: How to Download and Setup This Project
Follow these commands exactly in your terminal (Windows PowerShell or Mac/Linux Terminal) to copy these files onto your computer and configure your coding environment.

### 1. Clone the Repository
Download a complete copy of this project from GitHub onto your machine:
```bash
git clone https://github.com
```

### 2. Enter the Project Folder
Move your terminal path into the newly downloaded directory:
```bash
cd computer-vision-hub
```

### 3. Open the Workspace in VS Code
Launch Visual Studio Code directly inside this project folder:
```bash
code .
```

### 4. Install the Required Core Libraries
Run this single command inside your VS Code terminal to install all required packages automatically from our snapshot configuration file:
```bash
pip install -r requirements.txt
```


---

## 🗺️ Curriculum Code Walkthrough

### 🔬 Project 1: Digital Canvas Basics (`01_image_basics.py`)
**Goal:** Learn how a computer treats an image as a matrix of raw numbers.

* **What it does:** Generates a pure black image using math, draws a vibrant green target bounding box, overlays telemetry text, and renders it inside a native display window.
* **Core Concept:** 
  * Images are 3D arrays: `(Height, Width, Color Channels)`.
  * OpenCV uses **BGR** (Blue, Green, Red) channel order instead of RGB.
  * The coordinate system origin `(0,0)` sits at the **Top-Left** corner; the Y-axis increases as you move downward.
* **How to run it:**
  ```bash
  python 01_image_basics.py
  ```

### 🛣️ Project 2: Advanced Lane Detection (`02_lane_detection.py`)
**Goal:** Build a classical computer vision image-filtering pipeline to isolate structural highway lane markers.

* **The Pipeline Steps Explained:**
  1. **Grayscale Conversion:** Compresses a 3-channel color image into 1 channel. This removes distracting color data and lowers mathematical complexity so autonomous vehicles can process frames faster.
  2. **Gaussian Blurring:** Functions as a macro-details filter. It smooths out micro-textures like asphalt grain, gravel, and camera sensor static so the system doesn't confuse road roughness with structural lines.
  3. **Canny Edge Detection:** Computes sudden mathematical shifts in pixel brightness. Because noise was blurred out first, it cleanly isolates the true boundaries of the lane markings.
* **How to run it:**
  ```bash
  python 02_lane_detection.py
  ```

### 🤖 Project 3: Deep Learning Acceleration (`03_pytorch_verification.py`)
**Goal:** Verify your hardware environment can process high-speed deep learning matrix math using PyTorch.

* **What it does:** Audits your Python runtime, tests if an NVIDIA GPU (CUDA) is available to mimic Tesla's supercomputing training pipelines, and executes a baseline neural network matrix multiplication test.
* **How to run it:**
  ```bash
  python 03_pytorch_verification.py
  ```

---

## 📊 Understanding Your PyTorch Environment Results

When you run `03_pytorch_verification.py`, you are auditing your computer's machine learning capabilities. Here is how to interpret your terminal output:

### 1. The PyTorch Version Tag
If your version ends in `+cpu`, your environment is configured to run matrix math on your computer's main processor (CPU). This is perfect for learning! If it lists a CUDA version, you are connected to a high-speed graphics card.

### 2. GPU Acceleration: True vs. False
* **True:** Your machine has an active NVIDIA graphics card configured with CUDA drivers. This mimics Tesla's supercomputing server architecture for rapid deep learning training.
* **False:** Your machine is running calculations on the CPU. Do not panic! A CPU handles foundational matrix operations flawlessly for educational projects.

### 3. What is a "Tensor" Matrix?
At the bottom of your script output, you will see a grid of numbers labeled `tensor([[...]])`. 
* A **Tensor** is a multi-dimensional array of numbers utilized by PyTorch.
* The grid you see is the result of a **Matrix Multiplication** calculation.
* This exact mathematical process is the absolute core calculation behind how deep learning neural networks process camera pixels to detect objects in real time.

---

## 🧠 Student Challenges to Test Your Intuition
1. **The Grid Challenge:** In `01_image_basics.py`, try altering the `start_point` and `end_point` variables. Can you move the green box to the bottom-right corner of the canvas?
2. **The Blur Challenge:** In `02_lane_detection.py`, find the `cv2.GaussianBlur` line. Change the kernel size from `(5, 5)` to a massive number like `(25, 25)`. What happens to the edge lines on the right side of the screen? Why does this lower edge detection accuracy?
