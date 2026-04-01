import cv2

# Read image
img = cv2.imread('road.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges (cracks)
edges = cv2.Canny(gray, 50, 150)

# Save output
cv2.imwrite('output.jpg', edges)
