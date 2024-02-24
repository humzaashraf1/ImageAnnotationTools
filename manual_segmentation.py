import cv2
import numpy as np
import os

class PolygonDrawer:
    def __init__(self, image):
        self.image = image.copy()
        self.drawing = False
        self.polygon = []

    def draw(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.polygon = [(x, y)]
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.polygon.append((x, y))
            self.draw_polygon()
        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.polygon.append((x, y))
            self.draw_polygon()

    def draw_polygon(self):
        temp_image = self.image.copy()
        if len(self.polygon) > 1:
            cv2.polylines(temp_image, [np.array(self.polygon)], isClosed=False, color=(255, 255, 255), thickness=2)
        cv2.imshow("Draw Mask", temp_image)

def draw_freehand_polygon(image):
    drawer = PolygonDrawer(image)

    cv2.namedWindow("Draw Mask")
    cv2.setMouseCallback("Draw Mask", drawer.draw)

    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == 13:  # Enter key
            break

    cv2.destroyWindow("Draw Mask")

    mask = np.zeros_like(image, dtype=np.uint8)
    if drawer.polygon:
        polygon = np.array(drawer.polygon, dtype=np.int32)
        polygon = polygon.reshape((-1, 1, 2))
        cv2.fillPoly(mask, [polygon], 255)

    return mask

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is not None:
            mask = draw_freehand_polygon(image)
            mask_path = os.path.join(output_folder, image_file)
            cv2.imwrite(mask_path, mask)

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing images: ")
    output_folder = input("Enter the path to the output folder for masks: ")

    main(input_folder, output_folder)
