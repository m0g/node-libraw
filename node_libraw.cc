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

  void init(Local<Object> exports) {
    Nan::Set(
      exports,
      Nan::New<String>("hello").ToLocalChecked(),
      Nan::GetFunction(Nan::New<v8::FunctionTemplate>(Hello)).ToLocalChecked()
    );
  }

  NODE_MODULE(libraw, init)
}
