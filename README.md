# Node-libRAW

Asynchronous bindings for LibRaw.

[![NPM](https://nodei.co/npm/libraw.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/libraw/)

**Be careful this library is in alpha. The API is susceptible to change at any moment**

## Supported platforms

So far that library only supports Linux (tested on ubuntu 14.04 LTS) with node > 4.0

## Usage

``` js
import libraw from 'libraw';

// For extracting the RAW tiff
libraw.extract('./test.raf', './output')
  .then((output) => {
    console.log(output);
  });

// For extracting the embedded jpg thumbnail
libraw.extractThumb('./test.raf', './output')
  .then((output) => {
    console.log(output);
  });
```

## Note on LibRaw

This library doesn't come with LibRaw included, you will have to install it by yourself.

Depending on which distribution you are using, it might not be possible to decode RAW on modern camera (for instance Fuji X100T).

I'm planning on shipping node-libraw with the latest version of libraw, but due to my meager knowledge of C++ it's going to take some time.

Any contributions are, of course, welcome.

On linux: ```sudo apt-get install libraw-dev```
