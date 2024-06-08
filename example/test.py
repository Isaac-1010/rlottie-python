import os
import time
from rlottie_python import LottieAnimation

# List of files to process
files = ["subtitles-fes.json", "subtitles-fe.json", "subtitles-f.json"]

# List to store the results
results = []

for file in files:
    # Record the start time
    start_time = time.time()

    # Create a LottieAnimation object from the file
    anim = LottieAnimation.from_file(f"example/samples/{file}")

    # Get the total number of frames
    frames = anim.lottie_animation_get_totalframe()

    # Create an output directory based on the file name (without .json)
    output_dir = f"example/output/{os.path.splitext(file)[0]}"
    os.makedirs(output_dir, exist_ok=True)

    # Save each frame as a PNG in the output directory
    for i in range(frames):
        anim.save_frame(f"{output_dir}/{i}.png", frame_num=i)

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Store the result
    results.append((file, frames, elapsed_time))

# Print all the results together
for file, frames, elapsed_time in results:
    print(f"File: {file}, Frames: {frames}, Time Taken: {elapsed_time:.2f} seconds")

print("Processing completed.")
