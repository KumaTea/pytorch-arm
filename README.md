# pytorch-arm

[PyTorch][1], [vision][2], [audio][3], [text][4] and [csprng][5] wheels (whl) for **ARM / `armv7l`** devices

**`pip install torch -f https://torch.maku.ml/whl/stable.html`**

---

This repo is for releasing `arm` wheels.

For the readme, scripts and more detailed information, please check the main project: 

## **[pytorch-aarch64][6]**

---

# More Info

* `armv7l` wheels will not be built with `FFmpeg` support, because of its performance.

---

### Environment

Yes, pull an `armv7l` docker image, run it, and you are emulating ARMv7 now.

It's not as fast as using something like `gcc-arm-linux-gnu`, but it's that simple.

> Host: x86
> 
> Target: ARMv7 / `armv7l`
> 
> OS: Debian Buster / 10
> 
> GCC: v8.3.0
> 
> Compiling type: **Cross Compile**
> 
> Virtualization: **Docker**

[1]: https://github.com/pytorch/pytorch
[2]: https://github.com/pytorch/vision
[3]: https://github.com/pytorch/audio
[4]: https://github.com/pytorch/text
[5]: https://github.com/pytorch/csprng
[6]: https://github.com/KumaTea/pytorch-aarch64
