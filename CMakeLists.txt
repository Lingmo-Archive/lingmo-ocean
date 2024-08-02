cmake_minimum_required(VERSION 3.20)

project(ocean)
set(PROJECT_VERSION "2.9.0")
set(PROJECT_VERSION_MAJOR 6)

set(KF6_MIN_VERSION "6.0.0")
set(QT_MIN_VERSION "6.4.0")

include(GenerateExportHeader)
include(WriteBasicConfigVersionFile)
include(FeatureSummary)

find_package(ECM ${KF6_MIN_VERSION} REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR} ${CMAKE_SOURCE_DIR}/cmake)

include(CMakePackageConfigHelpers)
include(ECMInstallIcons)
include(KDEInstallDirs6)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)
include(KDEClangFormat)

include(GtkUpdateIconCache)


find_package(KF6FrameworkIntegration ${KF6_MIN_VERSION} CONFIG )
set_package_properties(KF${QT_MAJOR_VERSION}FrameworkIntegration PROPERTIES
    DESCRIPTION "KF6 Framework Integration"
    URL "https://projects.kde.org/projects/frameworks/frameworkintegration"
    TYPE OPTIONAL
    PURPOSE "Required to use KStyle convenience functionalities in style")

#
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH}  ${CMAKE_SOURCE_DIR}/cmake)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
#
include(CMakePackageConfigHelpers)
include(ECMInstallIcons)
include(ECMQtDeclareLoggingCategory)
include(KDECompilerSettings NO_POLICY_SCOPE)
include(KDEClangFormat)
include(KDEGitCommitHooks)

include(GtkUpdateIconCache)

set(BUILD_QT6 ON)

option(WITH_DECORATIONS "Build Ocean window decorations for KWin" ON)
if(WITH_DECORATIONS)
    find_package(KDecoration2 REQUIRED)
    add_subdirectory(kdecoration)
endif()

add_subdirectory(colors)
add_subdirectory(liboceancommon)
add_subdirectory(kstyle)
add_subdirectory(misc)

include(ECMSetupVersion)
ecm_setup_version(${PROJECT_VERSION} VARIABLE_PREFIX OCEAN
                  PACKAGE_VERSION_FILE "${CMAKE_CURRENT_BINARY_DIR}/OceanConfigVersion.cmake"
)

# create a Config.cmake and a ConfigVersion.cmake file and install them
set(CMAKECONFIG_INSTALL_DIR "${KDE_INSTALL_CMAKEPACKAGEDIR}/Ocean")

configure_package_config_file("${CMAKE_CURRENT_SOURCE_DIR}/OceanConfig.cmake.in"
                              "${CMAKE_CURRENT_BINARY_DIR}/OceanConfig.cmake"
	                      PATH_VARS KDE_INSTALL_FULL_DATADIR
                              INSTALL_DESTINATION  ${CMAKECONFIG_INSTALL_DIR})

