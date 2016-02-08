var fs = require('fs');
var expect = require('chai').expect;
var libraw = require('./libraw');

describe('LibRAW', function() {
  describe('Extracting thumbnail', function () {
    var outputFilename = '';

    it('should extract the thumbnail', function () {
      libraw.extractThumb('./test.raf', './output')
        .then(function(output) {
          expect(output).to.equal('./output.thumb.jpg');
          outputFilename = output;
        });
    });

    it('should check that the file has been properly created', function(done) {
      fs.access(outputFilename, fs.F_OK, function(err) {
        expect(err).to.be.null;
        done();
      });
    });

    it('should delete the file after creation', function(done) {
      fs.unlink(outputFilename, done);
    });
  });

  describe('Extracting TIFF', function () {
    var outputFilename = '';

    it('should extract the tiff', function () {
      this.timeout(90000);

      libraw.extract('./test.raf', './output')
        .then(function(output) {
          expect(output).to.equal('./output.tiff');
          outputFilename = output;
        });
    });

    it('should check that the file has been properly created', function(done) {
      fs.access(outputFilename, fs.F_OK, function(err) {
        expect(err).to.be.null;
        done();
      });
    });

    it('should delete the file after creation', function(done) {
      fs.unlink(outputFilename, done);
    });
  });

});
