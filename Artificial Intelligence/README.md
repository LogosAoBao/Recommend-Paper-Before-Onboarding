# 人工智能领域论文推荐

整理了人工智能核心领域的经典与前沿论文，覆盖大模型、基础架构、多模态、应用落地等方向，适合入门学习与深度研究参考：

## **一、大模型与基础架构**

### 1. Transform万物起源

- **论文**：[🔥*Attention Is All You Need*](https://arxiv.org/abs/1706.03762)
- **简介**：Transformer 架构奠基作，用注意力机制替代传统循环/卷积结构，开启大模型时代（BERT、GPT 均基于此拓展）。

### 2. Bert 预训练里程碑

- **论文**：[🔥*BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*](https://arxiv.org/abs/1810.04805)
- **简介**：双向预训练 + 掩码语言模型（MLM），开启 NLP 预训练范式

### 3. GPT 生成式大模型代表
- **论文**：[🔥*GPT-3: Language Models are Few-Shot Learners*](https://arxiv.org/abs/2005.14165)
- **论文**：[🔥*GPT-1: Improving Language Understanding by Generative Pre-Training*](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- **简介**：单向预训练 + 自回归生成，验证 “大参数 + 少样本” 能力

### 4. T5 统一框架
- **论文**：[🔥*T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer*](https://arxiv.org/abs/1910.10683)
- **简介**：提出 “Text-to-Text” 统一框架，将所有 NLP 任务转化为文本生成

### 2. Deepseek系列

- **论文**：[🔥*DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*](https://arxiv.org/abs/2501.12948)
- **简介**：基于 Transformer 架构，开发了基于大模型检索的 LLM 优化方法，在多模态、跨领域、多任务、多模态多任务等场景下表现优秀。

## **二、训练优化与效率提升**

### 1. 大规模训练技术
- **论文**:[🔥Efficient Large-Scale Language Model Training on GPU Clusters（Megatron-LM](https://arxiv.org/abs/2104.04473)
- **简介**:Megatron-LM 框架，基于单机多卡、多节点分布式训练，实现大规模模型训练。贡献：混合精度训练、模型并行、流水线并行等工程优化。
- 
### 2. 参数高效微调（PEFT）
- **论文**:[🔥LoRA：LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
- **论文**:[🔥QLoRA：QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
- **简介**:用低秩适应、量化技术降低微调成本（如在消费级 GPU 上微调）。
- 
### 3. 预训练数据与扩展定律
- **论文**:[🔥Scaling Laws：Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- **简介**:揭示模型性能与参数量、数据量的关系，指导模型设计。

## **三、多模态与跨领域融合**
### 1. 视觉与语言融合

- **论文**:[🔥*ViT：An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*](https://arxiv.org/abs/2010.11929)
- **简介**:将 Transformer 直接用于计算机视觉，证明纯注意力机制可媲美卷积神经网络（CNN），推动多模态大模型发展。
- **论文**:[🔥CLIP：Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- **简介**:将 Transformer 引入 CV 领域，打通文本与图像理解。

### 2. 多模态大模型
- **论文**:[🔥GPT-4V：GPT-4 Technical Report](https://arxiv.org/abs/2303.08774)
- **论文**:[🔥Qwen2-VL：Qwen2-VL: Enhancing Vision-Language Model’s Perception of the World at Any Resolution](https://arxiv.org/abs/2305.11401)
- **简介**：支持图像、视频、音频等多模态输入与生成。


