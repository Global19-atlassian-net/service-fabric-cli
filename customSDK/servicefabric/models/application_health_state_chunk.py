# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .entity_health_state_chunk import EntityHealthStateChunk


class ApplicationHealthStateChunk(EntityHealthStateChunk):
    """Represents the health state chunk of a application.
    The application health state chunk contains the application name, its
    aggregated health state and any children services and deployed applications
    that respect the filters in cluster health chunk query description.

    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param application_name: The name of the application, including the
     'fabric:' URI scheme.
    :type application_name: str
    :param application_type_name: The application type name as defined in the
     application manifest.
    :type application_type_name: str
    :param service_health_state_chunks: The list of service health state
     chunks in the cluster that respect the filters in the cluster health chunk
     query description.
    :type service_health_state_chunks:
     ~azure.servicefabric.models.ServiceHealthStateChunkList
    :param deployed_application_health_state_chunks: The list of deployed
     application health state chunks in the cluster that respect the filters in
     the cluster health chunk query description.
    :type deployed_application_health_state_chunks:
     ~azure.servicefabric.models.DeployedApplicationHealthStateChunkList
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'application_type_name': {'key': 'ApplicationTypeName', 'type': 'str'},
        'service_health_state_chunks': {'key': 'ServiceHealthStateChunks', 'type': 'ServiceHealthStateChunkList'},
        'deployed_application_health_state_chunks': {'key': 'DeployedApplicationHealthStateChunks', 'type': 'DeployedApplicationHealthStateChunkList'},
    }

    def __init__(self, **kwargs):
        super(ApplicationHealthStateChunk, self).__init__(**kwargs)
        self.application_name = kwargs.get('application_name', None)
        self.application_type_name = kwargs.get('application_type_name', None)
        self.service_health_state_chunks = kwargs.get('service_health_state_chunks', None)
        self.deployed_application_health_state_chunks = kwargs.get('deployed_application_health_state_chunks', None)
