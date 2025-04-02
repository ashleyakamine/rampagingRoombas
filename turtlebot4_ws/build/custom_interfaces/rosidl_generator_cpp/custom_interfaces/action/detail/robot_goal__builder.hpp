// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:action/RobotGoal.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__ACTION__DETAIL__ROBOT_GOAL__BUILDER_HPP_
#define CUSTOM_INTERFACES__ACTION__DETAIL__ROBOT_GOAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/action/detail/robot_goal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_Goal_goal_theta
{
public:
  explicit Init_RobotGoal_Goal_goal_theta(::custom_interfaces::action::RobotGoal_Goal & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::action::RobotGoal_Goal goal_theta(::custom_interfaces::action::RobotGoal_Goal::_goal_theta_type arg)
  {
    msg_.goal_theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Goal msg_;
};

class Init_RobotGoal_Goal_goal_y
{
public:
  explicit Init_RobotGoal_Goal_goal_y(::custom_interfaces::action::RobotGoal_Goal & msg)
  : msg_(msg)
  {}
  Init_RobotGoal_Goal_goal_theta goal_y(::custom_interfaces::action::RobotGoal_Goal::_goal_y_type arg)
  {
    msg_.goal_y = std::move(arg);
    return Init_RobotGoal_Goal_goal_theta(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Goal msg_;
};

class Init_RobotGoal_Goal_goal_x
{
public:
  Init_RobotGoal_Goal_goal_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotGoal_Goal_goal_y goal_x(::custom_interfaces::action::RobotGoal_Goal::_goal_x_type arg)
  {
    msg_.goal_x = std::move(arg);
    return Init_RobotGoal_Goal_goal_y(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_Goal>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_Goal_goal_x();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_Result_success
{
public:
  Init_RobotGoal_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::action::RobotGoal_Result success(::custom_interfaces::action::RobotGoal_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_Result>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_Result_success();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_Feedback_distance_from_goal
{
public:
  explicit Init_RobotGoal_Feedback_distance_from_goal(::custom_interfaces::action::RobotGoal_Feedback & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::action::RobotGoal_Feedback distance_from_goal(::custom_interfaces::action::RobotGoal_Feedback::_distance_from_goal_type arg)
  {
    msg_.distance_from_goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Feedback msg_;
};

class Init_RobotGoal_Feedback_current_theta
{
public:
  explicit Init_RobotGoal_Feedback_current_theta(::custom_interfaces::action::RobotGoal_Feedback & msg)
  : msg_(msg)
  {}
  Init_RobotGoal_Feedback_distance_from_goal current_theta(::custom_interfaces::action::RobotGoal_Feedback::_current_theta_type arg)
  {
    msg_.current_theta = std::move(arg);
    return Init_RobotGoal_Feedback_distance_from_goal(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Feedback msg_;
};

class Init_RobotGoal_Feedback_current_y
{
public:
  explicit Init_RobotGoal_Feedback_current_y(::custom_interfaces::action::RobotGoal_Feedback & msg)
  : msg_(msg)
  {}
  Init_RobotGoal_Feedback_current_theta current_y(::custom_interfaces::action::RobotGoal_Feedback::_current_y_type arg)
  {
    msg_.current_y = std::move(arg);
    return Init_RobotGoal_Feedback_current_theta(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Feedback msg_;
};

class Init_RobotGoal_Feedback_current_x
{
public:
  Init_RobotGoal_Feedback_current_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotGoal_Feedback_current_y current_x(::custom_interfaces::action::RobotGoal_Feedback::_current_x_type arg)
  {
    msg_.current_x = std::move(arg);
    return Init_RobotGoal_Feedback_current_y(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_Feedback>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_Feedback_current_x();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_SendGoal_Request_goal
{
public:
  explicit Init_RobotGoal_SendGoal_Request_goal(::custom_interfaces::action::RobotGoal_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::action::RobotGoal_SendGoal_Request goal(::custom_interfaces::action::RobotGoal_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_SendGoal_Request msg_;
};

class Init_RobotGoal_SendGoal_Request_goal_id
{
public:
  Init_RobotGoal_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotGoal_SendGoal_Request_goal goal_id(::custom_interfaces::action::RobotGoal_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotGoal_SendGoal_Request_goal(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_SendGoal_Request>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_SendGoal_Request_goal_id();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_SendGoal_Response_stamp
{
public:
  explicit Init_RobotGoal_SendGoal_Response_stamp(::custom_interfaces::action::RobotGoal_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::action::RobotGoal_SendGoal_Response stamp(::custom_interfaces::action::RobotGoal_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_SendGoal_Response msg_;
};

class Init_RobotGoal_SendGoal_Response_accepted
{
public:
  Init_RobotGoal_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotGoal_SendGoal_Response_stamp accepted(::custom_interfaces::action::RobotGoal_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_RobotGoal_SendGoal_Response_stamp(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_SendGoal_Response>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_SendGoal_Response_accepted();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_GetResult_Request_goal_id
{
public:
  Init_RobotGoal_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::action::RobotGoal_GetResult_Request goal_id(::custom_interfaces::action::RobotGoal_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_GetResult_Request>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_GetResult_Request_goal_id();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_GetResult_Response_result
{
public:
  explicit Init_RobotGoal_GetResult_Response_result(::custom_interfaces::action::RobotGoal_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::action::RobotGoal_GetResult_Response result(::custom_interfaces::action::RobotGoal_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_GetResult_Response msg_;
};

class Init_RobotGoal_GetResult_Response_status
{
public:
  Init_RobotGoal_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotGoal_GetResult_Response_result status(::custom_interfaces::action::RobotGoal_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_RobotGoal_GetResult_Response_result(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_GetResult_Response>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_GetResult_Response_status();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace action
{

namespace builder
{

class Init_RobotGoal_FeedbackMessage_feedback
{
public:
  explicit Init_RobotGoal_FeedbackMessage_feedback(::custom_interfaces::action::RobotGoal_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::action::RobotGoal_FeedbackMessage feedback(::custom_interfaces::action::RobotGoal_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_FeedbackMessage msg_;
};

class Init_RobotGoal_FeedbackMessage_goal_id
{
public:
  Init_RobotGoal_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotGoal_FeedbackMessage_feedback goal_id(::custom_interfaces::action::RobotGoal_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotGoal_FeedbackMessage_feedback(msg_);
  }

private:
  ::custom_interfaces::action::RobotGoal_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::action::RobotGoal_FeedbackMessage>()
{
  return custom_interfaces::action::builder::Init_RobotGoal_FeedbackMessage_goal_id();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__ACTION__DETAIL__ROBOT_GOAL__BUILDER_HPP_
