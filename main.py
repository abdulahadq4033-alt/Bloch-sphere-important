import numpy as np
import matplotlib.pyplot as plt
import qrcode

# -------------------- Create Bloch Sphere --------------------

phi, theta = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, color='cyan', alpha=0.3, edgecolor='gray')

ax.quiver(0, 0, 0, 1, 0, 0, color='r', linewidth=2)
ax.quiver(0, 0, 0, 0, 1, 0, color='g', linewidth=2)
ax.quiver(0, 0, 0, 0, 0, 1, color='b', linewidth=2)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Bloch Sphere")
ax.set_box_aspect([1, 1, 1])

# Save Bloch Sphere image
plt.savefig("bloch_sphere.png", dpi=300)
plt.close()

# -------------------- QR Code (OPENS PNG) --------------------

image_url = "https://github.com/abdulahadq4033-alt/Bloch-Sphere/bloch_sphere.png"

qr = qrcode.make(image_url)
qr.save("bloch_sphere_qr.png")

print("Bloch Sphere saved as bloch_sphere.png")
print("QR code saved as bloch_sphere_qr.png")
print("QR opens:", image_url)