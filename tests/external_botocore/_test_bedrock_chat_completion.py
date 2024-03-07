# Copyright 2010 New Relic, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

chat_completion_payload_templates = {
    "amazon.titan-text-express-v1": '{ "inputText": "%s", "textGenerationConfig": {"temperature": %f, "maxTokenCount": %d }}',
    "ai21.j2-mid-v1": '{"prompt": "%s", "temperature": %f, "maxTokens": %d}',
    "anthropic.claude-instant-v1": '{"prompt": "Human: %s Assistant:", "temperature": %f, "max_tokens_to_sample": %d}',
    "cohere.command-text-v14": '{"prompt": "%s", "temperature": %f, "max_tokens": %d}',
    "meta.llama2-13b-chat-v1": '{"prompt": "%s", "temperature": %f, "max_gen_len": %d}',
}

chat_completion_get_llm_message_ids = {
    "amazon.titan-text-express-v1": {
        "bedrock_key": [
            {
                "conversation_id": "my-awesome-id",
                "request_id": "81508a1c-33a8-4294-8743-f0c629af2f49",
                "message_id": None,  # UUID that varies with each run
            },
            {
                "conversation_id": "my-awesome-id",
                "request_id": "81508a1c-33a8-4294-8743-f0c629af2f49",
                "message_id": None,  # UUID that varies with each run
            },
        ]
    },
    "ai21.j2-mid-v1": {
        "bedrock_key": [
            {
                "conversation_id": "my-awesome-id",
                "request_id": "228ee63f-4eca-4b7d-b679-bc920de63525",
                "message_id": "1234-0",
            },
            {
                "conversation_id": "my-awesome-id",
                "request_id": "228ee63f-4eca-4b7d-b679-bc920de63525",
                "message_id": "1234-1",
            },
        ]
    },
    "anthropic.claude-instant-v1": {
        "bedrock_key": [
            {
                "conversation_id": "my-awesome-id",
                "request_id": "6a886158-b39f-46ce-b214-97458ab76f2f",
                "message_id": None,  # UUID that varies with each run
            },
            {
                "conversation_id": "my-awesome-id",
                "request_id": "6a886158-b39f-46ce-b214-97458ab76f2f",
                "message_id": None,  # UUID that varies with each run
            },
        ]
    },
    "cohere.command-text-v14": {
        "bedrock_key": [
            {
                "conversation_id": "my-awesome-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "message_id": "12912a17-aa13-45f3-914c-cc82166f3601-0",
            },
            {
                "conversation_id": "my-awesome-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "message_id": "12912a17-aa13-45f3-914c-cc82166f3601-1",
            },
        ]
    },
    "meta.llama2-13b-chat-v1": {
        "bedrock_key": [
            {
                "conversation_id": "my-awesome-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "message_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a-0",
            },
            {
                "conversation_id": "my-awesome-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "message_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a-1",
            },
        ]
    },
}

chat_completion_expected_events = {
    "amazon.titan-text-express-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "81508a1c-33a8-4294-8743-f0c629af2f49",
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "amazon.titan-text-express-v1",
                "response.model": "amazon.titan-text-express-v1",
                "response.usage.completion_tokens": 32,
                "response.usage.total_tokens": 44,
                "response.usage.prompt_tokens": 12,
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "FINISH",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "81508a1c-33a8-4294-8743-f0c629af2f49",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "What is 212 degrees Fahrenheit converted to Celsius?",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "amazon.titan-text-express-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "81508a1c-33a8-4294-8743-f0c629af2f49",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "\n1 degree Fahrenheit is 0.56 Celsius. Therefore, 212 degree Fahrenheit in Celsius would be 115.42.",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "amazon.titan-text-express-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
    "ai21.j2-mid-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "228ee63f-4eca-4b7d-b679-bc920de63525",
                "response_id": "1234",
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "ai21.j2-mid-v1",
                "response.model": "ai21.j2-mid-v1",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "endoftext",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": "1234-0",
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "228ee63f-4eca-4b7d-b679-bc920de63525",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "What is 212 degrees Fahrenheit converted to Celsius?",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "ai21.j2-mid-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": "1234-1",
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "228ee63f-4eca-4b7d-b679-bc920de63525",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "\n212 degrees Fahrenheit is equal to 100 degrees Celsius.",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "ai21.j2-mid-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
    "anthropic.claude-instant-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "6a886158-b39f-46ce-b214-97458ab76f2f",
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "anthropic.claude-instant-v1",
                "response.model": "anthropic.claude-instant-v1",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "max_tokens",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "6a886158-b39f-46ce-b214-97458ab76f2f",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "Human: What is 212 degrees Fahrenheit converted to Celsius? Assistant:",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "anthropic.claude-instant-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "6a886158-b39f-46ce-b214-97458ab76f2f",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": " Okay, here are the steps to convert 212 degrees Fahrenheit to Celsius:\n\n1) The formula to convert between Fahrenheit and Celsius is:\n   C = (F - 32) * 5/9\n\n2) Plug in 212 degrees Fahrenheit for F:\n   C = (212 - 32) * 5/9\n   C = 180 * 5/9\n   C = 100\n\n3) Therefore, 212 degrees Fahrenheit converted to Celsius is 100 degrees Celsius.",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "anthropic.claude-instant-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
    "cohere.command-text-v14": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "response_id": None,  # UUID that varies with each run
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "cohere.command-text-v14",
                "response.model": "cohere.command-text-v14",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "MAX_TOKENS",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "What is 212 degrees Fahrenheit converted to Celsius?",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "cohere.command-text-v14",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": " To convert from Fahrenheit to Celsius, you can use the following formula:\n\nCelsius = (Fahrenheit - 32) * 5/9\n\nIn this case, 212 degrees Fahrenheit is converted to Celsius as follows:\n\nCelsius = (212 - 32) * 5/9 = (180) * 5/9 = (180/9) = 20 degrees Celsius\n\nTherefore, 212 degrees Fahrenheit is equivalent to 20 degrees Celsius.\n\nIt's important to note that",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "cohere.command-text-v14",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
    "meta.llama2-13b-chat-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "meta.llama2-13b-chat-v1",
                "response.model": "meta.llama2-13b-chat-v1",
                "response.usage.prompt_tokens": 17,
                "response.usage.completion_tokens": 46,
                "response.usage.total_tokens": 63,
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "stop",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "What is 212 degrees Fahrenheit converted to Celsius?",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "meta.llama2-13b-chat-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": " Here's the answer:\n\n212°F = 100°C\n\nSo, 212 degrees Fahrenheit is equal to 100 degrees Celsius.",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "meta.llama2-13b-chat-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
}

