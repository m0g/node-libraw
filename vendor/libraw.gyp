{
  "targets": [
    {
      "target_name": "libraw",
      "type": "static_library",
      "sources": [
        "LibRaw/internal/dcraw_common.cpp",
        "LibRaw/internal/dcraw_fileio.cpp",
        "LibRaw/internal/demosaic_packs.cpp",
        "LibRaw/src/libraw_cxx.cpp",
        "LibRaw/src/libraw_datastream.cpp",
        "LibRaw/src/libraw_c_api.cpp"
      ],
      "include_dirs": [
        "./LibRaw-demosaic-pack-GPL2",
        "./LibRaw-demosaic-pack-GPL3",
        "./LibRaw"
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
        "-I./LibRaw-demosaic-pack-GPL2",
        "-DLIBRAW_DEMOSAIC_PACK_GPL2",
        "-I./LibRaw-demosaic-pack-GPL3",
        "-DLIBRAW_DEMOSAIC_PACK_GPL3",
        "-DUSE_JPEG8"
      ],
      'xcode_settings': {
        'MACOSX_DEPLOYMENT_TARGET': '10.12',
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'OTHER_CPLUSPLUSFLAGS': [
            "-pthread -w",
            '-fexceptions',
            "-DLIBRAW_NOTHREADS -w",
            "-I./LibRaw-demosaic-pack-GPL2",
            "-DLIBRAW_DEMOSAIC_PACK_GPL2",
            "-I./LibRaw-demosaic-pack-GPL3",
            "-DLIBRAW_DEMOSAIC_PACK_GPL3",
            "-DUSE_JPEG8"
        ],
      },
    }
  ]
}
