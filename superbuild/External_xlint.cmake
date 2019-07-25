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
  # LOG_DIR
  # ${CMAKE_BINARY_DIR}/xlint-log
  GIT_REPOSITORY
  "https://github.com/tfussell/xlnt.git"
  GIT_TAG
  "v1.3.0"
  INSTALL_COMMAND
  ""
)