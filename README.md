# Tensorflowing

## Using the official TensorFlow Docker image

https://hub.docker.com/r/tensorflow/tensorflow/

https://github.com/tensorflow/tensorflow
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/README.md

docker run -it -p 8888:8888 tensorflow/tensorflow
Go to your browser on http://localhost:8888/

## Running it locally

https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html#0

```shell
python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/sw_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=/sw_files/inception \
--output_graph=/sw_files/retrained_graph.pb \
--output_labels=/sw_files/retrained_labels.txt \
--image_dir /sw_files
```

```shell
python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/pkmn_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=/pkmn_files/inception \
--output_graph=/pkmn_files/retrained_graph.pb \
--output_labels=/pkmn_files/retrained_labels.txt \
--image_dir /pkmn_files
```


