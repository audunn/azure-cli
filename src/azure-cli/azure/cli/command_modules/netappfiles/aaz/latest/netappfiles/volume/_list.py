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
    "netappfiles volume list",
)
class List(AAZCommand):
    """List all volumes within the capacity pool

    :example: List all subvolumes of a ANF volume
        az netappfiles subvolume list -g mygroup --account-name myaccountname  --pool-name mypoolname --volume-name myvolumename
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.netapp/netappaccounts/{}/capacitypools/{}/volumes", "2023-05-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.account_name = AAZStrArg(
            options=["-a", "--account-name"],
            help="The name of the NetApp account",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,127}$",
            ),
        )
        _args_schema.pool_name = AAZStrArg(
            options=["-p", "--pool-name"],
            help="The name of the capacity pool",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$",
                max_length=64,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VolumesList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class VolumesList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes",
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
                    "poolName", self.ctx.args.pool_name,
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )
            _element.zones = AAZListType()

            properties = cls._schema_on_200.value.Element.properties
            properties.actual_throughput_mibps = AAZFloatType(
                serialized_name="actualThroughputMibps",
                flags={"read_only": True},
            )
            properties.avs_data_store = AAZStrType(
                serialized_name="avsDataStore",
            )
            properties.backup_id = AAZStrType(
                serialized_name="backupId",
                nullable=True,
            )
            properties.baremetal_tenant_id = AAZStrType(
                serialized_name="baremetalTenantId",
                flags={"read_only": True},
            )
            properties.capacity_pool_resource_id = AAZStrType(
                serialized_name="capacityPoolResourceId",
            )
            properties.clone_progress = AAZIntType(
                serialized_name="cloneProgress",
                nullable=True,
                flags={"read_only": True},
            )
            properties.cool_access = AAZBoolType(
                serialized_name="coolAccess",
            )
            properties.cool_access_retrieval_policy = AAZStrType(
                serialized_name="coolAccessRetrievalPolicy",
            )
            properties.coolness_period = AAZIntType(
                serialized_name="coolnessPeriod",
            )
            properties.creation_token = AAZStrType(
                serialized_name="creationToken",
                flags={"required": True},
            )
            properties.data_protection = AAZObjectType(
                serialized_name="dataProtection",
            )
            properties.data_store_resource_id = AAZListType(
                serialized_name="dataStoreResourceId",
                flags={"read_only": True},
            )
            properties.default_group_quota_in_ki_bs = AAZIntType(
                serialized_name="defaultGroupQuotaInKiBs",
            )
            properties.default_user_quota_in_ki_bs = AAZIntType(
                serialized_name="defaultUserQuotaInKiBs",
            )
            properties.delete_base_snapshot = AAZBoolType(
                serialized_name="deleteBaseSnapshot",
            )
            properties.enable_subvolumes = AAZStrType(
                serialized_name="enableSubvolumes",
            )
            properties.encrypted = AAZBoolType(
                flags={"read_only": True},
            )
            properties.encryption_key_source = AAZStrType(
                serialized_name="encryptionKeySource",
            )
            properties.export_policy = AAZObjectType(
                serialized_name="exportPolicy",
            )
            properties.file_access_logs = AAZStrType(
                serialized_name="fileAccessLogs",
                flags={"read_only": True},
            )
            properties.file_system_id = AAZStrType(
                serialized_name="fileSystemId",
                flags={"read_only": True},
            )
            properties.is_default_quota_enabled = AAZBoolType(
                serialized_name="isDefaultQuotaEnabled",
            )
            properties.is_large_volume = AAZBoolType(
                serialized_name="isLargeVolume",
            )
            properties.is_restoring = AAZBoolType(
                serialized_name="isRestoring",
            )
            properties.kerberos_enabled = AAZBoolType(
                serialized_name="kerberosEnabled",
            )
            properties.key_vault_private_endpoint_resource_id = AAZStrType(
                serialized_name="keyVaultPrivateEndpointResourceId",
            )
            properties.ldap_enabled = AAZBoolType(
                serialized_name="ldapEnabled",
            )
            properties.maximum_number_of_files = AAZIntType(
                serialized_name="maximumNumberOfFiles",
                flags={"read_only": True},
            )
            properties.mount_targets = AAZListType(
                serialized_name="mountTargets",
                flags={"read_only": True},
            )
            properties.network_features = AAZStrType(
                serialized_name="networkFeatures",
            )
            properties.network_sibling_set_id = AAZStrType(
                serialized_name="networkSiblingSetId",
                flags={"read_only": True},
            )
            properties.originating_resource_id = AAZStrType(
                serialized_name="originatingResourceId",
                nullable=True,
                flags={"read_only": True},
            )
            properties.placement_rules = AAZListType(
                serialized_name="placementRules",
            )
            properties.protocol_types = AAZListType(
                serialized_name="protocolTypes",
            )
            properties.provisioned_availability_zone = AAZStrType(
                serialized_name="provisionedAvailabilityZone",
                nullable=True,
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.proximity_placement_group = AAZStrType(
                serialized_name="proximityPlacementGroup",
            )
            properties.security_style = AAZStrType(
                serialized_name="securityStyle",
            )
            properties.service_level = AAZStrType(
                serialized_name="serviceLevel",
            )
            properties.smb_access_based_enumeration = AAZStrType(
                serialized_name="smbAccessBasedEnumeration",
                nullable=True,
            )
            properties.smb_continuously_available = AAZBoolType(
                serialized_name="smbContinuouslyAvailable",
            )
            properties.smb_encryption = AAZBoolType(
                serialized_name="smbEncryption",
            )
            properties.smb_non_browsable = AAZStrType(
                serialized_name="smbNonBrowsable",
            )
            properties.snapshot_directory_visible = AAZBoolType(
                serialized_name="snapshotDirectoryVisible",
            )
            properties.snapshot_id = AAZStrType(
                serialized_name="snapshotId",
                nullable=True,
            )
            properties.storage_to_network_proximity = AAZStrType(
                serialized_name="storageToNetworkProximity",
                flags={"read_only": True},
            )
            properties.subnet_id = AAZStrType(
                serialized_name="subnetId",
                flags={"required": True},
            )
            properties.t2_network = AAZStrType(
                serialized_name="t2Network",
                flags={"read_only": True},
            )
            properties.throughput_mibps = AAZFloatType(
                serialized_name="throughputMibps",
                nullable=True,
            )
            properties.unix_permissions = AAZStrType(
                serialized_name="unixPermissions",
                nullable=True,
            )
            properties.usage_threshold = AAZIntType(
                serialized_name="usageThreshold",
                flags={"required": True},
            )
            properties.volume_group_name = AAZStrType(
                serialized_name="volumeGroupName",
                flags={"read_only": True},
            )
            properties.volume_spec_name = AAZStrType(
                serialized_name="volumeSpecName",
            )
            properties.volume_type = AAZStrType(
                serialized_name="volumeType",
            )

            data_protection = cls._schema_on_200.value.Element.properties.data_protection
            data_protection.replication = AAZObjectType()
            data_protection.snapshot = AAZObjectType()
            data_protection.volume_relocation = AAZObjectType(
                serialized_name="volumeRelocation",
            )

            replication = cls._schema_on_200.value.Element.properties.data_protection.replication
            replication.endpoint_type = AAZStrType(
                serialized_name="endpointType",
            )
            replication.remote_volume_region = AAZStrType(
                serialized_name="remoteVolumeRegion",
            )
            replication.remote_volume_resource_id = AAZStrType(
                serialized_name="remoteVolumeResourceId",
                flags={"required": True},
            )
            replication.replication_id = AAZStrType(
                serialized_name="replicationId",
                flags={"read_only": True},
            )
            replication.replication_schedule = AAZStrType(
                serialized_name="replicationSchedule",
            )

            snapshot = cls._schema_on_200.value.Element.properties.data_protection.snapshot
            snapshot.snapshot_policy_id = AAZStrType(
                serialized_name="snapshotPolicyId",
            )

            volume_relocation = cls._schema_on_200.value.Element.properties.data_protection.volume_relocation
            volume_relocation.ready_to_be_finalized = AAZBoolType(
                serialized_name="readyToBeFinalized",
                flags={"read_only": True},
            )
            volume_relocation.relocation_requested = AAZBoolType(
                serialized_name="relocationRequested",
            )

            data_store_resource_id = cls._schema_on_200.value.Element.properties.data_store_resource_id
            data_store_resource_id.Element = AAZStrType()

            export_policy = cls._schema_on_200.value.Element.properties.export_policy
            export_policy.rules = AAZListType()

            rules = cls._schema_on_200.value.Element.properties.export_policy.rules
            rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.export_policy.rules.Element
            _element.allowed_clients = AAZStrType(
                serialized_name="allowedClients",
            )
            _element.chown_mode = AAZStrType(
                serialized_name="chownMode",
            )
            _element.cifs = AAZBoolType()
            _element.has_root_access = AAZBoolType(
                serialized_name="hasRootAccess",
            )
            _element.kerberos5_read_only = AAZBoolType(
                serialized_name="kerberos5ReadOnly",
            )
            _element.kerberos5_read_write = AAZBoolType(
                serialized_name="kerberos5ReadWrite",
            )
            _element.kerberos5i_read_only = AAZBoolType(
                serialized_name="kerberos5iReadOnly",
            )
            _element.kerberos5i_read_write = AAZBoolType(
                serialized_name="kerberos5iReadWrite",
            )
            _element.kerberos5p_read_only = AAZBoolType(
                serialized_name="kerberos5pReadOnly",
            )
            _element.kerberos5p_read_write = AAZBoolType(
                serialized_name="kerberos5pReadWrite",
            )
            _element.nfsv3 = AAZBoolType()
            _element.nfsv41 = AAZBoolType()
            _element.rule_index = AAZIntType(
                serialized_name="ruleIndex",
            )
            _element.unix_read_only = AAZBoolType(
                serialized_name="unixReadOnly",
            )
            _element.unix_read_write = AAZBoolType(
                serialized_name="unixReadWrite",
            )

            mount_targets = cls._schema_on_200.value.Element.properties.mount_targets
            mount_targets.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.mount_targets.Element
            _element.file_system_id = AAZStrType(
                serialized_name="fileSystemId",
                flags={"required": True},
            )
            _element.ip_address = AAZStrType(
                serialized_name="ipAddress",
                flags={"read_only": True},
            )
            _element.mount_target_id = AAZStrType(
                serialized_name="mountTargetId",
                flags={"read_only": True},
            )
            _element.smb_server_fqdn = AAZStrType(
                serialized_name="smbServerFqdn",
            )

            placement_rules = cls._schema_on_200.value.Element.properties.placement_rules
            placement_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.placement_rules.Element
            _element.key = AAZStrType(
                flags={"required": True},
            )
            _element.value = AAZStrType(
                flags={"required": True},
            )

            protocol_types = cls._schema_on_200.value.Element.properties.protocol_types
            protocol_types.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
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

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.value.Element.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
