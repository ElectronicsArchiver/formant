# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.model.v1 import ros_pb2 as protos_dot_model_dot_v1_dot_ros__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cprotos/model/v1/config.proto\x12\x08v1.model\x1a\x19protos/model/v1/ros.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xbe\x01\n\x17\x41gentConfigurationStore\x12#\n\ragent_version\x18\x01 \x01(\tR\x0c\x61gentVersion\x12\x42\n\rconfiguration\x18\x02 \x01(\x0b\x32\x1c.v1.model.AgentConfigurationR\rconfiguration\x12:\n\x0b\x66\x65\x61ture_set\x18\x03 \x01(\x0b\x32\x19.v1.model.AgentFeatureSetR\nfeatureSet\"\xa2\x03\n\x0f\x41gentFeatureSet\x12\x1c\n\ttelemetry\x18\x01 \x01(\x08R\ttelemetry\x12-\n\x12internal_telemetry\x18\x02 \x01(\x08R\x11internalTelemetry\x12\x16\n\x06teleop\x18\x03 \x01(\x08R\x06teleop\x12#\n\rcustom_events\x18\x04 \x01(\x08R\x0c\x63ustomEvents\x12)\n\x10triggered_events\x18\x05 \x01(\x08R\x0ftriggeredEvents\x12\x10\n\x03ssh\x18\x06 \x01(\x08R\x03ssh\x12\'\n\x0fport_forwarding\x18\x07 \x01(\x08R\x0eportForwarding\x12\x1a\n\x08\x63ommands\x18\x08 \x01(\x08R\x08\x63ommands\x12$\n\rinterventions\x18\t \x01(\x08R\rinterventions\x12\x1b\n\ton_demand\x18\n \x01(\x08R\x08onDemand\x12\x1d\n\napp_config\x18\x0b \x01(\x08R\tappConfig\x12!\n\x0c\x62lob_storage\x18\x0c \x01(\x08R\x0b\x62lobStorage\"z\n\x12\x41gentConfiguration\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12@\n\x08\x64ocument\x18\x03 \x01(\x0b\x32$.v1.model.AgentConfigurationDocumentR\x08\x64ocument\"\xeb\x05\n\x1a\x41gentConfigurationDocument\x12\x18\n\x07version\x18\x01 \x01(\x03R\x07version\x12\x42\n\x04tags\x18\x02 \x03(\x0b\x32..v1.model.AgentConfigurationDocument.TagsEntryR\x04tags\x12>\n\ttelemetry\x18\x03 \x01(\x0b\x32 .v1.model.TelemetryConfigurationR\ttelemetry\x12>\n\tresources\x18\x04 \x01(\x0b\x32 .v1.model.ResourcesConfigurationR\tresources\x12\x44\n\x0b\x61pplication\x18\x05 \x01(\x0b\x32\".v1.model.ApplicationConfigurationR\x0b\x61pplication\x12\x35\n\x06teleop\x18\x06 \x01(\x0b\x32\x1d.v1.model.TeleopConfigurationR\x06teleop\x12N\n\x0fport_forwarding\x18\x07 \x01(\x0b\x32%.v1.model.PortForwardingConfigurationR\x0eportForwarding\x12/\n\tblob_data\x18\x08 \x01(\x0b\x32\x12.v1.model.BlobDataR\x08\x62lobData\x12\x37\n\x0b\x64iagnostics\x18\t \x01(\x0b\x32\x15.v1.model.DiagnosticsR\x0b\x64iagnostics\x12\x43\n\x0fterminal_access\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x0eterminalAccess\x12:\n\x08\x61\x64\x61pters\x18\x0b \x03(\x0b\x32\x1e.v1.model.AdapterConfigurationR\x08\x61\x64\x61pters\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"v\n\x14\x41\x64\x61pterConfiguration\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x17\n\x07\x66ile_id\x18\x03 \x01(\tR\x06\x66ileId\x12!\n\x0c\x65xec_command\x18\x04 \x01(\tR\x0b\x65xecCommand\"\x88\x02\n\x13TeleopConfiguration\x12G\n\x0bros_streams\x18\x01 \x03(\x0b\x32&.v1.model.TeleopRosStreamConfigurationR\nrosStreams\x12P\n\x0e\x63ustom_streams\x18\x02 \x03(\x0b\x32).v1.model.TeleopCustomStreamConfigurationR\rcustomStreams\x12V\n\x10hardware_streams\x18\x03 \x03(\x0b\x32+.v1.model.TeleopHardwareStreamConfigurationR\x0fhardwareStreams\"S\n\x1bPortForwardingConfiguration\x12\x34\n\x07\x65nabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x07\x65nabled\"\xcf\x02\n\x1cTeleopRosStreamConfiguration\x12\x1d\n\ntopic_name\x18\x01 \x01(\tR\ttopicName\x12\x35\n\ntopic_type\x18\x02 \x01(\x0e\x32\x16.v1.model.ROSTopicTypeR\ttopicType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12!\n\x0c\x65ncode_video\x18\x04 \x01(\x08R\x0b\x65ncodeVideo\x12\x1f\n\x0b\x61udio_codec\x18\x05 \x01(\tR\naudioCodec\x12\x18\n\x07quality\x18\x06 \x01(\tR\x07quality\x12\x30\n\x14\x62\x61se_reference_frame\x18\x07 \x01(\tR\x12\x62\x61seReferenceFrame\x12\x1f\n\x0blocal_frame\x18\x08 \x01(\tR\nlocalFrame\"\x8a\x03\n!TeleopHardwareStreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12&\n\x0frtc_stream_type\x18\x02 \x01(\tR\rrtcStreamType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12#\n\rhw_descriptor\x18\x04 \x01(\tR\x0chwDescriptor\x12\x18\n\x07quality\x18\x05 \x01(\tR\x07quality\x12#\n\rhardware_type\x18\x06 \x01(\tR\x0chardwareType\x12\x30\n\x14rtsp_encoding_needed\x18\x07 \x01(\x08R\x12rtspEncodingNeeded\x12\x19\n\x08is_onvif\x18\x08 \x01(\x08R\x07isOnvif\x12&\n\x0fip_cam_username\x18\t \x01(\tR\ripCamUsername\x12&\n\x0fip_cam_password\x18\n \x01(\tR\ripCamPassword\"\xc4\x01\n\x1fTeleopCustomStreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12&\n\x0frtc_stream_type\x18\x02 \x01(\tR\rrtcStreamType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12!\n\x0c\x65ncode_video\x18\x04 \x01(\x08R\x0b\x65ncodeVideo\x12\x18\n\x07quality\x18\x05 \x01(\tR\x07quality\"\x7f\n\x16TelemetryConfiguration\x12\x37\n\x07streams\x18\x01 \x03(\x0b\x32\x1d.v1.model.StreamConfigurationR\x07streams\x12,\n\x03ros\x18\x02 \x01(\x0b\x32\x1a.v1.model.ROSConfigurationR\x03ros\"\xc6\x01\n\x18\x41pplicationConfiguration\x12\x65\n\x11\x63onfiguration_map\x18\x01 \x03(\x0b\x32\x38.v1.model.ApplicationConfiguration.ConfigurationMapEntryR\x10\x63onfigurationMap\x1a\x43\n\x15\x43onfigurationMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x95\x01\n\x16ResourcesConfiguration\x12/\n\x04\x64isk\x18\x01 \x01(\x0b\x32\x1b.v1.model.DiskConfigurationR\x04\x64isk\x12J\n\x12stream_throttle_hz\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x10streamThrottleHz\"g\n\x11\x44iskConfiguration\x12\x1f\n\x0b\x62uffer_size\x18\x01 \x01(\x03R\nbufferSize\x12\x31\n\x15on_demand_buffer_size\x18\x02 \x01(\x03R\x12onDemandBufferSize\"K\n\x10ROSConfiguration\x12\x37\n\x18world_reference_frame_id\x18\x01 \x01(\tR\x15worldReferenceFrameId\"\xdd\x06\n\x13StreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12;\n\x04tags\x18\x02 \x03(\x0b\x32\'.v1.model.StreamConfiguration.TagsEntryR\x04tags\x12\x31\n\tros_topic\x18\x03 \x01(\x0b\x32\x12.v1.model.ROSTopicH\x00R\x08rosTopic\x12\x46\n\x10ros_localization\x18\x04 \x01(\x0b\x32\x19.v1.model.ROSLocalizationH\x00R\x0frosLocalization\x12\x43\n\x0f\x64irectory_watch\x18\x05 \x01(\x0b\x32\x18.v1.model.DirectoryWatchH\x00R\x0e\x64irectoryWatch\x12\x31\n\tfile_tail\x18\x06 \x01(\x0b\x32\x12.v1.model.FileTailH\x00R\x08\x66ileTail\x12J\n\x12ros_transform_tree\x18\x07 \x01(\x0b\x32\x1a.v1.model.ROSTransformTreeH\x00R\x10rosTransformTree\x12*\n\x06\x63ustom\x18\t \x01(\x0b\x32\x10.v1.model.CustomH\x00R\x06\x63ustom\x12\x30\n\x08hardware\x18\n \x01(\x0b\x32\x12.v1.model.HardwareH\x00R\x08hardware\x12=\n\x0bthrottle_hz\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\nthrottleHz\x12\x36\n\x08\x64isabled\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x08\x64isabled\x12\x37\n\ton_demand\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x08onDemand\x12\x44\n\ttransform\x18\x15 \x01(\x0b\x32&.v1.model.StreamTransformConfigurationR\ttransform\x12\x18\n\x07quality\x18\x16 \x01(\tR\x07quality\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x0f\n\rconfiguration\"p\n\x1cStreamTransformConfiguration\x12P\n\x16video_encoding_enabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x14videoEncodingEnabled\"\x1e\n\x08\x42lobData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\tR\x04\x64\x61ta\"\x8d\x01\n\x0b\x44iagnostics\x12;\n\x0breport_logs\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\nreportLogs\x12\x41\n\x0ereport_metrics\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\rreportMetrics\"\x08\n\x06\x43ustom\"\xa1\x02\n\x08Hardware\x12#\n\rhw_descriptor\x18\x01 \x01(\tR\x0chwDescriptor\x12.\n\x13\x61udio_hw_descriptor\x18\x03 \x01(\tR\x11\x61udioHwDescriptor\x12#\n\rhardware_type\x18\x04 \x01(\tR\x0chardwareType\x12\x30\n\x14rtsp_encoding_needed\x18\x05 \x01(\x08R\x12rtspEncodingNeeded\x12\x19\n\x08is_onvif\x18\x06 \x01(\x08R\x07isOnvif\x12&\n\x0fip_cam_username\x18\x07 \x01(\tR\ripCamUsername\x12&\n\x0fip_cam_password\x18\x08 \x01(\tR\ripCamPassword\"\xa0\x01\n\x0e\x44irectoryWatch\x12\x1c\n\tdirectory\x18\x01 \x01(\tR\tdirectory\x12\x1c\n\textension\x18\x02 \x01(\tR\textension\x12/\n\tfile_type\x18\x03 \x01(\x0e\x32\x12.v1.model.FileTypeR\x08\x66ileType\x12!\n\x0cremote_agent\x18\x04 \x01(\x08R\x0bremoteAgent\"\xaf\x01\n\x08\x46ileTail\x12\x1a\n\x08\x66ilename\x18\x01 \x01(\tR\x08\x66ilename\x12\x35\n\x0b\x66ile_format\x18\x02 \x01(\x0e\x32\x14.v1.model.FileFormatR\nfileFormat\x12\x19\n\x08time_key\x18\x03 \x01(\tR\x07timeKey\x12\x1f\n\x0btime_format\x18\x04 \x01(\tR\ntimeFormat\x12\x14\n\x05regex\x18\x05 \x01(\tR\x05regex*&\n\nTeleopMode\x12\x0b\n\x07\x43OMMAND\x10\x00\x12\x0b\n\x07OBSERVE\x10\x01*&\n\nFileFormat\x12\x0e\n\nPLAIN_TEXT\x10\x00\x12\x08\n\x04JSON\x10\x01*;\n\x08\x46ileType\x12\x08\n\x04\x46ILE\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\x0f\n\x0bPOINT_CLOUD\x10\x04\x12\t\n\x05VIDEO\x10\x05\x42+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.model.v1.config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/FormantIO/genproto/go/v1/model'
  _AGENTCONFIGURATIONDOCUMENT_TAGSENTRY._options = None
  _AGENTCONFIGURATIONDOCUMENT_TAGSENTRY._serialized_options = b'8\001'
  _APPLICATIONCONFIGURATION_CONFIGURATIONMAPENTRY._options = None
  _APPLICATIONCONFIGURATION_CONFIGURATIONMAPENTRY._serialized_options = b'8\001'
  _STREAMCONFIGURATION_TAGSENTRY._options = None
  _STREAMCONFIGURATION_TAGSENTRY._serialized_options = b'8\001'
  _TELEOPMODE._serialized_start=5456
  _TELEOPMODE._serialized_end=5494
  _FILEFORMAT._serialized_start=5496
  _FILEFORMAT._serialized_end=5534
  _FILETYPE._serialized_start=5536
  _FILETYPE._serialized_end=5595
  _AGENTCONFIGURATIONSTORE._serialized_start=102
  _AGENTCONFIGURATIONSTORE._serialized_end=292
  _AGENTFEATURESET._serialized_start=295
  _AGENTFEATURESET._serialized_end=713
  _AGENTCONFIGURATION._serialized_start=715
  _AGENTCONFIGURATION._serialized_end=837
  _AGENTCONFIGURATIONDOCUMENT._serialized_start=840
  _AGENTCONFIGURATIONDOCUMENT._serialized_end=1587
  _AGENTCONFIGURATIONDOCUMENT_TAGSENTRY._serialized_start=1532
  _AGENTCONFIGURATIONDOCUMENT_TAGSENTRY._serialized_end=1587
  _ADAPTERCONFIGURATION._serialized_start=1589
  _ADAPTERCONFIGURATION._serialized_end=1707
  _TELEOPCONFIGURATION._serialized_start=1710
  _TELEOPCONFIGURATION._serialized_end=1974
  _PORTFORWARDINGCONFIGURATION._serialized_start=1976
  _PORTFORWARDINGCONFIGURATION._serialized_end=2059
  _TELEOPROSSTREAMCONFIGURATION._serialized_start=2062
  _TELEOPROSSTREAMCONFIGURATION._serialized_end=2397
  _TELEOPHARDWARESTREAMCONFIGURATION._serialized_start=2400
  _TELEOPHARDWARESTREAMCONFIGURATION._serialized_end=2794
  _TELEOPCUSTOMSTREAMCONFIGURATION._serialized_start=2797
  _TELEOPCUSTOMSTREAMCONFIGURATION._serialized_end=2993
  _TELEMETRYCONFIGURATION._serialized_start=2995
  _TELEMETRYCONFIGURATION._serialized_end=3122
  _APPLICATIONCONFIGURATION._serialized_start=3125
  _APPLICATIONCONFIGURATION._serialized_end=3323
  _APPLICATIONCONFIGURATION_CONFIGURATIONMAPENTRY._serialized_start=3256
  _APPLICATIONCONFIGURATION_CONFIGURATIONMAPENTRY._serialized_end=3323
  _RESOURCESCONFIGURATION._serialized_start=3326
  _RESOURCESCONFIGURATION._serialized_end=3475
  _DISKCONFIGURATION._serialized_start=3477
  _DISKCONFIGURATION._serialized_end=3580
  _ROSCONFIGURATION._serialized_start=3582
  _ROSCONFIGURATION._serialized_end=3657
  _STREAMCONFIGURATION._serialized_start=3660
  _STREAMCONFIGURATION._serialized_end=4521
  _STREAMCONFIGURATION_TAGSENTRY._serialized_start=1532
  _STREAMCONFIGURATION_TAGSENTRY._serialized_end=1587
  _STREAMTRANSFORMCONFIGURATION._serialized_start=4523
  _STREAMTRANSFORMCONFIGURATION._serialized_end=4635
  _BLOBDATA._serialized_start=4637
  _BLOBDATA._serialized_end=4667
  _DIAGNOSTICS._serialized_start=4670
  _DIAGNOSTICS._serialized_end=4811
  _CUSTOM._serialized_start=4813
  _CUSTOM._serialized_end=4821
  _HARDWARE._serialized_start=4824
  _HARDWARE._serialized_end=5113
  _DIRECTORYWATCH._serialized_start=5116
  _DIRECTORYWATCH._serialized_end=5276
  _FILETAIL._serialized_start=5279
  _FILETAIL._serialized_end=5454
# @@protoc_insertion_point(module_scope)
