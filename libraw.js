var libraw = require('./build/Release/raw');

console.log(libraw.hello('world'));
//console.log(libraw.openFile('./test.raf'));
console.log(libraw.extractThumb('./test.raf', './extracted'));
