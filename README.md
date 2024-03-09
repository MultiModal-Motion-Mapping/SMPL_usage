# Code for using SMPL

## installation

```bash
pip install smplx
pip install trimesh
```

## Essential files

`'data\SMPL_NEUTRAL.pkl'` can be downloaded as follows:

1. https://smpl.is.tue.mpg.de/ In this website, you can sign in and download it.

   <img src="https://image.wjrzm.com/i/2024/03/09/njxx41-2.png" alt="image-20240309142413403" style="zoom: 50%;" /><img src="https://image.wjrzm.com/i/2024/03/09/nk3lsb-2.png" alt="image-20240309142447897" style="zoom: 50%;" />

   rename the file `basicmodel_neutral_lbs_10_207_0_v1.1.0.pkl` to `SMPL_NEUTRAL.pkl`.

2. https://box.nju.edu.cn/f/5fcda3eaa1c64bceb994/ Since **private dissemination does not comply with the SMPL license**, try to use the above download method. **If downloaded this way, please do not distribute the file or link.**

## Visualize mesh

We use trimesh to generate files in obj format. If you want to visualize it, please use [MeshLab](https://www.meshlab.net/).

<img src="https://image.wjrzm.com/i/2024/03/09/no2lbu-2.png" alt="image-20240309143114515" style="zoom: 50%;" />