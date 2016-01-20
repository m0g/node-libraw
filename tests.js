var fs = require('fs');
var expect = require('chai').expect;
var libraw = require('./libraw');

describe('LibRAW', function() {
  describe('Extracting thumbnail', function () {
    var output = '';

    it('should extract the thumbnail', function () {
      output = libraw.extractThumb('./test.raf', './output');
      expect(output).to.equal('./output.thumb.jpg');
    });

    it('should check that the file has been properly created', function(done) {
      fs.access(output, fs.F_OK, function(err) {
        expect(err).to.be.null;
        done();
      });
    });

    it('should delete the file after creation', function(done) {
      fs.unlink(output, done);
    });
  });

  describe('Extracting TIFF', function () {
    var output = '';

    it('should extract the tiff', function () {
      this.timeout(90000);
      output = libraw.extract('./test.raf', './output');
      expect(output).to.equal('./output.tiff');
    });

    it('should check that the file has been properly created', function(done) {
      fs.access(output, fs.F_OK, function(err) {
        expect(err).to.be.null;
        done();
      });
    });

    it('should delete the file after creation', function(done) {
      fs.unlink(output, done);
    });
  });

});
