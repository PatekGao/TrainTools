# TrainTools

A repo used for accelerating Neural Network Training Process.  

本训练工具使用的数据集标准为YOLO格式

- check_datasets.py  
本脚本致力于检查数据集，运行本脚本可以确保目标数据集中".jpg"文件与".txt"文件一一对应  
需修改的内容：  
1.img_path=‘您的图片路径’  
2.label_path='您的标注路径'  
- split_train_val.py  
本脚本致力于将数据集划分为训练集与验证集，运行本脚本可以将数据集以一定比例分割开便于训练  
需修改的内容：  
1.image_original_path=‘数据集（图片）的原始路径’  
2.label_original_path=‘数据集（标注）的原始路径’  
3.train_image_path=‘训练集（图片）的目标路径’  
4.train_label_path=‘训练集（标注）的目标路径’  
5.val_image_path=‘验证集（图片）的目标路径’  
6.val_label_path=‘验证集（标注）的目标路径’  
7.（test_image_path=‘测试集（图片）的目标路径’）（optional）  
8.（test_label_path=‘测试集（图片）的目标路径’）（optional)    
9.train_percent=‘训练集的比率（0.x）’  
10.val_percent=‘验证集的比率（0.y）’  
11.（test_percent=‘测试集的比率（0.z）’) (optional)  
{x + y + (z) = 1}
- auto_annotations_v5(v7)  
这两个包致力于自动标注(支持yolov5与yolov7两种神经网络模型)，在提供.pt模型的情况下可以自动生成YOLO格式的标注文件(.txt)，再导入cvat检查并修改后便可以用作新一轮的数据集  
需修改的内容：  
1.在该包的根目录中放入神经网络模型  'best.pt'  
2.在本项目的根目录中的'images'目录中放入需要标注的图片  
3.其他选项可以参照'parser.add_argument'



