#include <stdio.h>
#include <iostream>
#include <fstream>
#include <v8.h>
#include <nan.h>

#include "libraw/libraw.h"

namespace node_libraw {
  using v8::Exception;
  using v8::Function;
  using v8::FunctionCallbackInfo;
  using v8::FunctionTemplate;
  using v8::Isolate;
  using v8::Local;
  using v8::Number;
  using v8::Object;
  using v8::String;
  using v8::Value;
  using v8::Null;

  NAN_METHOD(Hello) {
    Nan::HandleScope scope;

    v8::String::Utf8Value nameFromArgs(info[0]->ToString());
    std::string name = std::string(*nameFromArgs);
    std::string response = "hello " + name;

    info.GetReturnValue().Set(Nan::New(response).ToLocalChecked());
  }

  NAN_METHOD(OpenFile) {
    int ret = 0;
    //char thumbfn[1024];

    std::string thumbfn = "";

    Nan::HandleScope scope;

    // Creation of image processing object
    LibRaw RawProcessor;

#define P1  RawProcessor.imgdata.idata
#define S   RawProcessor.imgdata.sizes
#define C   RawProcessor.imgdata.color
#define T   RawProcessor.imgdata.thumbnail
#define P2  RawProcessor.imgdata.other
#define OUT RawProcessor.imgdata.params

    OUT.output_tiff = 1; // Let us output TIFF

    v8::String::Utf8Value nameFromArgs(info[0]->ToString());
    std::string filename = std::string(*nameFromArgs);

    std::ifstream file;
    file.open(filename, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<char> buffer(size);

    if (file.read(buffer.data(), size)) {
      std::cout << size << "\n";
      ret = RawProcessor.open_buffer(buffer.data(), size);

      if(ret != LIBRAW_SUCCESS) {
        RawProcessor.recycle(); 
      }

      // Let us unpack the image
      if( (ret = RawProcessor.unpack() ) != LIBRAW_SUCCESS) {
        //fprintf(stderr,"Cannot unpack_thumb %s\n", filename);
        std::cout << "Cannot unpack " << filename << "\n";
      }

      if( (ret = RawProcessor.unpack_thumb() ) != LIBRAW_SUCCESS){
        std::cout << "Cannot unpack_thumb " << filename << "\n";
      }
      else {
        //snprintf(thumbfn, sizeof(thumbfn), "%s.%s", filename, T.tformat == LIBRAW_THUMBNAIL_JPEG ? "thumb.jpg" : "thumb.ppm");
        thumbfn = "test.jpg";

        if( LIBRAW_SUCCESS != (ret = RawProcessor.dcraw_thumb_writer(thumbfn.c_str()))){
          std::cout << "Cannot write " << thumbfn << "\n";
        }
      }
    }

    file.close();
  }

  void init(Local<Object> exports) {
    Nan::Set(
      exports,
      Nan::New<String>("hello").ToLocalChecked(),
      Nan::GetFunction(Nan::New<v8::FunctionTemplate>(Hello)).ToLocalChecked()
    );

    Nan::Set(
      exports,
      Nan::New<String>("openFile").ToLocalChecked(),
      Nan::GetFunction(Nan::New<v8::FunctionTemplate>(OpenFile)).ToLocalChecked()
    );
  }

  NODE_MODULE(libraw, init)
}
