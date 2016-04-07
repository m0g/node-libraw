{
  "targets": [
    {
      "target_name": "libraw",
      "type": "static_library",
      "sources": [
        "LibRaw-0.17.1/internal/dcraw_common.cpp",
        "LibRaw-0.17.1/internal/dcraw_fileio.cpp",
        "LibRaw-0.17.1/internal/demosaic_packs.cpp",
        "LibRaw-0.17.1/src/libraw_cxx.cpp",
        "LibRaw-0.17.1/src/libraw_datastream.cpp",
        "LibRaw-0.17.1/src/libraw_c_api.cpp"
      ],
      "include_dirs": [ 
        "./LibRaw-demosaic-pack-GPL2-0.17.1",
        "./LibRaw-demosaic-pack-GPL3-0.17.1",
        "./LibRaw-0.17.1"
      ],
      "libraries": [
        "-ljpeg8"
      ],
      "cflags": [ 
        "-Wdeprecated-declarations",
        "-pthread -w"
      ],
      "cflags_cc": [
        "-pthread -w",
        "-fexceptions",
        "-DLIBRAW_NOTHREADS -w",
        "-I./LibRaw-demosaic-pack-GPL2-0.17.1",
        "-DLIBRAW_DEMOSAIC_PACK_GPL2",
        "-I./LibRaw-demosaic-pack-GPL3-0.17.1",
        "-DLIBRAW_DEMOSAIC_PACK_GPL3",
        "-DUSE_JPEG8"
      ]
    }
  ]
}

