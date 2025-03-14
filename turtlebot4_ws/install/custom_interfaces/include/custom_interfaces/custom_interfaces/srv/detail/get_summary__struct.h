// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:srv/GetSummary.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__GET_SUMMARY__STRUCT_H_
#define CUSTOM_INTERFACES__SRV__DETAIL__GET_SUMMARY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'get_summary'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/GetSummary in the package custom_interfaces.
typedef struct custom_interfaces__srv__GetSummary_Request
{
  rosidl_runtime_c__String get_summary;
} custom_interfaces__srv__GetSummary_Request;

// Struct for a sequence of custom_interfaces__srv__GetSummary_Request.
typedef struct custom_interfaces__srv__GetSummary_Request__Sequence
{
  custom_interfaces__srv__GetSummary_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__GetSummary_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'summary'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/GetSummary in the package custom_interfaces.
typedef struct custom_interfaces__srv__GetSummary_Response
{
  bool success;
  rosidl_runtime_c__String summary;
} custom_interfaces__srv__GetSummary_Response;

// Struct for a sequence of custom_interfaces__srv__GetSummary_Response.
typedef struct custom_interfaces__srv__GetSummary_Response__Sequence
{
  custom_interfaces__srv__GetSummary_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__GetSummary_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__GET_SUMMARY__STRUCT_H_
