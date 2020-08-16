import difflib
import cv2

# Function for calculate hash
def calc_image_hash(image):
    resized = cv2.resize(image, (8,8), interpolation = cv2.INTER_AREA) # Resize image
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) # Convert it to black and whit
    avg = gray_image.mean() # Average pixel value
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0) # Threshold binarization
    # Calculate the hash
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x,y]
            if val == 255:
                _hash = _hash+"1"
            else:
                _hash = _hash+"0"
    return _hash

# Compare two hashes
def compare_image(image1, image2):
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
