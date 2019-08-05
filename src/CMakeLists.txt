project(${PROJECT_NAME})
find_package(Qt5Core REQUIRED)
find_package(Qt5Widgets REQUIRED)

set(CMAKE_AUTOMOC ON)

# add_subdirectory(ExcelLib)

file(
  GLOB
  PROJECT_SRC
  ${PROJECT_SOURCE_DIR}/*.c*
)

file(
  GLOB
  PROJECT_INC
  ${PROJECT_SOURCE_DIR}/*.h*
)

file(
  GLOB
  PROJECT_UI
  ${PROJECT_SOURCE_DIR}/*.ui
)

qt5_wrap_ui(
  PROJECT_UI_INC
  ${PROJECT_UI}
)

file(
  GLOB
  PROJECT_QRC
  ${PROJECT_SOURCE_DIR}/*.qrc
)

qt5_add_resources(
  PROJECT_QRC_SRC
  ${PROJECT_QRC}
)

# link_directories(${CMAKE_BINARY_DIR}/xlint-build/installed/lib)

add_executable(
  ${PROJECT_NAME}
  ${PROJECT_SRC}
  ${PROJECT_INC}
  ${PROJECT_UI}
  ${PROJECT_UI_INC}
  ${PROJECT_QRC}
  ${PROJECT_QRC_SRC}
)

target_link_libraries(
  ${PROJECT_NAME}
  PUBLIC
  Qt5::Core
  Qt5::Widgets
  # debug xlntd
  # optimized xlnt
)

target_include_directories(
  ${PROJECT_NAME}
  PUBLIC
  ${PROJECT_BINARY_DIR}
  ${PROJECT_SOURCE_DIR}
  # ${CMAKE_BINARY_DIR}/xlint-build/installed/include
)