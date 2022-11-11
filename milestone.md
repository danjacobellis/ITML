# Compressed Learning

[original proposal](https://danjacobellis.net/ITML/_static/proposal.pdf)

## Lossy compression standards

While hundereds of lossy compression techniques have been standardized, only a few have been widely deployed. We will put aside inter-frame video compression for now and focus on audio, image, and intra-frame video compression since our goal is to exploit the transform and quantization steps.

| Standard       | Introduced | Signal | Transform         | Quantization                   |
|----------------|------------|--------|-------------------|--------------------------------|
| MPEG Layer III | 1991       | Audio  | block DCT and FFT | Perceptual quantization vector |
| JPEG           | 1992       | Image  | block DCT         | Perceptual quantization matrix |
| JPEG 2000      | 2000       | Image  | Separable Wavelet | Scalar quantization            |
| CELT/Opus      | 2011       | Audio  | block DCT         | Pyramid vector quantization    |
| HEVC           | 2013       | Image  | block DCT and DST | Perceptual quantization matrix |
| Soundstream    | 2021       | Audio  | Learned           | Residual vector quantization   |

</center> Table 1. Summary of transform and quantization techniques used in some lossy compression standards. </center>

### Transforms

The block DCT and its variants dominate among commonly used codecs. Some notable exceptions are:

* JPEG 2000 (which is the standard for digital cinema where inter-frame compression is forbidden). The separable wavelet transform used in JPEG 2000 still suffers many of the sample limitations of DCT-based transforms. Although complex wavelet transforms allow sparse representations of singularities or oriented components, none have become popular for lossy compression.
* Low rate speech codecs focus on modeling properties of human voice (pitch, formants, etc) but are not suitable for other types of signals like music.
* Emerging standards which use learned transforms. Soundstream (Google) and Encodec (META), based on the vector quantized VAE, have recently become standardized. It's possible that learned image and video codecs will soon become standardized as well.

### Quantization

Tthe dominant approach to quantization is to define a perceptual quantization matrix (or vector) $Q$ and perform the simple quantization $B = round(\frac{G}{Q})$, where $G$ is the transformed signal and $B$ is the quantizated representation.

However, variants of vector quantization are now being deployed in standards:

* CELT (now integrated into the OPUS standard) normalizes transform coefficients to one, then separately codes the unit vector from the magnitude. This allows the use of pyramid vector quantization which is much more efficient but only applicable to unit vectors.
* Soundstream uses several low-complexity vector quantizers, each predicting the residual of the previous.

## Why integrate compression and learning?

Consider the task of image classification and the original AlexNet architecture. Strided convolutional layers and pooling reduce the dimensionalty from 224x224x3 at the input to feature maps of size 3x3x256 at the output. This reduction in size greatly reduces the cost of learning the fully connected layers which predict the image class. All values are represented as 32-bit floating point during training, so the convolutional layers increase the density of class related in



## Approaches to integrating compression and learning

A core challenge to learning from compressed data is that, in the conventional approach to DNN optimization, all input samples are represented using floating point. This approach was popularized because of the convenience and power of GPUs which provide high throughput 32-bit floating point computation. Although 16-bit float hardware is now widely available and 8-bit floating point standards are on the horizon, lowering the precision leads to significant issues representing gradients during optimization.

For example, consider the convolutional layers of the original AlexNet. 224x224x3 images at the input are reduced to 3x3x256 feature maps. 

Suppose that the inputs are 128x128 RGB Although the input size is much larger than the output, when properly trained, the amount of class information should be roughly the same. In other words, the function of the layers is to increase the information density of the class.

Now consider the same operation

## Standardized ML compression techniques

## Natural signal representation modeling

## Approaches to integrating compression and learning

## Comparison of learned filters with conventional transforms

## References

[Dictionaries for Sparse Representation Modeling (2010)](https://ieeexplore.ieee.org/abstract/document/5452966)

[End-to-end Optimized Image Compression (2017)](https://www.cns.nyu.edu/~lcv/iclr2017/)

[SoundStream: An End-to-End Neural Audio Codec (2022)](https://ieeexplore.ieee.org/abstract/document/9625818)