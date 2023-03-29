## Convert Any Model to TFLite 

## Let's get to the point :

We'll be using [this](https://github.com/onnx/onnx-tensorflow) repo as a part of our project.

The process is simple to :
- convert `onnx` model to tensorflow `pb` model.  
- convert `pb` model to `tflite` model.

## Setup :

```
git clone https://github.com/hiteshhedwig/to-tflite-edge
```

```
git submodule update --init
```

```
./build.sh
```

## Some heads up :
- If you have an onnx model converted from pytorch model. Make sure you exported the onnx model in torch package <= 1.7
- If you face some errors, try and see if you have non-simplified onnx model version. Simplified onnx version gives trouble
- Raise issue if some issue is faced. I'll try my best to help.

## Process :

### ONNX to PB :
```
onnx-tf convert -i "mobilenetv2.onnx" -o  "mobilenetv2.pb"
```

### PB to Tflite:
```
python to_tflite.py "/path/to/pbmodel"

```
