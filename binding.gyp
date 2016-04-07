{
  "targets": [
    {
      "target_name": "node_libraw",
      "sources": [ "node_libraw.cc" ],
      "include_dirs" : [
        "vendor/LibRaw/",
        "<!(node -e \"require('nan')\")"
      ],
      "libraries": [ "-Wl,-rpath,./build/Release/raw.a" ],
      'dependencies': [
        'vendor/libraw.gyp:libraw',
      ]
    }
  ],
}
