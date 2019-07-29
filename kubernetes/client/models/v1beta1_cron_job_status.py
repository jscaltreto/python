# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CronJobStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'active': 'list[V1ObjectReference]',
        'last_schedule_time': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'last_schedule_time': 'lastScheduleTime'
    }

    def __init__(self, active=None, last_schedule_time=None):
        """
        V1beta1CronJobStatus - a model defined in Swagger
        """

        self._active = None
        self._last_schedule_time = None
        self.discriminator = None

        if active is not None:
          self.active = active
        if last_schedule_time is not None:
          self.last_schedule_time = last_schedule_time

    @property
    def active(self):
        """
        Gets the active of this V1beta1CronJobStatus.
        A list of pointers to currently running jobs.

        :return: The active of this V1beta1CronJobStatus.
        :rtype: list[V1ObjectReference]
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this V1beta1CronJobStatus.
        A list of pointers to currently running jobs.

        :param active: The active of this V1beta1CronJobStatus.
        :type: list[V1ObjectReference]
        """

        self._active = active

    @property
    def last_schedule_time(self):
        """
        Gets the last_schedule_time of this V1beta1CronJobStatus.
        Information when was the last time the job was successfully scheduled.

        :return: The last_schedule_time of this V1beta1CronJobStatus.
        :rtype: datetime
        """
        return self._last_schedule_time

    @last_schedule_time.setter
    def last_schedule_time(self, last_schedule_time):
        """
        Sets the last_schedule_time of this V1beta1CronJobStatus.
        Information when was the last time the job was successfully scheduled.

        :param last_schedule_time: The last_schedule_time of this V1beta1CronJobStatus.
        :type: datetime
        """

        self._last_schedule_time = last_schedule_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1CronJobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
