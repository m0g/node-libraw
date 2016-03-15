{
  "targets": [
    {
      "target_name": "node_libraw",
      "sources": [ "node_libraw.cc" ],
      "include_dirs" : [
        "vendor/LibRaw-0.17.1",
        "<!(node -e \"require('nan')\")"
      ],
      'dependencies': [
        'vendor/raw.gyp:libraw',
      ]
    }
  ],
}
