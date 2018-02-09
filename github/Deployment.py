# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
# ##############################################################################

import github.GithubObject
import github.PaginatedList

import github.GitCommit
import github.NamedUser


class Deployment(github.GithubObject.CompletableGithubObject):
    """
    This class represents Commits. The reference can be found here http://developer.github.com/v3/git/repos/deployments/
    """

    def __repr__(self):
        return self.get__repr__({"sha": self._sha.value})

    @property
    def auto_merge(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._auto_merge)
        return self._NoneIfNotSet(self._auto_merge)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def environment(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._environment)
        return self._NoneIfNotSet(self._environment)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def payload(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._payload)
        return self._NoneIfNotSet(self._payload)

    @property
    def production_environment(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._production_environment)
        return self._NoneIfNotSet(self._production_environment)

    @property
    def sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._sha)
        return self._NoneIfNotSet(self._sha)

    @property
    def task(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._task)
        return self._NoneIfNotSet(self._task)

    @property
    def transient_environment(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._transient_environment)
        return self._NoneIfNotSet(self._transient_environment)

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def _identity(self):
        return self.id

    def _initAttributes(self):
        self._auto_merge = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._environment = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._payload = github.GithubObject.NotSet
        self._production_environment = github.GithubObject.NotSet
        self._sha = github.GithubObject.NotSet
        self._task = github.GithubObject.NotSet
        self._task = github.GithubObject.NotSet
        self._transient_environment = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "auto_merge" in attributes:  # pragma no branch
            assert attributes["auto_merge"] is None or isinstance(
                attributes["auto_merge"], bool), attributes["auto_merge"]
            self._auto_merge = attributes["auto_merge"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(
                attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(
                attributes["description"], (str, unicode)), attributes["description"]
            self._description = attributes["description"]
        if "environment" in attributes:  # pragma no branch
            assert attributes["environment"] is None or isinstance(
                attributes["environment"], (str, unicode)), attributes["environment"]
            self._environment = attributes["environment"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "payload" in attributes:  # pragma no branch
            assert attributes["payload"] is None or isinstance(
                attributes["payload"], (str, unicode)), attributes["payload"]
            self._payload = attributes["payload"]
        if "production_environment" in attributes:  # pragma no branch
            assert attributes["production_environment"] is None or isinstance(
                attributes["production_environment"], bool), attributes["production_environment"]
            self._production_environment = attributes["production_environment"]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "task" in attributes:  # pragma no branch
            assert attributes["task"] is None or isinstance(attributes["task"], (str, unicode)), attributes["task"]
            self._task = attributes["task"]
