from rlottie_python import LottieAnimation
from PIL import Image

anim = LottieAnimation.from_file("example/samples/subtitles.json")

# Method 1: Saving the frame to file directly
anim.save_frame("example/output/frame30.png", frame_num=30)


