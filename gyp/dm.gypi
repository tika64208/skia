# GYP for "dm" (Diamond Master, a.k.a Dungeon master, a.k.a GM 2).
{
  'include_dirs': [
    '../dm',
    '../gm',
    '../tests',
    '../src/images',
    '../src/lazy',
    '../src/core',
    '../src/effects',
    '../src/pipe/utils/',
    '../src/utils',
    '../src/utils/debugger',
    '../tools',
  ],
  'dependencies': [
    'etc1.gyp:libetc1',
    'flags.gyp:flags',
    'jsoncpp.gyp:jsoncpp',
    'skia_lib.gyp:skia_lib',
    'tools.gyp:crash_handler',
    'tools.gyp:sk_tool_utils',
  ],
  'includes': [
    'gmslides.gypi',
    'pathops_unittest.gypi',
    'tests.gypi',
  ],
  'sources': [
    '../dm/DM.cpp',
    '../dm/DMCpuGMTask.cpp',
    '../dm/DMExpectationsTask.cpp',
    '../dm/DMGpuGMTask.cpp',
    '../dm/DMPDFRasterizeTask.cpp',
    '../dm/DMPDFTask.cpp',
    '../dm/DMPipeTask.cpp',
    '../dm/DMQuiltTask.cpp',
    '../dm/DMReporter.cpp',
    '../dm/DMSKPTask.cpp',
    '../dm/DMSerializeTask.cpp',
    '../dm/DMTask.cpp',
    '../dm/DMTaskRunner.cpp',
    '../dm/DMTestTask.cpp',
    '../dm/DMUtil.cpp',
    '../dm/DMWriteTask.cpp',
    '../gm/gm.cpp',
    '../gm/gm_expectations.cpp',

    '../src/pipe/utils/SamplePipeControllers.cpp',
    '../src/utils/debugger/SkDebugCanvas.cpp',
    '../src/utils/debugger/SkDrawCommand.cpp',
    '../src/utils/debugger/SkObjectParser.cpp',
    '../tools/LazyDecodeBitmap.cpp',
  ],
  'conditions': [
    [ 'skia_gpu == 1', {
      'dependencies': [ 'gputest.gyp:skgputest' ],
    }],
  ],
}
