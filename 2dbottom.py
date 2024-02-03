import cv2
import numpy as np

# Load the base image
base_img = cv2.imread("base_image.jpg")

# Load the overlay image
overlay_img = cv2.imread("overlay_image.png", cv2.IMREAD_UNCHANGED)

# Get the height and width of both images
base_height, base_width = base_img.shape[:2]
overlay_height, overlay_width = overlay_img.shape[:2]

# Scale the overlay image to match the size of the base image
scaled_overlay = cv2.resize(overlay_img, (base_width, base_height),
                            interpolation = cv2.INTER_AREA)

# Create an alpha channel to control the transparency of the overlay
mask = scaled_overlay[:, :, 3] / 255.0
mask = np.repeat(mask[:, :, np.newaxis], 3, axis=2)

# Perform the overlay by blending the two images
result = cv2.addWeighted(base_img, 1.0, scaled_overlay, 0.7, 0.0)

# Show the result
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
