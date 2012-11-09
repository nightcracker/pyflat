#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
SET(CMAKE_IMPORT_FILE_VERSION 1)

# Compute the installation prefix relative to this file.
GET_FILENAME_COMPONENT(_IMPORT_PREFIX "${CMAKE_CURRENT_LIST_FILE}" PATH)
GET_FILENAME_COMPONENT(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
GET_FILENAME_COMPONENT(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)

# Import target "png15" for configuration "MinSizeRel"
SET_PROPERTY(TARGET png15 APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
SET_TARGET_PROPERTIES(png15 PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/libpng15.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_MINSIZEREL "C:/programming/python/pyflat/c/zlib-1.2.7/build/Release/zlib.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/libpng15.dll"
  )

LIST(APPEND _IMPORT_CHECK_TARGETS png15 )
LIST(APPEND _IMPORT_CHECK_FILES_FOR_png15 "${_IMPORT_PREFIX}/lib/libpng15.lib" "${_IMPORT_PREFIX}/bin/libpng15.dll" )

# Import target "png15_static" for configuration "MinSizeRel"
SET_PROPERTY(TARGET png15_static APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
SET_TARGET_PROPERTIES(png15_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_MINSIZEREL "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_MINSIZEREL "C:/programming/python/pyflat/c/zlib-1.2.7/build/Release/zlib.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/lib/libpng15_static.lib"
  )

LIST(APPEND _IMPORT_CHECK_TARGETS png15_static )
LIST(APPEND _IMPORT_CHECK_FILES_FOR_png15_static "${_IMPORT_PREFIX}/lib/libpng15_static.lib" )

# Loop over all imported files and verify that they actually exist
FOREACH(target ${_IMPORT_CHECK_TARGETS} )
  FOREACH(file ${_IMPORT_CHECK_FILES_FOR_${target}} )
    IF(NOT EXISTS "${file}" )
      MESSAGE(FATAL_ERROR "The imported target \"${target}\" references the file
   \"${file}\"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   \"${CMAKE_CURRENT_LIST_FILE}\"
but not all the files it references.
")
    ENDIF()
  ENDFOREACH()
  UNSET(_IMPORT_CHECK_FILES_FOR_${target})
ENDFOREACH()
UNSET(_IMPORT_CHECK_TARGETS)

# Cleanup temporary variables.
SET(_IMPORT_PREFIX)

# Commands beyond this point should not need to know the version.
SET(CMAKE_IMPORT_FILE_VERSION)