function(build_Qt6)
    set(QT_MAJOR_VERSION 6)
    include(KDEInstallDirs6)
    include(KDECMakeSettings)

    if(UNIX AND NOT APPLE AND NOT ANDROID)
        find_package(Qt6 ${REQUIRED_QT_VERSION} CONFIG REQUIRED DBus)
        set(HAVE_QTDBUS ${Qt6DBus_FOUND})

        option(WITH_DECORATIONS "Build Ocean window decorations for KWin" ON)
        option(WITH_WALLPAPERS "Install Ocean default wallpapers" ON)

        find_package(KF6FrameworkIntegration ${KF6_MIN_VERSION} CONFIG )
        set_package_properties(KF${QT_MAJOR_VERSION}FrameworkIntegration PROPERTIES
            DESCRIPTION "KF6 Framework Integration"
            URL "https://projects.kde.org/projects/frameworks/frameworkintegration"
            TYPE OPTIONAL
            PURPOSE "Required to use KStyle convenience functionalities in style")

        find_package(KF6KCMUtils ${KF6_MIN_VERSION})
        set_package_properties(KF6KCMUtils PROPERTIES
            TYPE REQUIRED
            DESCRIPTION "Helps create configuration modules"
            PURPOSE "KCMUtils used for the configuration modules or the decoration and Qt Style"
        )
    else()
        set(WITH_DECORATIONS OFF)
        set(WITH_WALLPAPERS OFF)
    endif()

    find_package(Qt6 ${QT_MIN_VERSION} REQUIRED CONFIG COMPONENTS Widgets)

    find_package(KF6 ${KF6_MIN_VERSION} REQUIRED COMPONENTS
        CoreAddons
        ColorScheme
        Config
        GuiAddons
        I18n
        IconThemes
        WindowSystem)

    find_package(Qt6 ${QT_MIN_VERSION} OPTIONAL_COMPONENTS Quick)
    if(${Qt6Quick_FOUND})
        find_package(KF6LingmoUIPlatform ${KF6_MIN_VERSION} REQUIRED)
    endif()

    set(OCEAN_HAVE_KSTYLE ${KF6FrameworkIntegration_FOUND})
    set(OCEAN_HAVE_QTQUICK ${Qt6Quick_FOUND})

    # https://bugreports.qt.io/browse/QTBUG-114706
    add_library(Qt::Core ALIAS Qt6::Core)
    add_library(Qt::Gui ALIAS Qt6::Gui)
    add_library(Qt::OpenGL ALIAS Qt6::OpenGL)
    add_library(Qt::Network ALIAS Qt6::Network)
    if(Qt6_VERSION_MINOR GREATER 6)
        add_library(Qt::PlatformModuleInternal ALIAS Qt6::PlatformModuleInternal)
    endif()

    add_subdirectory(kstyle kstyle6)
    add_subdirectory(liboceancommon liboceancommon6)
    add_subdirectory(misc)

    if(WITH_DECORATIONS)
        find_package(KDecoration2 REQUIRED)
        add_subdirectory(kdecoration)
    endif()
    if (WITH_WALLPAPERS)
        add_subdirectory(wallpapers)
    endif()

    ki18n_install(po)

    # create a Config.cmake and a ConfigVersion.cmake file and install them
    include(ECMSetupVersion)
    ecm_setup_version(${PROJECT_VERSION} VARIABLE_PREFIX OCEAN
        PACKAGE_VERSION_FILE "${CMAKE_CURRENT_BINARY_DIR}/OceanConfigVersion.cmake"
    )
    set(CMAKECONFIG_INSTALL_DIR "${KDE_INSTALL_CMAKEPACKAGEDIR}/Ocean")

    configure_package_config_file("${CMAKE_CURRENT_SOURCE_DIR}/OceanConfig.cmake.in"
                                  "${CMAKE_CURRENT_BINARY_DIR}/OceanConfig.cmake"
                                  PATH_VARS KDE_INSTALL_FULL_DATADIR
                                  INSTALL_DESTINATION  ${CMAKECONFIG_INSTALL_DIR}
    )
    install(FILES  "${CMAKE_CURRENT_BINARY_DIR}/OceanConfig.cmake"
                   "${CMAKE_CURRENT_BINARY_DIR}/OceanConfigVersion.cmake"
            DESTINATION "${CMAKECONFIG_INSTALL_DIR}"
            COMPONENT Devel
    )

    unset(QUERY_EXECUTABLE CACHE)
endfunction()
if(BUILD_QT6)
    build_Qt6()
endif()

function(build_colors_and_cursors)
    # While it is technically not 100% correct to use versionless
    # KDEInstallDirs while (maybe) building for both Qt versions,
    # it doesn't really matter at the end, because colors and cursors
    # only use ICONDIR and DATADIR which both do not depend on the version
    include(KDEInstallDirs)
    add_subdirectory(colors)
    add_subdirectory(cursors)
endfunction()

build_colors_and_cursors()
# add clang-format target for all our real source files
file(GLOB_RECURSE ALL_CLANG_FORMAT_SOURCE_FILES *.cpp *.h)
kde_clang_format(${ALL_CLANG_FORMAT_SOURCE_FILES})

install(FILES  "${CMAKE_CURRENT_BINARY_DIR}/OceanConfig.cmake"
               "${CMAKE_CURRENT_BINARY_DIR}/OceanConfigVersion.cmake"
        DESTINATION "${CMAKECONFIG_INSTALL_DIR}"
        COMPONENT Devel
)

feature_summary(WHAT ALL INCLUDE_QUIET_PACKAGES FATAL_ON_MISSING_REQUIRED_PACKAGES)
