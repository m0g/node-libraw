{
  "targets": [
    {
      "target_name": "libraw",
      "sources": [ "node_libraw.cc" ],
      "libraries": [
        "-lraw",
      ],
      "include_dirs" : ["<!(node -e \"require('nan')\")"]
    }
  ],
}
