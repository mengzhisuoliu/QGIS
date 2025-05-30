
########################################################
# Files

set (offline_editing_plugin_SRCS
  offline_editing_plugin.cpp
  offline_editing_plugin_gui.cpp
  offline_editing_progress_dialog.cpp
)

set (offline_editing_plugin_UIS
  offline_editing_plugin_guibase.ui
  offline_editing_progress_dialog_base.ui
)

set (offline_editing_plugin_RCCS  offline_editing_plugin.qrc)

########################################################
# Build

qt_wrap_ui(offline_editing_plugin_UIS_H ${offline_editing_plugin_UIS})

add_library (plugin_offlineediting MODULE
  ${offline_editing_plugin_SRCS}
  ${offline_editing_plugin_RCCS}
  ${offline_editing_plugin_UIS_H}
)

# require c++17
target_compile_features(plugin_offlineediting PRIVATE cxx_std_17)

target_link_libraries(plugin_offlineediting
  qgis_core
  qgis_gui
)

include_directories(
  ${CMAKE_SOURCE_DIR}/src/plugins

  ${CMAKE_CURRENT_BINARY_DIR}
)

########################################################
# Install

install(TARGETS plugin_offlineediting
	RUNTIME DESTINATION ${QGIS_PLUGIN_DIR}
	LIBRARY DESTINATION ${QGIS_PLUGIN_DIR}
)
