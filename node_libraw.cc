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

  NAN_METHOD(ExtractThumb) {
    Nan::HandleScope scope;

    LibRaw RawProcessor;

    v8::String::Utf8Value filenameFromArgs(info[0]->ToString());
    std::string filename = std::string(*filenameFromArgs);
    v8::String::Utf8Value outputFromArgs(info[1]->ToString());
    std::string output = std::string(*outputFromArgs);

    std::string extension = "thumb.ppm";

    std::ifstream file;
    file.open(filename, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<char> buffer(size);

    if (file.read(buffer.data(), size)) {
      RawProcessor.open_buffer(buffer.data(), size);
      RawProcessor.unpack();
      RawProcessor.unpack_thumb();

      if (RawProcessor.imgdata.thumbnail.tformat == LIBRAW_THUMBNAIL_JPEG) {
        extension = "thumb.jpg";
      }

      output = output + "." + extension;
      RawProcessor.dcraw_thumb_writer(output.c_str());
      RawProcessor.recycle();

      info.GetReturnValue().Set(Nan::New(output).ToLocalChecked());
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
      Nan::New<String>("extractThumb").ToLocalChecked(),
      Nan::GetFunction(Nan::New<v8::FunctionTemplate>(ExtractThumb)).ToLocalChecked()
    );
  }

  NODE_MODULE(libraw, init)
}
