# 🔵 Bloch Sphere Visualization with QR Code

This project visualizes a **Bloch Sphere**, a geometric representation of a **single qubit** in quantum computing, using **Python and Matplotlib**.  
It also generates a **QR code** that opens the Bloch Sphere image (`.png`) directly in a web browser.

---

## 📌 What is a Bloch Sphere?

The Bloch Sphere is a unit sphere used to represent the state of a qubit:

## Quantum State Representation (Bloch Sphere)

A general single-qubit quantum state can be written as:

|\psi⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩

### Meaning of each term

- |\psi⟩  
  The quantum state of a single qubit.

- |0⟩, |1⟩  
  The computational basis states.

- θ ∈ [0, π] (polar angle)  
  Controls the probability of measuring |0⟩ or |1⟩.

- φ ∈ [0, 2π) (azimuthal angle)  
  Controls the relative phase between the basis states.

- e^{iφ}  
  A complex phase factor, where i = √(-1).

### Measurement probabilities

P(|0⟩) = cos²(θ/2)  
P(|1⟩) = sin²(θ/2)

P(|0⟩) + P(|1⟩) = 1

### Bloch Sphere Interpretation

The angles θ and φ correspond to a point on the Bloch sphere with coordinates:

x = sinθ cosφ  
y = sinθ sinφ  
z = cosθ

Each point on the sphere represents a unique pure qubit state (up to a global phase).

### Special cases

| State | θ | φ |
|------|---|---|
| |0⟩ | 0 | any |
| |1⟩ | π | any |
| |+⟩ = (|0⟩ + |1⟩)/√2 | π/2 | 0 |
| |-⟩ = (|0⟩ − |1⟩)/√2 | π/2 | π |

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
