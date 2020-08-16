"""Module for working with images."""
import cv2

def calc_image_hash(image):
    """Function for calculate hash."""
    resized = cv2.resize(image, (8,8), interpolation = cv2.INTER_AREA) # Resize image
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) # Convert it to black and whit
    avg = gray_image.mean() # Average pixel value
    _, threshold_image = cv2.threshold(gray_image, avg, 255, 0) # Threshold binarization
    # Calculate the hash
    _hash = ""
    for x_coordinate in range(8):
        for y_coordinate in range(8):
            val = threshold_image[x_coordinate, y_coordinate]
            if val == 255:
                _hash = _hash+"1"
            else:
                _hash = _hash+"0"
    return _hash

def compare_image(image1, image2):
    """Compare two hashes."""
    hash1 = calc_image_hash(image1)
    hash2 = calc_image_hash(image2)
    i = 0
    count = 0
    while i < len(hash1):
        if hash1[i] != hash2[i]:
            count += 1
        i += 1
    print(count)
    return count
