
########################################################
# Files

set (topol_SRCS
  topol.cpp
  rulesDialog.cpp
  checkDock.cpp
  topolError.cpp
  topolTest.cpp
  dockModel.cpp
)

set (topol_UIS
  rulesDialog.ui
  checkDock.ui
)

set (topol_RCCS  topol.qrc)

########################################################
# Build

qt_wrap_ui(topol_UIS_H  ${topol_UIS})

add_library (plugin_topology MODULE ${topol_SRCS} ${topol_RCCS} ${topol_UIS_H})

# require c++17
target_compile_features(plugin_topology PRIVATE cxx_std_17)

include_directories(
  ${CMAKE_SOURCE_DIR}/src/plugins

  ${CMAKE_BINARY_DIR}/src/ui
  ${CMAKE_CURRENT_BINARY_DIR}
)

target_link_libraries(plugin_topology
  qgis_core
  qgis_gui
)


########################################################
# Install

install(TARGETS plugin_topology
  RUNTIME DESTINATION ${QGIS_PLUGIN_DIR}
  LIBRARY DESTINATION ${QGIS_PLUGIN_DIR})

