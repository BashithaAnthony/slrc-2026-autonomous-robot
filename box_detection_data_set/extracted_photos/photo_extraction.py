import cv2
import os

def extract_every_nth_frame(video_path, output_folder, n):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % n == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:06d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"{video_path} → Saved {saved_count} frames out of {frame_count}")


# ---------- LIST OF VIDEOS ----------
video_paths = [
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-082742.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-082928.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-083016.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-083041.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-083152.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-083351.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-083546.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-083732.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-083950.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-084047.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-084139.avi",
    r"C:/Users/user/OneDrive/Desktop/SLRC/Raw_videos/Arena Testing/output_20260315-084511.avi",
]

# ---------- OUTPUT ROOT FOLDER ----------
output_root = r"C:/Users/user/OneDrive/Desktop/SLRC/Extracted_photos/Arena Testing"

# ---------- FRAME INTERVAL ----------
n = 17


# ---------- PROCESS ALL VIDEOS ----------
for video_path in video_paths:

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = os.path.join(output_root, video_name)

    extract_every_nth_frame(video_path, output_folder, 25)
