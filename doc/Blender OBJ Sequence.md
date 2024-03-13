# Blender 渲染OBJ序列

## 动机

生成时序`.obj`格式文件，想要更高质量渲染，所以选用Blender。但是Blender自带导入`.obj`格式只能一帧一帧导入，再进行时序编辑效率很低。故想要找到Blender渲染时序`.obj`文件的方法，在Github中找到[neverhood311/Stop-motion-OBJ: A Blender add-on for importing a sequence of OBJ meshes as frames (github.com)](https://github.com/neverhood311/Stop-motion-OBJ)，实际测试后十分符合需求。

## 安装

首先，下载https://github.com/neverhood311/Stop-motion-OBJ/releases/download/v2.1.1/Stop-motion-OBJ-v2.1.1.zip

接着，打开Blender

`编辑`->`偏好设置`<img src="https://image.wjrzm.com/i/2024/03/13/ix5idj-2.png" alt="image-20240313114356007" style="zoom:50%;" />

`插件`->`安装`<img src="https://image.wjrzm.com/i/2024/03/13/iyfspn-2.png" alt="image-20240313114621946" style="zoom:50%;" />

选择下载好的`Stop-motion-OBJ-v2.1.1.zip`<img src="https://image.wjrzm.com/i/2024/03/13/j0xd4l-2.png" alt="image-20240313115040119" style="zoom: 67%;" />，安装插件。

## 使用

`文件`->`导入`->`Mesh Sequence`<img src="https://image.wjrzm.com/i/2024/03/13/j1w3vm-2.png" alt="image-20240313115201756" style="zoom:50%;" />

找到对应的文件夹，在右下角`Sequence Settings`位置文件名处，填写`.obj`文件的前面几个固定的字符（例如文件名格式为`00XXX_0.obj`，XXX为三位递增序号，则填入`00`），`Cache Mode`选`Cached`，接着点击`Select Folder`，等待一会即可导入`.obj`序列。<img src="https://image.wjrzm.com/i/2024/03/13/j4zf2t-2.png" alt="image-20240313115720722" style="zoom: 50%;" />

选中右上角`场景集合`里面的`_sequence`<img src="https://image.wjrzm.com/i/2024/03/13/jvzfyh-2.png" alt="image-20240313120255626" style="zoom:50%;" />

点击下方序列播放按钮，即可进行时序`.obj`格式的预览。后续渲染等工作则正常使用Blender即可。<img src="https://image.wjrzm.com/i/2024/03/13/jwu348-2.png" alt="image-20240313120358955" style="zoom: 50%;" />

