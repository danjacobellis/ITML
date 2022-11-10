# Compressed Learning

[original proposal](https://danjacobellis.net/ITML/_static/proposal.pdf)

## Lossy compression standards

While hundereds of lossy compression techniques have been standardized, only a few have been widely deployed. We will put aside inter-frame video compression for now and focus on audio, image, and intra-frame video compression since our goal is to exploit the transform and quantization steps.

| Standard       | Introduced | Signal | Transform         | Quantization                   |
|----------------|------------|--------|-------------------|--------------------------------|
| MPEG Layer III | 1991       | Audio  | block DCT and FFT | Perceptual quantization vector |
| JPEG           | 1992       | Image  | block DCT         | Perceptual quantization matrix |
| JPEG 2000      | 2000       | Image  | Separable Wavelet | Scalar quantization            |
| CELT           | 2011       | Audio  | block DCT         | Pyramid vector quantization    |
| HEVC           | 2013       | Image  | block DCT and DST | Perceptual quantization matrix |
| Daala          | 2013       | Image  | block DCT         | Pyramid vector quantization    |
| Soundstream    | 2021       | Audio  | Learned           | Residual vector quantization   |

</center> Table 1. Summary of transform and quantization techniques used in some lossy compression standards. </center>

The block DCT and its variants dominate among commonly used codecs. Some notable exceptions are:

* JPEG 2000 (which is the standard for digital cinema where inter-frame compression is forbidden). The separable wavelet transform used in JPEG 2000 still suffers many of the sample limitations of DCT-based transforms. Although complex wavelet transforms allow sparse representations of singularities or oriented components, none have become popular for lossy compression.
* Low rate speech codecs which focus on modeling properties of human voice (pitch, formants, etc) which are not suitable for general-purpose use.
* Emerging standards which use learning-based techniques. Soundstream (Google) and Encodec (META) have recently become standardized. It's likely that learned image and video codecs will soon become standardized as well.

Likewise, the dominant approach to quantization is to define a perceptual quantization matrix (or vector) $Q$ and perform the simple quantization $B = round(\frac{G}{Q})$ (where $G$ is the transformed signal and $B$ is the quantizated representation).

However, variants of vector quantization are now being deployed in standards:

* CELT (now integrated into the OPUS standard) and Daala (now part of AV1) normalize transform coefficients to one, then separately codes this unit vector from the magnitude. This allows the use of pyramid vector quantization which is much more efficient but only applicable to unit vectors.

## Standardized ML compression techniques

## Natural signal representation modeling

## Approaches to integrating compression and learning

## Comparison of learned filters with conventional transforms

## References

[Dictionaries for Sparse Representation Modeling (2010)](https://ieeexplore.ieee.org/abstract/document/5452966)

[End-to-end Optimized Image Compression (2017)](https://www.cns.nyu.edu/~lcv/iclr2017/)

[SoundStream: An End-to-End Neural Audio Codec (2022)](https://ieeexplore.ieee.org/abstract/document/9625818)