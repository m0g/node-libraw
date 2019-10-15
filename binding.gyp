{
  "targets": [
    {
      "target_name": "node_libraw",
      "sources": [ "node_libraw.cc" ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ],
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
