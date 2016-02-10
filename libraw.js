const raw = require('./build/Release/node-libraw');

const libraw = {
  extract: function(input, output) {
    return new Promise(function(resolve, reject) {
      raw.extract(input, output, function(err, output) {
        if (err)
          reject(err);
        else
          resolve(output);
      });
    });
  },

  extractThumb: function(input, output) {
    return new Promise(function(resolve, reject) {
      raw.extractThumb(input, output, function(err, output) {
        if (err)
          reject(err);
        else
          resolve(output);
      });
    });
  }
};

module.exports = libraw;
