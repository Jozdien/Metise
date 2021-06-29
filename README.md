# Metise

[Arxiv](https://arxiv.org/abs/2106.10542) | [Colab](https://colab.research.google.com/drive/1eIQfcljLeq5gWOipm9fyuVoVvX0zenLZ)

Tensorflow implementation to learn a decompression mapping on images compressed using colour density.

For example:

![enter image description here](https://i.ibb.co/8Y5v4rQ/Figure-1.png)

If the differences look subtle, that's due to the fact that at full-scale, the compressed images (with a compression factor of 2.667) look more discrete, and pushing the factor even higher distorts it beyond visually lossless return.  It may, however, be possible with training on larger datasets for a longer period of time.

## Running the Code 

The Colab repository for the paper contains all the code, with some description as well.  We recommend running it there.

## Acknowledgements

Code and network architecture heavily borrowed from the [pix2pix](https://github.com/phillipi/pix2pix) framework.
