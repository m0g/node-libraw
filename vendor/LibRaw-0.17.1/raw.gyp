{
  "targets": [
    {
      "target_name": "libraw",
      "type": "static_library",
      "sources": [
        "internal/dcraw_common.cpp",
        "internal/dcraw_fileio.cpp",
        "internal/demosaic_packs.cpp",
        "src/libraw_cxx.cpp",
        "src/libraw_datastream.cpp",
        "src/libraw_c_api.cpp"
      ],
      "include_dirs": [ 
        "."
      ],
      "libraries": [
        "-ljpeg8"
      ],
      "cflags": [ 
        "-pthread -w"
      ],
      "cflags_cc": [
        "-pthread -w",
        "-fexceptions",
        "-Wdeprecated-declarations",
        "-I/node-libraw/vendor/LibRaw-demosaic-pack-GPL2-0.17.1",
        "-DLIBRAW_DEMOSAIC_PACK_GPL2",
        "-I/node-libraw/vendor/LibRaw-demosaic-pack-GPL3-0.17.1",
        "-DLIBRAW_DEMOSAIC_PACK_GPL3",
        "-DUSE_JPEG8"
      ]
    }
  ]
}

