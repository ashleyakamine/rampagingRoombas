// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_interfaces:srv/GetSummary.idl
// generated code does not contain a copyright notice
#include "custom_interfaces/srv/detail/get_summary__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `get_summary`
#include "rosidl_runtime_c/string_functions.h"

bool
custom_interfaces__srv__GetSummary_Request__init(custom_interfaces__srv__GetSummary_Request * msg)
{
  if (!msg) {
    return false;
  }
  // get_summary
  if (!rosidl_runtime_c__String__init(&msg->get_summary)) {
    custom_interfaces__srv__GetSummary_Request__fini(msg);
    return false;
  }
  return true;
}

void
custom_interfaces__srv__GetSummary_Request__fini(custom_interfaces__srv__GetSummary_Request * msg)
{
  if (!msg) {
    return;
  }
  // get_summary
  rosidl_runtime_c__String__fini(&msg->get_summary);
}

bool
custom_interfaces__srv__GetSummary_Request__are_equal(const custom_interfaces__srv__GetSummary_Request * lhs, const custom_interfaces__srv__GetSummary_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // get_summary
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->get_summary), &(rhs->get_summary)))
  {
    return false;
  }
  return true;
}

bool
custom_interfaces__srv__GetSummary_Request__copy(
  const custom_interfaces__srv__GetSummary_Request * input,
  custom_interfaces__srv__GetSummary_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // get_summary
  if (!rosidl_runtime_c__String__copy(
      &(input->get_summary), &(output->get_summary)))
  {
    return false;
  }
  return true;
}

custom_interfaces__srv__GetSummary_Request *
custom_interfaces__srv__GetSummary_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__srv__GetSummary_Request * msg = (custom_interfaces__srv__GetSummary_Request *)allocator.allocate(sizeof(custom_interfaces__srv__GetSummary_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interfaces__srv__GetSummary_Request));
  bool success = custom_interfaces__srv__GetSummary_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interfaces__srv__GetSummary_Request__destroy(custom_interfaces__srv__GetSummary_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interfaces__srv__GetSummary_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interfaces__srv__GetSummary_Request__Sequence__init(custom_interfaces__srv__GetSummary_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__srv__GetSummary_Request * data = NULL;

  if (size) {
    data = (custom_interfaces__srv__GetSummary_Request *)allocator.zero_allocate(size, sizeof(custom_interfaces__srv__GetSummary_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interfaces__srv__GetSummary_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interfaces__srv__GetSummary_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_interfaces__srv__GetSummary_Request__Sequence__fini(custom_interfaces__srv__GetSummary_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_interfaces__srv__GetSummary_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_interfaces__srv__GetSummary_Request__Sequence *
custom_interfaces__srv__GetSummary_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__srv__GetSummary_Request__Sequence * array = (custom_interfaces__srv__GetSummary_Request__Sequence *)allocator.allocate(sizeof(custom_interfaces__srv__GetSummary_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interfaces__srv__GetSummary_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interfaces__srv__GetSummary_Request__Sequence__destroy(custom_interfaces__srv__GetSummary_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interfaces__srv__GetSummary_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interfaces__srv__GetSummary_Request__Sequence__are_equal(const custom_interfaces__srv__GetSummary_Request__Sequence * lhs, const custom_interfaces__srv__GetSummary_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interfaces__srv__GetSummary_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interfaces__srv__GetSummary_Request__Sequence__copy(
  const custom_interfaces__srv__GetSummary_Request__Sequence * input,
  custom_interfaces__srv__GetSummary_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interfaces__srv__GetSummary_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interfaces__srv__GetSummary_Request * data =
      (custom_interfaces__srv__GetSummary_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interfaces__srv__GetSummary_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interfaces__srv__GetSummary_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interfaces__srv__GetSummary_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `summary`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
custom_interfaces__srv__GetSummary_Response__init(custom_interfaces__srv__GetSummary_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // summary
  if (!rosidl_runtime_c__String__init(&msg->summary)) {
    custom_interfaces__srv__GetSummary_Response__fini(msg);
    return false;
  }
  return true;
}

void
custom_interfaces__srv__GetSummary_Response__fini(custom_interfaces__srv__GetSummary_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // summary
  rosidl_runtime_c__String__fini(&msg->summary);
}

bool
custom_interfaces__srv__GetSummary_Response__are_equal(const custom_interfaces__srv__GetSummary_Response * lhs, const custom_interfaces__srv__GetSummary_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // summary
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->summary), &(rhs->summary)))
  {
    return false;
  }
  return true;
}

bool
custom_interfaces__srv__GetSummary_Response__copy(
  const custom_interfaces__srv__GetSummary_Response * input,
  custom_interfaces__srv__GetSummary_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // summary
  if (!rosidl_runtime_c__String__copy(
      &(input->summary), &(output->summary)))
  {
    return false;
  }
  return true;
}

custom_interfaces__srv__GetSummary_Response *
custom_interfaces__srv__GetSummary_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__srv__GetSummary_Response * msg = (custom_interfaces__srv__GetSummary_Response *)allocator.allocate(sizeof(custom_interfaces__srv__GetSummary_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interfaces__srv__GetSummary_Response));
  bool success = custom_interfaces__srv__GetSummary_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interfaces__srv__GetSummary_Response__destroy(custom_interfaces__srv__GetSummary_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interfaces__srv__GetSummary_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interfaces__srv__GetSummary_Response__Sequence__init(custom_interfaces__srv__GetSummary_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__srv__GetSummary_Response * data = NULL;

  if (size) {
    data = (custom_interfaces__srv__GetSummary_Response *)allocator.zero_allocate(size, sizeof(custom_interfaces__srv__GetSummary_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interfaces__srv__GetSummary_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interfaces__srv__GetSummary_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_interfaces__srv__GetSummary_Response__Sequence__fini(custom_interfaces__srv__GetSummary_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_interfaces__srv__GetSummary_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_interfaces__srv__GetSummary_Response__Sequence *
custom_interfaces__srv__GetSummary_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__srv__GetSummary_Response__Sequence * array = (custom_interfaces__srv__GetSummary_Response__Sequence *)allocator.allocate(sizeof(custom_interfaces__srv__GetSummary_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interfaces__srv__GetSummary_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interfaces__srv__GetSummary_Response__Sequence__destroy(custom_interfaces__srv__GetSummary_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interfaces__srv__GetSummary_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interfaces__srv__GetSummary_Response__Sequence__are_equal(const custom_interfaces__srv__GetSummary_Response__Sequence * lhs, const custom_interfaces__srv__GetSummary_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interfaces__srv__GetSummary_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interfaces__srv__GetSummary_Response__Sequence__copy(
  const custom_interfaces__srv__GetSummary_Response__Sequence * input,
  custom_interfaces__srv__GetSummary_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interfaces__srv__GetSummary_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interfaces__srv__GetSummary_Response * data =
      (custom_interfaces__srv__GetSummary_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interfaces__srv__GetSummary_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interfaces__srv__GetSummary_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interfaces__srv__GetSummary_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
