# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.31
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1ResourceHealth(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'health': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'health': 'health',
        'resource_id': 'resourceID'
    }

    def __init__(self, health=None, resource_id=None, local_vars_configuration=None):  # noqa: E501
        """V1ResourceHealth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._health = None
        self._resource_id = None
        self.discriminator = None

        if health is not None:
            self.health = health
        self.resource_id = resource_id

    @property
    def health(self):
        """Gets the health of this V1ResourceHealth.  # noqa: E501

        Health of the resource. can be one of:  - Healthy: operates as normal  - Unhealthy: reported unhealthy. We consider this a temporary health issue               since we do not have a mechanism today to distinguish               temporary and permanent issues.  - Unknown: The status cannot be determined.             For example, Device Plugin got unregistered and hasn't been re-registered since.  In future we may want to introduce the PermanentlyUnhealthy Status.  # noqa: E501

        :return: The health of this V1ResourceHealth.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this V1ResourceHealth.

        Health of the resource. can be one of:  - Healthy: operates as normal  - Unhealthy: reported unhealthy. We consider this a temporary health issue               since we do not have a mechanism today to distinguish               temporary and permanent issues.  - Unknown: The status cannot be determined.             For example, Device Plugin got unregistered and hasn't been re-registered since.  In future we may want to introduce the PermanentlyUnhealthy Status.  # noqa: E501

        :param health: The health of this V1ResourceHealth.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def resource_id(self):
        """Gets the resource_id of this V1ResourceHealth.  # noqa: E501

        ResourceID is the unique identifier of the resource. See the ResourceID type for more information.  # noqa: E501

        :return: The resource_id of this V1ResourceHealth.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this V1ResourceHealth.

        ResourceID is the unique identifier of the resource. See the ResourceID type for more information.  # noqa: E501

        :param resource_id: The resource_id of this V1ResourceHealth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_id is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ResourceHealth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ResourceHealth):
            return True

        return self.to_dict() != other.to_dict()