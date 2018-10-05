export CUDA_VISIBLE_DEVICES="1" && python cornell_grasp_train.py --epochs 100 --load_hyperparams '~/datasets/logs/hyperopt_logs_cornell/2018-02-23-09-35-21_-vgg_dense_model-dataset_cornell_grasping-grasp_success/2018-02-23-09-35-21_-vgg_dense_model-dataset_cornell_grasping-grasp_success_hyperparams.json' --kfold_split_type imagewise --load_weights '/media/ahundt/datasets/logs/logs_cornell/2018-02-23-16-35-38_-vgg_dense_model-dataset_cornell_grasping-grasp_success/2018-02-23-16-35-38_-vgg_dense_model-dataset_cornell_grasping-grasp_success-epoch-082-val_loss-0.257-val_binary_accuracy-0.913.h5' --fine_tuning True