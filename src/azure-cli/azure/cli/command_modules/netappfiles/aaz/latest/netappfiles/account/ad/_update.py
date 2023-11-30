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
    "netappfiles account ad update",
)
class Update(AAZCommand):
    """Updates an active directory to the account

    :example: Update an active directory on the account
        az netappfiles account ad update -g mygroup --name myname --active-directory-id 13641da9-c0e9-4b97-84fc-4f8014a93848 --username ad_username --password ad_password --domain northeurope --dns 1.2.3.4 --smb-server-name SMBSERVER
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.netapp/netappaccounts/{}", "2023-05-01", "properties.activeDirectories[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, self._output)

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
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,127}$",
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

        # define Arg Group "Body.properties.activeDirectories[]"

        _args_schema = cls._args_schema
        _args_schema.ad_name = AAZStrArg(
            options=["--ad-name"],
            arg_group="Body.properties.activeDirectories[]",
            help="Name of the active directory machine. This optional parameter is used only while creating kerberos volume",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=64,
                min_length=1,
            ),
        )
        _args_schema.administrators = AAZListArg(
            options=["--administrators"],
            arg_group="Body.properties.activeDirectories[]",
            help="Users to be added to the Built-in Administrators active directory group. A list of unique usernames without domain specifier",
            nullable=True,
        )
        _args_schema.aes_encryption = AAZBoolArg(
            options=["--aes-encryption"],
            arg_group="Body.properties.activeDirectories[]",
            help="If enabled, AES encryption will be enabled for SMB communication.",
            nullable=True,
        )
        _args_schema.allow_local_nfs_users_with_ldap = AAZBoolArg(
            options=["--allow-local-ldap-users", "--allow-local-nfs-users-with-ldap"],
            arg_group="Body.properties.activeDirectories[]",
            help="If enabled, NFS client local users can also (in addition to LDAP users) access the NFS volumes.",
            nullable=True,
        )
        _args_schema.backup_operators = AAZListArg(
            options=["--backup-operators"],
            arg_group="Body.properties.activeDirectories[]",
            help="Users to be added to the Built-in Backup Operator active directory group. A list of unique usernames without domain specifier",
            nullable=True,
        )
        _args_schema.dns = AAZStrArg(
            options=["--dns"],
            arg_group="Body.properties.activeDirectories[]",
            help="Comma separated list of DNS server IP addresses (IPv4 only) for the Active Directory domain",
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)((, ?)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))*$",
            ),
        )
        _args_schema.domain = AAZStrArg(
            options=["--domain"],
            arg_group="Body.properties.activeDirectories[]",
            help="Name of the Active Directory domain",
            nullable=True,
        )
        _args_schema.encrypt_dc_connections = AAZBoolArg(
            options=["--encrypt-dc-connections"],
            arg_group="Body.properties.activeDirectories[]",
            help="If enabled, Traffic between the SMB server to Domain Controller (DC) will be encrypted.",
            nullable=True,
        )
        _args_schema.kdc_ip = AAZStrArg(
            options=["--kdc-ip"],
            arg_group="Body.properties.activeDirectories[]",
            help="kdc server IP addresses for the active directory machine. This optional parameter is used only while creating kerberos volume.",
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)((, ?)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))*$",
            ),
        )
        _args_schema.ldap_over_tls = AAZBoolArg(
            options=["--ldap-over-tls"],
            arg_group="Body.properties.activeDirectories[]",
            help="Specifies whether or not the LDAP traffic needs to be secured via TLS.",
            nullable=True,
        )
        _args_schema.ldap_search_scope = AAZObjectArg(
            options=["--ldap-search-scope"],
            arg_group="Body.properties.activeDirectories[]",
            help="LDAP Search scope options",
            nullable=True,
        )
        _args_schema.ldap_signing = AAZBoolArg(
            options=["--ldap-signing"],
            arg_group="Body.properties.activeDirectories[]",
            help="Specifies whether or not the LDAP traffic needs to be signed.",
            nullable=True,
        )
        _args_schema.organizational_unit = AAZStrArg(
            options=["--organizational-unit"],
            arg_group="Body.properties.activeDirectories[]",
            help="The Organizational Unit (OU) within the Windows Active Directory",
            nullable=True,
        )
        _args_schema.password = AAZStrArg(
            options=["--password"],
            arg_group="Body.properties.activeDirectories[]",
            help="Plain text password of Active Directory domain administrator, value is masked in the response",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=64,
            ),
        )
        _args_schema.preferred_servers_for_ldap_client = AAZStrArg(
            options=["-p", "--preferred-servers-for-ldap-client"],
            arg_group="Body.properties.activeDirectories[]",
            help="Comma separated list of IPv4 addresses of preferred servers for LDAP client. At most two comma separated IPv4 addresses can be passed.",
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)((, ?)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))?)?$",
                max_length=32,
            ),
        )
        _args_schema.security_operators = AAZListArg(
            options=["--security-operators"],
            arg_group="Body.properties.activeDirectories[]",
            help="Domain Users in the Active directory to be given SeSecurityPrivilege privilege (Needed for SMB Continuously available shares for SQL). A list of unique usernames without domain specifier",
            nullable=True,
        )
        _args_schema.server_root_ca_certificate = AAZStrArg(
            options=["--server-root-ca-cert", "--server-root-ca-certificate"],
            arg_group="Body.properties.activeDirectories[]",
            help="When LDAP over SSL/TLS is enabled, the LDAP client is required to have base64 encoded Active Directory Certificate Service's self-signed root CA certificate, this optional parameter is used only for dual protocol with LDAP user-mapping volumes.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=10240,
                min_length=1,
            ),
        )
        _args_schema.site = AAZStrArg(
            options=["--site"],
            arg_group="Body.properties.activeDirectories[]",
            help="The Active Directory site the service will limit Domain Controller discovery to",
            nullable=True,
        )
        _args_schema.smb_server_name = AAZStrArg(
            options=["--smb-server-name"],
            arg_group="Body.properties.activeDirectories[]",
            help="NetBIOS name of the SMB server. This name will be registered as a computer account in the AD and used to mount volumes",
            nullable=True,
        )
        _args_schema.username = AAZStrArg(
            options=["--username"],
            arg_group="Body.properties.activeDirectories[]",
            help="A domain user account with permission to create machine accounts",
            nullable=True,
        )

        administrators = cls._args_schema.administrators
        administrators.Element = AAZStrArg(
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )

        backup_operators = cls._args_schema.backup_operators
        backup_operators.Element = AAZStrArg(
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )

        ldap_search_scope = cls._args_schema.ldap_search_scope
        ldap_search_scope.group_dn = AAZStrArg(
            options=["group-dn"],
            help="This specifies the group DN, which overrides the base DN for group lookups.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=255,
            ),
        )
        ldap_search_scope.group_membership_filter = AAZStrArg(
            options=["group-membership-filter"],
            help="This specifies the custom LDAP search filter to be used when looking up group membership from LDAP server.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=255,
            ),
        )
        ldap_search_scope.user_dn = AAZStrArg(
            options=["user-dn"],
            help="This specifies the user DN, which overrides the base DN for user lookups.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=255,
            ),
        )

        security_operators = cls._args_schema.security_operators
        security_operators.Element = AAZStrArg(
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AccountsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.selectors.subresource.required())
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.selectors.subresource.required())
        yield self.AccountsCreateOrUpdate(ctx=self.ctx)()
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
                    "api-version", "2023-05-01",
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
            _UpdateHelper._build_schema_net_app_account_read(cls._schema_on_200)

            return cls._schema_on_200

    class AccountsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}",
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
                    "api-version", "2023-05-01",
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

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_net_app_account_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.selectors.subresource.required())

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("activeDirectoryId", AAZStrType, ".active_directory_id", typ_kwargs={"nullable": True})
            _builder.set_prop("adName", AAZStrType, ".ad_name")
            _builder.set_prop("administrators", AAZListType, ".administrators")
            _builder.set_prop("aesEncryption", AAZBoolType, ".aes_encryption")
            _builder.set_prop("allowLocalNfsUsersWithLdap", AAZBoolType, ".allow_local_nfs_users_with_ldap")
            _builder.set_prop("backupOperators", AAZListType, ".backup_operators")
            _builder.set_prop("dns", AAZStrType, ".dns")
            _builder.set_prop("domain", AAZStrType, ".domain")
            _builder.set_prop("encryptDCConnections", AAZBoolType, ".encrypt_dc_connections")
            _builder.set_prop("kdcIP", AAZStrType, ".kdc_ip")
            _builder.set_prop("ldapOverTLS", AAZBoolType, ".ldap_over_tls")
            _builder.set_prop("ldapSearchScope", AAZObjectType, ".ldap_search_scope")
            _builder.set_prop("ldapSigning", AAZBoolType, ".ldap_signing")
            _builder.set_prop("organizationalUnit", AAZStrType, ".organizational_unit")
            _builder.set_prop("password", AAZStrType, ".password", typ_kwargs={"flags": {"secret": True}})
            _builder.set_prop("preferredServersForLdapClient", AAZStrType, ".preferred_servers_for_ldap_client")
            _builder.set_prop("securityOperators", AAZListType, ".security_operators")
            _builder.set_prop("serverRootCACertificate", AAZStrType, ".server_root_ca_certificate", typ_kwargs={"flags": {"secret": True}})
            _builder.set_prop("site", AAZStrType, ".site")
            _builder.set_prop("smbServerName", AAZStrType, ".smb_server_name")
            _builder.set_prop("username", AAZStrType, ".username")

            administrators = _builder.get(".administrators")
            if administrators is not None:
                administrators.set_elements(AAZStrType, ".")

            backup_operators = _builder.get(".backupOperators")
            if backup_operators is not None:
                backup_operators.set_elements(AAZStrType, ".")

            ldap_search_scope = _builder.get(".ldapSearchScope")
            if ldap_search_scope is not None:
                ldap_search_scope.set_prop("groupDN", AAZStrType, ".group_dn")
                ldap_search_scope.set_prop("groupMembershipFilter", AAZStrType, ".group_membership_filter")
                ldap_search_scope.set_prop("userDN", AAZStrType, ".user_dn")

            security_operators = _builder.get(".securityOperators")
            if security_operators is not None:
                security_operators.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.selectors.subresource.required(),
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

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
        user_assigned_identities.Element = AAZObjectType()

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


__all__ = ["Update"]
