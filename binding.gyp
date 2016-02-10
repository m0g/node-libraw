{
  "includes": [ "vendor/raw.gyp" ],
  "targets": [
    {
      "target_name": "node_libraw",
      "sources": [ "node_libraw.cc" ],
      "include_dirs" : [
        "build/Release",
        "vendor/LibRaw-0.17.1",
        "<!(node -e \"require('nan')\")"
      ],
      "libraries": [
        "-lraw",
        "-Wl,-rpath,./build/Release/"
      ]
    }
  ],
}