chat_completion_streaming_expected_events = {
    "amazon.titan-text-express-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "b427270f-371a-458d-81b6-a05aafb2704c",
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "amazon.titan-text-express-v1",
                "response.model": "amazon.titan-text-express-v1",
                "response.usage.completion_tokens": 35,
                "response.usage.total_tokens": 47,
                "response.usage.prompt_tokens": 12,
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "FINISH",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "b427270f-371a-458d-81b6-a05aafb2704c",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "What is 212 degrees Fahrenheit converted to Celsius?",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "amazon.titan-text-express-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "b427270f-371a-458d-81b6-a05aafb2704c",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "\n1 degree Fahrenheit is 0.56 degrees Celsius. Therefore, 212 degree Fahrenheit in Celsius would be 115.72.",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "amazon.titan-text-express-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
    "anthropic.claude-instant-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "a645548f-0b3a-47ce-a675-f51e6e9037de",
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "anthropic.claude-instant-v1",
                "response.model": "anthropic.claude-instant-v1",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "stop_sequence",
                "response.usage.completion_tokens": 99,
                "response.usage.prompt_tokens": 19,
                "response.usage.total_tokens": 118,
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "a645548f-0b3a-47ce-a675-f51e6e9037de",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "Human: What is 212 degrees Fahrenheit converted to Celsius? Assistant:",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "anthropic.claude-instant-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "a645548f-0b3a-47ce-a675-f51e6e9037de",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": " Here are the steps to convert 212 degrees Fahrenheit to Celsius:\n\n1) The formula to convert between Fahrenheit and Celsius is:\n   C = (F - 32) * 5/9\n\n2) Plug in 212 degrees Fahrenheit for F:\n   C = (212 - 32) * 5/9\n   C = 180 * 5/9\n   C = 100\n\n3) Therefore, 212 degrees Fahrenheit is equal to 100 degrees Celsius.",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "anthropic.claude-instant-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
    "cohere.command-text-v14": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "response_id": None,  # UUID that varies with each run
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "cohere.command-text-v14",
                "response.model": "cohere.command-text-v14",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "MAX_TOKENS",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "What is 212 degrees Fahrenheit converted to Celsius?",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "cohere.command-text-v14",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "12912a17-aa13-45f3-914c-cc82166f3601",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": " 212°F is equivalent to 100°C. \n\nFahrenheit and Celsius are two temperature scales commonly used in everyday life. The Fahrenheit scale is based on 32°F for the freezing point of water and 212°F for the boiling point of water. On the other hand, the Celsius scale uses 0°C and 100°C as the freezing and boiling points of water, respectively. \n\nTo convert from Fahrenheit to Celsius, we subtract 32 from the Fahrenheit temperature and multiply the result",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "cohere.command-text-v14",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
    "meta.llama2-13b-chat-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "api_key_last_four_digits": "CRET",
                "duration": None,  # Response time varies each test run
                "request.model": "meta.llama2-13b-chat-v1",
                "response.model": "meta.llama2-13b-chat-v1",
                "response.usage.prompt_tokens": 17,
                "response.usage.completion_tokens": 46,
                "response.usage.total_tokens": 63,
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "response.choices.finish_reason": "stop",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 2,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "What is 212 degrees Fahrenheit converted to Celsius?",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "meta.llama2-13b-chat-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "9a64cdb0-3e82-41c7-873a-c12a77e0143a",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": " Here's the answer:\n\n212°F = 100°C\n\nSo, 212 degrees Fahrenheit is equal to 100 degrees Celsius.",
                "role": "assistant",
                "completion_id": None,
                "sequence": 1,
                "response.model": "meta.llama2-13b-chat-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
                "is_response": True,
            },
        ),
    ],
}

