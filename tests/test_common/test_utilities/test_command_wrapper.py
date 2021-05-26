import sys
from unittest import TestCase

from cloudshell.shell.core.driver_context import (
    ConnectivityContext,
    ReservationContextDetails,
    ResourceCommandContext,
    ResourceContextDetails,
)

from cloudshell.cp.vcenter.common.wrappers.command_wrapper import CommandWrapper

if sys.version_info >= (3, 0):
    from unittest.mock import MagicMock, create_autospec, patch
else:
    from mock import MagicMock, create_autospec, patch


class TestCommandWrapper(TestCase):
    def setUp(self):
        self.si = MagicMock()
        self.logger = MagicMock()
        self.pv_service = MagicMock()
        self.pv_service.connect = MagicMock(return_value=self.si)
        self.cloud_shell_helper = MagicMock()
        self.resource_model_parser = MagicMock()

    def test_execute_command_with_params_and_vcetner_data_model_with_session_inject(
        self,
    ):
        # arrange
        def fake_command_with_connection_return_true_1(
            si, vcenter_data_model, session, fake1, fake2
        ):
            return True

        def fake_command_with_connection_return_true_2(
            si, session, vcenter_data_model, fake1, fake2
        ):
            return True

        with patch(
            "cloudshell.cp.vcenter.common.wrappers.command_wrapper.CloudShellSessionContext"
        ) as session:
            wrapper = CommandWrapper(
                pv_service=self.pv_service,
                resource_model_parser=self.resource_model_parser,
                context_based_logger_factory=MagicMock(),
            )
            context = self._create_resource_command_context()

            # act
            res_1 = wrapper.execute_command_with_connection(
                context, fake_command_with_connection_return_true_1, "param 1", "param2"
            )
            res_2 = wrapper.execute_command_with_connection(
                context, fake_command_with_connection_return_true_2, "param 1", "param2"
            )
            # assert
            self.assertTrue(res_1)
            self.assertTrue(res_2)

    def test_execute_command_with_params_and_vcetner_data_model_inject(self):
        # arrange
        def fake_command_with_connection_return_true(
            si, vcenter_data_model, fake1, fake2
        ):
            return True

        with patch(
            "cloudshell.cp.vcenter.common.wrappers.command_wrapper.CloudShellSessionContext"
        ) as session:
            wrapper = CommandWrapper(
                pv_service=self.pv_service,
                resource_model_parser=self.resource_model_parser,
                context_based_logger_factory=MagicMock(),
            )
            context = self._create_resource_command_context()

            # act
            res = wrapper.execute_command_with_connection(
                context, fake_command_with_connection_return_true, "param 1", "param2"
            )
            # assert
            self.assertTrue(res)

    def test_execute_command_with_params_and_session_inject(self):
        # arrange
        def fake_command_with_connection_return_true(si, session, fake1, fake2):
            return True

        with patch(
            "cloudshell.cp.vcenter.common.wrappers.command_wrapper.CloudShellSessionContext"
        ) as session:
            wrapper = CommandWrapper(
                pv_service=self.pv_service,
                resource_model_parser=self.resource_model_parser,
                context_based_logger_factory=MagicMock(),
            )
            context = self._create_resource_command_context()

            # act
            res = wrapper.execute_command_with_connection(
                context, fake_command_with_connection_return_true, "param 1", "param2"
            )
            # assert
            self.assertTrue(res)

    def test_execute_command_with_params(self):
        # arrange
        def fake_command_with_connection_return_true(si, fake1, fake2):
            return True

        with patch(
            "cloudshell.cp.vcenter.common.wrappers.command_wrapper.CloudShellSessionContext"
        ) as session:
            wrapper = CommandWrapper(
                pv_service=self.pv_service,
                resource_model_parser=self.resource_model_parser,
                context_based_logger_factory=MagicMock(),
            )
            context = self._create_resource_command_context()

            # act
            res = wrapper.execute_command_with_connection(
                context, fake_command_with_connection_return_true, "param 1", "param2"
            )
            # assert
            self.assertTrue(res)
            session.assert_called_with(context)

    def _create_resource_command_context(self):
        context = create_autospec(ResourceCommandContext)
        context.reservation = create_autospec(ReservationContextDetails)
        context.reservation.reservation_id = "test_resrvation"
        context.reservation.domain = "Global"
        context.resource = create_autospec(ResourceContextDetails)
        context.resource.name = "vCenter VMWare"
        context.resource.user = "uzer"
        context.resource.address = "127.0.0.1"
        context.connectivity = create_autospec(ConnectivityContext)
        context.connectivity.server_address = "127.0.0.1"
        context.connectivity.admin_auth_token = "token"
        return context
