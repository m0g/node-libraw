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
      "cflags": [ 
        "-pthread -w",
        "-Wdeprecated-declarations"
      ],
      "cflags_cc": [
        "-pthread -w",
        "-DLIBRAW_NOTHREADS -w",
        "-fexceptions",
        "-Wdeprecated-declarations"
      ]
    }
  ]
}