chat_completion_invalid_model_error_events = [
    (
        {"type": "LlmChatCompletionSummary"},
        {
            "id": None,  # UUID that varies with each run
            "appName": "Python Agent Test (mlmodel_openai)",
            "transaction_id": "transaction-id",
            "conversation_id": "my-awesome-id",
            "span_id": None,
            "trace_id": "trace-id",
            "api_key_last_four_digits": "CRET",
            "duration": None,  # Response time varies each test run
            "request.model": "does-not-exist",
            "request.temperature": 0.7,
            "request.max_tokens": 100,
            "response.number_of_messages": 1,
            "vendor": "bedrock",
            "ingest_source": "Python",
            "error": True,
        },
    ),
    (
        {"type": "LlmChatCompletionMessage"},
        {
            "id": None,
            "appName": "Python Agent Test (mlmodel_openai)",
            "conversation_id": "my-awesome-id",
            "request_id": "",
            "span_id": None,
            "trace_id": "trace-id",
            "transaction_id": "transaction-id",
            "content": "You are a scientist.",
            "role": "system",
            "response.model": "",
            "completion_id": None,
            "sequence": 0,
            "vendor": "bedrock",
            "ingest_source": "Python",
        },
    ),
]

chat_completion_invalid_access_key_error_events = {
    "amazon.titan-text-express-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "",
                "api_key_last_four_digits": "-KEY",
                "duration": None,  # Response time varies each test run
                "request.model": "amazon.titan-text-express-v1",
                "response.model": "amazon.titan-text-express-v1",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 1,
                "error": True,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "Invalid Token",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "amazon.titan-text-express-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
    ],
    "ai21.j2-mid-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "",
                "api_key_last_four_digits": "-KEY",
                "duration": None,  # Response time varies each test run
                "request.model": "ai21.j2-mid-v1",
                "response.model": "ai21.j2-mid-v1",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 1,
                "error": True,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "Invalid Token",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "ai21.j2-mid-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
    ],
    "anthropic.claude-instant-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "",
                "api_key_last_four_digits": "-KEY",
                "duration": None,  # Response time varies each test run
                "request.model": "anthropic.claude-instant-v1",
                "response.model": "anthropic.claude-instant-v1",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 1,
                "error": True,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "Human: Invalid Token Assistant:",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "anthropic.claude-instant-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
    ],
    "cohere.command-text-v14": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "",
                "api_key_last_four_digits": "-KEY",
                "duration": None,  # Response time varies each test run
                "request.model": "cohere.command-text-v14",
                "response.model": "cohere.command-text-v14",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 1,
                "error": True,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "Invalid Token",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "cohere.command-text-v14",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
    ],
    "meta.llama2-13b-chat-v1": [
        (
            {"type": "LlmChatCompletionSummary"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "transaction_id": "transaction-id",
                "span_id": None,
                "trace_id": "trace-id",
                "request_id": "",
                "api_key_last_four_digits": "-KEY",
                "duration": None,  # Response time varies each test run
                "request.model": "meta.llama2-13b-chat-v1",
                "response.model": "meta.llama2-13b-chat-v1",
                "request.temperature": 0.7,
                "request.max_tokens": 100,
                "vendor": "bedrock",
                "ingest_source": "Python",
                "response.number_of_messages": 1,
                "error": True,
            },
        ),
        (
            {"type": "LlmChatCompletionMessage"},
            {
                "id": None,  # UUID that varies with each run
                "appName": "Python Agent Test (external_botocore)",
                "conversation_id": "my-awesome-id",
                "request_id": "",
                "span_id": None,
                "trace_id": "trace-id",
                "transaction_id": "transaction-id",
                "content": "Invalid Token",
                "role": "user",
                "completion_id": None,
                "sequence": 0,
                "response.model": "meta.llama2-13b-chat-v1",
                "vendor": "bedrock",
                "ingest_source": "Python",
            },
        ),
    ],
}

chat_completion_expected_client_errors = {
    "amazon.titan-text-express-v1": {
        "http.statusCode": 403,
        "error.message": "The security token included in the request is invalid.",
        "error.code": "UnrecognizedClientException",
    },
    "ai21.j2-mid-v1": {
        "http.statusCode": 403,
        "error.message": "The security token included in the request is invalid.",
        "error.code": "UnrecognizedClientException",
    },
    "anthropic.claude-instant-v1": {
        "http.statusCode": 403,
        "error.message": "The security token included in the request is invalid.",
        "error.code": "UnrecognizedClientException",
    },
    "cohere.command-text-v14": {
        "http.statusCode": 403,
        "error.message": "The security token included in the request is invalid.",
        "error.code": "UnrecognizedClientException",
    },
    "meta.llama2-13b-chat-v1": {
        "http.statusCode": 403,
        "error.message": "The security token included in the request is invalid.",
        "error.code": "UnrecognizedClientException",
    },
}
