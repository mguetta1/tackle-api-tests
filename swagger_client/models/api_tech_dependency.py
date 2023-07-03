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


class ApiTechDependency(object):
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
        'create_time': 'str',
        'create_user': 'str',
        'id': 'int',
        'indirect': 'bool',
        'labels': 'list[str]',
        'name': 'str',
        'sha': 'str',
        'update_user': 'str',
        'version': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'create_user': 'createUser',
        'id': 'id',
        'indirect': 'indirect',
        'labels': 'labels',
        'name': 'name',
        'sha': 'sha',
        'update_user': 'updateUser',
        'version': 'version'
    }

    def __init__(self, create_time=None, create_user=None, id=None, indirect=None, labels=None, name=None, sha=None, update_user=None, version=None, _configuration=None):  # noqa: E501
        """ApiTechDependency - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._create_user = None
        self._id = None
        self._indirect = None
        self._labels = None
        self._name = None
        self._sha = None
        self._update_user = None
        self._version = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if id is not None:
            self.id = id
        if indirect is not None:
            self.indirect = indirect
        if labels is not None:
            self.labels = labels
        self.name = name
        if sha is not None:
            self.sha = sha
        if update_user is not None:
            self.update_user = update_user
        if version is not None:
            self.version = version

    @property
    def create_time(self):
        """Gets the create_time of this ApiTechDependency.  # noqa: E501


        :return: The create_time of this ApiTechDependency.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiTechDependency.


        :param create_time: The create_time of this ApiTechDependency.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiTechDependency.  # noqa: E501


        :return: The create_user of this ApiTechDependency.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiTechDependency.


        :param create_user: The create_user of this ApiTechDependency.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def id(self):
        """Gets the id of this ApiTechDependency.  # noqa: E501


        :return: The id of this ApiTechDependency.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTechDependency.


        :param id: The id of this ApiTechDependency.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def indirect(self):
        """Gets the indirect of this ApiTechDependency.  # noqa: E501


        :return: The indirect of this ApiTechDependency.  # noqa: E501
        :rtype: bool
        """
        return self._indirect

    @indirect.setter
    def indirect(self, indirect):
        """Sets the indirect of this ApiTechDependency.


        :param indirect: The indirect of this ApiTechDependency.  # noqa: E501
        :type: bool
        """

        self._indirect = indirect

    @property
    def labels(self):
        """Gets the labels of this ApiTechDependency.  # noqa: E501


        :return: The labels of this ApiTechDependency.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ApiTechDependency.


        :param labels: The labels of this ApiTechDependency.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this ApiTechDependency.  # noqa: E501


        :return: The name of this ApiTechDependency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiTechDependency.


        :param name: The name of this ApiTechDependency.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sha(self):
        """Gets the sha of this ApiTechDependency.  # noqa: E501


        :return: The sha of this ApiTechDependency.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this ApiTechDependency.


        :param sha: The sha of this ApiTechDependency.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def update_user(self):
        """Gets the update_user of this ApiTechDependency.  # noqa: E501


        :return: The update_user of this ApiTechDependency.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiTechDependency.


        :param update_user: The update_user of this ApiTechDependency.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

    @property
    def version(self):
        """Gets the version of this ApiTechDependency.  # noqa: E501


        :return: The version of this ApiTechDependency.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiTechDependency.


        :param version: The version of this ApiTechDependency.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ApiTechDependency, dict):
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
        if not isinstance(other, ApiTechDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiTechDependency):
            return True

        return self.to_dict() != other.to_dict()
