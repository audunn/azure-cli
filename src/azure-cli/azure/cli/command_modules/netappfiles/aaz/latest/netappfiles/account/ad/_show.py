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
    "netappfiles account ad show",
)
class Show(AAZCommand):
    """Get the specified ANF active directory

    :example: Get an active directory on the account
        az netappfiles account ad show -g mygroup --name myname --active-directory-id 13641da9-c0e9-4b97-84fc-4f8014a93848
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.netapp/netappaccounts/{}", "2024-03-01", "properties.activeDirectories[]"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
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
        _args_schema.account_name = AAZStrArg(
            options=["-a", "-n", "--name", "--account-name"],
            help="The name of the NetApp account",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\\-_]{0,127}$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.active_directory_id = AAZStrArg(
            options=["--active-directory-id"],
            help="Id of the Active Directory",
            required=True,
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AccountsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.activeDirectories
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].activeDirectoryId == self.ctx.args.active_directory_id,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.activeDirectories
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].activeDirectoryId == self.ctx.args.active_directory_id,
                filters
            )
            idx = next(filters, [len(result)])[0]
            result[idx] = value
            return

    class AccountsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}",
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
                    "accountName", self.ctx.args.account_name,
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
                    "api-version", "2024-03-01",
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
            _ShowHelper._build_schema_net_app_account_read(cls._schema_on_200)

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_net_app_account_read = None

    @classmethod
    def _build_schema_net_app_account_read(cls, _schema):
        if cls._schema_net_app_account_read is not None:
            _schema.etag = cls._schema_net_app_account_read.etag
            _schema.id = cls._schema_net_app_account_read.id
            _schema.identity = cls._schema_net_app_account_read.identity
            _schema.location = cls._schema_net_app_account_read.location
            _schema.name = cls._schema_net_app_account_read.name
            _schema.properties = cls._schema_net_app_account_read.properties
            _schema.system_data = cls._schema_net_app_account_read.system_data
            _schema.tags = cls._schema_net_app_account_read.tags
            _schema.type = cls._schema_net_app_account_read.type
            return

        cls._schema_net_app_account_read = _schema_net_app_account_read = AAZObjectType()

        net_app_account_read = _schema_net_app_account_read
        net_app_account_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        net_app_account_read.id = AAZStrType(
            flags={"read_only": True},
        )
        net_app_account_read.identity = AAZObjectType()
        net_app_account_read.location = AAZStrType(
            flags={"required": True},
        )
        net_app_account_read.name = AAZStrType(
            flags={"read_only": True},
        )
        net_app_account_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        net_app_account_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        net_app_account_read.tags = AAZDictType()
        net_app_account_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_net_app_account_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_net_app_account_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType(
            nullable=True,
        )

        _element = _schema_net_app_account_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_net_app_account_read.properties
        properties.active_directories = AAZListType(
            serialized_name="activeDirectories",
        )
        properties.disable_showmount = AAZBoolType(
            serialized_name="disableShowmount",
            nullable=True,
            flags={"read_only": True},
        )
        properties.encryption = AAZObjectType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        active_directories = _schema_net_app_account_read.properties.active_directories
        active_directories.Element = AAZObjectType()

        _element = _schema_net_app_account_read.properties.active_directories.Element
        _element.active_directory_id = AAZStrType(
            serialized_name="activeDirectoryId",
            nullable=True,
        )
        _element.ad_name = AAZStrType(
            serialized_name="adName",
        )
        _element.administrators = AAZListType()
        _element.aes_encryption = AAZBoolType(
            serialized_name="aesEncryption",
        )
        _element.allow_local_nfs_users_with_ldap = AAZBoolType(
            serialized_name="allowLocalNfsUsersWithLdap",
        )
        _element.backup_operators = AAZListType(
            serialized_name="backupOperators",
        )
        _element.dns = AAZStrType()
        _element.domain = AAZStrType()
        _element.encrypt_dc_connections = AAZBoolType(
            serialized_name="encryptDCConnections",
        )
        _element.kdc_ip = AAZStrType(
            serialized_name="kdcIP",
        )
        _element.ldap_over_tls = AAZBoolType(
            serialized_name="ldapOverTLS",
        )
        _element.ldap_search_scope = AAZObjectType(
            serialized_name="ldapSearchScope",
        )
        _element.ldap_signing = AAZBoolType(
            serialized_name="ldapSigning",
        )
        _element.organizational_unit = AAZStrType(
            serialized_name="organizationalUnit",
        )
        _element.password = AAZStrType(
            flags={"secret": True},
        )
        _element.preferred_servers_for_ldap_client = AAZStrType(
            serialized_name="preferredServersForLdapClient",
        )
        _element.security_operators = AAZListType(
            serialized_name="securityOperators",
        )
        _element.server_root_ca_certificate = AAZStrType(
            serialized_name="serverRootCACertificate",
            flags={"secret": True},
        )
        _element.site = AAZStrType()
        _element.smb_server_name = AAZStrType(
            serialized_name="smbServerName",
        )
        _element.status = AAZStrType(
            flags={"read_only": True},
        )
        _element.status_details = AAZStrType(
            serialized_name="statusDetails",
            flags={"read_only": True},
        )
        _element.username = AAZStrType()

        administrators = _schema_net_app_account_read.properties.active_directories.Element.administrators
        administrators.Element = AAZStrType()

        backup_operators = _schema_net_app_account_read.properties.active_directories.Element.backup_operators
        backup_operators.Element = AAZStrType()

        ldap_search_scope = _schema_net_app_account_read.properties.active_directories.Element.ldap_search_scope
        ldap_search_scope.group_dn = AAZStrType(
            serialized_name="groupDN",
        )
        ldap_search_scope.group_membership_filter = AAZStrType(
            serialized_name="groupMembershipFilter",
        )
        ldap_search_scope.user_dn = AAZStrType(
            serialized_name="userDN",
        )

        security_operators = _schema_net_app_account_read.properties.active_directories.Element.security_operators
        security_operators.Element = AAZStrType()

        encryption = _schema_net_app_account_read.properties.encryption
        encryption.identity = AAZObjectType()
        encryption.key_source = AAZStrType(
            serialized_name="keySource",
        )
        encryption.key_vault_properties = AAZObjectType(
            serialized_name="keyVaultProperties",
        )

        identity = _schema_net_app_account_read.properties.encryption.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.user_assigned_identity = AAZStrType(
            serialized_name="userAssignedIdentity",
        )

        key_vault_properties = _schema_net_app_account_read.properties.encryption.key_vault_properties
        key_vault_properties.key_name = AAZStrType(
            serialized_name="keyName",
            flags={"required": True},
        )
        key_vault_properties.key_vault_id = AAZStrType(
            serialized_name="keyVaultId",
            flags={"read_only": True},
        )
        key_vault_properties.key_vault_resource_id = AAZStrType(
            serialized_name="keyVaultResourceId",
            flags={"required": True},
        )
        key_vault_properties.key_vault_uri = AAZStrType(
            serialized_name="keyVaultUri",
            flags={"required": True},
        )
        key_vault_properties.status = AAZStrType(
            flags={"read_only": True},
        )

        system_data = _schema_net_app_account_read.system_data
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

        tags = _schema_net_app_account_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_net_app_account_read.etag
        _schema.id = cls._schema_net_app_account_read.id
        _schema.identity = cls._schema_net_app_account_read.identity
        _schema.location = cls._schema_net_app_account_read.location
        _schema.name = cls._schema_net_app_account_read.name
        _schema.properties = cls._schema_net_app_account_read.properties
        _schema.system_data = cls._schema_net_app_account_read.system_data
        _schema.tags = cls._schema_net_app_account_read.tags
        _schema.type = cls._schema_net_app_account_read.type


__all__ = ["Show"]
