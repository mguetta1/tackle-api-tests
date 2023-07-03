# coding: utf-8

"""
    MTA 6.2 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ApiFileReport(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'effort': 'int',
        'file': 'str',
        'incidents': 'int',
        'issue_id': 'int'
    }

    attribute_map = {
        'effort': 'effort',
        'file': 'file',
        'incidents': 'incidents',
        'issue_id': 'issueId'
    }

    def __init__(self, effort=None, file=None, incidents=None, issue_id=None, _configuration=None):  # noqa: E501
        """ApiFileReport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._effort = None
        self._file = None
        self._incidents = None
        self._issue_id = None
        self.discriminator = None

        if effort is not None:
            self.effort = effort
        if file is not None:
            self.file = file
        if incidents is not None:
            self.incidents = incidents
        if issue_id is not None:
            self.issue_id = issue_id

    @property
    def effort(self):
        """Gets the effort of this ApiFileReport.  # noqa: E501


        :return: The effort of this ApiFileReport.  # noqa: E501
        :rtype: int
        """
        return self._effort

    @effort.setter
    def effort(self, effort):
        """Sets the effort of this ApiFileReport.


        :param effort: The effort of this ApiFileReport.  # noqa: E501
        :type: int
        """

        self._effort = effort

    @property
    def file(self):
        """Gets the file of this ApiFileReport.  # noqa: E501


        :return: The file of this ApiFileReport.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ApiFileReport.


        :param file: The file of this ApiFileReport.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def incidents(self):
        """Gets the incidents of this ApiFileReport.  # noqa: E501


        :return: The incidents of this ApiFileReport.  # noqa: E501
        :rtype: int
        """
        return self._incidents

    @incidents.setter
    def incidents(self, incidents):
        """Sets the incidents of this ApiFileReport.


        :param incidents: The incidents of this ApiFileReport.  # noqa: E501
        :type: int
        """

        self._incidents = incidents

    @property
    def issue_id(self):
        """Gets the issue_id of this ApiFileReport.  # noqa: E501


        :return: The issue_id of this ApiFileReport.  # noqa: E501
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this ApiFileReport.


        :param issue_id: The issue_id of this ApiFileReport.  # noqa: E501
        :type: int
        """

        self._issue_id = issue_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiFileReport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiFileReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiFileReport):
            return True

        return self.to_dict() != other.to_dict()
