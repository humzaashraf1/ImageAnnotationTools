import cv2
import pandas as pd
import os

# Function to display image and wait for key press
def display_image(image_path):
    img = cv2.imread(image_path)
    cv2.imshow('Image', img)
    key = cv2.waitKey(0)
    return key

# Function to process images in a folder
def process_images(folder_path):
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    df_left = pd.DataFrame(columns=['File Path'])
    df_right = pd.DataFrame(columns=['File Path'])

    for image in images:
        image_path = os.path.join(folder_path, image)
        key = display_image(image_path)

        if key == ord('a'):
            df_left = df_left.append({'File Path': image_path}, ignore_index=True)
        elif key == ord('d'):
            df_right = df_right.append({'File Path': image_path}, ignore_index=True)

    cv2.destroyAllWindows()
    return df_left, df_right

# Function to save dataframes to Excel files
def save_to_excel(df, file_name, file_path):
    full_path = os.path.join(file_path, file_name)
    df.to_excel(full_path, index=False)

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    output_path = input("Enter the output folder path: ")

    df_left, df_right = process_images(folder_path)

    left_file_name = 'df_left.xlsx'
    right_file_name = 'df_right.xlsx'

    save_to_excel(df_left, left_file_name, output_path)
    save_to_excel(df_right, right_file_name, output_path)

    print(f"Dataframes saved to {os.path.join(output_path, left_file_name)} and {os.path.join(output_path, right_file_name)}")
