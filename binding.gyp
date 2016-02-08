{
  "includes": [ "vendor/raw.gyp" ],
  "targets": [
    {
      "target_name": "node-libraw",
      "sources": [ "node_libraw.cc" ],
      "libraries": [ 
        "-lraw"
       ],
      "include_dirs" : [
        "vendor/LibRaw-0.17.1",
        "<!(node -e \"require('nan')\")"
      ]
    }
  ],
}
