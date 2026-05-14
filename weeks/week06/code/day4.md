## 1. Neural Network Architectures

### Transformers

- Architecture based on self-attention mechanisms
- Processes sequences in parallel (unlike RNNs)
- Foundation for modern LLMs (GPT, BERT, Claude)
- Key components: Multi-head attention, positional encoding, feed-forward networks

### Recurrent Neural Networks (RNN)

- Sequential processing architecture
- Maintains hidden state across time steps
- Suitable for time-series and sequential data
- Limitation: Vanishing gradient problem in long sequences

### Long Short-Term Memory (LSTM)

- Enhanced RNN with gating mechanisms
- Solves vanishing gradient problem
- Gates: Input, Forget, Output
- Better at capturing long-term dependencies

### Convolutional Neural Networks (CNN)

- Specialized for grid-like data (images, spatial data)
- Uses convolution operations and pooling layers
- Feature extraction through hierarchical learning
- Efficient parameter sharing through weight reuse

### N-grams

- Statistical language model
- Predicts next item based on previous N-1 items
- Simple but limited context understanding
- Foundation for early NLP approaches

---

## 2. Machine Learning Training Paradigms

### Supervised Learning

- Training with labeled input-output pairs
- Model learns mapping from inputs to known outputs
- Examples: Classification, regression tasks
- Requires high-quality labeled datasets

### Unsupervised Learning

- Training without labeled outputs
- Discovers patterns and structure in data
- Examples: Clustering, dimensionality reduction, anomaly detection
- Useful when labels are expensive or unavailable

### Reinforcement Learning

- Agent learns through interaction with environment
- Optimizes for cumulative reward
- Trial-and-error learning approach
- Applications: Game playing, robotics, optimization

### Self-Supervised Learning

- Creates supervision signal from data itself
- No manual labeling required
- Examples: Masked language modeling, next token prediction
- Powers modern LLM pre-training

---

## 3. Core AI Concepts

### Data Types

- **Labeled Data**: Data with known outputs/annotations
- **Unlabeled Data**: Raw data without annotations

### Deep Learning

- Multi-layer neural networks
- Learns hierarchical feature representations
- Requires significant computational resources
- Excels at complex pattern recognition

### Computer Vision

- AI systems that interpret visual information
- Tasks: Object detection, image classification, segmentation
- Built primarily on CNN architectures

### Natural Language Processing (NLP)

- Processing and understanding human language
- Tasks: Translation, sentiment analysis, question answering
- Modern approaches use transformer-based models

### LLM Customization Approaches

**Prompt Engineering**

- Crafting effective input prompts
- No model modification required
- Quick iteration and testing
- Limited by context window

**Retrieval-Augmented Generation (RAG)**

- Retrieves relevant information from external knowledge base
- Augments prompts with retrieved context
- No model retraining needed
- Keeps information up-to-date

**Fine-tuning**

- Retraining model on domain-specific data
- Modifies model weights
- Better domain adaptation
- Requires computational resources and training data

### Foundational Models

- Large pre-trained models serving as starting points
- Trained on broad, diverse datasets
- Can be adapted to specific tasks
- Examples: GPT-4, Claude, LLaMA

### Model Access Types

- **Open Source**: Publicly available weights and architecture (LLaMA, Mistral)
- **Closed Source**: API access only, proprietary (GPT-4, Claude)

### Vector Databases

- Stores high-dimensional embeddings
- Enables semantic search and similarity matching
- Essential for RAG systems
- Examples: Pinecone, Weaviate, ChromaDB

### Key Platforms & Tools

**Hugging Face**

- Repository for ML models and datasets
- Transformers library for model implementation
- Community-driven model sharing

**LangChain**

- Framework for building LLM applications
- Chains together LLM calls and tools
- Simplifies RAG and agent development

### LLM Development Phases

1. **Data Collection**: Gathering diverse training data
2. **Pre-training**: Learning language patterns on large corpus
3. **Fine-tuning**: Adapting to specific tasks/domains
4. **Alignment**: RLHF to align with human preferences
5. **Evaluation**: Testing performance and safety
6. **Deployment**: Serving model to users

---

## 4. Model Parameters

### What are Parameters?

- Learnable weights in neural networks
- Adjusted during training process
- Determine model's behavior and capabilities

### Parameter Scale in LLMs

- Small models: <1B parameters (efficient, faster)
- Medium models: 1B-10B parameters (balanced)
- Large models: 10B-100B+ parameters (high capability)

### Key Considerations

- More parameters ≠ always better
- Trade-offs: Capability vs. cost vs. latency
- Inference requires proportional compute resources
- Parameter count affects memory requirements
