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


class V1beta1RoleRef(object):
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
        'api_group': 'str',
        'kind': 'str',
        'name': 'str'
    }

    attribute_map = {
        'api_group': 'apiGroup',
        'kind': 'kind',
        'name': 'name'
    }

    def __init__(self, api_group=None, kind=None, name=None):
        """
        V1beta1RoleRef - a model defined in Swagger
        """

        self._api_group = None
        self._kind = None
        self._name = None
        self.discriminator = None

        self.api_group = api_group
        self.kind = kind
        self.name = name

    @property
    def api_group(self):
        """
        Gets the api_group of this V1beta1RoleRef.
        APIGroup is the group for the resource being referenced

        :return: The api_group of this V1beta1RoleRef.
        :rtype: str
        """
        return self._api_group

    @api_group.setter
    def api_group(self, api_group):
        """
        Sets the api_group of this V1beta1RoleRef.
        APIGroup is the group for the resource being referenced

        :param api_group: The api_group of this V1beta1RoleRef.
        :type: str
        """
        if api_group is None:
            raise ValueError("Invalid value for `api_group`, must not be `None`")

        self._api_group = api_group

    @property
    def kind(self):
        """
        Gets the kind of this V1beta1RoleRef.
        Kind is the type of resource being referenced

        :return: The kind of this V1beta1RoleRef.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta1RoleRef.
        Kind is the type of resource being referenced

        :param kind: The kind of this V1beta1RoleRef.
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1beta1RoleRef.
        Name is the name of resource being referenced

        :return: The name of this V1beta1RoleRef.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1RoleRef.
        Name is the name of resource being referenced

        :param name: The name of this V1beta1RoleRef.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, V1beta1RoleRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
