from rlottie_python import LottieAnimation
from PIL import Image

anim = LottieAnimation.from_file("example/samples/subtitles-fes.json")
# anim = LottieAnimation.from_file("rlottie/example/resource/Text_Test_HELL_3_RangeSelector.json")
frames = anim.lottie_animation_get_totalframe()
print(f"{frames = }")

for i in range(0, frames-1):
    anim.save_frame(f"example/output/test1/{i}.png", frame_num=i)




