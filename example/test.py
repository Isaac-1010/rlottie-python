from rlottie_python import LottieAnimation
from PIL import Image

anim = LottieAnimation.from_file("example/samples/subtitles-fe.json")
# anim = LottieAnimation.from_file("rlottie/example/resource/Text_Test_HELL_3_RangeSelector.json")

# Method 1: Saving the frame to file directly
anim.save_frame("example/output/framefe.png", frame_num=3)


