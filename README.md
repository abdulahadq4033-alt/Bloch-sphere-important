# 🔵 Bloch Sphere Visualization with QR Code

This project visualizes a **Bloch Sphere**, a geometric representation of a **single qubit** in quantum computing, using **Python and Matplotlib**.  
It also generates a **QR code** that opens the Bloch Sphere image (`.png`) directly in a web browser.

---

## 📌 What is a Bloch Sphere?

The Bloch Sphere is a unit sphere used to represent the state of a qubit:

\[
|\psi\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle
\]

- **Z-axis** → basis states |0⟩ and |1⟩  
- **X and Y axes** → superposition and phase  
- Any pure qubit state corresponds to a point on the surface of the sphere  

---

## ✨ Features

- 3D Bloch Sphere visualization
- Clearly labeled X, Y, and Z axes
- High-resolution PNG output
- Automatically generated QR code
- QR code opens the Bloch Sphere image in a browser
- Simple and beginner-friendly Python code

---

## 🛠️ Technologies Used

- Python  
- NumPy  
- Matplotlib  
- qrcode (PIL)

---

## 📦 Installation

Install the required dependencies:

```bash
pip install numpy matplotlib qrcode[pil]
