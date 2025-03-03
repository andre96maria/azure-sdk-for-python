# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import pytest

from azure.ai.language.questionanswering.authoring import QuestionAnsweringAuthoringClient
from azure.core.credentials import AzureKeyCredential

from helpers import QnaAuthoringHelper
from testcase import QuestionAnsweringTestCase


class TestCreateAndDeploy(QuestionAnsweringTestCase):

    def test_create_project_aad(self, recorded_test, qna_creds):
        token = self.get_credential(QuestionAnsweringAuthoringClient)
        client = QuestionAnsweringAuthoringClient(qna_creds["qna_endpoint"], token)

        # create project
        project_name = "IssacNewton"
        client.create_project(
            project_name=project_name,
            options={
                "description": "biography of Sir Issac Newton",
                "language": "en",
                "multilingualResource": True,
                "settings": {
                    "defaultAnswer": "no answer"
                }
            })

        # list projects
        qna_projects = client.list_projects()
        found = False
        for p in qna_projects:
            if ("projectName" in p) and p["projectName"] == project_name:
                found = True
        assert found

    def test_create_project(self, recorded_test, qna_creds):
        client = QuestionAnsweringAuthoringClient(qna_creds["qna_endpoint"], AzureKeyCredential(qna_creds["qna_key"]))

        # create project
        project_name = "IssacNewton"
        client.create_project(
            project_name=project_name,
            options={
                "description": "biography of Sir Issac Newton",
                "language": "en",
                "multilingualResource": True,
                "settings": {
                    "defaultAnswer": "no answer"
                }
            })

        # list projects
        qna_projects = client.list_projects()
        found = False
        for p in qna_projects:
            if ("projectName" in p) and p["projectName"] == project_name:
                found = True
        assert found

    def test_deploy_project(self, recorded_test, qna_creds):
        client = QuestionAnsweringAuthoringClient(qna_creds["qna_endpoint"], AzureKeyCredential(qna_creds["qna_key"]))

        # create deployable project
        project_name = "IssacNewton"
        QnaAuthoringHelper.create_test_project(
            client,
            project_name=project_name,
            is_deployable=True,
            **self.kwargs_for_polling,
        )

        # test deploy
        deployment_name = "production"
        deployment_poller = client.begin_deploy_project(
            project_name=project_name,
            deployment_name=deployment_name,
            **self.kwargs_for_polling
        )
        deployment_poller.result()

        # assert
        deployments = client.list_deployments(
            project_name=project_name
        )
        deployment_found = False
        for d in deployments:
            if ("deploymentName" in d) and d["deploymentName"] == deployment_name:
                deployment_found = True
        assert deployment_found
