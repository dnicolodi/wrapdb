runtest = executable('runtest', files('runtest.c', 'test.c'), dependencies: mpdec_dep)

testdata = custom_target(
  'gettests',
  command: [
    find_program('gettests.py'),
    join_paths(meson.current_source_dir(), 'testdata_dist'),
    join_paths(meson.current_build_dir(), 'testdata')],
  output: 'testdata.stamp',
  build_always_stale: true)

test(
  'libmpdec/official', runtest,
  args: files('official.decTest'),
  depends: testdata,
  workdir: meson.current_build_dir())

test(
  'libmpdec/additional', runtest,
  args: files('additional.decTest'),
  depends: testdata,
  workdir: meson.current_build_dir())
