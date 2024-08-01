add_definitions(-DTRANSLATION_DOMAIN="ocean_kwin_deco")

find_package(KF6 REQUIRED COMPONENTS CoreAddons GuiAddons ConfigWidgets WindowSystem I18n IconThemes)
find_package(Qt6 CONFIG REQUIRED COMPONENTS DBus)

set(OCEAN_HAVE_X11 FALSE)

################# configuration #################
configure_file(config-ocean.h.cmake ${CMAKE_CURRENT_BINARY_DIR}/config-ocean.h )

################# includes #################
include_directories(${CMAKE_SOURCE_DIR}/liboceancommon)
include_directories(${CMAKE_BINARY_DIR}/liboceancommon)

################# newt target #################
### plugin classes
set(oceandecoration_SRCS
    oceanbutton.cpp
    oceandecoration.cpp
    oceanexceptionlist.cpp
    oceansettingsprovider.cpp
    oceansizegrip.cpp)

# Bring back QString(char *)
remove_definitions(-DQT_NO_CAST_FROM_ASCII)
remove_definitions(-DQT_NO_KEYWORDS)

### build library
kconfig_add_kcfg_files(oceandecoration_SRCS oceansettings.kcfgc)
add_library(oceandecoration MODULE
    ${oceandecoration_SRCS}
    ${oceandecoration_config_SRCS}
    ${oceandecoration_config_PART_FORMS_HEADERS})

set_target_properties(oceandecoration PROPERTIES
  OUTPUT_NAME org.kde.ocean)

target_link_libraries(oceandecoration
    PRIVATE
        oceancommon6
        Qt6::DBus
        Qt6::Widgets
        KF6::CoreAddons
        KF6::ConfigGui
        KF6::GuiAddons
        KF6::I18n
        KF6::IconThemes
        KDecoration2::KDecoration
)

if(OCEAN_HAVE_X11)
  target_link_libraries(oceandecoration
    PUBLIC
      XCB::XCB)
endif()


install(TARGETS oceandecoration DESTINATION ${KDE_INSTALL_PLUGINDIR}/${KDECORATION_PLUGIN_DIR})

add_subdirectory(config)
