#
# Copyright Barco N.V. All Rights Reserved.
#
message(STATUS "\n-- || Processing asio - starting")

cmake_minimum_required( VERSION 3.14 )
project( asio VERSION 1.18.1 )

########################################################################
# asio header only library
########################################################################
add_library(asio INTERFACE)
add_library(asio::asio ALIAS asio )

target_include_directories(asio  SYSTEM INTERFACE # TODO_MADAU: is SYSTEM needed
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>  
)

# ASIO specific definitions, we want to use it standalone and header only
target_compile_definitions(asio  INTERFACE
    ASIO_STANDALONE
    ASIO_HEADER_ONLY
)

########################################################################
# Installation
########################################################################
include(GNUInstallDirs) # provides CMAKE_INSTALL_{INCLUDE|LIB|BIN}DIR variables
include(CMakePackageConfigHelpers) # provides write_basic_package_version_file()


#### Copy header files ####
install(DIRECTORY include/ # trailing slash important to not copy include folder into include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING PATTERN "*.?pp"
)

### cmake files ###
# Create asioConfigVersion.cmake
set( version_config "${CMAKE_CURRENT_BINARY_DIR}/asioConfigVersion.cmake" )
write_basic_package_version_file( "${version_config}"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion )

# Create asioTargets.cmake
install( TARGETS asio
    EXPORT asioConfigTargets
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/asio )
export( TARGETS asio NAMESPACE asio:: FILE asioTargets.cmake )

# Install files
if( WIN32 AND NOT CYGWIN)
    set( CONFIG_LOC CMake )
else( )
    set( CONFIG_LOC "${CMAKE_INSTALL_LIBDIR}/cmake/asio" )
endif( )
install( EXPORT asioConfigTargets
  FILE asioTargets.cmake
  NAMESPACE asio::
  DESTINATION ${CONFIG_LOC} )
install (
  FILES cmake/asioConfig.cmake "${version_config}"
  DESTINATION ${CONFIG_LOC})

message(STATUS "|| Processing project asio - finished\n")
