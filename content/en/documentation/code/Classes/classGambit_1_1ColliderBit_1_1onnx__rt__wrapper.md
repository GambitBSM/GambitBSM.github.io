---
title: "class Gambit::ColliderBit::onnx_rt_wrapper"

description: "[No description available]"

---

# class Gambit::ColliderBit::onnx_rt_wrapper



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[onnx_rt_wrapper](/documentation/code/classes/classgambit_1_1colliderbit_1_1onnx__rt__wrapper/#function-onnx-rt-wrapper)**(const std::string & filename, const std::string & runname ="GambitONNXrt") |
| | **[onnx_rt_wrapper](/documentation/code/classes/classgambit_1_1colliderbit_1_1onnx__rt__wrapper/#function-onnx-rt-wrapper)**() =delete |
| void | **[compute](/documentation/code/classes/classgambit_1_1colliderbit_1_1onnx__rt__wrapper/#function-compute)**(std::vector< std::vector< float > > & inputs, std::vector< std::vector< float > > & outputs) const<br>Given a multi-node input vector, populate and return the multi-node output vector.  |
| void | **[compute](/documentation/code/classes/classgambit_1_1colliderbit_1_1onnx__rt__wrapper/#function-compute)**(std::vector< float > & inputs, std::vector< float > & outputs)<br>Given a single-node input vector, populate and return the single-node output vector.  |

## Friends

|                | Name           |
| -------------- | -------------- |
| std::ostream & | **[operator<<](/documentation/code/classes/classgambit_1_1colliderbit_1_1onnx__rt__wrapper/#friend-operator)**(std::ostream & os, const [onnx_rt_wrapper](/documentation/code/classes/classgambit_1_1colliderbit_1_1onnx__rt__wrapper/) & rort) <br>Printing function for debugging.  |

## Public Functions Documentation

### function onnx_rt_wrapper

```
onnx_rt_wrapper(
    const std::string & filename,
    const std::string & runname ="GambitONNXrt"
)
```


### function onnx_rt_wrapper

```
onnx_rt_wrapper() =delete
```


### function compute

```
void compute(
    std::vector< std::vector< float > > & inputs,
    std::vector< std::vector< float > > & outputs
) const
```

Given a multi-node input vector, populate and return the multi-node output vector. 

Check that number of input nodes matches what the model expects


### function compute

```
void compute(
    std::vector< float > & inputs,
    std::vector< float > & outputs
)
```

Given a single-node input vector, populate and return the single-node output vector. 

## Friends

### friend operator<<

```
friend std::ostream & operator<<(
    std::ostream & os,

    const onnx_rt_wrapper & rort
);
```

Printing function for debugging. 

-------------------------------

Updated on 2026-11-03 at 14:50:43 +0000