# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network nsg rule show",
)
class Show(AAZCommand):
    """Get the details of a network security group rule.

    :example: Get the details of a network security group rule.
        az network nsg rule show -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule
    """

    _aaz_info = {
        "version": "2018-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networksecuritygroups/{}/securityrules/{}", "2018-11-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.nsg_name = AAZStrArg(
            options=["--nsg-name"],
            help="Name of the network security group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the network security group rule.",
            required=True,
            id_part="child_name_1",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SecurityRulesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SecurityRulesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules/{securityRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkSecurityGroupName", self.ctx.args.nsg_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "securityRuleName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType()
            _schema_on_200.id = AAZStrType()
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties
            properties.access = AAZStrType(
                flags={"required": True},
            )
            properties.description = AAZStrType()
            properties.destination_address_prefix = AAZStrType(
                serialized_name="destinationAddressPrefix",
            )
            properties.destination_address_prefixes = AAZListType(
                serialized_name="destinationAddressPrefixes",
            )
            properties.destination_application_security_groups = AAZListType(
                serialized_name="destinationApplicationSecurityGroups",
            )
            properties.destination_port_range = AAZStrType(
                serialized_name="destinationPortRange",
            )
            properties.destination_port_ranges = AAZListType(
                serialized_name="destinationPortRanges",
            )
            properties.direction = AAZStrType(
                flags={"required": True},
            )
            properties.priority = AAZIntType()
            properties.protocol = AAZStrType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.source_address_prefix = AAZStrType(
                serialized_name="sourceAddressPrefix",
            )
            properties.source_address_prefixes = AAZListType(
                serialized_name="sourceAddressPrefixes",
            )
            properties.source_application_security_groups = AAZListType(
                serialized_name="sourceApplicationSecurityGroups",
            )
            properties.source_port_range = AAZStrType(
                serialized_name="sourcePortRange",
            )
            properties.source_port_ranges = AAZListType(
                serialized_name="sourcePortRanges",
            )

            destination_address_prefixes = cls._schema_on_200.properties.destination_address_prefixes
            destination_address_prefixes.Element = AAZStrType()

            destination_application_security_groups = cls._schema_on_200.properties.destination_application_security_groups
            destination_application_security_groups.Element = AAZObjectType()
            _ShowHelper._build_schema_application_security_group_read(destination_application_security_groups.Element)

            destination_port_ranges = cls._schema_on_200.properties.destination_port_ranges
            destination_port_ranges.Element = AAZStrType()

            source_address_prefixes = cls._schema_on_200.properties.source_address_prefixes
            source_address_prefixes.Element = AAZStrType()

            source_application_security_groups = cls._schema_on_200.properties.source_application_security_groups
            source_application_security_groups.Element = AAZObjectType()
            _ShowHelper._build_schema_application_security_group_read(source_application_security_groups.Element)

            source_port_ranges = cls._schema_on_200.properties.source_port_ranges
            source_port_ranges.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_application_security_group_read = None

    @classmethod
    def _build_schema_application_security_group_read(cls, _schema):
        if cls._schema_application_security_group_read is not None:
            _schema.etag = cls._schema_application_security_group_read.etag
            _schema.id = cls._schema_application_security_group_read.id
            _schema.location = cls._schema_application_security_group_read.location
            _schema.name = cls._schema_application_security_group_read.name
            _schema.properties = cls._schema_application_security_group_read.properties
            _schema.tags = cls._schema_application_security_group_read.tags
            _schema.type = cls._schema_application_security_group_read.type
            return

        cls._schema_application_security_group_read = _schema_application_security_group_read = AAZObjectType()

        application_security_group_read = _schema_application_security_group_read
        application_security_group_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        application_security_group_read.id = AAZStrType()
        application_security_group_read.location = AAZStrType()
        application_security_group_read.name = AAZStrType(
            flags={"read_only": True},
        )
        application_security_group_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        application_security_group_read.tags = AAZDictType()
        application_security_group_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_application_security_group_read.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
            flags={"read_only": True},
        )

        tags = _schema_application_security_group_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_application_security_group_read.etag
        _schema.id = cls._schema_application_security_group_read.id
        _schema.location = cls._schema_application_security_group_read.location
        _schema.name = cls._schema_application_security_group_read.name
        _schema.properties = cls._schema_application_security_group_read.properties
        _schema.tags = cls._schema_application_security_group_read.tags
        _schema.type = cls._schema_application_security_group_read.type


__all__ = ["Show"]
