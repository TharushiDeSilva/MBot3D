# Install script for directory: /home/tharushi/MBot3D/src/octomap-devel/octomap

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/octomap" TYPE FILE FILES
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/AbstractOcTree.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/AbstractOccupancyOcTree.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/ColorOcTree.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/CountingOcTree.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/MCTables.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/MapCollection.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/MapNode.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTree.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeBase.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeBaseImpl.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeDataNode.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeKey.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeNode.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeStamped.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OccupancyOcTreeBase.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/Pointcloud.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/ScanGraph.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/octomap.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/octomap_deprecated.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/octomap_timing.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/octomap_types.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/octomap_utils.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/MapCollection.hxx"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/MapNode.hxx"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeBaseImpl.hxx"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeDataNode.hxx"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OcTreeIterator.hxx"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/OccupancyOcTreeBase.hxx"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/octomap/math" TYPE FILE FILES
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/math/Pose6D.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/math/Quaternion.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/math/Utils.h"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/include/octomap/math/Vector3.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/octomap" TYPE FILE FILES "/home/tharushi/MBot3D/src/octomap-devel/octomap/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/octomap" TYPE FILE FILES
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/build/InstallFiles/octomap-config.cmake"
    "/home/tharushi/MBot3D/src/octomap-devel/octomap/build/InstallFiles/octomap-config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/tharushi/MBot3D/src/octomap-devel/octomap/build/lib/pkgconfig/octomap.pc")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/tharushi/MBot3D/src/octomap-devel/octomap/build/src/math/cmake_install.cmake")
  include("/home/tharushi/MBot3D/src/octomap-devel/octomap/build/src/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/tharushi/MBot3D/src/octomap-devel/octomap/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
