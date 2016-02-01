{
  "includes": [ "vendor/LibRaw-0.17.1/raw.gyp" ],
  "targets": [
    {
      "target_name": "node-libraw",
      "sources": [ "node_libraw.cc" ],
      "libraries": [
        "-lraw"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ],
}
