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


class PolicyV1beta1HostPortRange(object):
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
        'max': 'int',
        'min': 'int'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, max=None, min=None):
        """
        PolicyV1beta1HostPortRange - a model defined in Swagger
        """

        self._max = None
        self._min = None
        self.discriminator = None

        self.max = max
        self.min = min

    @property
    def max(self):
        """
        Gets the max of this PolicyV1beta1HostPortRange.
        max is the end of the range, inclusive.

        :return: The max of this PolicyV1beta1HostPortRange.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this PolicyV1beta1HostPortRange.
        max is the end of the range, inclusive.

        :param max: The max of this PolicyV1beta1HostPortRange.
        :type: int
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")

        self._max = max

    @property
    def min(self):
        """
        Gets the min of this PolicyV1beta1HostPortRange.
        min is the start of the range, inclusive.

        :return: The min of this PolicyV1beta1HostPortRange.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this PolicyV1beta1HostPortRange.
        min is the start of the range, inclusive.

        :param min: The min of this PolicyV1beta1HostPortRange.
        :type: int
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")

        self._min = min

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
        if not isinstance(other, PolicyV1beta1HostPortRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
