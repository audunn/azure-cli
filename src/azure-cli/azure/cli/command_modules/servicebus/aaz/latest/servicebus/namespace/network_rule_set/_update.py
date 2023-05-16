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
    "servicebus namespace network-rule-set update",
)
class Update(AAZCommand):
    """Update NetworkRuleSet for a Namespace.
    """

    _aaz_info = {
        "version": "2022-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.servicebus/namespaces/{}/networkrulesets/default", "2022-10-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The namespace name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.default_action = AAZStrArg(
            options=["--default-action"],
            arg_group="Properties",
            help="Default Action for Network Rule Set",
            nullable=True,
            enum={"Allow": "Allow", "Deny": "Deny"},
        )
        _args_schema.ip_rules = AAZListArg(
            options=["--ip-rules"],
            arg_group="Properties",
            help="List of IpRules",
            nullable=True,
        )
        _args_schema.public_network_access = AAZStrArg(
            options=["--public-network-access"],
            arg_group="Properties",
            help="This determines if traffic is allowed over public network. By default it is enabled.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.enable_trusted_service_access = AAZBoolArg(
            options=["-t", "--enable-trusted-service-access"],
            arg_group="Properties",
            help="Value that indicates whether Trusted Service Access is Enabled or not.",
            nullable=True,
        )
        _args_schema.virtual_network_rules = AAZListArg(
            options=["--virtual-network-rules"],
            arg_group="Properties",
            help="List VirtualNetwork Rules",
            nullable=True,
        )

        ip_rules = cls._args_schema.ip_rules
        ip_rules.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.ip_rules.Element
        _element.action = AAZStrArg(
            options=["action"],
            help="The IP Filter Action",
            nullable=True,
            enum={"Allow": "Allow"},
        )
        _element.ip_address = AAZStrArg(
            options=["ip-address"],
            help="IP Mask",
            nullable=True,
        )

        virtual_network_rules = cls._args_schema.virtual_network_rules
        virtual_network_rules.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.virtual_network_rules.Element
        _element.ignore_missing_endpoint = AAZBoolArg(
            options=["missing-endpoint", "ignore-missing-endpoint"],
            help="Value that indicates whether to ignore missing VNet Service Endpoint",
            nullable=True,
        )
        _element.subnet = AAZStrArg(
            options=["subnet"],
            help="Resource ID of Virtual Network Subnet",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NamespacesGetNetworkRuleSet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.NamespacesCreateOrUpdateNetworkRuleSet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NamespacesGetNetworkRuleSet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/networkRuleSets/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2022-10-01-preview",
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
            _UpdateHelper._build_schema_network_rule_set_read(cls._schema_on_200)

            return cls._schema_on_200

    class NamespacesCreateOrUpdateNetworkRuleSet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/networkRuleSets/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2022-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

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
            _UpdateHelper._build_schema_network_rule_set_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("defaultAction", AAZStrType, ".default_action")
                properties.set_prop("ipRules", AAZListType, ".ip_rules")
                properties.set_prop("publicNetworkAccess", AAZStrType, ".public_network_access")
                properties.set_prop("trustedServiceAccessEnabled", AAZBoolType, ".enable_trusted_service_access")
                properties.set_prop("virtualNetworkRules", AAZListType, ".virtual_network_rules")

            ip_rules = _builder.get(".properties.ipRules")
            if ip_rules is not None:
                ip_rules.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.ipRules[]")
            if _elements is not None:
                _elements.set_prop("action", AAZStrType, ".action")
                _elements.set_prop("ipMask", AAZStrType, ".ip_address")

            virtual_network_rules = _builder.get(".properties.virtualNetworkRules")
            if virtual_network_rules is not None:
                virtual_network_rules.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.virtualNetworkRules[]")
            if _elements is not None:
                _elements.set_prop("ignoreMissingVnetServiceEndpoint", AAZBoolType, ".ignore_missing_endpoint")
                _elements.set_prop("subnet", AAZObjectType)

            subnet = _builder.get(".properties.virtualNetworkRules[].subnet")
            if subnet is not None:
                subnet.set_prop("id", AAZStrType, ".subnet", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_network_rule_set_read = None

    @classmethod
    def _build_schema_network_rule_set_read(cls, _schema):
        if cls._schema_network_rule_set_read is not None:
            _schema.id = cls._schema_network_rule_set_read.id
            _schema.location = cls._schema_network_rule_set_read.location
            _schema.name = cls._schema_network_rule_set_read.name
            _schema.properties = cls._schema_network_rule_set_read.properties
            _schema.system_data = cls._schema_network_rule_set_read.system_data
            _schema.type = cls._schema_network_rule_set_read.type
            return

        cls._schema_network_rule_set_read = _schema_network_rule_set_read = AAZObjectType()

        network_rule_set_read = _schema_network_rule_set_read
        network_rule_set_read.id = AAZStrType(
            flags={"read_only": True},
        )
        network_rule_set_read.location = AAZStrType(
            flags={"read_only": True},
        )
        network_rule_set_read.name = AAZStrType(
            flags={"read_only": True},
        )
        network_rule_set_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        network_rule_set_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        network_rule_set_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_network_rule_set_read.properties
        properties.default_action = AAZStrType(
            serialized_name="defaultAction",
        )
        properties.ip_rules = AAZListType(
            serialized_name="ipRules",
        )
        properties.public_network_access = AAZStrType(
            serialized_name="publicNetworkAccess",
        )
        properties.trusted_service_access_enabled = AAZBoolType(
            serialized_name="trustedServiceAccessEnabled",
        )
        properties.virtual_network_rules = AAZListType(
            serialized_name="virtualNetworkRules",
        )

        ip_rules = _schema_network_rule_set_read.properties.ip_rules
        ip_rules.Element = AAZObjectType()

        _element = _schema_network_rule_set_read.properties.ip_rules.Element
        _element.action = AAZStrType()
        _element.ip_mask = AAZStrType(
            serialized_name="ipMask",
        )

        virtual_network_rules = _schema_network_rule_set_read.properties.virtual_network_rules
        virtual_network_rules.Element = AAZObjectType()

        _element = _schema_network_rule_set_read.properties.virtual_network_rules.Element
        _element.ignore_missing_vnet_service_endpoint = AAZBoolType(
            serialized_name="ignoreMissingVnetServiceEndpoint",
        )
        _element.subnet = AAZObjectType()

        subnet = _schema_network_rule_set_read.properties.virtual_network_rules.Element.subnet
        subnet.id = AAZStrType(
            flags={"required": True},
        )

        system_data = _schema_network_rule_set_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_network_rule_set_read.id
        _schema.location = cls._schema_network_rule_set_read.location
        _schema.name = cls._schema_network_rule_set_read.name
        _schema.properties = cls._schema_network_rule_set_read.properties
        _schema.system_data = cls._schema_network_rule_set_read.system_data
        _schema.type = cls._schema_network_rule_set_read.type


__all__ = ["Update"]
