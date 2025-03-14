// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/GetSummary.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__GET_SUMMARY__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__GET_SUMMARY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/srv/detail/get_summary__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_GetSummary_Request_get_summary
{
public:
  Init_GetSummary_Request_get_summary()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::GetSummary_Request get_summary(::custom_interfaces::srv::GetSummary_Request::_get_summary_type arg)
  {
    msg_.get_summary = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::GetSummary_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::GetSummary_Request>()
{
  return custom_interfaces::srv::builder::Init_GetSummary_Request_get_summary();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_GetSummary_Response_summary
{
public:
  explicit Init_GetSummary_Response_summary(::custom_interfaces::srv::GetSummary_Response & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::srv::GetSummary_Response summary(::custom_interfaces::srv::GetSummary_Response::_summary_type arg)
  {
    msg_.summary = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::GetSummary_Response msg_;
};

class Init_GetSummary_Response_success
{
public:
  Init_GetSummary_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetSummary_Response_summary success(::custom_interfaces::srv::GetSummary_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_GetSummary_Response_summary(msg_);
  }

private:
  ::custom_interfaces::srv::GetSummary_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::GetSummary_Response>()
{
  return custom_interfaces::srv::builder::Init_GetSummary_Response_success();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__GET_SUMMARY__BUILDER_HPP_
