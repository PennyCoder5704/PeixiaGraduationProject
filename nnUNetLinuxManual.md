1.参考如下链接2，关于nnUNet的训练教程；
2.代码部分：（以下是根据参考教程改动的部分）
①　设置nnUNet读取文件的路径，源代码中通过环境变量设定的方式没成		 功，可直接将路径写入到paths.py中；
②　整理数据集这一步中，按照教程建立好文件夹之后，执行源代码			 dataset_coversion中要处理的数据类型；
③　转换数据集格式这一步中，如果完成了②的步骤，直接修改文件夹名		 字；如：将Task08_HepaticVessel改为Task008_HepaticVessel；
④　推理部分参看链接3，使用predict_simple代码；
⑤　其他部分严格按照参考教程，可以跑通。

参考
1.https://github.com/MIC-DKFZ/nnunet
2.https://blog.csdn.net/weixin_42061636/article/details/107623757?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522160749817319724838557083%252522%25252C%252522scm%252522%25253A%25252220140713.130102334..%252522%25257D&request_id=160749817319724838557083&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-107623757.nonecase&utm_term=nnunet
3.https://blog.csdn.net/weixin_42061636/article/details/107719274?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522160749817319725211958571%252522%25252C%252522scm%252522%25253A%25252220140713.130102334.pc%25255Fall.%252522%25257D&request_id=160749817319725211958571&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-11-107719274.nonecase&utm_term=nnunet