// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: protos/agent/v1/agent.proto

#include "protos/agent/v1/agent.pb.h"
#include "protos/agent/v1/agent.grpc.pb.h"

#include <grpcpp/impl/codegen/async_stream.h>
#include <grpcpp/impl/codegen/sync_stream.h>
#include <gmock/gmock.h>
namespace v1 {
namespace agent {

class MockAgentStub : public Agent::StubInterface {
 public:
  MOCK_METHOD2(StreamDataRaw, ::grpc::ClientWriterInterface< ::v1::model::Datapoint>*(::grpc::ClientContext* context, ::v1::agent::StreamDataResponse* response));
  MOCK_METHOD4(AsyncStreamDataRaw, ::grpc::ClientAsyncWriterInterface< ::v1::model::Datapoint>*(::grpc::ClientContext* context, ::v1::agent::StreamDataResponse* response, ::grpc::CompletionQueue* cq, void* tag));
  MOCK_METHOD3(PrepareAsyncStreamDataRaw, ::grpc::ClientAsyncWriterInterface< ::v1::model::Datapoint>*(::grpc::ClientContext* context, ::v1::agent::StreamDataResponse* response, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PostData, ::grpc::Status(::grpc::ClientContext* context, const ::v1::model::Datapoint& request, ::v1::agent::PostDataResponse* response));
  MOCK_METHOD3(AsyncPostDataRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::PostDataResponse>*(::grpc::ClientContext* context, const ::v1::model::Datapoint& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncPostDataRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::PostDataResponse>*(::grpc::ClientContext* context, const ::v1::model::Datapoint& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(CreateInterventionRequest, ::grpc::Status(::grpc::ClientContext* context, const ::v1::model::InterventionRequest& request, ::v1::model::InterventionRequest* response));
  MOCK_METHOD3(AsyncCreateInterventionRequestRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::model::InterventionRequest>*(::grpc::ClientContext* context, const ::v1::model::InterventionRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncCreateInterventionRequestRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::model::InterventionRequest>*(::grpc::ClientContext* context, const ::v1::model::InterventionRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(GetInterventionRequest, ::grpc::Status(::grpc::ClientContext* context, const ::v1::agent::GetInterventionRequestRequest& request, ::v1::model::InterventionRequest* response));
  MOCK_METHOD3(AsyncGetInterventionRequestRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::model::InterventionRequest>*(::grpc::ClientContext* context, const ::v1::agent::GetInterventionRequestRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncGetInterventionRequestRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::model::InterventionRequest>*(::grpc::ClientContext* context, const ::v1::agent::GetInterventionRequestRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(GetInterventionResponse, ::grpc::Status(::grpc::ClientContext* context, const ::v1::agent::GetInterventionResponseRequest& request, ::v1::model::InterventionResponse* response));
  MOCK_METHOD3(AsyncGetInterventionResponseRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::model::InterventionResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetInterventionResponseRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncGetInterventionResponseRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::model::InterventionResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetInterventionResponseRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(GetStreamsConfiguration, ::grpc::Status(::grpc::ClientContext* context, const ::v1::agent::GetStreamsConfigurationRequest& request, ::v1::agent::GetStreamsConfigurationResponse* response));
  MOCK_METHOD3(AsyncGetStreamsConfigurationRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::GetStreamsConfigurationResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetStreamsConfigurationRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncGetStreamsConfigurationRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::GetStreamsConfigurationResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetStreamsConfigurationRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(GetApplicationConfiguration, ::grpc::Status(::grpc::ClientContext* context, const ::v1::agent::GetApplicationConfigurationRequest& request, ::v1::agent::GetApplicationConfigurationResponse* response));
  MOCK_METHOD3(AsyncGetApplicationConfigurationRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::GetApplicationConfigurationResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetApplicationConfigurationRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncGetApplicationConfigurationRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::GetApplicationConfigurationResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetApplicationConfigurationRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(GetAgentConfiguration, ::grpc::Status(::grpc::ClientContext* context, const ::v1::agent::GetAgentConfigurationRequest& request, ::v1::agent::GetAgentConfigurationResponse* response));
  MOCK_METHOD3(AsyncGetAgentConfigurationRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::GetAgentConfigurationResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetAgentConfigurationRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncGetAgentConfigurationRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::GetAgentConfigurationResponse>*(::grpc::ClientContext* context, const ::v1::agent::GetAgentConfigurationRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(Health, ::grpc::Status(::grpc::ClientContext* context, const ::v1::agent::HealthRequest& request, ::v1::agent::HealthResponse* response));
  MOCK_METHOD3(AsyncHealthRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::HealthResponse>*(::grpc::ClientContext* context, const ::v1::agent::HealthRequest& request, ::grpc::CompletionQueue* cq));
  MOCK_METHOD3(PrepareAsyncHealthRaw, ::grpc::ClientAsyncResponseReaderInterface< ::v1::agent::HealthResponse>*(::grpc::ClientContext* context, const ::v1::agent::HealthRequest& request, ::grpc::CompletionQueue* cq));
};

} // namespace v1
} // namespace agent
