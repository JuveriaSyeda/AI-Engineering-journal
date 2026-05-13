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

## LLM Types

1.  Base Model

    Better for fine-tunning and learning a new skill

2.  Chat/Instruct Model

    Better for chat/ conversations

3.  Reasoning/Thinking Model

    Better for problem solving

## Frontier Models- Strengths and Pitfall

### Performance

1. Syntesizing information

Answering a question in depth with a structured, well researched answer and often including a summary

#### Capabilities include:

- Answering questions in depth
- Generating well-structured explanations
- Providing summaries alongside detailed responses
- Organizing complex topics clearly

2. Fleshing out a skeleton

From a couple of notes,building out a well crafted email, or a blog post, and iterating on it with you until perfect

3. Coding

The ability to write and debug code is remarkable

#### Capabilities include:

- Writing code across multiple languages
- Debugging and explaining errors
- Generating boilerplate and reusable code
- Assisting with problem solving and implementation

### Limitations

1. Specialized domains

Most are not phd's, not even close to

#### Limitations include:

- Limited deep expertise in niche domains
- Can produce shallow or partially correct explanations
- May miss domain-specific nuances

2. Recent events

Limited knowledge beyond training cut-off date; code often uses legacy APIs/models

#### Common issues:

- Lack of awareness of recent developments
- Use of outdated APIs, libraries, or tools
- Suggestions based on deprecated practices
- Can Confidently make mistakes

Some curious blindspots
Can jump to conclusions when coding

#### Observed behaviors:

- Hallucinating facts or references
- Jumping to conclusions while coding
- Missing obvious edge cases
- Producing convincing but incorrect outputs

### Experimented with Chat-Based AI Products

Tested multiple AI chat products through Web UIs to better understand:

- Response quality
- Reasoning capabilities
- Strengths and weaknesses
- Differences in coding assistance

### Introduction to agentic AI

Learned and experimented with Agentic AI concepts:

- Autonomous task execution
