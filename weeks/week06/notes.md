Experimented Ollama to run LLMs locally

Today, I understood the difference between open-source and closed-source AI models.

## Open Source vs Closed Source Models

`Open Source Models`

- Model weights are publicly available
- Can run locally on personal systems
- More customization and flexibility
- Useful for experimentation and privacy-focused projects

### Examples:

- Llama
- Mistral
- Gemma

`Closed Source Models`

- Controlled by companies
- Access mostly through APIs
- Better optimized and production-ready in many cases
- Easier to use but limited customization

### Examples:

- GPT models by OpenAI
- Claude by Anthropic
- Gemini by Google

## OpenAI SDK and Native SDK

Understood about and api endpoints calling

openai.chat.completions.create()

`Native SDK`

Official SDK provided by the model provider
Gives access to provider-specific features

### Examples:

- OpenAI SDK
- Anthropic SDK
- Google Gemini SDK

`OpenAI-Compatible SDK`

- Many providers support the OpenAI API format
- Same client structure can work across multiple providers
- Easier to switch bet

### Key Understanding

The OpenAI SDK has become a common standard interface for interacting with LLMs.

## Different Ways to Use AI Models

Today I explored three major ways to use AI models.

1. Chat Interface

Directly interacting with models using chat applications.

#### Examples:

- ChatGPT
- Claude
- Gemini

#### Use Cases:

- Learning
- Brainstorming
- Quick tasks

2. Cloud APIs

Using models through APIs in applications.

#### Benefits:

- Easy integration
- Scalable
- No need for powerful hardware

Example Flow:

client.chat.completions.create(
model="gpt-4.1",
messages=[
{"role": "user", "content": "Hello"}
]
)

3. Local Inference
   Running models directly on a local machine.

#### Tools explored:

- Ollama
- Hugging Face Transformers

#### Advantages

- Better privacy
- Offline usage
- More control over models

#### Challenges

- Requires good hardware
- Large models consume more memory
