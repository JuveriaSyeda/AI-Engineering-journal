# PROMPT ENGINEERING

Successfully prints the response from the model
google-generativeai deprecated Nov 2025, replaced by google-genai

# 📘 Prompt Engineering for Developers — Notes

# 🧠 1. What is Prompt Engineering?

👉 Prompt Engineering = Writing **clear instructions** so the AI gives the **correct output**

### 💡 Key Idea:

> Better prompt → Better output

---

### 🔄 Flow

```text
User Prompt → LLM → Response
```

---

### ✅ Example

❌ Bad:

```text
Explain Python
```

✅ Good:

```text
Explain Python in simple terms for beginners in 3 bullet points
```

---

### 🧾 Summary

- Be specific
- Guide the model
- Control output format

---

# 🎯 2. Principle 1: Write Clear & Specific Instructions

👉 The most important rule

---

## 🔧 Tactics

---

### 2.1 📦 Use Delimiters

```text
Summarize the text below:

"""
Python is a programming language...
"""
```

👉 Helps AI clearly separate input

---

### 2.2 🪜 Break Tasks into Steps

```text
1. Summarize the text
2. Extract key points
3. Give 2 examples
```

---

### 2.3 🎭 Assign Role

```text
You are a senior software engineer.
Explain REST APIs.
```

---

### 2.4 📏 Specify Output Format

```text
Explain AI in:
- 3 bullet points
- Simple language
```

---

### 2.5 📚 Provide Examples (Few-shot)

```text
Input: Apple → Fruit
Input: Car → Vehicle
Input: Cat →
```

---

### 2.6 🚫 Add Constraints

```text
Explain in simple terms. Do not use technical jargon.
```

---

### 🔄 Flow

```text
Clear Instructions → Better Understanding → Accurate Output
```

---

### 🧾 Summary

- Use delimiters
- Break tasks
- Define role
- Control format
- Add examples

---

# 🧠 3. Principle 2: Give the Model Time to Think

👉 Let the AI reason step-by-step

---

### ❌ Bad

```text
Solve this math problem
```

---

### ✅ Good

```text
Solve step-by-step and explain reasoning
```

---

### 🔄 Flow

```text
Problem → Step-by-step reasoning → Final answer
```

---

### 🧾 Summary

- Encourage reasoning
- Improves accuracy
- Useful for complex tasks

---

# 🧩 4. Prompt Structure (Best Practice)

```text
Role → Task → Context → Input → Output Format
```

---

### ✅ Example

```text
You are a Python expert.

Task: Explain the code
Context: Beginner audience

Code:
"""
def add(a, b):
    return a + b
"""

Output:
- Simple explanation
- 1 example
```

---

### 🧾 Summary

- Always structure prompts
- Reduces ambiguity
- Improves consistency

---

# 🔄 5. Iterative Prompting

👉 Improve prompts step-by-step

---

### Flow

```text
Prompt → Output → Refine Prompt → Better Output
```

---

### Example

1st Prompt:

```text
Explain AI
```

Improved:

```text
Explain AI in simple terms with 2 real-world examples
```

---

### 🧾 Summary

- Start simple
- Refine continuously
- Observe outputs

---

# 💬 6. Multi-turn Conversations

👉 Maintain context across messages

---

### Example

```json
[
  { "role": "system", "content": "You are helpful" },
  { "role": "user", "content": "What is Python?" },
  { "role": "assistant", "content": "Python is a programming language" },
  { "role": "user", "content": "Is it easy?" }
]
```

---

### 🔄 Flow

```text
Previous Messages → Context → Better Response
```

---

### 🧾 Summary

- Pass full conversation
- Enables memory
- Improves relevance

---

# ⚡ 7. Streaming (Real-world Concept)

👉 Responses come **token-by-token**

---

### Flow

```text
LLM → Token → UI → Token → UI → ...
```

---

### Example

```python
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

---

### 🧾 Summary

- Improves UX
- Feels real-time
- Used in production apps

---

# 🧠 8. System vs User Prompt

---

### System Prompt

👉 Defines behavior

```text
You are a helpful assistant
```

---

### User Prompt

👉 Actual question

```text
Explain machine learning
```

---

### 🧾 Summary

- System = rules
- User = task

---

# ⚠️ 9. Common Mistakes

- Vague prompts
- No structure
- No examples
- Too many tasks at once
- Ignoring output format

---

# 🚀 10. Best Practices

- Be clear and specific
- Use structured prompts
- Iterate and refine
- Add constraints
- Use examples

---

# 🧾 Final Summary

👉 Prompt Engineering is about:

```text
Clarity + Structure + Iteration = Better AI Output
```

---
