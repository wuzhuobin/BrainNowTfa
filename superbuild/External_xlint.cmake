include(ExternalProject)
ExternalProject_Add(
  xlint
  TMP_DIR
  ${CMAKE_BINARY_DIR}/xlint-tmp
  STAMP_DIR
  ${CMAKE_BINARY_DIR}/xlint-stamp
  DOWNLOAD_DIR
  ${CMAKE_BINARY_DIR}/xlint
  SOURCE_DIR
  ${CMAKE_BINARY_DIR}/xlint
  BINARY_DIR
  ${CMAKE_BINARY_DIR}/xlint-build
  INSTALL_DIR
  ${CMAKE_BINARY_DIR}/xlint-install
  # INSTALL_COMMAND
  # ""
  # LOG_DIR
  # ${CMAKE_BINARY_DIR}/xlint-log
  GIT_REPOSITORY
  "https://github.com/tfussell/xlnt.git"
  GIT_TAG
  "v1.3.0"
  CMAKE_CACHE_ARGS
  -DTESTS:BOOL=OFF
  # -DSTATIC:BOOL=ON
  # -DSTATIC_CRT:BOOL=ON
)

add_custom_target(
  xlint_copy
  ALL
  COMMAND
  ${CMAKE_COMMAND} -E copy_directory ${CMAKE_BINARY_DIR}/xlint-build/installed/lib ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/Debug
  COMMAND
  ${CMAKE_COMMAND} -E copy_directory ${CMAKE_BINARY_DIR}/xlint-build/installed/lib ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/Release
  COMMAND
  ${CMAKE_COMMAND} -E copy_directory ${CMAKE_BINARY_DIR}/xlint-build/installed/bin ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/Debug
  COMMAND
  ${CMAKE_COMMAND} -E copy_directory ${CMAKE_BINARY_DIR}/xlint-build/installed/bin ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/Release
  DEPENDS
  xlint
)