################# dependencies #################
### Qt/KDE
find_package(Qt6 REQUIRED CONFIG COMPONENTS Widgets)

################# oceanstyle target #################
set(oceancommon_LIB_SRCS
    oceanboxshadowrenderer.cpp
)

add_library(oceancommon6 ${oceancommon_LIB_SRCS})

generate_export_header(oceancommon6
    BASE_NAME oceancommon
    EXPORT_FILE_NAME oceancommon_export.h)

target_link_libraries(oceancommon6
    PUBLIC
        Qt6::Core
        Qt6::Gui)

set_target_properties(oceancommon6 PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
    POSITION_INDEPENDENT_CODE TRUE)

install(TARGETS oceancommon6 ${INSTALL_TARGETS_DEFAULT_ARGS} LIBRARY NAMELINK_SKIP)
