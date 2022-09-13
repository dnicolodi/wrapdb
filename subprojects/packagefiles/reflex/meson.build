project('reflex', 'cpp',
        version: '3.2.11',
        license: 'BSD-3-Clause',
        meson_version: '>=0.49.0')

includes = include_directories('include')

cpp = meson.get_compiler('cpp')

flags = cpp.get_supported_arguments(['-Wno-non-virtual-dtor'])
add_project_arguments(flags, language: 'cpp')

if get_option('sse2').enabled()
  # check whether ${CXX} supports 
  if cpp.compiles('''
        #include <emmintrin.h>
        __m128i n = _mm_set1_epi8(42);
        ''',
        name: 'SSE2 intrinsics',
        cppflags: '-march=native')
    SIMD_FLAGS = '-msse2 -DHAVE_SSE2'
  endif
endif

#     AC_ARG_ENABLE(avx,
#       [AS_HELP_STRING([--disable-avx],
#                       [disable AVX optimizations])],
#       [with_no_avx="yes"],
#       [with_no_avx="no"])
#     AC_MSG_CHECKING(for --disable-avx)
#     if test "x$with_no_avx" = "xno"; then
#       AC_MSG_RESULT(no)
#       AC_MSG_CHECKING([whether ${CXX} supports AVX intrinsics])
#       save_CXXFLAGS=$CXXFLAGS
#       CXXFLAGS="-march=native"
#       AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <immintrin.h>]], [[__m512 n = _mm512_set1_epi8(42); (void)_mm512_cmpeq_epi8_mask(n, n);]])],
#                         [mavx_ok=yes],
#                         [mavx_ok=no])
#       if test "x$mavx_ok" = "xyes"; then
#         SIMD_FLAGS="-msse2 -DHAVE_AVX512BW"
#         SIMD_AVX2_FLAGS="-mavx2"
#         SIMD_AVX512BW_FLAGS="-mavx512bw"
#       else
#         AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <immintrin.h>]], [[__m256i n = _mm256_set1_epi8(42); (void)_mm256_movemask_epi8(_mm256_and_si256(n, n));]])],
#                           [mavx_ok=yes],
#                           [mavx_ok=no])
#         if test "x$mavx_ok" = "xyes"; then
#           SIMD_FLAGS="-msse2 -DHAVE_AVX2"
#           SIMD_AVX2_FLAGS="-mavx2"
#         fi
#       fi
#       CXXFLAGS=$save_CXXFLAGS
#       AC_MSG_RESULT($mavx_ok)
#     else
#       AC_MSG_RESULT(yes)
#     fi
#   fi
# else
#   AC_MSG_RESULT(yes)
#   SIMD_FLAGS=
# fi

# if test "x$SIMD_FLAGS" = "x"; then
# AC_ARG_ENABLE(neon,
#   [AS_HELP_STRING([--disable-neon],
#                   [disable ARM NEON/AArch64 optimizations])],
#   [with_no_neon="yes"],
#   [with_no_neon="no"])
# AC_MSG_CHECKING(for --disable-neon)
# if test "x$with_no_neon" = "xno"; then
#   AC_MSG_RESULT(no)
#   AC_MSG_CHECKING([whether ${CXX} supports ARM NEON/AArch64 intrinsics])
#   AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <arm_neon.h>]], [[uint64x2_t n; uint64_t m = vgetq_lane_u64(n, 0);]])],
#                     [mneon_ok=yes],
#                     [mneon_ok=no])
#   if test "x$mneon_ok" = "xyes"; then
#     SIMD_FLAGS="-DHAVE_NEON"
#   else
#     save_CXXFLAGS=$CXXFLAGS
#     CXXFLAGS="-march=native"
#     AC_PREPROC_IFELSE([AC_LANG_PROGRAM([[#include <arm_neon.h>]], [[uint64x2_t n; uint64_t m = vgetq_lane_u64(n, 0);]])],
#                       [mneon_ok=yes],
#                       [mneon_ok=no])
#     if test "x$mneon_ok" = "xyes"; then
#       AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <arm_neon.h>]], [[uint64x2_t n; uint64_t m = vgetq_lane_u64(n, 0);]])],
#                         [mneon_ok=yes],
#                         [mneon_ok=no])
#       if test "x$mneon_ok" = "xyes"; then
#         SIMD_FLAGS="-march=native -DHAVE_NEON"
#       else
#         CXXFLAGS="-march=native -mfpu=neon"
#         AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <arm_neon.h>]], [[uint64x2_t n; uint64_t m = vgetq_lane_u64(n, 0);]])],
#                           [mneon_ok=yes],
#                           [mneon_ok=no])
#         if test "x$mneon_ok" = "xyes"; then
#           SIMD_FLAGS="-march=native -mfpu=neon -DHAVE_NEON"
#         fi
#       fi
#     fi
#   fi
#   CXXFLAGS=$save_CXXFLAGS
#   AC_MSG_RESULT($mneon_ok)
# else
#   AC_MSG_RESULT(yes)
#   SIMD_FLAGS=
# fi
# fi



unicode_sources = files(
  'unicode/block_scripts.cpp',
  'unicode/language_scripts.cpp',
  'unicode/letter_scripts.cpp',
)

libreflex_sources = files(
  'lib/convert.cpp',
  'lib/debug.cpp',
  'lib/error.cpp',
  'lib/input.cpp',
  'lib/matcher.cpp',
  'lib/pattern.cpp',
  'lib/posix.cpp',
  'lib/unicode.cpp',
  'lib/utf8.cpp',
)

libreflexmin_sources = files(
  'lib/debug.cpp',
  'lib/error.cpp',
  'lib/input.cpp',
  'lib/matcher.cpp',
  'lib/pattern.cpp',
  'lib/utf8.cpp',
)

#no dllexport being used here. Must use static library.
if cpp.get_argument_syntax() != 'msvc'
  libreflexmin = library(
    'reflexmin',
    libreflexmin_sources,
    include_directories : includes)

  libreflex = library(
    'reflex',
    libreflex_sources, unicode_sources,
    include_directories : includes)
else
  libreflexmin = static_library(
    'reflexmin',
    libreflexmin_sources,
    include_directories : includes)

  libreflex = static_library(
    'reflex',
    libreflex_sources, unicode_sources,
    include_directories : includes)
endif

subdir('src')

reflex_dep = declare_dependency(
  link_with : libreflex,
  include_directories : includes)
